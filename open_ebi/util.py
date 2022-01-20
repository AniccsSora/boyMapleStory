import pyautogui
import os

def check_message_box(msg):
    res = None
    res = pyautogui.confirm(msg)
    if res == 'Cancel':
        return False
    if res == 'OK':
        return True
    return None

def find_all(img, confidence=0.8):
    """
    :param img: 圖片路徑
    :return: list[Box()...]
    """
    assert os.path.exists(img)
    targets = pyautogui.locateAllOnScreen(img, grayscale=False, confidence=confidence)
    res = [target for target in targets]
    if len(res) == 0:
        pyautogui.alert(text=f"沒有在螢幕中找到 {img} (confidence:{confidence})",
                        title='警告', button='OK')
    return res

def find_and_click(img, tar_limit=1, confidence=0.90):
    assert os.path.exists(img)
    targets = pyautogui.locateAllOnScreen(img, grayscale=False, confidence=confidence)
    res = [target for target in targets]
    if len(res) > 0:
        pyautogui.moveTo(res[0], duration=0.1)
        pyautogui.click(clicks=1, interval=0.1)
    # if len(res) == 0:
    #     pyautogui.alert(text=f"沒有在螢幕中找到 {img} (confidence:{confidence})",
    #                     title='警告', button='OK')
    # if len(res) != tar_limit:
    #     pyautogui.alert(text=f"程式找到 {len(res)} 個目標，但是限制是 {tar_limit} 個, "
    #                          f"(confidence:{confidence})",
    #                     title='警告', button='OK')
    #     exit(87)

    # for box in res:
    #     pyautogui.moveTo(box, duration=0.5)
    #     pyautogui.click(clicks=1, interval=0.25)
