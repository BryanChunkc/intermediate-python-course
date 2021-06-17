import random

def main():
  dicetotal = 0
  dicerolls = 2
  
  for i in range(0,dicerolls):
    roll = random.randint(1,6)
    dicetotal += roll 

  print(f'You rolled a {dicetotal}')

if __name__== "__main__":
  main()
