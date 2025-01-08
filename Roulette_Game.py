import random
#single player roulette game

board = []

#set up scoring data here/list of all possible bet spots which can be printed out later




def main():
  chips = int(20)
  currentSpot = int()


  while chips > 0:
    #ask for bet/number of chips
    print(f"You have {chips} chips")
    betSpot = int(input("Enter where you would like to be one: "))
    betAmount = int(input("Enter the amount of chips: "))

    
    currentSpot = random.randint(0,36) #36 is actually 00
    if currentSpot == 36:
      print(f"Spot landed on is 00 ")
    print(f"Spot landed on is {currentSpot}")
    if betSpot == currentSpot:
      winAmount = betAmount * 35
      print(f"You win {winAmount}!")
      chips += winAmount
    
    

    #deal with adding or removing chips here


if __name__ == "__main__":
  main()
