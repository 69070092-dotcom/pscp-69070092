Status = input()
num = int(input())

total = 0

for i in range(num):
    price = float(input())
    total += price

if Status == "Y":
    total = total * 0.95
elif Status == "N" and total >= 500:
    total = total * 0.97
else:
    total = total

total = total + 0.0000001
print(f"{total:.2f}")
