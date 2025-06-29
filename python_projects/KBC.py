import random 


questiondata = [
    {
        "question": "What is the capital of India?",
        "options": ["Delhi", "mumbai", "Kolkata", "Ahemdabad"],
        "correct_answer_index": 2, 
        "money": 1000
    },
    {
        "question": "Which planet is known as the 'Red Planet'?",
        "options": ["Earth", "Mars", "Jupiter", "Venus"],
        "correct_answer_index": 1, 
        "money": 2000
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
        "correct_answer_index": 3, 
        "money": 5000
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet"],
        "correct_answer_index": 2, 
        "money": 10000
    },
    {
        "question": "What is the chemical symbol for water?",
        "options": ["O2", "H2O", "CO2", "N2"],
        "correct_answer_index": 1, 
        "money": 20000
    },
    {
        "question": "What is the square root of 64?",
        "options": ["6", "7", "8", "9"],
        "correct_answer_index": 2, 
        "money": 40000
    },
    {
        "question": "Which country is home to the kangaroo?",
        "options": ["New Zealand", "South Africa", "Australia", "Canada"],
        "correct_answer_index": 2, 
        "money": 80000
    },
    {
        "question": "What is the longest river in the world?",
        "options": ["Amazon River", "Nile River", "Yangtze River", "Mississippi River"],
        "correct_answer_index": 1, 
        "money": 160000
    },
    {
        "question": "Which famous scientist developed the theory of relativity?",
        "options": ["Isaac Newton", "Galileo Galilei", "Albert Einstein", "Stephen Hawking"],
        "correct_answer_index": 2, 
        "money": 320000
    },
    {
        "question": "What is the smallest prime number?",
        "options": ["0", "1", "2", "3"],
        "correct_answer_index": 2, 
        "money": 640000
    }
]

currentmoney = 0
lifeline50 = False 

def displayquestions(quenumber, questioninfo, usedoptions=None):
    print(f"\n Question {quenumber + 1} --- (For Rs{questioninfo['money']:,})")
    print(questioninfo['question'])

    optionstodisplay = []
    for i, option in enumerate(questioninfo['options']):
        if usedoptions is None or i not in usedoptions:
            optionstodisplay.append(f"{i + 1}. {option}")
        else:
            optionstodisplay.append(f"{i + 1}. ") 

    for opt_str in optionstodisplay:
        print(opt_str)

    print("\nType your answer (1, 2, 3, or 4) or '5050' for lifeline, or 'quit' to exit.")

def getplayerinput():
    while True:
        playerrawinput = input("Your choice: ").strip().lower()

        if playerrawinput == 'quit':
            return 'quit'
        elif playerrawinput == '5050':
            return '5050'
        
        try:
            choice = int(playerrawinput)
            if 1 <= choice <= 4:
                return choice 
            else:
                print("That's not a valid option number. Please choose 1, 2, 3, or 4.")
        except ValueError:
            print("Invalid input. Please enter a number (1-4), '5050', or 'quit'.")

def lifeline50(questioninfo):
    global lifeline50 

    if lifeline50:
        print("You've already used your 50/50 lifeline for this game!")
        return None 

    print("--- Using 50/50 Lifeline! ---")
    lifeline50 = True 

    correctindex = questioninfo['correct_answer_index']
    incorrectoptions = [i for i in range(len(questioninfo['options'])) if i != correctindex]

    optionstoremove = random.sample(incorrectoptions, 2)
    
    print("Two incorrect options have been removed.")
    return optionstoremove

def playkbc():
    global currentmoney 
    
    random.shuffle(questiondata)

    print("--- Welcome to Kaun Banega Crorepati! ---")
    print("Answer questions correctly to win virtual money!")
    print("You have one 50/50 lifeline. Type '5050' to use it.")
    print("Type 'quit' anytime to leave with your current winnings.")

    options_to_hide = None 

    for i, questioninfo in enumerate(questiondata):
        displayquestions(i, questioninfo, options_to_hide)
        
        playerchoice = getplayerinput()

        if playerchoice == 'quit':
            print(f"\nYou decided to quit. You walk away with ${currentmoney:,}!")
            break 
        elif playerchoice == '5050':
            options_to_hide = lifeline50(questioninfo)
            if options_to_hide is not None:
                displayquestions(i, questioninfo, options_to_hide)
                playerchoice = getplayerinput()
                if playerchoice == 'quit': 
                    print(f"\nYou decided to quit. You walk away with ${currentmoney:,}!")
                    break
                elif playerchoice == '5050': 
                    print("You've already used 50/50 for this question.")
                    playerchoice = getplayerinput() 
                    if playerchoice == 'quit':
                         print(f"\nYou decided to quit. You walk away with ${currentmoney:,}!")
                         break
        
        if playerchoice - 1 == questioninfo['correct_answer_index']:
            currentmoney += questioninfo['money']
            print(f"CORRECT! You've won ${questioninfo['money']:,}.")
            print(f"Your total winnings: ${currentmoney:,}")
            options_to_hide = None 
        else:
            correctanswertext = questioninfo['options'][questioninfo['correct_answer_index']]
            print(f"INCORRECT! The correct answer was: {correctanswertext}.")
            print(f"Game Over! You walk away with Rs{currentmoney:,}!") 
            break 

    else: 
        print("\n--- CONGRATULATIONS! YOU'VE ANSWERED ALL QUESTIONS! ---")
        print(f"You are a true KBC champion! Your final winnings: ${currentmoney:,}")

if __name__ == "__main__":
    playkbc()

