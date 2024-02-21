'''1.Create a list with employee basic details (name, eid, designation, date of joining,
phone no) and another list with no, of working days,no of leave availed, pay per day,
spl intensive and income tax percentage. Calculate the salary and updated in first list.'''

n=int(input("Enter the number of employees to be listed"))
Emp_det=[]
Emp_det2=[]
for i in range (0,n):
    ename=input("Enter the Employee Name")
    eid= int(input("Enter the Employee Id"))
    edes=input("Enter the employee Designation")
    DOJ=input("Enter the date of joining of the employee")
    eph=int(input("Enter the employee contact number"))
Emp_det.append(ename)
Emp_det.append(eid)
Emp_det.append(edes)
Emp_det.append(DOJ)
Emp_det.append(eph)
for j in range(0,n):
    No_of_working=int(input("Enter the number of working days"))
    leave_availed=int(input("enter the number of leaves availed"))
    payperday=int(input("Enter the pay per day"))
    inten=int(input("Enter the intensive"))
    incometax=int(input("Enter the income tax "))
Emp_det2.append(No_of_working)
Emp_det2.append(leave_availed)
Emp_det2.append(payperday)
Emp_det2.append(inten)
Emp_det2.append(incometax)

for i in range(n):
    salary=(Emp_det2[0]-Emp_det2[1])*Emp_det2[2]+Emp_det2[3]
    totalsal=salary-(salary*Emp_det2[4]/100)
    Emp_det.append(totalsal)
print( " The Overall salary of each employee is :",Emp_det)

'''2.Write a Python function find_unique_pairs(nums, target) that takes in a list of
integers nums and an integer target, and returns a list of tuples representing the
unique pairs of numbers that sum up to the target.'''

 
def find_unique_Pairs(num, target):
    res = []
    while num:
        n = num.pop()
        diff = target - n
        if diff in num:
            res.append((diff, n))
    return res
     
n=int(input("Enter the total numbers of integers"))
target=int(input("Enter the target value"))
num=[]
for i in range (0,n):
    element=int(input("Enter the values"))
    num.append(element)

print(find_unique_Pairs(num, target))
     

    
    
          
         
