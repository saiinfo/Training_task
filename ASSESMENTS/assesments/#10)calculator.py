#calculator
#add
def add(x,y):
    return x+y
#subtract
def subtract(x,y):
    return x-y
#multiply
def multiply(x,y):
    return x*y
#divide
def divide(x,y):
    return x/y

print("Select options:")
print("1:Addition")
print("2:Subtraction")
print("3:Multiply")
print("4:Divide")

while True:
    choice = input("Enter choice(1/2/3/4): ")
    if choice in ('1', '2', '3', '4'):
        try:
            number1 = float(input("Enter first number: "))
            number2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if choice == '1':
            print(number1, "+", number2, "=", add(number1, number2))
        elif choice == '2':
            print(number1, "-", number2, "=", subtract(number1, number2))
        elif choice == '3':
            print(number1, "*", number2, "=", multiply(number1, number2))
        elif choice == '4':
            print(number1, "/", number2, "=", divide(number1, number2))
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")