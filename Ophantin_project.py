
quiz = [ {  "question": "What year was starz universit founded?", 
            "options": ["1. 2014", "2. 2010", "3. 2006", "4. 2018"],
            "answer": 2
         }, 

         { "question": "Where is starz university located?",
           "options": ["1. Paynesville", "2. Sinkor Airfield", "3. Broad St.", "4. Nimba"], 
           "answer": 2 
         }, 

         { "question": "Who is the corrent board chair of Starz university?",
           "options": ["1. Larthin Dathong", "2. Mr. Dolokelen", "3. Abert Momo", "4. Bill Gayflor"], 
           "answer": 1 
         }, 

         { "question": "What are the official Colors of Starz University?",
           "options": ["1. Red & Black", "2. Blue and White", "3. Yellow & green", "4. Gold and black"], 
           "answer": 4 
         }, 

         { "question": "Starz university has how many compusis?",
           "options": ["1. two", "2. three", "3. five", "4. four"], 
           "answer": 3 
         } 
        ]

def run_quiz(quiz):
    score = 0
    for q in quiz:
        print(q["question"])
        for option in q["options"]:
            print(option)
        answer = int(input("Enter the number of your answer: "))
        if answer == q["answer"]:
            print("Correct!")
            score += 1
        else: 
            print("Wrong! The correct answer was option", q["answer"])
            print()
    print(f"Your final score is: {score} out of {len(quiz)}")

run_quiz(quiz)
