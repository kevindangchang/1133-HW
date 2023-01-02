print("enter rod size")
rod = int(input())
twenty_Five = int(rod/25)
print(twenty_Five, "rods each 25 feet")
remainder = rod % 25
ten = int(remainder/10)
print(ten, "rods each 10 feet")
remainder2 = remainder % 10
print(remainder2, "rods each one feet")


