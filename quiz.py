questions = [
    {
        "question": "what is the capital of france?",
        "options": ["A) london", "B)parris","C)Rome","D)madrid"],
        "answer": "B"
    },

    {
       "question":"when did chernobyl incident occur?",
       "options" : ["A) march 1995","B)april 1986","C)december 1993","D)none of the above"],
       "answer": "B"
   },
   {
       "question":"how many ballon-dors does messi has?",
       "options": ["A)4","B)6","C)5","D) 8"],
       "answer": "D"

   },
   {
      "question":"who won the election of U.S 2026",
      "options": ["A)kamala harris","B)donald trump","jill stein","cornel west"],
      "answer": "B"
    }


]

def quiz():
    score = 0
    for i,q in enumerate(questions, 1):
        print(f"questions{i}: {q['question']}")
        for option in q['options']:
            print(option)

        answer = input("your answer  {A,B,C,D}: ").strip().upper()
        if answer == q['answer'].strip().upper():
            print("correct")
            score +=1
        else:
            print(f"Wrong answer :( the answer was {q['answer']}")
    
    print(f"\n your final score is {score} out of {len(questions)}, keep learning :)")
quiz()