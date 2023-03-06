"""

Games to add:
- Craps
- Blackjack

"""

import random, sys

class Casino:
	def __init__(self):
		self.account_balance = 0
		self.first_run = True

	def input_ext(self, string):
		new_input = input(string)
		split_string = new_input.split(" ")
		if split_string[0].lower() == "q":
			print("Thank you for visiting! We hope you come again soon!!")
			sys.exit()
		return new_input

	def open_casino(self):
		if self.first_run:
			print("Welcome to the Casino! You can exit any time by typing 'q'")
			self.first_run = False
		while True:
			casino_choice = self.input_ext("""Please enter a number from the choices. What would you like to do? (type the number of your selection)
1. Deposit money into your account
2. Play the slot machine
3. Play Roulette
b. Check balance
q. Leave casino
Choice: """)
			if casino_choice.lower() not in ['1', '2', '3', 'b', 'q']:
				continue
			else:
				match casino_choice:
					case "1":
						self.deposit_money()
						break
					case "2":
						self.play_slot_machine()
						break
					case "3":
						self.play_roulette()
					case "b":
						print(" ")
						print(f"Your current account balance is: $" + str(self.account_balance))
						print(" ")
						self.open_casino()
						break
				break
	
	def deposit_money(self):
		is_valid_number = False
		deposit_amount = 0
		while not is_valid_number:
			deposit_amount = self.input_ext("How much money would you like to deposit? $")
			if not deposit_amount.isdigit():
				print("Please enter a number")
				continue
			deposit_amount = int(deposit_amount)
			if deposit_amount <= 0:
				print("Please enter an amount higher than $0")
				continue
			is_valid_number = True
			print(f"You deposited ${deposit_amount} to your account")
			self.account_balance = deposit_amount
			self.open_casino()
		return deposit_amount

	def check_bet_amount(self, amount):
		if not amount.isdigit():
			print("Please enter a number")
			return 0
		amount = int(amount)
		if self.account_balance < 1:
			print("You have no money and need to deposit more. Please proceed to the teller window")
			self.deposit_money()
			return 0
		if amount <= 0:
			print("Please enter an amount higher than $0")
			return 0
		if amount > self.account_balance:
			print(f"Please enter an amount lower than your account balance. You have ${self.account_balance}")
			return 0
		return 1
		
	def play_slot_machine(self):
		is_valid_number = False
		bet_amount = 0
		slots_items = ["Gold Bar", "Cherries", "Clover", "Lemon"] #, "Horseshoe", "Lucky 7", "Diamond", "Heart", "Grapes", "Orange", "Apple", "Gold Bell", "Olive"
		slot1 = random.choice(slots_items)
		slot2 = random.choice(slots_items)
		slot3 = random.choice(slots_items)
		play_again = ""
		while not is_valid_number:
			bet_amount = self.input_ext("How much would you like to bet? $")
			if not self.check_bet_amount(bet_amount):
				continue
			bet_amount = int(bet_amount)
			is_valid_number = True
			print(f"You are placing a ${bet_amount} bet")
			spin_y_or_n = self.input_ext("Would you now like to spin the machine? (Y or N) ").upper()
			while True:
				if spin_y_or_n == "Y":
					print(f"You rolled {slot1} | {slot2} | {slot3}")
					if(slot1 == slot2 and slot2 == slot3):
						slot_machine_winnings = random.randrange(bet_amount, 5000)
						print(f"You won {slot_machine_winnings}!")
						self.account_balance += slot_machine_winnings
						play_again = self.input_ext("Play again? (Y or N) ").upper()
						while True:
							if play_again == "Y":
								self.play_slot_machine()
								break
							else:
								self.open_casino()
								break
					else:
						self.account_balance -= bet_amount
						play_again = self.input_ext("You lost! New account balance: $" + str(self.account_balance) + ". Play again? (Y or N) ").upper()
						while True:
							if play_again == "Y":
								self.play_slot_machine()
								break
							else:
								self.open_casino()
								break
					break
				elif spin_y_or_n == "N":
					self.open_casino()
					break
				else:
					spin_y_or_n = self.input_ext("Please enter only Y or N to spin the slot machine: ").upper()
					continue
		return bet_amount
		
	def play_roulette(self):
		is_valid_entry = False
		bet_number = 0
		bet_amount = 0
		play_again = ""
		while not is_valid_entry:
			bet_amount = self.input_ext("Roulette! How much would you like to bet? $")
			if not self.check_bet_amount(bet_amount):
				continue
			bet_amount = int(bet_amount)
			print(f"You are placing a ${bet_amount} bet")
			break
		while not is_valid_entry:
			bet_number = self.input_ext("Pick a bet number between 1 and 36 ")
			if int(bet_number) < 1 or int(bet_number) > 36:
				continue
			break
		bet_number = int(bet_number)
		while not is_valid_entry:
			bet_color = self.input_ext("Now pick a color: Red or Black ")
			if (bet_color.lower() != "red") and (bet_color.lower() != "black"):
				continue
			break
		print(f"You are placing a ${bet_amount} bet on {bet_color} number {bet_number}")
		spin_y_or_n = self.input_ext("Would you now like to spin the roulette? (Y or N) ").upper()
		while True:
			if spin_y_or_n == "Y":
				redorblack = random.choice(['red', 'black'])
				winning_number = random.choice([bet_number, random.randrange(1, 37), random.randrange(1, 37)])
				if (winning_number == bet_number) and (redorblack == bet_color):
					print(f"You rolled {redorblack} number {winning_number}. Your choices matched. You won {bet_amount*2}!")
					self.account_balance += bet_amount*2
					play_again = self.input_ext("New account balance: $" + str(self.account_balance) + ". Play again? (Y or N) ").upper()
					while True:
						if play_again == "Y":
							self.play_roulette()
							break
						else:
							self.open_casino()
							break
				else:
					print(f"You rolled {redorblack} number {winning_number}. Your choices did not match. You lost {bet_amount}!")
					self.account_balance -= bet_amount
					play_again = self.input_ext("New account balance: $" + str(self.account_balance) + ". Play again? (Y or N) ").upper()
					while True:
						if play_again == "Y":
							self.play_roulette()
							break
						else:
							self.open_casino()
							break
				break
			elif spin_y_or_n == "N":
				self.open_casino()
				break
			else:
				spin_y_or_n = self.input_ext("Please enter only Y or N to spin the slot machine: ").upper()
				continue



casino = Casino()
casino.open_casino()