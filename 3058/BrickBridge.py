"""[LEARNING LOGS] BrickBridge"""
a = int(input())
b = int(input())
c = int(input())

big = min(b, c // 5)
remaining = c - (big * 5)

if remaining <= a:
    print(remaining)
else:
    print(-1)
