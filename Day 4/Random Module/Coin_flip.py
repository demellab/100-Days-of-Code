import random

random_no = random.randrange(0,100)
print(random_no)

if random_no % 2 == 0:
    print("Even")
else:
    print("Odd")