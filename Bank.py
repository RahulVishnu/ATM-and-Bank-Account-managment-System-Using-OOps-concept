import secrets
#
class Bank_accnt:
    no_of_cust = 0
    
    #Creating Account number using secrets package which genrates or returns string of he value, then it will convert the string to number.
    hexstring = secrets.token_hex(4)
    accnt_num = int(hexstring, 16)
    
    def __init__(self, name, mobile_No, initial_depo, pin):
        self.name = name
        self.cust_acc_num = Bank_accnt.accnt_num
        self.acc_balance = initial_depo
        self.pin = pin

        Bank_accnt.accnt_num = Bank_accnt.accnt_num + 1
        Bank_accnt.no_of_cust = Bank_accnt.no_of_cust + 1
    
    def basic_details(self):
        print(f'User: {self.name}\t Account No: {self.cust_acc_num}\t Balance: ₹{self.acc_balance}')
    
    def deposit(self):
        amount = int(input('Enter the deposite Amount: '))
        if amount > 0:
            self.acc_balance = self.acc_balance + amount
            print('Trasaction completed. Currect Balance: ₹{self.acc_balance}')
        else:
            print('Invalid amount transaction aborted')
    
    def withdrawl(Self):
        amount = int(input('Enter the withdrawl amount: '))
        if amount <= self.acc_balance and amount>0:
            self.acc_balance = self.acc_balance - amount
            print(f'Trasaction completed. Current Balance: ₹{self.acc_balance}')
        else:
            print('Invalid amount transaction aborted')
    
    def payment(self,other):
        amount = int(input('Enter the payment amount: '))
        if amount <= self.acc_balance and amount > 0:
            self.acc_balance = self.acc_balance - amount
            other.acc_balance = other.acc_balance + amount
            print(f'Transactio  completed. Current Balance: ₹{self.acc_balance}')
        else:
            print('Invalid amount transaction aborted')

if __name__ == '__main__':
    
    cust1 = Bank_accnt(name=input('Enter Your Name please:'), mobile_No= int(input('Enter Your mobile number properly: ')), initial_depo=int(input('Enter Your amount for initial deposite: ')), pin=int(input('Enter Your Security pin: ')))
    cust2 = Bank_accnt(name=input('Enter Your Name please:'), mobile_No= int(input('Enter Your mobile number properly: ')), initial_depo=int(input('Enter Your amount for initial deposite: ')), pin=int(input('Enter Your Security pin: ')))
    print(cust1.basic_details())
    print(cust2.basic_details())
    # cust1.deposit()
    # print(cust1.basic_details())
    # cust1.withdrawl()
    # print(cust1.basic_details())
    