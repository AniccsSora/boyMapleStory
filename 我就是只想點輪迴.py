import pyautogui
import time
from random import randint
from pynput import mouse
from hclacc import SkillNoter
from pynput.keyboard import Key, Controller

pyautogui.FAILSAFE = True


def count_down(secs):
    print(f"倒數 {secs} 秒")
    for i in range(secs):
        print("\t  剩餘 {:3.0f} 秒...".format(secs-i))
        time.sleep(1)
    print("結束！！")


def location_pic(pic_name):
    loc = pyautogui.locateOnScreen(pic_name, confidence=0.8)
    assert loc is not None
    assert len(loc) == 4  # 代表他找到的東西不唯一座標四位數組成

    return pyautogui.center(loc)

def on_click(x, y, button, pressed):
    print(f"滑鼠在 ({int(x)}, {int(y)}) 按下。")
    if not pressed:
        return False

def regis_skill():
    noter = SkillNoter()
    # 輪
    loopListener = mouse.Listener(
        on_click=noter.loop_on_click
    )
    loopListener.start()
    print("請點下 輪迴 技能位置...")
    while not noter.have_loop_position():
        pass
    print("等待 1 秒...")
    time.sleep(1)
    # --- 燒
    fireListener = mouse.Listener(
        on_click=noter.fire_on_click
    )
    fireListener.start()
    print("請點下 燃燒 技能位置...")
    while not noter.have_fire_position():
        pass
    print("等待 1 秒...")
    time.sleep(1)
    # --- 幽暗
    yamiListener = mouse.Listener(
        on_click=noter.yami_on_click
    )
    yamiListener.start()
    print("請點下 幽暗 技能位置...")
    while not noter.have_yami_position():
        pass
    print("等待 1 秒...")
    time.sleep(1)

    return noter

def leftRight(kb):
    kb.press(Key.left)
    time.sleep(0.2)
    kb.release(Key.left)
    time.sleep(0.3)
    kb.press(Key.right)
    time.sleep(0.53)
    kb.release(Key.right)
    time.sleep(0.24)
    kb.press(Key.left)
    time.sleep(0.1)
    kb.release(Key.left)
    time.sleep(0.01)

def pressKey(kb_controller, target_key):
    time.sleep(0.01)
    kb.press(target_key)
    time.sleep(0.34)
    kb.release(target_key)
    time.sleep(0.15)

if __name__ == "__main__":

    # just press
    if False:
        time.sleep(3)
        pyautogui.doubleClick()
        while True:
            print("wait 120...")
            time.sleep(120)
            pyautogui.doubleClick()
            print("clicked!")

    # 只輪燒
    shipa_mode = True
    # 倫燒模式下_要不要加幽暗?
    in_shipa_mode_and_use_dark = False

    # 註冊技能按鍵
    noter = regis_skill()

    first_fire_delaytime = int(input("第一個燒的時間還剩下幾分鐘？："))

    time.sleep(3)
    kb = Controller()

    current_wait = 1
    loop_times = 0
    fire_times = 0
    yami_times = 0
    akatsukinojinn_time = 120
    akatsukinojinn_next = 0


    _clicked_oni_token = False
    _oni_cooldown_cnt = 0

    first_run = True
    while True:

        # 輪
        go_loop_ = randint(1, 1000)
        print(f"輪骰:{go_loop_}")
        if go_loop_ > 980:  # current_wait % noter.loop_each == 0 or first_run
            print("點輪")
            pyautogui.moveTo(noter.loop_position)
            time.sleep(0.3)
            pyautogui.doubleClick()
            loop_times += 1
            noter.update_loop_each()

        # 燒
        if current_wait > noter.next_fireUse\
                or (first_fire_delaytime*60==current_wait):
            if 125 < randint(1, 1000):
                print("燃燒")
                pyautogui.moveTo(noter.fire_position)
                time.sleep(0.3)
                pyautogui.doubleClick()
                fire_times += 1
                noter.update_fire_nextUseTime()
            else:
                pass

        if shipa_mode != True:
            # 幽暗
            if current_wait % noter.yami_each == 0 or first_run:
            #if False:
                print("幽暗")
                pyautogui.moveTo(noter.yami_position)
                time.sleep(0.3)
                pyautogui.doubleClick()
                yami_times += 1
                noter.update_yami_each()

                if 20 > randint(1,100):
                    print("左右～")
                    leftRight(kb)
                    current_wait+=1

            if 20 > randint(1,100):
                pressKey(kb, Key.page_up)

            if 30 > randint(1,100):
                pressKey(kb, Key.end)

            # 鬼神
            if 20 > randint(1,100):

                if _clicked_oni_token:  # 有失放過
                    if _oni_cooldown_cnt > 29:
                        _clicked_oni_token = False
                        _oni_cooldown_cnt = 0

                else:
                    _clicked_oni_token = True
                    pressKey(kb, Key.home)
                    _oni_cooldown_cnt = 0

            _oni_cooldown_cnt += 1


            if 20 > randint(1,100):
                pressKey(kb, 'g')
            if -1 > randint(1,100):
                pressKey(kb, '2')
        else:
            # C%輪燒
            if in_shipa_mode_and_use_dark:
                # 幽暗
                if current_wait % noter.yami_each == 0 or first_run:
                #if False:
                    print("幽暗")
                    pyautogui.moveTo(noter.yami_position)
                    time.sleep(0.3)
                    pyautogui.doubleClick()
                    yami_times += 1
                    noter.update_yami_each()

        time.sleep(1)
        print("執行中 {:5.0f} 秒  (輪按下 {:3.0f} 次, 燒按下 {:3.0f} 次)".
              format(current_wait, loop_times, fire_times))
        print("  還有 {:3.0f} 秒要放輪.".format(noter.loop_each-(current_wait % noter.loop_each)))
        if noter.next_fireUse == 0:
            noter.next_fireUse = 1
        print("  還有 {:3.0f} 秒要放燒.".format(noter.next_fireUse - (current_wait % noter.next_fireUse)))
        current_wait += 1
        first_run = False
