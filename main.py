import random

def main():
    
    has_played = False
    highscore = 0
    
    while True:
        print(f"Welcome to the Number Guessing Game {"again" if has_played else ""}, your current high score is {highscore} attempts!")
        print("\nPlease select the difficulty level:" +
            "\n1) Easy (10 Chances)" +
            "\n2) Medium (5 Chances)" +
            "\n3) Hard (3 chances)" +
            "\nEnter 0 if you'd like to exit.."
            )

        difficulties = {
            1: (10, "Easy"),
            2: (5, "Medium"),
            3: (3, "Hard")
        }
        answer = 0
        attempts = 0
        max_attempts = 0

        while True:
            try:
                response = int(input("\nEnter your choice: "))
                
                if response == 0: return
                if response < 1 and response > 3: continue
                
                max_attempts = difficulties[response][0]
                answer = random.randint(1, 100)
                
                print(f"Great, you have selected the {difficulties[response][1]} difficulty level.")
                print("Let's start the game!")
                print(f"I'm thinking of a number between 1 and 100, you have {max_attempts} attempts left!")
                
                break
            except:
                print("Please enter a valid response.")
            
        while attempts < max_attempts:
            try:
                response = int(input("\nEnter your guess: "))
                if response == answer:
                    
                    if attempts < highscore or highscore == 0: highscore = attempts
                    print(f"Congratulations, you guessed the number in {attempts} attempts!\n")
                    break
                else:
                    attempts += 1
                    print(f"Incorrect, the number is {"less" if response > answer else "greater"} than {response}. You have {max_attempts - attempts} attempts left!")
            except:
                print("Please enter a valid response.")
        
        if attempts >= max_attempts: print("You've ran out of attempts, better luck next time!\n")
        has_played = True
            
if __name__ == "__main__":
    main()
    exit()