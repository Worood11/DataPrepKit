import numpy as np
import pandas as pd

def read_csv(file_path):
    return pd.read_csv(file_path)

def read_excel(file_path):
    return pd.read_excel(file_path)

def read_json(file_path):
    return pd.read_json(file_path)

def generate_summary(data):
    summary = {
        'num_rows': len(data),
        'num_columns': len(data.columns),
        'column_names': data.columns.tolist(),
        'missing_values': data.isnull().sum().to_dict(),
        'mean': data.mean().to_dict(),
        'median': data.median().to_dict(),
        'mode': data.mode().to_dict(),
    }
    return summary

def handle_missing_values(data, strategy='remove'):
    if strategy == 'remove':
        return data.dropna()
    elif strategy == 'impute':
        data.replace([np.inf, -np.inf], np.nan, inplace=True)  # Convert inf to NaN for imputation
        for column in data.select_dtypes(include=['float64']).columns:
            data[column].fillna(data[column].mean(), inplace=True)
        return data
    else:
        raise ValueError("Invalid strategy. Choose from 'remove' or 'impute'.")

def encode_categorical_data(data):
    return data

