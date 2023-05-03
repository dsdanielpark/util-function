import numpy as np


def convert(x):
    x = x.strip()
    x = x[1:-1]
    x = np.fromstring(x, sep=" ")
    return x


def col_convert(df, columns):
    """Restores a column whose array is stored as a string type back to an array type.

    :param df: pd.DataFrame object
    :type df: _type_
    :param columns: Column name where array is stored as string type(str, list)
    :type columns: _type_
    :return: pd.DataFrame object
    :rtype: _type_
    """
    if type(columns) == list:
        for col in columns:
            df[col] = df[col].apply(convert)
    elif type(columns) == str:
        df[col] = df[col].apply(convert)
    else:
        print("Only str or list are allowed as column arguments.")

    return df
