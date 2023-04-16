def main(a):
    a=int(input())
    """
    If the number is positive, increase it to 1,otherwise leave unchanged.
    Args:
        a: integer
    Returns:
        a: a increased by 1 if positive, else unchanged.
    """
    if a>0:
        x=a+1
    if a<0:
        x=a
    return x
print(main('a')) 

