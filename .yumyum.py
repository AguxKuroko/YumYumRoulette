import random
print("Welcome to YumYumRoulette! Let's roll the dice and discover your delicious destiny")
print('''
⠀⠀⠀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⡏⡏⠀⡼⠊⢉⡕⠒⠂⠄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠘⢦⢣⠀⠁⠀⡜⡄⠀⠀⣠⠔⠋⠓⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠘⣷⣤⠧⡀⠀⠰⠀⠀⣬⠃⠀⠀⠀⡠⠖⠋⠲⢄⡀⠀⠀⠀⠀⠀⠀
⠀⠙⡝⢿⡉⣢⡀⠀⠈⠁⠀⠀⢀⡪⠂⠀⠀⠀⢀⣈⢢⡀⠀⠀⠀⠀
⠀⠀⠈⠢⡹⢠⣮⢵⢄⡀⠀⠀⠘⠀⠀⠀⠀⣔⠡⠐⠂⠚⢆⠀⠀⠀
⠀⠀⠀⠀⠈⠢⣑⠨⢷⣌⣓⣤⣀⠀⠀⠀⠜⠀⠀⠀⠀⠀⠀⢣⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠑⠦⣀⠈⠉⣻⣗⣦⢄⣀⠀⠀⠀⠀⠀⠀⢸⠀⠆
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠢⢈⢹⣉⣂⡾⢿⢒⠶⠒⢲⡖⠁⠃⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠒⠤⣈⡉⠓⠒⠡⢽⡿⠈⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠙⠉⠉⠀⠀⠀⠀
''')
names_string = input("Share your favorite dishes, separated by spaces, and let YumYumRoulette choose your culinary adventure!\n")
names = names_string.split()

names_list = names_string.split() # zmiana w liste
num_items = len(names_list)
random_numberr = random.randint(0,num_items - 1)
print(f"YumYumRoulette has chosen a delightful dish for you: {names_list[random_numberr]}.\nBon appétit!")
