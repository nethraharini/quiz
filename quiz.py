questions = [  
    {
        "question": "What is the capital of France?",
        "options": ["A) London", "B) Paris", "C) Rome", "D) Madrid"],
        "answer": "B"
    },
    {    
        "question": "When did the Chernobyl incident occur?",
        "options" : ["A) March 1995", "B) April 1986", "C) December 1993", "D) None of the above"],
        "answer": "B"
    },
    {
        "question": "How many Ballon d'Or awards does Messi have?",
        "options": ["A) 4", "B) 6", "C) 5", "D) 8"],
        "answer": "D"
    },
    {
        "question": "Who won the U.S. election in 2024?",
        "options": ["A) Kamala Harris", "B) Donald Trump", "C) Jill Stein", "D) Cornel West"],
        "answer": "B"
    }
]

def quiz():
    score = 0
    for i, q in enumerate(questions, 1):
        print(f"\nQuestion {i}: {q['question']}")
        for option in q['options']:
            print(option)
        
        while True:
            try:
                answer = input("Your answer (A, B, C, D): ").strip().upper()
                if answer not in ['A', 'B', 'C', 'D']:
                    raise ValueError("Invalid input! Please enter A, B, C, or D.")
                
                if answer == q['answer']:
                    print("Correct!")
                    score += 1
                else:
                    print(f"Wrong answer. The correct answer was {q['answer']}.")
                break  # Exit the loop if a valid answer is entered
            except ValueError as e:
                print(e)
    
    print(f"\nYour final score is {score} out of {len(questions)}. Keep learning! :)")

quiz()
