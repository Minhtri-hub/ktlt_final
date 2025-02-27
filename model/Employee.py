class Employee:
    def __init__(self,EmployeeId,EmployeeName,EmployeeUsername,EmployeePass):
        self.EmployeeId=EmployeeId
        self.EmployeeName=EmployeeName
        self.EmployeeUserName=EmployeeUsername


    def __str__(self):
        return f"{self.customerid}\t{self.customername}\t{self.quantity}\t{self.age}\t{self.info}\t{self.email}"