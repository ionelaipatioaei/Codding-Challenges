print("E365 Arrow-up Notation")
print("Use '|' to represent an arrow and put a space between the elements \n Example: 2 || 4")

calculate = input("Please enter the numbers which you want calculate \n").split(" ")

def up_arrow(a, arrows, b):
    if arrows == 1:
        return a ** b
    if arrows >= 1 and b == 0:
        return 1
    return up_arrow(a, arrows - 1, (up_arrow(a, arrows, b - 1)))

print("Your result is:", up_arrow(int(calculate[0]), len(calculate[1]), int(calculate[2])))