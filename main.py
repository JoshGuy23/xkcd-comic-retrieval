import requests
import random
from tkinter import *
from PIL import Image, ImageTk
from io import BytesIO
from urllib.request import urlopen


def raise_window(w):
    w.attributes('-topmost', 1)
    w.attributes('-topmost', 0)


def display_comic(comic):
    image = urlopen(comic["img"]).read()
    im = Image.open(BytesIO(image))

    window = Tk()
    window.title(comic["safe_title"])
    window.config(padx=20, pady=20)
    window.lift()
    raise_window(window)

    get_image = ImageTk.PhotoImage(im)
    image_label = Label(image=get_image, pady=50)
    image_label.grid(column=0, row=0)

    alt_text_label = Label(text=comic["alt"])
    alt_text_label.grid(column=0, row=1)

    window.mainloop()
    im.close()


def get_comic():
    response = requests.get(url="https://xkcd.com/info.0.json")
    response.raise_for_status()

    current_comic = response.json()
    return current_comic


def choose_comic():
    current_comic = get_comic()
    max_num = current_comic["num"]

    comic_choice = input("Would you like to read:\nA. The current comic,\nor\nB. A random comic?\n").lower()

    if comic_choice == "a":
        display_comic(current_comic)
    elif comic_choice == "b":
        chosen_comic = random.randint(1, max_num)
        comic_endpoint = f"https://xkcd.com/{chosen_comic}/info.0.json"
        response = requests.get(url=comic_endpoint)
        response.raise_for_status()
        current_comic = response.json()
        display_comic(current_comic)
    else:
        print("A or B.")


choose_comic()
