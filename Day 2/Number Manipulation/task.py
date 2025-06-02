bmi = 84 / 1.65 ** 2
print(bmi)

print(int(bmi)) #flooring the number to the lowest whole number

print(round(bmi)) #will round it to the closest whole number

print(round(bmi,3))

#assignment operators

score = 3
score += 1
print(score)

#F strings
print("Your score is: ", score)

#example of F Strings
score = 3
height = 104.4
weight = 45

print(f"Your score is = {score}, your height is: {104.4}, your weight is: {weight}")