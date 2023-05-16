#first push to github
import random

def get_choices():
  player_choice = input("Jan Ken! Enter a choice (rock, paper, scissors): ")
  options = ["rock", "paper", "scissors"]
  cpu_choice = random.choice(options)
  choices = {"player": player_choice, "cpu": cpu_choice}
  return choices


def check_win(player, cpu):
  print(f"You chose {player}, cpu chose {cpu}")
  if player == cpu:
    return ("It's a tie!")
  elif player == "rock":
    if cpu == "scissors":
      return "Rock smashes scissors! You win!"
    else:
      return "Paper covers rock! You lose!"
  elif player == "paper":
    if cpu == "rock":
      return "Paper covers rock! You win!"
    else:
      return "Scissors cuts paper! You lose!"
  elif player == "scissors":
    if cpu == "paper":
      return "Scissors cuts paper! You win!"
    else:
      return "Rock smashes scissors! You lose"


choices = get_choices()
result = check_win(choices["player"], choices["cpu"])
print(result)
