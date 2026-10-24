"""[LEARNING LOGS] B - Fully pair?"""
word = input()
unpaired = ""

for i in word:
    if (word.count(i)) % 2:
      if i not in unpaired:
        unpaired += i

if not unpaired:
    print("fully paired")
else:
    print(unpaired)
