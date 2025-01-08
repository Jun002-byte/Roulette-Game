import random
#single player roulette game

board = []

#set up scoring data here/list of all possible bet spots which can be printed out later


chips = int(20)
currentSpot = int()

def main():
  while chips > 0:
    #ask for bet/number of chips
    print(f"You have {chips} chips")
    betSpot = input("Enter where you would like to be one: ")
    betAmount = input("Enter the amount of chips: ")
    
    currentSpot = random.randint(0,36) #36 is actually 00
    print(f"You bet on {betSpot}, for {betAmount} chips\nSpot landed on is {currentSpot}, you [enter win or lose here and amount]")

    #deal with adding or removing chips here


if __name__ == "__main__":
  main()
