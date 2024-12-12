# def calculate(expression): #for more than 1 operators
#     # Remove leading and trailing whitespace from the expression
#     expression = expression.strip()

#     # Check for each operator and recursively calculate the result
#     for i in range(len(expression)):
#         if expression[i] == "+":
#             return calculate(expression[:i]) + calculate(expression[i+1:])
#         elif expression[i] == "-":
#             return calculate(expression[:i]) - calculate(expression[i+1:])
#         elif expression[i] == "*":
#             return calculate(expression[:i]) * calculate(expression[i+1:])
#         elif expression[i] == "/":
#             return calculate(expression[:i]) / calculate(expression[i+1:])
    
#     try:
#         # Convert the remaining part of the expression to a float
#         return float(expression)
#     except ValueError:
#         # Handle invalid expressions
#         print("Invalid expression")
#         return None

# def main():
#     user_input = "2 + 2 + 2"
#     answer = calculate(user_input)
#     if answer is not None:
#         print(f"Answer: {answer:.1f}")

# main()


def calculate(expression): #for 1 operator
    
    expression = expression.strip()

    for i in range(len(expression)):
        
        if expression[i] == "+":
            result = int(expression[:i]) + int(expression[i+1:])
            return float(result)
        elif expression[i] == "-":
            result = int(expression[:i]) - int(expression[i+1:])
            return float(result)
        elif expression[i] == "*":
            result = int(expression[:i]) * int(expression[i+1:])
            return float(result)
        elif expression[i] == "/":
            result = int(expression[:i]) / int(expression[i+1:])
            return float(result)
    else:
        print("Invalid expression")
        return None

def main():     
    
    user_input = input("Expression: ")
    answer = calculate(user_input)
    if answer is not None:
        print(f"{answer:.1f}")

main()
#1) example: type 1 + 1 + 1;
#2) send to 'calculate' function;
#3) strip the expression of leading/trailing whitespaces;
#4) if symbol(operator) is there, then split the expression into two parts, where i is at center of spliting
    #(1, 1 + 1);
#5) send both parts into calculation separately (calculate(expression[:i]) and calculate(expression[i+1:]));
#6) if one part has another operator, then split that part into another two parts 
    #until there is no symbol(operator) left and lone float values of numbers returned into equation of  
    #parent expression;
#7) results are combined using appropriate operator (+ and +);
#8) return float value of the result. If error, then print "Invalid expression" and return "None".