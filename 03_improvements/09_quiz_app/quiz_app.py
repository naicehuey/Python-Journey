import json
import random

def save_history(history):
    with open("quiz_history.json", "w") as f:
        json.dump(history, f)

def load_history():
    try:
        with open("quiz_history.json", "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []    
    
history = load_history()

def lines():
    print("=" *40)

def run_quiz():
    lines()
    print("     Running Quiz")
    lines()
    try:
        number = int(input("Between 1. Math and 2. Geography, Which quiz would you like? "))
        if number not in (1,2):
            print("Its 1 or 2")
            return
        
        quiz = {"math" :[
            {"question" : "What is  2 + 2: ", "answer":"4"},
            {"question" : "What is 5*8:  ", "answer" : "40"},
            {"question" : "What is 5+8:  ", "answer" : "13"},
            {"question" : "What is 2*8:  ", "answer" : "16"},
            {"question" : "What is 2*8:  ", "answer" : "16"}
                    ],
                "geography": [
                    {"question" : "What is capital of Malawi? ", "answer" : "lilongwe"},
                    {"question" : "What is capital of France? ", "answer" : "paris"},
                    {"question" : "What is capital of UK? ", "answer" : "London"},
                    {"question" : "What is capital of China? ", "answer" : "Beijing"}
                ]
        }

        if number == 1:
            selected = quiz["math"]
            category_name = "Math"
        else:
            selected = quiz["geography"]
            category_name = "Geography"

        score = 0
        
        random.shuffle(selected)
        for q in selected:
            user_answer = input(q["question"]).strip()
            if user_answer.lower() == q["answer"].lower():
                print("You got it right")
                score += 1
            else:
                print(f"You got it wrong\nHere is the right answer: {q['answer']}")

        print(f"You scored {score}/{len(selected)}")
        percentage = (score/len(selected)) * 100
        print(f"Percentage: {percentage:.0f}%")
        if percentage >= 50:
            print("Results: PASSED")
        else:
            print("Results: FAILED")
            
        added = {"category" : category_name, "score" : percentage}
        history.append(added)

    except ValueError:
        print("Enter a number")
        return

def show_history():
    lines()
    print("     Show History")
    if len(history) == 0:
        print("No results yet")
        return
    
    for i, h in enumerate(history, start=1):
        print(f"{i}. {h['category']} {h['score']:.0f}%")

def show_stats():
    lines()
    print("     Show Stats")
    lines()
    if len(history) == 0:
        print("No data yet")
        return
    
    scores = [h["score"] for h in history]
    avg = sum(scores) / len(scores)
    best = max(scores)

    print(f"Total quizzes: {len(scores)}")
    print(f"Average score: {avg:.0f}%")
    print(f"Best score: {best:.0f}%")

def again():
    while True:
        run_quiz()
        print("Do you wanna try again? ")
        ask = input("(Y/N): ").strip().lower()
        if ask != "y":
            print("Thank you for taking the quiz!!")
            break

def menu():
    while True:
        lines()
        print("     Main Menu")
        lines()
        try:
            menux = [
                "1. Take Quiz",
                "2. View History",
                "3. View Stats",
                "4. Exit"
            ]
            for item in menux:
                print(item)
                
            lines()
            chose = int(input("Whats your option: "))
            lines()

            if chose == 1:
                again()
                save_history(history)
            elif chose == 2:
                show_history()
            elif chose == 3:
                show_stats()
            elif chose == 4:
                print("Thank you for your time")
                break
            else:
                print("wrong Input!")

        except ValueError:
            print("Wrong Answer")

menu()