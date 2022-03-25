from ast import arg
from doctest import Example
from email.policy import default
from tkinter import N
import database
import argparse

## TODO: implement different function for each case, then call these function
##          when needed

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
        #####
        # delete that part later
        train_set = database.get(proto,'train')
        test_set = database.get(proto,'test')
        print(train_set, test_set)
        #####
        
        # use the given preprocessing method
        


if __name__ == "__main__":
    main()
