import pyautogui
from util import *
import os

def click_box_(box_position):
    pyautogui.moveTo(box, duration=0.1)
    pyautogui.click(clicks=2, interval=0.1)


if __name__ == "__main__":
    pyautogui.PAUSE = 0.1  # pause after each PyAutoGUI call
    # pyautogui.onScreen(x, y)
    tar = find_all("./ebi.png", confidence=0.90)
    ok_img = "./OK.png"
    yes_img = "./yes.png"

    if check_message_box(f"螢幕上有 {len(tar)} 個艾比箱子嗎?"):
        for box in tar:
            click_box_(box)
            for times in range(50):
                find_and_click(ok_img)
                find_and_click(yes_img)
                pass
    else:
         print("不開始，程式結束")