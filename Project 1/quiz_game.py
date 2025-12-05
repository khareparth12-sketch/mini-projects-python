print("Welcome to the Quiz Game!")

playing  = input("Do you want to play? ")

if playing.lower() != "yes":
    print("Maybe next time!")
    quit()

print("Great! Let's start the game.")
score =0

answer = input("What is the capital of France? ")
if answer.lower() == "paris":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is Paris.")
    
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is Central Processing Unit.")

answer = input("Which planet is known as the Red Planet? ")
if answer.lower() == "mars":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is Mars.")

answer = input("How many states are there in the United States? ")
if answer.lower() == "50":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is 50.")

answer = input("What is the largest ocean on Earth? ")
if answer.lower() == "pacific ocean":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is Pacific Ocean.")

if score == 5:
    print("Amazing! You got all questions correct!")
elif score >= 3:
    print("Well done! You scored", score, "out of 5.")
elif score >= 1:
    print("You scored", score, "out of 5. Better luck next time!")
else:
    print("You scored 0 out of 5. Don't give up, try again!")