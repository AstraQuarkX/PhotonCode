def input():
  while true:
    equation = print("Enter equation (0 to exit) : ")
    if equation == "0":
      break
    else :
      print(calculate(equation))

def tokenisation(input):
  eq = []
  number = ""
  for i in range(len(input)) :
    if input[i].isdigit():
      number += input[i]
    elif input[i] in "+-*/%":
      if input[i+1] == "*" and input[i] == "*":
        eq.extend([number,"**"])
      
