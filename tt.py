def find_peak(list_of_integers):
    length = len(list_of_integers)
    if length == 0:
        return None
    if length == 1:
        return (list_of_integers[0])
    if length == 2:
        return list_of_integers[0] if list_of_integers[0] >= list_of_integers[1] else list_of_integers[1]

    for idx in range(0, length):
        value = list_of_integers[idx]
        if (idx > 0 and idx < length - 1 and
                list_of_integers[idx + 1] <= value and list_of_integers[idx - 1] <= value):
                return value
        elif idx == 0 and list_of_integers[idx + 1] <= value:
            return value
        elif idx == length - 1 and list_of_integers[idx - 1] <= value:
            return value
    return None