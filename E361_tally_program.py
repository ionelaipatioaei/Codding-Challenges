print("E361 Tally Program")

code = list(input("Please enter the string \n"))
points = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0}

# Little error checking, needs work!
# for item in code:
#     for check in ("a", "b", "c", "d", "e"):
#         if item == check or item == check.upper():
#             break
#         else:
#             print(f"Unknown letter found in code: {item}")
#             break

for i in range(0, len(code)):
    if code[i] == code[i].lower():
        points[code[i].lower()] += 1
    elif code[i] == code[i].upper():
        points[code[i].lower()] -= 1

print(points)
