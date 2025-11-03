import random
from colorama import Fore, Style, init

init(autoreset=True)

print(f"{Fore.CYAN}Enter your name: {Style.RESET_ALL}")
player_name = input().strip()




def get_player_choice():
    while True:
        choice = input(f"{Fore.CYAN}Enter your choice (rock, paper, scissors): {Style.RESET_ALL}").lower()
        if choice in ["rock", "paper", "scissors"]:
            return choice
        else:
            print(f"{Fore.RED}Invalid choice. Please choose rock, paper, or scissors.{Style.RESET_ALL}")

def get_ai_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(player_choice, ai_choice):
    if player_choice == ai_choice:
        return "tie"
    elif (player_choice == "rock" and ai_choice == "scissors") or \
         (player_choice == "paper" and ai_choice == "rock") or \
         (player_choice == "scissors" and ai_choice == "paper"):
        return "player"
    else:
        return "ai"

def play_game():
    player_score = 0
    ai_score = 0

    print(f"{Fore.MAGENTA}Welcome to Rock-Paper-Scissors {player_name}! {Style.RESET_ALL}")

    while True:
        player_choice = get_player_choice()
        ai_choice = get_ai_choice()

        print(f"{Fore.YELLOW}You chose: {player_choice}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}AI chose: {ai_choice}{Style.RESET_ALL}")

        winner = determine_winner(player_choice, ai_choice)

        if winner == "player":
            player_score += 1
            print(f"{Fore.GREEN}You win this round!{Style.RESET_ALL}")
        elif winner == "ai":
            ai_score += 1
            print(f"{Fore.RED}AI wins this round!{Style.RESET_ALL}")
        else:
            print(f"{Fore.BLUE}It's a tie!{Style.RESET_ALL}")

        print(f"{Fore.WHITE}Score: Player {player_score} - AI {ai_score}{Style.RESET_ALL}")

        play_again = input(f"{Fore.CYAN}Would you like to play again {player_name}? (yes/no): {Style.RESET_ALL}").lower()
        if play_again != "yes" and play_again != "no":
            print(f"{Fore.RED}Invalid input.{Style.RESET_ALL}")
            continue
        elif play_again != "yes":
            print(f"{Fore.MAGENTA}Thanks for playing {player_name}! Final score: Player {player_score} - AI {ai_score}{Style.RESET_ALL}")
            break
        else:
            continue
if __name__ == "__main__":
    play_game()