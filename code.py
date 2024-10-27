import random
import time

def clear_screen():
    #Clear screen with newlines for better visibility
    print("\n" * 50)

def get_difficulty():
    #Get difficulty level from user and return corresponding range and attempts
    while True:
        print("\nChoose difficulty level:")
        print("1. Easy (1-50, 10 attempts)")
        print("2. Medium (1-100, 7 attempts)")
        print("3. Hard (1-200, 5 attempts)")
        
        try:
            choice = int(input("Enter your choice (1-3): "))
            if choice == 1:
                return 1, 50, 10
            elif choice == 2:
                return 1, 100, 7
            elif choice == 3:
                return 1, 200, 5
            else:
                print("Invalid choice! Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input! Please enter a number.")

def get_valid_guess(min_num, max_num):
    #Get and validate user's guess
    while True:
        try:
            guess = int(input(f"\nEnter your guess ({min_num}-{max_num}): "))
            if min_num <= guess <= max_num:
                return guess
            else:
                print(f"Please enter a number between {min_num} and {max_num}!")
        except ValueError:
            print("Invalid input! Please enter a number.")

def calculate_score(attempts_left, max_attempts):
    #Calculate score based on remaining attempts
    base_score = 1000
    return int(base_score * (attempts_left / max_attempts))

def play_game():
    # Main game function
    # Game initialization
    print("\n=== Welcome to the Number Guessing Game! ===")
    player_name = input("Enter your name: ")
    
    while True:
        # Get difficulty settings
        min_num, max_num, max_attempts = get_difficulty()
        target_number = random.randint(min_num, max_num)
        attempts_left = max_attempts
        
        print(f"\nGame Started! I'm thinking of a number between {min_num} and {max_num}")
        print(f"You have {attempts_left} attempts to guess it.")
        
        # Main game loop
        start_time = time.time()
        
        while attempts_left > 0:
            print(f"\nAttempts left: {attempts_left}")
            guess = get_valid_guess(min_num, max_num)
            
            if guess == target_number:
                time_taken = round(time.time() - start_time, 2)
                score = calculate_score(attempts_left, max_attempts)
                print(f"\nCongratulations, {player_name}! You've won! 🎉")
                print(f"You guessed the number in {max_attempts - attempts_left + 1} attempts!")
                print(f"Time taken: {time_taken} seconds")
                print(f"Score: {score} points")
                break
            elif guess < target_number:
                print("Too low! Try a higher number.")
            else:
                print("Too high! Try a lower number.")
            
            attempts_left -= 1
            
            # Show warning when attempts are running low
            if attempts_left in [2, 1]:
                print(f"⚠️ Warning: Only {attempts_left} attempts remaining!")
        
        if attempts_left == 0:
            print(f"\nGame Over! The number was {target_number}")
            print("Better luck next time!")
        
        # Ask to play again
        while True:
            play_again = input("\nWould you like to play again? (yes/no): ").lower()
            if play_again in ['yes', 'no']:
                break
            print("Please enter 'yes' or 'no'")
        
        if play_again == 'no':
            print(f"\nThanks for playing, {player_name}! See you next time! 👋")
            break
        
        clear_screen()

if __name__ == "__main__":
    play_game()