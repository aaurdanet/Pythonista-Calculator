from art import logo


#Add
def add(n1, n2):
  return n1 + n2


#Subtract
def subtract(n1, n2):
  return n1 - n2


#Multiply
def multiply(n1, n2):
  return n1 * n2


#Divide
def divide(n1, n2):
  return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
  print(logo)
  num1 = float(input("What is the first number? "))

  for symbol in operations:
    print(symbol)

  keepGoing = True

  while keepGoing:

    operation_symbol = input("Pick an operatior: ")
    num2 = float(input("What's the next number? "))

    calculation_function = operations[operation_symbol]

    Fanswer = calculation_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {Fanswer}")

    yesno = input(
        f"Type 'y' to continue calculating with {Fanswer}, or type 'n' to reset and start new calculation: "
    )

    if yesno == "y":
      num1 = Fanswer
    else:
      keepGoing = False
      calculator()


calculator()

