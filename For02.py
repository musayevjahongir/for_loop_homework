def main(n):
    """
    Return numbers from zero to n in a string view.
    Args:
        n: int
    Returns:
        string: return  answer
    """
    a=[]
    for i in range(n):
        a.append(str(i))
    return ",".join(a)
print(main(3))