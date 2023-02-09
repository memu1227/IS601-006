import sys
#a = sys.maxsize
#a *= sys.maxsize
#print(f"a is {a}")
a = 0
#b = 0
for i in range(5):
    #b += 0.1
    if i % 2 == 0:
        a += 1
    if a % 2 == 0:
        a -= 1
    #print(f"b: {b}")
print(f"a is {a}")

#its 1 bc it starts at 0 and then stops at 1
