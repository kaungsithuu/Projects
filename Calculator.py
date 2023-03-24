print("This a calculator using python language.")
num1 = float(input("What is your first numer: "))
print("""Choose 
+ for addition
- for subtraction 
* for multiplication
/ for division
""")
operator = (input("Operator: "))
num2 = float(input("What is your second number: "))
if operator == "+":
    ans = num1 + num2
if operator == "-":
    ans = num1 - num2
if operator == "*":
    ans = num1 * num2
if operator == "/":
    ans = num1 / num2
    print(num1, operator, num2, "=", ans)
else:
  print("Invalid operator")