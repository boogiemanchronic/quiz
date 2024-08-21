print("Welcome to tht planet quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What is the third planet from the sun? ")
if answer.lower() == "venus":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What planet has rings? ")
if answer.lower() == "saturn":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What is the largest planet? ")
if answer.lower() == "jupiter":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")


print("You got " + str(score) + " questions correct!")
print("You got " + str((score /3 ) * 100) + "%.")