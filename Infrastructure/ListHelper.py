def isNextElement(generalArray: list ,array: list, element):
    index = findIndex(generalArray, element)
    if generalArray[index-1] == array[-1].rank:
        return True
    return False

def findIndex(generalArray, element):
    for index, item in enumerate(generalArray):
        if item == element:
            return index
    return None
