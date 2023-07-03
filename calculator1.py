#let define a function 
def calculate(num1,num2,operator):
    int_num1=int(num1)
    int_num2=int(num2)
    result=0
    if operator=="+":
        result=int_num1+int_num2
    elif operator=="-":
        result=int_num1-int_num2
    elif operator=="/":
        if int_num2==0:
            print("second number cannot be 0")
            return False
        else:
            result=int_num1/int_num2
    elif operator=="*":
        result=int_num1*int_num2
    return result 
#function ends here        

operator_list=["+","-","/","*"] #operator list quite flexiable. add whatever you want :D 

go_program=True

while go_program:
    try:
        # number 1 and number two same time with comma 
        enter_numbers=input("Enter two numbers separated with a comma, 0,0 for exit:")
        no1, no2 = enter_numbers.split(",")  # so you can enter 2 numbers in same line
    except ValueError:
        print("Please enter two numbers separated by a comma.")
        continue

    if no1=="0" and no2=="0":
        break

    if all(n.strip() == "" for n in (no1, no2)):
        print("please enter two numbers")
        continue

    operator=input("and operator")
    while operator not in operator_list:
        print(f"invalid operator use a valid operator: {operator_list} ")
        operator=input("and operator")

    try:
        result=calculate(no1, no2, operator)
    except ValueError:
        print("Please enter valid numbers.")
        continue

    print(f' {no1} {operator} {no2} = {result}')
