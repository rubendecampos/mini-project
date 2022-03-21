import database


## TODO: implement different function for each case, then call these function
##          when needed

def main():
    """main function that is call by the command line"""
    data = database.load_data('white-wine')
    database.create_protocols(data,3)
    train_set = database.get('proto2','train')
    print(train_set)

if __name__ == "__main__":
    main()
