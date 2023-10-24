def valid_char_in_string(popList: list, charSet: list) -> bool:
    valid = True
    #check for chars in charset
    if not isinstance(popList, list):
        return False
    for item in popList:
        if not isinstance(item, str):
            return False
    if not isinstance(charSet, list):
        return False
    for character in charSet:
        if len(character) > 1:
            return False
        if not isinstance(character, str):
            return False
    for item in popList:
        if not isinstance(item, str):
            return False
        for character in item:
            if character not in charSet:
                valid = False
    return valid
if __name__ == "__main__":
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