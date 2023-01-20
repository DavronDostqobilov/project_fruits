def get_frutis_name(data:str)->list:
    """
    This function returns the names of the fruits

    args:
        data: CSV file with the fruits data
    returns:
        list: list of fruits names
    """
    f=open(data)
    ans=f.read()
    ans=ans.split('\n')
    list1=[]
    javob=[]
    for i  in ans:
        list1.append(i.split(','))
    list1.pop(0)
    for j in list1:
        javob.append(j[0])
    return javob
print(get_frutis_name('fruits.csv'))

    