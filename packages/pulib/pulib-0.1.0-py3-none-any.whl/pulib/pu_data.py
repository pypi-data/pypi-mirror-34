import math

def pn_from_dataframe(dataframe, data_column, pos_class):
    '''
    Function to generate random positive-negative data from any pandas dataframe. It returns the same dataset with a 'y' column containing the positive-negative data.

    REQUIRED

    dataframe: pandas.Dataframe to be extracted to positive-negative.
    data_column: dataframe column to be compared to extract the positive class.
    pos_class: class in the data_column to be considered as positive.

    OPTIONAL

    pos_size: positive rate (if between 0 and 1) or positive literal number (greater than one).
    pos_size will default to 0.8 if no value is specified.
    '''

    dataframe = dataframe.sample(frac=1).reset_index(drop=True)

    for index, value in enumerate(dataframe.loc[:, data_column]):
        if value == pos_class:
            dataframe.loc[index, 'y'] = 1
        else:
            dataframe.loc[index, 'y'] = -1

    return dataframe

def pu_from_y_train(y_train, pos_rate=0.5):
    '''
    Function to generate positive-unlabeled data from a y_train. It returns the same y_train containing only positive-unlabeled data.

    REQUIRED

    y_train: pandas.Dataframe to be extracted to positive-unlabeled.

    OPTIONAL

    pos_rate: positive rate (if between 0 and 1) or positive literal number (greater than one).
    pos_rate will default to 0.8 if no value is specified.
    '''

    if pos_rate > 0:
        if pos_rate < 1:
            pos_total = math.floor(pos_rate * len(y_train[y_train == 1]))

        if pos_rate > 1:
            pos_total = pos_rate

        y_train = y_train.sample(frac=1).reset_index(drop=True)

        pos_actual = 0
        for index, _ in enumerate(y_train):
            if(y_train.loc[index] == 1):
                if pos_actual < pos_total:
                    pos_actual += 1
                else:
                    y_train.loc[index] = 0
            
            else:
                y_train.loc[index] = 0

        return y_train

    else:
        raise ArithmeticError('pos_rate must be greater than 0')
