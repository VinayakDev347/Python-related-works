## ------------------------------------------------------------------
"""Guessing Game"""

sec_no = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess_no = int(input("Guess a number: "))
    guess_count += 1
    if guess_no == sec_no:
        print("You find it!!!")
        break
    else:
        print("try again")
        # guess_count += 1
else:
    print("Your guissing chance is over!!!")
## ------------------------------------------------------------------
