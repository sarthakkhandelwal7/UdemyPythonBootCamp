"""Bank Account Manager - Create a class called Account which will be an abstract class for three other classes called CheckingAccount, SavingsAccount
and BusinessAccount. Manage credits and debits from these accounts through an ATM style program."""
pin = 7189
class BankAccountManager():
	def __init__(self):
		self.debit_amount = 0
		self.credit_amount = 0
		self.balance = 0
		
	def manage_exchanges(self,credit_or_debit):
		if credit_or_debit.lower() == 'c':
			self.credit_amount = int(input("Please enter the amount: "))
			self.balance += self.credit_amount
		if credit_or_debit.lower() == 'd' :
			self.debit_amount = int(input("Please enter the amount: "))
			if self.balance >= self.debit_amount:
				self.balance -= self.debit_amount
			else:
				print('Insufficient balance!')
	def show_details(self):
		print(f'Your bank balance is {self.balance}')
account_type = ''
checking_account = BankAccountManager()
savings_account = BankAccountManager()
business_account = BankAccountManager()
repeat = 'y' 
while repeat == 'y':
	pin_check = int(input("Welcome please enter the pin: "))
	if pin_check == pin:
		try:
			account_type = input('For CheckingAccount:c \n For BusinessAccount:b \n For SavingsAccount:s \n For Account details:d \n Enter your choice: ')
			if account_type.lower() == 'c':
				choice = input('Do you want to credit or debit: ')
				checking_account.manage_exchanges(choice)
			elif account_type.lower() == 'b':
				choice = input('Do you want to credit or debit: ')
				business_account.manage_exchanges(choice)
			elif account_type.lower() == 's':
				choice = input('Do you want to credit or debit: ')
				savings_account.manage_exchanges(choice)
			elif account_type.lower() == 'd':
				account_type = input('Which account: ')
				if account_type.lower() == 'c':
					checking_account.show_details()
				elif account_type.lower() == 'b':
					business_account.show_details()
				elif account_type.lower() == 's':
					savings_account.show_details()
				else:
					print('Enter valid choice')
		except:
			print('Enter valid choice')
	else:
		print('Enter valid pin ')
	repeat = input('Do you want to enter your account y/n: ')
