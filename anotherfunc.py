# classification func


def classify(array):
    total = sum(array)
    avg = total/len(array)
    if abs(avg - 40) < abs(avg - 80):
        return 40
    else:
        return 80
