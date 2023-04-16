def main(a):
    """
    If the number is positive, increase it to 1,if the number is negative decrease it to 2.
    If it is 0, assign 10.
    Args:
        a: integer
    Returns:
        a: integer
    """
    if a>0:
        x=a+1
    if a<0:
        x=a-2
    if a==0:
        x=10
    return x
a=int(input())
print(main(a))