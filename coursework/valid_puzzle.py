def valid_puzzle(puzzle: list) -> bool:
    valid = True
    length = len(puzzle[0])
    for item in puzzle:
        if len(item) != length:
            valid = False
        if isinstance(item, str) is False:
            valid = False
        