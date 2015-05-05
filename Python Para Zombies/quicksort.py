#quickSort usando linguagem funcional
def quicksort(v) :
    if len(v) <=1:
        return v

    pivot = v[0]
    equals = [x for x in v if x == pivot]