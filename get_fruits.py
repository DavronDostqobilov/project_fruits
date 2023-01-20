def get_fruits(file_path: str):
    """
    Reads the file file_path and returns a list of fruits
    
    Args:
        file_path (str): absolute file path
    Returns:
        list: list of fruits
    """
    f=open(file_path)
    ans=f.read()
    ans=ans.split('\n')
    list1=[]
    for i in ans:
        list1.append(i.split(','))
    return list1
print(get_fruits('fruits.csv'))
