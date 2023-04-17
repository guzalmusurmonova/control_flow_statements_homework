def main(a):
    """
    The two-digit integer is given.
    Replace the digits of the number.
    True if the resulting number is less than or equal to the old number, otherwise return False.
    
    Args:
        a: integer
    Returns:
        boolean: True if the resulting number is less than or equal to the old number, otherwise return False.
    """
    x1=a%10
    x2=a//10
    y=10*a//10+a%10
    if y<a:
        s="true"
    if y>a:
        s="false"
    return s 
print(main(57))