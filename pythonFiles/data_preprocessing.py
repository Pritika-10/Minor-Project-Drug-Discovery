
import pandas as pd

def load_data(file_path):
    """Load the dataset from a CSV file."""
    return pd.read_csv(file_path)

def clean_data(df):
    """Clean and preprocess the data."""
    # Example: Remove rows with missing SMILES
    return df.dropna(subset=['SMILES'])
