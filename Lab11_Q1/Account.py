from datetime import datetime

class Account:
    def __init__(self, acc_no , acc_name , initial_balance:0.0):
        self.acc_no = acc_no
        self.acc_name = acc_name
        self.acc_balance = initial_balance
        self.status = 'Active'
        self.transaction_history = []

    def d_acc_details(self):
        if self.status== 'Active':
            print(f'Account number: {self.acc_no}')
            print(f'Account name: {self.acc_name}')
            print(f'Account balance: {self.acc_balance}')
            print(f'Status: {self.status}')
        elif self.status== 'Inactive':
            print(f'Account number: {self.acc_no}')
            print(f'Account name: {self.acc_name}')
            print('This account is Inactive.')
        elif self.status== 'Blocked':
            print('This account is Blocked!!')
        else:
            print('Invalid status entry.')

    def deposit(self,amount):
        if self.status== 'Active':
            if amount>0:
                self.acc_balance += amount
                self.add_transaction('Deposit', amount)
                print(f'Deposited {amount} in the account.')
        elif self.status=='Inactive':
            print('Account is Inactive. No deposits allowed.')
        elif self.status=='Blocked':
            print('This account is Blocked!!')
        
    def withdraw(self,amount):
        if self.status== 'Active':
            if amount>0 and amount<= self.acc_balance:
                self.acc_balance -= amount
                self.add_transaction('Withdrawal', amount)
                print(f'{amount} withdrawn from the account.')
            else:
                print('Invalid withdrawal amount or Insuficient Balance.')
        elif self.status=='Inactive':
            print('Account is Inactive. No withdrawal allowed.')
        elif self.status=='Blocked':
            print('This account is Blocked!!')

    def check_transaction_history(self):
        if self.status == "Active":
            print("Transaction History:")
            for transaction in self.transaction_history:
                print(transaction)
        elif self.status == "Blocked":
            print("Account is Blocked. Transaction history not available.")
        elif self.status=='Inactive':
            print("Account is Inactive. Transaction history not available.")   
        
    def add_transaction(self, transaction_type, amount):
        transaction_details = {
            "type": transaction_type,
            "amount": amount,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.transaction_history.append(transaction_details)
        if len(self.transaction_history) > 5:
            self.transaction_history.pop(0)


    




