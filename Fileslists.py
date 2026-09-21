games_files = open("games.txt", "r", encoding="utf-8")
lines_in_file = games_files.readlines()
for line in lines_in_file:
    print(line)
    print("will show after each line")
print("this will print once after")

