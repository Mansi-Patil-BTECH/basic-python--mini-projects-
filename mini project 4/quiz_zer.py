# the quizzer application

def run_quiz():
    questions = [
        {
            "question": "When is World Enviroment Day celebrated?",
            "options": [
                "a) 5th June",
                "b) 5th July",
                "c) 5th August",
                "d) 5th September",
            ],
            "answer": "a) 5th June",
        },
        {
            "question": "Which is the longest desert in the world?",
            "options": ["a) Sahara", "b) Gobi", "c) Kalahari", "d) Antarctic"],
            "answer": "a) Sahara",
        },
        {
            "question": "Which is the largest country on the earth?",
            "options": ["a) USA", "b) Russia", "c) China", "d) India"],
            "answer": "b) Russia",
        },
        {
            "question": "What is the captial of Japan? ",
            "options": ["a) Tokyo", "b) Beijing", "c) Seoul", "d) Bangkok"],
            "answer": "a) Tokyo",
        },
        {
            "question": "What is the real name of Mr. Bean?",
            "options": [
                "a) Rowan Atkinson",
                "b) Jim Carrey",
                "c) Will Ferrell",
                "d) Adam Sandler",
            ],
            "answer": "a) Rowan Atkinson",
        },
    ]

    score = 0

    ''' enumerate funtion is used to get both the index and value from the list .
        Example:
            for index , value in enumerate (['a','b','c','d'])
            print (index, value)
    '''

    for index, q in enumerate(questions):
        # print(index , q)
        print(f"Q{index + 1}: {q['question']}")
        for option in q["options"]:
            print(option)

        user_answer = input("Your answer (A/B/C/D): ")
        # print(user_answer.strip().upper(), q['answer'][0].upper():)
        if user_answer.strip().upper() == q["answer"][0].upper():
            print("Correct!\n")
            score += 1
        else:
            print("Wrong!\n")

    print(f"Your final score is{score}/{len(questions)}")


run_quiz()

#run