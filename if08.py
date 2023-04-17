def main(a):
    """
    Given an integer a, check the following conditions:
    "two-digit odd number",
    "two-digit even number",
    "three-digit odd number",
    "three-digit even number"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    if a//10>=1 and a%2!=0:
        s="two-digit odd number"
    if a//10>=1 and a%2==0:
        s="two-digit even number"
    if a//100>=1 and a%2!=0:
        s="three-digit odd number"
    if a//100>=1 and a%2==0:
        s="three-digit even number"

  
    return s 
print(main(57))