def test_number(a, b, c):
    if a == b or abs(b - a) == 1 and a == c or abs(a - c) == 1 and b == c or abs(c - b) == 1:
        return False
    else:
        return True


x = int(input("Please enter your first value: "))
y = int(input("Please enter your second value: "))
z = int(input("Please enter your third value: "))

print (test_number(x, y, z))
