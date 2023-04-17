def main(temp):
    """
    Display the message according to the following temperature conditions given to you in Celsius:
    Temp<0: "Freezing"
    Temp 1-10: "Very Cold"
    Temp 11-20: "Cold"
    Temp 21-30: "Normal"
    Temp 31-40: "Hot"
    Temp >40: "Very Hot"

    Args:
        temp: integer
    Returns:
        string: the message to print
    """
    if temp<0:
        s="freezing"
    if 1<=temp<10:
        s="very cold"
    if 11<=temp<20:
        s="cold"
    if 21<=temp<30:
        s="normal"
    if 31<=temp<40:
        s="hot"
    if temp>40:
        s="very hot"
    return s
a=int(input()) 
print(main(a))