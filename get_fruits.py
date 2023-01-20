import csv
def get_fruits(file_path: str):
    """
    Reads the file file_path and returns a list of fruits
    
    Args:
        file_path (str): absolute file path
    Returns:
        list: list of fruits
    """
    f=open(file_path)
    ans=csv.reader(f)
    return list(ans)
print(get_fruits('fruits.csv'))
