
def find_operator(string):
    for op in string:
        if op=="+":
            return op
        elif op=="-":
            return op
        elif op=="*":
            return op
        elif op=="/":
            return op

def calculation(num1,num2,op):
    if op=="+":
        return num1+num2;
    elif op=="-":
        return num1-num2;
    elif op=="*":
        return num1*num2;
    elif op=="/":
        return num1/num2;

inp = input("Enter the Celculation: ")
op=find_operator(inp)
index=inp.index(op)
num1=int(inp[0:index])
num2=int(inp[index:len(inp)])
print("Result is",calculation(num1,num2,op))
print("thank you")
