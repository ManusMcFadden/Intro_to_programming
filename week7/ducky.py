class ducky:

    def __init__(self, iterable):
        self.iterable = iterable

    def sum_iter_value(self):
        iterable = self.iterable
        iter_to_test = []
        sum = 0
        if isinstance(iterable, str):
            iter_to_test = iterable.replace(" ", ",").split(',')
        else:
            iter_to_test = iterable
        for item in iter_to_test:
            if not isinstance(item, int):
                if item.isnumeric():
                    sum += float(item)
            else:
                sum += item
        return sum
