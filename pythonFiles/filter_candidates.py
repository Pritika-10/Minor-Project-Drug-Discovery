
def filter_by_score(df, threshold):
    """Filter molecules by docking score threshold."""
    return df[df['Docking_Score'] < threshold]
