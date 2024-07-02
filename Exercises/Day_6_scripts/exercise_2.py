with open("exercise_2.txt", "a") as f:
    while True:
        user_input = input("Please enter a value: ")
        if user_input.lower() == "stop":
            break

        f.write(user_input+"\n")
