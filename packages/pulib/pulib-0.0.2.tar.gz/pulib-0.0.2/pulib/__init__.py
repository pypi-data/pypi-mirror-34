import math

def generate_pu_data(dataframe, data_column, pos_class, pos_size=0.8):
    '''
    Function to generate random positive-unlabeled data from any dataset. It returns the same dataset with a 'y' column containing the positive-unlabeled data.
    REQUIRED:
    dataframe = pd.Dataframe to be extracted to positive unlabeled.
    data_column = dataframe column to be compared to extract the positive class.
    pos_class = class in the data_column to be considered as positive.
    OPTIONAL:
    pos_size = positive rate (if between 0 and 1) or positive literal number (greater than one).
    pos_size will default to 0.8 if no value is specified.
    '''
    if pos_size >= 0:
        if pos_size < 1:
            positive_total = math.floor(pos_size * len(dataframe.loc[:, data_column]))

        if pos_size > 1:
            positive_total = pos_size

        positive_number = 0
        for index, value in enumerate(dataframe.loc[index, data_column].sample(frac=1)):
            if positive_number < positive_total and value == pos_class:
                dataframe.loc[index, 'y'] = 1
            else:
                dataframe.loc[index, 'y'] = 0

        return dataframe
