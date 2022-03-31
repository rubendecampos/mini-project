import argparse

import database
import preprocessing
import algorithm
import analysis

import numpy as np


def main():
    """main function that is call by the command line"""

    example_doc = """\
examples:

    1. a list of different examples
    
    2. second example"""

    parser = argparse.ArgumentParser(
        usage="python %(prog)s [options]",
        description="This perform a Linear Regression and a Regression Tree on one out of"
                    "two dataset (Wine quality or House prices)",
        epilog=example_doc,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument(
        '--dataset',
        choices=['wine', 'white-wine', 'red-wine', 'housing'],
        default='white-wine',
        help="decide which dataset will be used for this experiment (wine is the combination of"
             "both red and white wine). It can be %(choices)s (by default : %(default)s)"
    )

    parser.add_argument(
        '--prep',
        choices=['minmax','znorm','poly-minmax', 'poly-znorm'],
        default='minmax',
        help="decide which preprocessing method is going to be used."
             "It can be %(choices)s (by default : %(default)s)"
    )

    parser.add_argument(
        '-p',
        '--protocol',
        choices=['proto0', 'proto1', 'proto2'],
        nargs='*',
        default=['proto0', 'proto1', 'proto2'],
        help="decide which protocol will be processed for this experiment. "
             "Available options are %(choices)s (by default : %(default)s)"
    )

    args = parser.parse_args()

    # load the dataset chosen by the user
    data = database.load_data(args.dataset)
    database.create_protocols(data,3)

    # process only the protocols listed by the user
    protocols = args.protocol
    for proto in protocols:

        # get the training set and test set
        train_set = database.get(proto,'train')
        test_set = database.get(proto,'test')

        # use the given preprocessing method
        preproc = args.prep
        if preproc == 'minmax':
            prep_test, prep_train = preprocessing.preprocess(train_set,test_set,'min_max',poly_choice=False)
        elif preproc == 'znorm':
            prep_test, prep_train = preprocessing.preprocess(train_set,test_set,'z_norm',poly_choice=False)
        elif preproc == 'poly-minmax':
            prep_test, prep_train = preprocessing.preprocess(train_set,test_set,'min_max',poly_choice=True)
        elif preproc == 'poly-znorm':
            prep_test, prep_train = preprocessing.preprocess(train_set,test_set,'z_norm',poly_choice=True)
        
        print("\n%s table using the %s method : " % (proto, preproc))
        print(50 * "-")

        # compute the two algorithm (Linear Regression and Regression Tree)
        prediction_lin = algorithm.train_algo(prep_train, prep_test, 'LIN_REGRESSION')
        prediction_tree = algorithm.train_algo(prep_train, prep_test, 'DECISION_TREE')

        # compare the result
        expected = np.array(test_set.pop('quality'))
        error_lin = analysis.analyser(expected, prediction_lin)
        error_tree = analysis.analyser(expected, prediction_tree)

        print("Absolute error using Linear Regression  |  %d" % error_lin)
        print("Absolute error using Regression Tree    |  %d" % error_tree)


if __name__ == "__main__":
    main()
