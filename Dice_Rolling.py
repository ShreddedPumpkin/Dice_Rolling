from ask_user import ask_user
    
import random

min_ = ask_user("Please input the minimum number of your dice: ", int)
max_ = ask_user("Please input the maximum number of your dice: ", int, lambda x: x > min_, "Maximum must be larger than minimum.")
n = ask_user("How many times do you want to roll the dice: ", int)

rolls = [random.randint(min_, max_) for _ in range(n)]
for roll in rolls:
    print(roll)

print("Dice rolling simulator has ended")