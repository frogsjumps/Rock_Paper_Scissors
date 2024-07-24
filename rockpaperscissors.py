## Rock Paper Scissors program

from random import choice as ch

user_score = 0
computer_score = 0

while user_score < 3 and computer_score < 3:  # Use 'and' instead of 'or'

    user_choice = input("\nEnter R (for rock), P (for paper), or S (for scissors): ")
    computer_choice = ch(["R", "P", "S"])

    if user_choice == computer_choice:
        print('')
        print('Draw')
        print(f'Your score is {user_score} and computer score is {computer_score}')
    elif (user_choice == "R" and computer_choice == "P") or \
         (user_choice == "P" and computer_choice == "S") or \
         (user_choice == "S" and computer_choice == "R"):
        print('')
        print('You lost!')
        computer_score += 1
        print(f'Your score is {user_score} and computer score is {computer_score}')
    elif (user_choice == "P" and computer_choice == "R") or \
         (user_choice == "S" and computer_choice == "P") or \
         (user_choice == "R" and computer_choice == "S"):
        print('')
        print('You won!')
        user_score += 1
        print(f'Your score is {user_score} and computer score is {computer_score}')
    else:
        print('')
        print('Invalid input. Please enter R, P, or S.')

# Print final scores
print(f"Your score: {user_score}, Computer's score: {computer_score}")
