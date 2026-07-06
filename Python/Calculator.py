def tokenisation(equation):
    eq = []
    num = ""
    for i in range(0, len(equation)):
        if equation[i].isdigit() or equation[i] == ".":
            num += equation[i]
        elif equation[i] in "+-*/%" and equation[i-1] not in "+-*/%":
            if equation[i] == "*" and equation[i+1] == "*":
                operator = "**"
            elif equation[i] == "/" and equation[i+1] == "/":
                operator = "//"
            elif equation[i] in "+-*/%" and equation[i+1] not in "*/":
                operator = equation[i]
            if num =="":
                eq += [operator]
            else: 
                eq += [float(num),operator]
                num = ""
    eq += [float(num)]
    if eq[0] == "-":
        eq = [-eq[1]] + eq[2::]
    return eq

def calculation(e):
    val = e.copy()
    while len(val) > 1:
        if "**" in val:
            o = val.index("**")
            val.insert(o-1,val[o-1]**val[o+1])
            del val[o:o+3]
        elif "*" in val:
            o = val.index("*")
            val.insert(o-1,val[o-1]*val[o+1])
            del val[o:o+3]
        elif "/" in val:
            o = val.index("/")
            val.insert(o-1,val[o-1]/val[o+1])
            del val[o:o+3]
        elif "//" in val:
            o = val.index("//")
            val.insert(o-1,val[o-1]//val[o+1])
            del val[o:o+3]
        elif "%" in val:
            o = val.index("%")
            val.insert(o-1,val[o-1]%val[o+1])
            del val[o:o+3]
        elif "-" in val:
            o = val.index("-")
            val.insert(o-1,val[o-1]-val[o+1])
            del val[o:o+3]
        elif "+" in val:
            o = val.index("+")
            val.insert(o-1,val[o-1]+val[o+1])
            del val[o:o+3]
    print(f"= {round(val[0],4)}")

while True:
    a = str(input("Enter equation (0 to exit) : "))
    if a == "0":
        break
    else:
        calculation(tokenisation(a))
