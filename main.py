import random
from art import logo

def deal_card():
  """return random card"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return cards[random.randint(0, len(cards) - 1)]


def calculate_score(list):
    """caculate scores"""
    cards_sum = sum(list)
    if cards_sum == 21 and len(list) == 2:
      return 0
    if 11 in list and cards_sum > 21:
      list.remove(11)
      list.append(1)
      # for i in range(0, len(list)):
      #   if card_list[i] == 11:
      #     card_list[i] == 1
    return cards_sum

def compare(user_score, computer_score):
    if user_score == computer_score:
      print("draw")
    elif computer_score == 0:
      print("you lose")
    elif user_score == 0:
      print("you win")
    elif user_score > 21:
      print("you lose")
    elif computer_score > 21:
      print("you win")
    elif user_score > computer_score:
      print("you win")
    else:
      print("you lose")

def play():
  game = True
  user_cards = []
  computer_cards = [] 

  print(logo)

  for _ in range(2):  
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  print("yours: ", user_cards)  

  user_score = calculate_score(user_cards)
  com_score = calculate_score(computer_cards)
  while game:
    if user_score == 0 or user_score  > 21 or com_score == 0 or com_score > 21:
      game = False
    else:
      answer = input("draw card? 'y' or 'n': ")
      if answer == "y":
        user_cards.append(deal_card())
        user_score = calculate_score(user_cards)
        print("yours: ", user_cards)
      else:
        game = False
  
  while com_score  != 0 and com_score < 17 :
    computer_cards.append(deal_card())
    com_score = calculate_score(computer_cards)

  print("yours: ", user_cards)
  print("computer's: ", computer_cards)
  compare(user_score, com_score)
  #Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
if input("do you want to play? 'y' or 'n'? ") == 'y':
  play()
else:
  game = False