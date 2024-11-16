def ask_user():
    questions = {"How are you?": "I'm Fine", "What are you doing?": "Learn Python programing language.", "What is the waether today?": "I is cold outside."}
    
    while True:
        user_input = input("Ask the question: ")
        if user_input in questions:
            ansver = questions.get(user_input)
            print(ansver)
            break
        else:
            print("It is complicated to answer your question. Sory.")
            

#ask_user()