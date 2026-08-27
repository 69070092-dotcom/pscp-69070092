"""[LEARNING LOGS] จำนวนในช่วง [A,B] ที่หารด้วย d เหลือเศษ r"""
A = int(input())
B = int(input())
D = int(input())
R = int(input())

count = 0

for i in range(A,B + 1):
    if i % D == R:
        count += 1

print(count)
