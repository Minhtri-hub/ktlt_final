class Customer:
    def __init__(self,customerid=None,customername=None,quantity=None,age=None,info=None ):
        self.customeris=customerid
        self.customername=customername
        self.quantity=quantity
        self.age=age
        self.info=info
    def __str__(self):
        return f"{self.customerid}\t{self.customername}\t{self.quantity}\t{self.age}\t{self.info}"
