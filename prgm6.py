Employee = dict()

while True:
    print('\n====== Employee Database ======')
    print('1. Create Employee\n2. Add New Employee\n3. Search Employee\n4. Delete Employee\n5. Display\n')
    print('===================================')

    Choice = int(input('Enter the Choice: '))

    if Choice == 1:
        n = int(input('Enter the Number of Employees: '))
        for i in range(n):
            print('-----------------------------')
            print('Enter the Employee ({}) Details'.format(i+1))
            print('-----------------------------')

            EmpDetails = []
            EmpName = input('Enter the Employee Name: ')
            EmpDOB = input('Enter the DOB: ')
            Designation = input('Enter the Designation: ')

            EmpDetails.append(EmpName)
            EmpDetails.append(EmpDOB)
            EmpDetails.append(Designation)
            EmpId = int(input('Enter the EmployeeId: '))
            Employee[EmpId] = EmpDetails
            print('-----------------------------')

    elif Choice == 2:
        EmpId = int(input('Enter the EmployeeId: '))

        EmpDetails = []
        EmpName = input('Enter the Employee Name: ')
        EmpDOB = input('Enter the DOB: ')
        Designation = input('Enter the Designation: ')

        EmpDetails.append(EmpName)
        EmpDetails.append(EmpDOB)
        EmpDetails.append(Designation)
        Employee[EmpId] = EmpDetails
        print('-----------------------------')

    elif Choice == 3:
        EId = int(input('Enter the EmployeeId to Display: '))
        print(Employee.get(EId))
        print('-----------------------------')

    elif Choice == 4:
        EId = int(input('Enter the EmployeeId to Delete: '))
        print(Employee.pop(EId))
        print('-----------------------------')

    elif Choice == 5:
        Status = bool(Employee)
        if Status == False:
            print('\n No Employee Details Found to Print \n')
        else:
            print(Employee)

    else:
        print('Invalid Choice!')
        break
