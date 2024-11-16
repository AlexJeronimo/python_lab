def hello_user():
    while True:
        try:
            user_input = input("How are you? ")
            if user_input == "Good":
                print("Wery well")
                break
        except KeyboardInterrupt:
            print(f"\nBye")
            break

hello_user()