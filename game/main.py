import random


def choose_options():
  options = ("piedra", "papel", "tijera")
  user_option = input("elige piedra papel o tijera: ")
  user_option = user_option.lower()
  if user_option not in options:
    print("no es valida la opcion ahuevado")
    #continue
    return None,None
  computer_option = random.choice(options)

  print("opcion escogida por usuario: ",user_option)
  print("opcion escogida por computadora: ",computer_option)
  return user_option, computer_option

def check_rules(user_option,computer_option,user_wins,computer_wins):
  if user_option == computer_option:
    print("empate")
  elif user_option == "piedra":
    if computer_option == "tijera":
      print("ganaste")
      print("User gana")
      user_wins+=1
    else:
      print("perdiste")
      print("computadora gana")
      computer_wins+=1
  elif user_option == "papel":
    if computer_option == "piedra":
      print("ganaste")
      print("User gana")
      user_wins+=1
    else:
      print("perdiste")
      print("computadora gana")
      computer_wins+=1
  elif user_option == "tijera":
    if computer_option == "papel":
      print("ganaste")
      print("User gana")
      user_wins+=1
    else:
      print("perdiste")
      print("computadora gana")
      computer_wins+=1
  return user_wins,computer_wins


def check_winner(user_wins,computer_wins):
  if computer_wins == 2:
    print("la computadora te gano manco")
    exit()
  if user_wins == 2:
    print("hurra le ganaste a un objeto")
    exit()


def run_game():
  computer_wins = 0
  user_wins = 0
  rondas = 1

  while True:
    print("*"*10)
    print("RONDA", rondas)
    print("*"*10)
    rondas +=1 

    print("computer_wins", computer_wins)
    print("user_wins", user_wins)
  
    user_option,computer_option = choose_options()
    user_wins, computer_wins = check_rules(user_option,computer_option, user_wins, 
                                           computer_wins)
    check_winner(user_wins, computer_wins) 
  
run_game()

