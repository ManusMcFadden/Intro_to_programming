"""
Introduction to Programming Coursework 1

@author: Manus McFadden
"""


def valid_puzzle(puzzle: list) -> bool:
    valid = True  # will be the returned variable
    # length of first item that all other lengths will be checked against
    length = len(puzzle[0])
    for item in puzzle:  # iterate through each item
        if len(item) != length:  # make sure all items have the same length
            valid = False
        if isinstance(item, str) is False:  # make sure all the items are strings
            valid = False
    if isinstance(puzzle, list) is False:  # make sure the puzzle input was a list
        valid = False
    return valid


def similarity_grouping(data: list) -> list:
    list_output = []  # create list to be returned
    if isinstance(data, list) is False:  # make sure the input is a list
        return list_output
    for item1 in data:
        found = False  # tracks whether there is a similarity between lists
        for item2 in list_output:  # check for every item already added to the output list
            if str(item1) in item2:  # check for similarity between two lists
                item2.append(item1)  # add to nested list
                found = True
        if found is False:  # add first instance if none is already there
            list_output.append([item1])
    return list_output
# is int 1 same as str1


def highest_count_items(data: str) -> list:
    # list of items separated by their commas in the string
    list_input = data.split(",")
    list_spaceless = []  # list of items after the spaces have been removed
    dict_count = {}  # dictionary comtaining the item as the key and the count as the value
    list_letters_added = []  # list of all items that have been added to the dictionary
    list_greatest = []  # list of the items with most instances
    list_output = []  # list to be returned
    for item in list_input:  # iterate through items in the input list
        # remove spaces and add to new list
        list_spaceless.append(item.strip())
    for item in list_spaceless:  # iterate through the spaceless list and if the letter has not been seen before, add it to the dictionary, othjerwise add one to its count
        if item not in list_letters_added:
            dict_count.update({item: 1})
            list_letters_added.append(item)
        else:
            dict_count[item] += 1
    for i, key in enumerate(dict_count):
        if len(list_greatest) == 0:  # add an initial value to the list to compare others against
            list_greatest.append(key)
        # if there is a new highest replace everything
        elif dict_count[key] > dict_count[list_greatest[0]]:
            list_greatest = []
            list_greatest.append(key)
        # if there is a new joint highest add it
        elif dict_count[key] == dict_count[list_greatest[0]]:
            list_greatest.append(key)
    # add the keys and values to a nested list like the output requires
    for i in range(len(list_greatest)):
        list_output.append([])
        list_output[i].append(list_greatest[i])
        list_output[i].append(dict_count[list_greatest[i]])
    return list_output


def valid_char_in_string(popList: list, charSet: list) -> bool:
    valid = True  # variable to be returned
    if not isinstance(popList, list):  # make sure the entered poplist is a list
        return False
    if not isinstance(charSet, list):  # make sure charset is a list
        return False
    for character in charSet:  # make sure every item in charset is a character
        if len(character) > 1:
            return False
        if not isinstance(character, str):
            return False
    for item in popList:
        if not isinstance(item, str):  # make sure every item in the poplist is a string
            return False
        for character in item:  # make sure every item in the poplist only contains characters in the character set
            if character not in charSet:
                valid = False
    return valid


def total_price(unit: int) -> float:
    unit = int(unit)  # turn the input to an integer if it is not already
    six_packs = unit // 6  # find the number of 6 packs
    # find the remainder to get the number of singles after the 6 packs have been grouped
    single_units = unit % 6
    # work out the price before discount based on the prices for 6 packs and doubles
    added_price = six_packs * 5 + single_units * 1.25
    if added_price >= 20:  # award 10 percent discount if price is over 20
        total = added_price * 0.9
    else:
        total = added_price
    return total  # return total price


if __name__ == "__main__":
    # sample test for task 1.1
    puzzle1 = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
               'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
               'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']

    puzzle2 = ['NAROUNDDL', 'EDCIT', 'UWSWEDZYA', 'OTCONVOYV',
               'BOSEVRUCI', 'BLLCGLPBD', 'TEENAGEDL', 'TREWZLCGY',
               'RAPLEBAYG', 'ATYTBIWRA', 'YEMROFINU']

    puzzle3 = ['RUNAROU', ['EDCITOA'], ('ZYUWSWE'), 'AKOTCYV',
               'LSBOSEI', 'BOBLLCG', 'LKTEENA', 'ISTREWY',
               'AURAPLE', 'RDATYTB', 'TEYEMRO']
    puzzle4 = 'roundandround'
    print(valid_puzzle(puzzle1))
    print(valid_puzzle(puzzle2))
    print(valid_puzzle(puzzle3))
    print(valid_puzzle(puzzle4))

    # sample test for task 1.2
    data1 = [2, 1, 2, 1]
    data2 = [5, 4, 5, 5, 4, 3]
    data3 = [1, 2, 1, 3, 'a', 'b', "a",  'c']
    print(similarity_grouping(data1))
    print(similarity_grouping(data2))
    print(similarity_grouping(data3))

    # sample test for task 1.3
    data4 = ("3, 13, 7, 9, 3, 3, 5, 7, 12, 13, 11, 13, 8, 7, 5, 14, 15, 3, 9,"
             "7, 5, 9, 14, 3, 8, 2, 5, 5, 8, 14, 11, 11, 12, 8, 5, 3, 3, 10,"
             "3, 10, 7, 7, 10, 10, 2, 7, 4, 8, 1, 5")
    data5 = ("British Gas, British Gas, Ovo, Igloo, Igloo, Octopus, Bulb,"
             "Shell, E.ON, Npower, British Gas, Octopus, Igloo, Npower, Igloo,"
             "Shell, Scottish Power, Bulb, EDF, Bulb, EDF, Bulb,"
             "Scottish Power, Octopus, Scottish Power, Octopus, Octopus, EDF,"
             "Ovo, Shell, Octopus, E.ON, British Gas, Bulb, Npower, Shell,"
             "Scottish Power, Npower, Scottish Power, Npower")
    data6 = ("aac, ctt, gat, ccc, gcc, ctg, gtc, tcg, ccg, cca, ata, cca,"
             "tat, ata, cac, gcg, cca, gta, gtg, gac, taa, ata, gtc, aat, gct,"
             "gta, ggc, tgc, tca, ctt, tgt, ata, acc, tgc, gac, cgc, atc, cgt,"
             "tac, agg, ctt, cgc, cgc, tgg, gcg, tgg, taa, cta, aaa, tgc, cgt,"
             "tgc, gac, tta, aag, taa, act, cca, tac, agg, cgc, gtg, cca, gcg,"
             "gtt, gag, tca, aca, tct, gta, ata, ctt, gat, tcg, tcg, cac, cgt,"
             "tac, caa, aac, ctg, tgt, aag, ttc, ccc, tcc, ctc, cct, aga, gtt,"
             "tga, gaa, cct, ctc, tct, ggt, gcc, tct, ccc, agt, caa, gac, ccc,"
             "cgc")
    print(highest_count_items(data4))
    print(highest_count_items(data5))
    print(highest_count_items(data6))

    # sample test for task 1.4
    popList1 = ['00000', '00001', '00010', '00011', '00100']
    popList2 = ['aac', 'ctt', 'gat', 'ccc', 'gcc', 'ctg', 'gtc', 'tcg',
                'ccg', 'cca', 'ata']
    popList3 = ['aac', 'ctt', 'gat', 'ccc', 'gcc', 'ctg', 'gtc']
    charSet1 = ['0', '1']
    charSet2 = ['a', 'c', 't', 'g']
    charSet3 = ['a', 'c']
    charSet4 = '01'
    print(valid_char_in_string(popList1, charSet1))
    print(valid_char_in_string(popList2, charSet2))
    print(valid_char_in_string(popList3, charSet3))
    print(valid_char_in_string(popList1, charSet4))

    # sample test for task 1.5
    print(total_price(3))
    print(total_price(12))
    print(total_price(15))
    print(total_price(26))
