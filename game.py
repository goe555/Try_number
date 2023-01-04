import random
target = random.randint(0, 10)
count = 0
while True:
    n = int(input("Enter a number 0-10  :"))
    count += 1
    if n < target:
        print("low")
    elif n > target:
        print("high")
    else:
        print("-------You Win-------")
        break
print("You try %d time" % count)