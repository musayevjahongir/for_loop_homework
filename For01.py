def main(n):
    """
    Return numbers from zero to n in a list view.
    Args:
        n: int
    Returns:
        list: return  answer
    """
    a=[]
    for i in range(0,n):
        a.append(i)
    return a
print(main(5))
