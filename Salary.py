# File name: Salary.py
# Student ID: S26s1978
# Student name: Laila Aljunaibi


# Function to calculate hra
def calculate_hra(basic_pay):
    hra = 0
    if basic_pay <= 2500:
        hra = 600
    elif basic_pay > 2500 and basic_pay <= 4000:
        hra = 950
    elif basic_pay > 4000:
        hra = 1250
    return hra


# Function to calculate salary
def calculate_salary(basic_pay,hra,da):
    salary = basic_pay+hra+da
    return salary

# Main function
if __name__ =='__main__':
    name = input("Please write Doctor's name: ")
    basic_pay = int(input("Please Enter your basic pay(in OMR): "))
    hra = calculate_hra(basic_pay)
    da = basic_pay*(60/100)
    salary = calculate_salary(basic_pay,hra,da)
    print(f"The salary of the doctor is: {salary}")
