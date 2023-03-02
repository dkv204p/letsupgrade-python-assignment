# Taking input from user for Principal amount, time and rate of interest
P = float(input("Enter the principal amount: "))
T = float(input("Enter the time in years: "))
R = float(input("Enter the rate of interest: "))

# Calculating Simple Interest
SI = (P * T * R) / 100

# Displaying the result
print("The Simple Interest is:", SI)
