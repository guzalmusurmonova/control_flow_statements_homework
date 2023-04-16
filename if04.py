def main(a,b,c):
    """
    Find number of positive numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of positive numbers in the given numbers
    """
    if a>0:
        x=a//a
    if a<0:
        x=0
    if b>0:
        x=b//b+x
    if b<0:
        x=0
    if c>0:
        x=c//c+x
    if c<0:
        x=0
    return x
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
print(main(a,b,c))