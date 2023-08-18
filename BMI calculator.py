Weight = input("Enter your weight in kgs: ")
Height = input("Enter your height in cms: ")
M = (float(Height) * 0.01)
M_square = M * M
BMI = float(Weight) / float(M_square)
print("Your BMI is " + str(BMI))
