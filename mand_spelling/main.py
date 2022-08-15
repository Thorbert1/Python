import random
import keyboard
import time
import multiline_input
from gtts import gTTS
import os

words = multiline_input.get_minput("enter the list of words you wanna test:")
random.shuffle(words)

def main():
    i = 0
    while i < len(words):

        if keyboard.is_pressed("n"):
            myObj = gTTS(text = words[i], lang = 'zh-CN', slow = False)
            myObj.save("word.mp3")
            os.system("word.mp3")
            i = i + 1

    print("test over")


if __name__ == "__main__":
    main()
