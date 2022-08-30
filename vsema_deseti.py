from pynput.keyboard import Key, Controller
import time
import keyboard
import pathlib

keyboard = Controller()

num_of_lines = 0
course = 0
interval = 0
count = 5
file_name = ""


def write(text_file, inter):
    path = str(pathlib.Path(__file__).parent.resolve()) + "/data/"
    source = path + text_file

    with open(source, 'r') as file:
        content = file.readlines()
        num_of_lines = len(content)    
    with open(source, 'r', encoding= 'utf-8') as f:
        for i in range(num_of_lines):
            line = f.readline()
            for char in line:
                keyboard.press(char)
                keyboard.release(char)
                time.sleep(interval/1000)
            keyboard.press(Key.enter)   


while True:
    try:
        course = int(input("Zadej číslo lekce(1-44): "))
        if course > 0 and course < 45:
            if course in range(1,10):
                file_name = "0"+ str(course) + ".txt"
            else:
                file_name = str(course) + ".txt"
            break
        else:
            print("Byl zadán chybný vstup.")
    except:
        print("Byl zadán chybný vstup.")

while True:
    try:
        interval = int(input("Zadej interval (5-1000). Nižší číslo zmanená větší rychlost: "))
        if interval > 4 and interval < 1001:
            break
        else:
            print("Byl zadán chybný vstup.")
    except:
        print("Byl zadán chybný vstup.")

input("Po stisku ENTER program začne za 5 vteřin.")
for i in range(5):
    time.sleep(1)
    print(count)
    count -= 1


write(file_name, interval)