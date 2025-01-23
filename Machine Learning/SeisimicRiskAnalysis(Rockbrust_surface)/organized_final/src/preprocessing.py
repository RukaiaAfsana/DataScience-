import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder

def load_data(file_path):
    print(file_path)
    return pd.DataFrame(pd.read_excel(file_path)) 



import pandas as pd

def handle_missing_values(df, strategy='mean', fill_value=None):
    """
    Handle missing values in a DataFrame using different imputation strategies.

    Args:
        df (pd.DataFrame): Input DataFrame.
        strategy (str): Imputation strategy ('mean', 'median', 'mode', 'constant').
        fill_value (any, optional): Value to fill missing data if strategy is 'constant'.

    Returns:
        pd.DataFrame: DataFrame with missing values handled.
    """
    if df.isnull().sum().sum() == 0:
        print("No missing values found in the DataFrame.")
        return df

    df_filled = df.copy()

    # Separate numeric & categorical columns
    numeric_cols = df.select_dtypes(include=['number']).columns
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns  # For text & categorical features

    if strategy in ['mean', 'median']:
        if not numeric_cols.empty:
            if strategy == 'mean':
                df_filled[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
            elif strategy == 'median':
                df_filled[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())

    elif strategy == 'mode':
        for col in df.columns:
            df_filled[col] = df[col].fillna(df[col].mode()[0])  # Mode for both numeric & categorical

    elif strategy == 'constant':
        if fill_value is None:
            raise ValueError("fill_value must be provided when strategy is 'constant'.")
        df_filled = df.fillna(fill_value)

    else:
        raise ValueError("Strategy not supported. Choose from 'mean', 'median', 'mode', or 'constant'.")

    return df_filled




def drop_columns_with_high_nulls(df, threshold=0.95):
    """Drop columns where a high proportion of values are missing (NaN).

    Args:
        df (pd.DataFrame): Input DataFrame.
        threshold (float): Proportion threshold for dropping columns (default is 0.95).

    Returns:
        pd.DataFrame: DataFrame with columns dropped.
    """
    null_ratio = df.isnull().mean()  # Compute the proportion of null values per column
    cols_to_drop = null_ratio[null_ratio >= threshold].index  # Select columns exceeding threshold
    print(f"Columns dropped: {list(cols_to_drop)}")  # Display dropped columns
    #df=  df.drop(columns=cols_to_drop,inplace = True)
    #print(df.isnull().sum())
    return df.drop(columns=cols_to_drop)



def encode_categorical_columns(df):
    """Encode categorical columns using Label Encoding."""
    label_encoders = {}
    for column in df.select_dtypes(include=['object']).columns:
        le = LabelEncoder()
        df[column] = le.fit_transform(df[column])
        label_encoders[column] = le
    return df, label_encoders



def scale_features(df):
    """Scale numerical features using Standard Scaler."""
    scaler = StandardScaler()
    df[df.columns] = scaler.fit_transform(df[df.columns])
    return df, scaler


def data_info(df):
    print(df.info())
    print(df.isnull().sum())

def remove_white_extra_white_Space(df):
    df.columns = df.columns.str.strip()  # Remove extra spaces from column names
    return df






def preprocess_data(df):
    print("Before Preprocessing: ")
    data_info(df)
    """Complete preprocessing pipeline."""
    df = remove_white_extra_white_Space(df)
    df= drop_columns_with_high_nulls(df)
    df = handle_missing_values(df,"mode")
    print("After Preprocessing: ")
    data_info(df)
    
    #df, label_encoders = encode_categorical_columns(df)
    #df, scaler = scale_features(df)
    return df #, label_encoders, scaler
