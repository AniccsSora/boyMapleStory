import pyautogui
import time
from random import randint
from pynput import mouse
import ClickNoter
from pynput.keyboard import Key, Controller, KeyCode

pyautogui.FAILSAFE = True

def button_regist():
    noter = ClickNoter.BtnNoter()
    # 製作按鈕
    makeBtnListener = mouse.Listener(
        on_click=noter.make_btn_on_click
    )
    makeBtnListener.start()
    print("請點下 製作按鈕 位置...")
    while not noter.have_make_btn_position():
        pass
    print("等待 1 秒...")
    time.sleep(1)
    # --- 確認製作 OK
    dialog_OK_btn_Listener = mouse.Listener(
        on_click=noter.OK_dialog_btn_on_click
    )
    dialog_OK_btn_Listener.start()
    print("請點下 OK 按鈕位置...")
    while not noter.have_OK_dialog_btn_position():
        pass
    print("等待 1 秒...")
    time.sleep(1)
    # --- 製作完成的 確認
    complete_chk_btn_Listener = mouse.Listener(
        on_click=noter.complete_chk_btn_on_click
    )
    complete_chk_btn_Listener.start()
    print("請點下 製作完成 按鈕位置...")
    while not noter.have_complete_chk_btn():
        pass
    print("等待 1 秒...")
    time.sleep(1)

    return noter

def count_down(sec):
    for _ in range(sec):
        p = '.'*(_ % 4)
        print(f"\r倒數 {sec-_} 秒 {p}", end="")
        time.sleep(1)


def pressKey(kb_controller, target_key):
    time.sleep(0.01)
    kb_controller.press(target_key)
    time.sleep(0.34)
    kb_controller.release(target_key)
    time.sleep(0.15)


if __name__ == "__main__":
    # kb = Controller()
    # if True:  # test
    #     time.sleep(3)
    #     pressKey(kb, '\'')
    #     time.sleep(9999)


    noter = button_regist()  # 利用 noter 記憶按鈕位置
    tane_total = int(input("有多少瓶 杜松的種子精油? :"))
    make_potion_max_time = tane_total // 10

    print(f"等待 {noter.potion_cd} 秒 後開始製作第一批...")
    count_down(noter.potion_cd)

    print("\n=== 開始製作 ===")
    # 開始 製作迴圈
    for make_cnt in range(make_potion_max_time):
        # 1: 按下 製作按鈕
        pyautogui.moveTo(noter.make_btn_position)
        time.sleep(0.3)
        pyautogui.doubleClick()

        # 2: 按下 OK按鈕
        pyautogui.moveTo(noter.OK_dialog_btn_position)
        time.sleep(0.3)
        pyautogui.doubleClick()
        time.sleep(4)  # 跑製作動畫

        # 3: 按下 確定按鈕
        pyautogui.moveTo(noter.complete_chk_btn)
        time.sleep(0.3)
        pyautogui.doubleClick()

        # 4: 等待製作 cd
        print(f"\r已經製作號第 {make_cnt+1}/{make_potion_max_time} 批。等待冷卻...")
        count_down(300)
