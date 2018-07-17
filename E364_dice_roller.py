from random import randint

print("E364 Dice Roller")

dice = input("Enter a combination! \n").split("d")
result = []

for i in range(0, int(dice[0])):
    result.append(randint(1, int(dice[1])))

print(str(sum(result)) + ":" , result)