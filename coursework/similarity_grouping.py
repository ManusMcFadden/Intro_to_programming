def similarity_grouping(data: list) -> list:
    list_output = []
    if isinstance(data, list) is False:
        return list_output
    for item1 in data:
        #if isinstance(item1, int):
            #integer = True
        found = False
        for item2 in list_output:
            if item1 in item2:
                item2.append(item1)
                found = True
        if found is False:
            list_output.append([item1])
    return list_output
if __name__ == "__main__":
    data1 = [2, 1, 2, 1]
    data2 = [5, 4, 5, 5, 4, 3]
    data3 = [1, 2, 1, 3, 'a', 'b', "a",  'c']
    print(similarity_grouping(data1))
    print(similarity_grouping(data2))
    print(similarity_grouping(data3))