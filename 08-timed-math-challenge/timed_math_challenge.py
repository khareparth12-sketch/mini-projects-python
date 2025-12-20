import random
import time

OPERATOR = ["+", "-", "*", "/", "%"]
MIN_OPERAND = 1
MAX_OPERAND = 100
TOTAL_PROBLEMS = 10

def generate_prob():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATOR)

    exp = str(left) + " " + operator + " " + str(right)
    answer = eval(exp)
    return exp, answer

wrong = 0

input("Press enter to start!")
print("---------------------------")

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    exp, answer = generate_prob()
    print(f"Problem #{i} is: {exp} = ?")
    guess = input()
    
    while True:
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
total_time = round(end_time - start_time, 2)

print("---------------------------")
print(f"Nice work! You took {total_time} seconds!")