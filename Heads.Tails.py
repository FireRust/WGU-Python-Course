import random

#print(dir(random))
#help(random.random)

coin_toss = input("Heads or Tails? ").lower()

toss_coin = random.random()

if 0 < toss_coin < 0.5:
    print("It was Heads!")
else:
    print("It was Tails!")

print(toss_coin)


h_t = random.randint(0, 1)
if h_t == 0:
    print("Heads")
else:
    print("Tails")