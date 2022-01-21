import pyautogui
from util import *
import os

def click_box_(box_position):
    pyautogui.moveTo(box, duration=0.1)
    pyautogui.click(clicks=2, interval=0.1)


def find_all_cnt(img, confidence=0.80):
    """
        :param img: 圖片路徑
        :return: 目標數量
        """
    assert os.path.exists(img)
    targets = pyautogui.locateAllOnScreen(img, grayscale=False, confidence=confidence)
    res = [target for target in targets]

    return len(res)

if __name__ == "__main__":
    pyautogui.PAUSE = 0.05  # pause after each PyAutoGUI call
    # pyautogui.onScreen(x, y)
    ebi_img = "./ebi.png"
    ok_img = "./OK.png"
    yes_img = "./yes.png"

    tar = find_all(ebi_img, confidence=0.90)

    if check_message_box(f"螢幕上有 {len(tar)} 個艾比箱子嗎?"):
        for box in tar:
            if find_all_cnt(ebi_img, confidence=0.9) > 0:
                click_box_(box)
            for times in range(50):
                _f1 = find_and_click(ok_img)
                _f2 = find_and_click(yes_img)
                if (_f1 is not True) or (_f2 is not True):
                    break
    else:
         print("不開始，程式結束")