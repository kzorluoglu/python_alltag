# Input
age = input("Please type your Age: ")
print(age)

# Example Inputs
weightStr = input("Please type your Weight (kg): ")
heightStr = input("Please type your Body Height (m): ")

weight = float(weightStr)
height =  float(heightStr)

bmi = weight / height ** 2
print("BMI Score is : " + str(bmi))
