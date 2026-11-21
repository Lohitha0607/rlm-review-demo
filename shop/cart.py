def total(items):
    return sum(item.price for item in items)


def average(items):
    return total(items) / len(items)
