"""
NOTE: I am not 100% sure this program works,
      Steam has a limit when entering product codes,
      around 6 or 7 i think?

Since this program is open source, you may mod this however you want it.
"""

import random
import string
import easygui as eg # pip install easygui
from colorama import init, Fore, Style # pip install colorama
from datetime import datetime

init(autoreset=True)

def WARNING():
    eg.msgbox("This program is for educational purposes only. Do not use it to generate or distribute pirated Steam keys.\n", "WARNING!")

def generate_steam_key(length=15):
    chars = string.ascii_uppercase.replace('I', '').replace('O', '').replace('L', '').replace('V', '').replace('Y', '')  # Exclude I, O, L, V, Y
    chars += '23456789'  # Add digits, exclude 0 and 1
    group_size = 5
    num_groups = length // group_size
    groups = []
    for _ in range(num_groups):
        group = ''.join(random.choice(chars) for _ in range(group_size))
        groups.append(group)
    return '-'.join(groups)

def generate_5x5(length=25):
    chars = string.ascii_uppercase.replace('I', '').replace('O', '').replace('L', '').replace('V', '').replace('Y', '')
    chars += '23456789'
    group_size = 5
    num_groups = length // group_size
    groups = []
    for _ in range(num_groups):
        group = ''.join(random.choice(chars) for _ in range(group_size))
        groups.append(group)
    return '-'.join(groups)

if __name__ == "__main__":
    WARNING()
    print(Fore.CYAN + Style.BRIGHT + "="*40)
    print(Fore.YELLOW + Style.BRIGHT + "      Steam Key Generator")
    print(Fore.CYAN + Style.BRIGHT + "="*40)
    print(Fore.GREEN + "Choose key format:")
    print(Fore.MAGENTA + "1." + Fore.WHITE + " 15-character " + Fore.LIGHTBLACK_EX + "(XXXXX-XXXXX-XXXXX)")
    print(Fore.MAGENTA + "2." + Fore.WHITE + " 25-character " + Fore.LIGHTBLACK_EX + "(XXXXX-XXXXX-XXXXX-XXXXX-XXXXX)")
    choice = input(Fore.CYAN + "Enter 1 or 2: " + Style.RESET_ALL).strip()
    while choice not in ('1', '2'):
        choice = input(Fore.RED + "Please enter 1 or 2: " + Style.RESET_ALL).strip()

    num_keys = input(Fore.CYAN + "How many Steam keys do you want to generate? " + Style.RESET_ALL)
    while not num_keys.isdigit() or int(num_keys) < 1:
        num_keys = input(Fore.RED + "Please enter a valid positive number: " + Style.RESET_ALL)
    num_keys = int(num_keys)

    # Prepare file name with current date and time
    now = datetime.now()
    filename = f"steamkeys_{now.strftime('%Y%m%d_%H%M%S')}.txt"

    batch_size = 20
    generated = 0
    keys = []

    print(Fore.CYAN + "\nGenerating your Steam keys...\n" + Style.RESET_ALL)

    while generated < num_keys:
        to_generate = min(batch_size, num_keys - generated)
        for _ in range(to_generate):
            if choice == '1':
                key = generate_steam_key()
            else:
                key = generate_5x5()
            print(Fore.YELLOW + Style.BRIGHT + key)
            keys.append(key)
        generated += to_generate
        if generated < num_keys:
            input(Fore.GREEN + Style.BRIGHT + "\nPress ENTER to continue..." + Style.RESET_ALL)

    # Save to file
    with open(filename, "w") as f:
        for key in keys:
            f.write(key + "\n")

    print(Fore.CYAN + Style.BRIGHT + f"\nAll keys generated! Saved to {filename}\n" + Style.RESET_ALL)
