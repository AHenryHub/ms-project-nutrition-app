def switch(select_option):
    if selection == "1":
        print("Call add service")
    elif selection == "2":
        print("Call edit service")
    elif selection == "3":
        print("Call delete service")
    elif selection == "4":
        print("Call add service")
    elif selection == "5":
        print("Call edit service")
    elif selection == "6":
        print("Call delete service")
    else:
        print("Invalid input.")

while True:
    print("Options")
    print("1. Add ingredient")
    print("2. Edit ingredient")
    print("3. Delete ingredient")
    print("4. Add recipe")
    print("5. Edit recipe")
    print("6. Delete recipe")

    selection = input()

    switch(selection)
