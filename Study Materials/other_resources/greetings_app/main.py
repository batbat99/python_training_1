def greet_person():
    person_name = input("What is the name of the person? ")
    person_title = input("What is the title (if not added no title will be used)? ")

    if person_title:
        print(f"Hello ther, {person_title} {person_name}!")
    else:
        print(f"Hello {person_name}!")


def main():
    options = ["Greet a Person", "Exit"]
    while True:
        for i, option in enumerate(options):
            print(f"{i+1}- {option}")
        
        user_input = input("What would you like to choose: ")
        try:
            index = int(user_input)
            if index <=0:
                raise Exception()
            selected_option = options[index-1]
        except:
            print("Invalid Option")
            continue

        if selected_option == "Exit":
            break
        elif selected_option == "Greet a Person":
            greet_person()

main()