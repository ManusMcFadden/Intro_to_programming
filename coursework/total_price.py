def total_price(unit: int) -> float:
    unit = int(unit)
    six_packs = unit // 6
    single_units = unit % 6
    added_price = six_packs * 5 + single_units * 1.25
    if added_price >= 20:
        total = added_price * 0.9
    else:
        total = added_price
    return total
if __name__ == "__main__":
    print(total_price(3))
    print(total_price(12))
    print(total_price(15))
    print(total_price(26))