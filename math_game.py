import random

def math_game():
        
    while True:
        first_level_numbers = random.randint(1, 10)
        first_level_numbers2 = random.randint(1,10)

        second_level_numbers = random.randint(100, 200)
        second_level_numbers2 = random.randint(100, 200)

        third_level_numbers = random.randint(500, 1000)
        third_level_numbers2 = random.randint(500, 1000)

        level = input("Choose level (1 , 2 , 3): ")
        operators = input("Choose your operator (add, subtract, divide, multiply): ")


        if level == "1":
            num1, num2 = first_level_numbers, first_level_numbers2
        elif level == "2":
            num1, num2 = second_level_numbers, second_level_numbers2
        elif level == "3":
            num1, num2 = third_level_numbers, third_level_numbers2


        if operators == "add":
            print("What is ", num1 , "+", num2)
            answer = num1 + num2
        elif operators == "subtract":
            print("What is ",num1, "-", num2)
            answer = num1 - num2
        elif operators == "divide":
            print("What is ",num1, "/", num2)
            answer = num1 / num2
        elif operators == "multiply":
            print("What is ",num1, "*", num2)
            answer = num1 * num2

        human_input = input("What is the answer: ")
        human_input = float(human_input)
        
        
        if human_input == answer:
            print("You have guessed right!")
        else:
            print("Incorrect answer try again: ")
            


        another = input("Wanna play again! (yes/no) ").strip().lower()

        if another != "yes":
            break
    


math_game()
    

    
    