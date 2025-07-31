class BankAccount:
	def __init__(self, account_balance, initial_balance=0):
		"""Initialize the bank account with an initial balance."""
		self.account_balance = account_balance
		self.initial_balance = initial_balance

	def deposit(self, amount):
		"""Deposit a specified amount into the account."""
		if amount > 0:
			self.account_balance += amount
			print(f"Deposited: {amount}")
		else:
			print("Deposit amount must be positive.")
	
	def withdraw(self, amount):
		"""Withdraw a specified amount from the account."""
		if amount > 0 and amount <= self.account_balance:
			self.account_balance -= amount
			print(f"Withdrew: {amount}")
		else:
			print("Insufficient funds")


	def display_balance(self):
		"""Display the current account balance."""
		print(f"Current balance: ${self.account_balance}")