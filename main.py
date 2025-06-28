import random 
responses=[
  "yes,definitely!",
  "no,not now." ,
  "ask again later.",
  "it is certain.",
  "very doubtful.",
  "outlook is good",
  "better not tell you now.",
  "concentrate and ask again.",    
]
def get_random_response():
    return random.choice(responses)

def get_user_guess():
    while True:
        try:
            guess=int(input("enter your guess(1-100):"))
            if 1<=guess<=100:
                return guess
            else:
                print("please enter a number between 1 and 100.")
        except ValueError:
            print("invalid input! please enter a number")
            

def display_response(response):
    print("\n the magic 8-ball says:",response,"\n")

def play_again():
    while True:
        choice=input("do you want to ask another question?(yes/no):").strip().lower()
        if choice=="yes":
            return True 
        elif choice=="no":
            print("thanks for playing!goodbye!")
            return False
        else:
            print("please type yes or no.")
            
def magic_8_ball():
    print("welcome to the magic 8-ball")
    while True:
        question= get_user_guess()
        if question is None:
            break
        response= get_random_response()
        display_response(response)
        if not play_again():
            break
        
magic_8_ball()   
        
