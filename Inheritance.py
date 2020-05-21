from random import randint

class Person:
    def __init__(self, gender, first_name, last_name, address):
        self.gender = gender
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        
    def get_gender(self):
        return self.gender
        
    def get_first_name(self):
        return self.first_name
    
    def get_last_name(self):
        return self.last_name
    
    def get_address(self):
        return self.address
    
class Customer(Person):
    def __init__(self, gender, first_name, last_name, address):
        super().__init__(gender, first_name, last_name, address)
        self.__id_number = '{:09}'.format(randint(1, 10**9))
        self.__reward_points = 0
        
    def get_id_number(self):
        return self.__id_number
    
    def get_reward_points(self):
        return self.__reward_points
    
class Employee(Person):
    def __init__(self, gender, first_name, last_name, address, SSN, hire_date):
        super().__init__(gender, first_name, last_name, address)
        self.__SSN = SSN
        self.__hire_date = hire_date
        
    def get_SSN(self):
        return self.__SSN
    
    def get_hire_date(self):
        return self.__hire_date
    
class Driver(Employee):
    def __init__(self, gender, first_name, last_name, address, SSN, hire_date, pay_rate):
        super().__init__(gender, first_name, last_name, address, SSN, hire_date)
        self.__pay_rate = pay_rate
        self.__daily_tips = 0
        
    def get_pay_rate(self):
        return self.__pay_rate
    
    def get_daily_tips(self):
        return self.__daily_tips
    
def print_bio(person):
    print("First Name: " + person.get_first_name())
    print("Last Name: " + person.get_last_name())
    print("Gender: " + person.get_gender())
    print("Address: " + person.get_address())

def create_Person():
    print("Person() class test:")
    person = Person("Male", "Will", "Oden", "652 Gold Lane, New York, NY, 05278")
    print_bio(person)
    print("")
    
def create_Customer():
    print("Customer() class test:")
    customer = Customer("Male", "Bill", "Oden", "652 Gold Lane, New York, NY, 05278")
    print_bio(customer)
    print("ID Number: " + customer.get_id_number())
    print("Reward Points: " + str(customer.get_reward_points()))
    print("")
    
def create_Employee():
    print("Employee() class test:")
    employee = Employee("Female", "Amy", "Oden", "652 Gold Lane, New York, NY, 05278", "000-46-7532", "05/07/2016")
    print_bio(employee)
    print("SSN: " + employee.get_SSN())
    print("Hire Date: " + employee.get_hire_date())
    print("")
    
def create_Driver():
    print("Driver() class test:")
    driver = Driver("Female", "Rose", "Oden", "652 Gold Lane, New York, NY, 05278", "000-46-7532", "05/07/2016", 8)
    print_bio(driver)
    print("SSN: " + driver.get_SSN())
    print("Hire Date: " + driver.get_hire_date())
    print("Pay Rate: $" + str(driver.get_pay_rate()) + "/hr")
    print("Daily Tips: $" + str(driver.get_daily_tips()))
    print("")

def main():
    create_Person()
    create_Customer()
    create_Employee()
    create_Driver()
    
main()