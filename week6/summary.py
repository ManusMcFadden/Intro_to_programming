def summarise_data(file, col_index):
    if col_index > 2 or col_index < 0 or not isinstance(col_index, int):
        raise IndexError("col_index out of range.")
    max = 0
    min = float('inf')
    sum = 0
    count = 0
    with open(file, "r") as fileObject:
        while True:
            line = fileObject.readline()
            if line == "":
                break
            else:
                splitLine = line.split(",")
                try:
                    int(splitLine[col_index])
                except:
                    raise ValueError("invalid value in data.")
                count += 1
                sum += int(splitLine[col_index])
                if int(splitLine[col_index]) > max:
                    max = splitLine[col_index]
                if int(splitLine[col_index]) < min:
                    min = splitLine[col_index]
    mean = round(sum / count, 2)
    outputList = [max, min, sum, count, mean]
    return outputList


if __name__ == "__main__":
    #  test valid arguments
    print(summarise_data("data.txt", 1))

    #  test out of range col_index, data.txt only has 3 columns
    print(summarise_data("data.txt", 5))

    # test invalid col_index, col_index should be integer
    print(summarise_data("data.txt", "a"))

    # test invalid value in file, contains a "abc" in the second column
    print(summarise_data("data2.txt", 1))
