from random import randint
import pyautogui
import time
from random import randint
from pynput import mouse
import ClickNoter
from pynput.keyboard import Key, Controller, KeyCode


BTN_UNIT_FUNCTION = ['get_x_y', 'on_click', 'have_position']
BTN_UNIT_PARAM = ['xy']

def get_xy(ddict):
    if ddict['xy'] is None:
        return -1, -1
    return ddict['xy'][0], ddict['xy'][1]


def build_btn_on_click_fucntion(ddict):
    def _(btn_position, x, y, button, pressed):
        btn_position = ddict['xy']
        if btn_position is None:
            print(f"滑鼠在 ({int(x)}, {int(y)}) 按下 製作完成 的 確認。")
            btn_position = (int(x), int(y))
            return btn_position
        if not pressed:
            return False
    return _
class EnhenceBtnNoter:

    def __init__(self, key_dict):
        self.key_dict = key_dict
        self._build()

    def _build(self):
        # 針對 3 function 客製
        for key_name in self.key_dict.keys():
            # 製作 單位按鈕的 param dict
            params_dict = dict.fromkeys(BTN_UNIT_PARAM)
            params_dict['xy'] = None
            # 製作 單位按鈕的 function
            #
            func_dict = dict().fromkeys(BTN_UNIT_FUNCTION)
            # 完成 三種 function : ['get_x_y', 'on_click', 'have_position']
            func_dict['get_x_y'] = get_xy
            func_dict['on_click'] = build_btn_on_click_fucntion
            func_dict['have_position'] = lambda _: _ is not None
            #
            self.key_dict[key_name] = {'param': params_dict,
                                       'func': func_dict}
    # ================================================
    def have_make_btn_position(self):
        return self.make_btn_position is not None
    def make_btn_on_click(self, x, y, button, pressed):
        if self.make_btn_position is None:
            print(f"滑鼠在 ({int(x)}, {int(y)}) 按下 製作按鈕。")
            self.make_btn_position = (int(x), int(y))
        if not pressed:
            return False
    def get_make_btn_position_x_y(self):
        if self.make_btn_position is None:
            return -1, -1
        return self.make_btn_position[0], self.make_btn_position[1]
    # =================================================


if __name__ == "__main__":
    # 單位 btn 所具有 func

    btn_s = dict().fromkeys(["製作按鈕", "對話框OK按鈕", "完成 確認按鈕"])  # 固定 param
    noter = EnhenceBtnNoter(key_dict=btn_s)
    param = noter.key_dict['製作按鈕']['param']
    print(param['xy'])



    for key_name in btn_s.keys():
        # param
        param = noter.key_dict[key_name]['param']
        # get funcions
        get_xy_func = noter.key_dict[key_name]['func']['get_x_y']
        have_position_func = noter.key_dict[key_name]['func']['have_position']
        on_click = noter.key_dict[key_name]['func']['on_click']

        btnListener = mouse.Listener(
            on_click=btn_s[key_name]['func']['on_click']
        )
        btnListener.start()
        print(f"請點下 {key_name} 製作按鈕 位置...")
        while param['xy'] is None:
            pass




