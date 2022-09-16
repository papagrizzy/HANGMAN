def rep(list, old, new):
    for i in range(len(list)):
        if old == list[i]:
            list[i] = new
            break
    return list
while True:
    game_resource = input("Enter the Word: ").upper()
    game_hint = input("Enter a hint for the word: ").capitalize()
    LENGTH = len(game_resource)
    counter = 0
    resource_list = [i for i in game_resource]
    if LENGTH<=4:
        chances = 3
    elif LENGTH>4 and LENGTH<=7:
        chances = 5
    elif LENGTH>7:
        chances=7
    temp_st_list = ["_ " for _ in range(len(resource_list))]
    win = False
    while counter<chances:
        choice = input("Enter Word: ").upper()
        if choice in resource_list:
            while choice in resource_list:
                temp_st_list[resource_list.index(choice)] = f'{choice} '
                rep(resource_list, choice, "*")
            print("Correct!!")
            print("".join(temp_st_list))
            if "_ " not in temp_st_list:
                print("You Win!!")
                win = True
                break
        counter+=1
    if not win:
        print("You losee!!")
    runstat = input("Want to Continue?(Y/N): ").upper()
    if runstat == "N":
        print("Quitting.....")
        quit()