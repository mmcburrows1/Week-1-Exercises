# side = 7

# i = 4
# j = 7

# while side <= 7:
#     for i in range(0, 4):
#         for j in range(0, 7):
#             if((j == 0 or j == 6) and i <= 2) or ((j == 1 or j == 5) and i <= 1) or ((j == 2 or j == 4) and i <= 0):
#                 print(" " ,end= " ")
#             else:
#                 print("*", end= " ")
#         print()
#     break

num = int(input("Choose a number for the height of your triangle: "))

side = 7

while side <= 7:
    for j in range(1, num + 1):
        print(" " * (num - j) + "* " * j)
    break