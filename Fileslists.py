games_files = open("games.txt", "r", encoding="utf-8")
lines_in_file = games_files.readlines()
#for line in lines_in_file:
    #print(line)
    #print("will show after each line")
#print("this will print once after")

with open("games.txt", "r", encoding="utf-8") as lines_in_file:
    for line in lines_in_file:
        game_info = line.split("|")
        price = float(game_info[2])
        copies_sold = int(game_info[3])
        profit = price * copies_sold
        game_name = game_info[0]
        print (f"{game_name} earned ${profit}")