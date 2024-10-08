def guess_number():
	low = 1
	high = 100
	attempts = 0
	print("\nThink of a number between 1 and 100, and I will try to guess it. ")
	
	while True:
		guess = (low+high) // 2
		attempts += 1
		print(f"\nMy guess is: {guess}")
		feedback = input("\nIs it too high (H), too low (L), or correct (C)? ").upper()
		
		if feedback == "H":
			high = guess - 1
		elif feedback == "L":
			low = guess + 1
		elif feedback == "C":
			print(f"\nCongratulations! I guessed the number in {attempts} attempts.")
			break
		else:
			print("Invalid input. Please enter H, L, or C.")
		
print("---- To-Do List Manager ----")
guess_number()