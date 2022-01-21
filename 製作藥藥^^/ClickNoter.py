from random import randint


class BtnNoter:

    def __init__(self):
        self.make_btn_position = None
        self.OK_dialog_btn_position = None
        self.complete_chk_btn = None
        self.potion_cd = 300   # 藥水製作冷卻秒數
    # ================================================
    def have_make_btn_position(self):
        return self.make_btn_position is not None

    def have_OK_dialog_btn_position(self):
        return self.OK_dialog_btn_position is not None

    def have_complete_chk_btn(self):
        return self.complete_chk_btn is not None
    # ================================================
    def make_btn_on_click(self, x, y, button, pressed):
        if self.make_btn_position is None:
            print(f"滑鼠在 ({int(x)}, {int(y)}) 按下 製作按鈕。")
            self.make_btn_position = (int(x), int(y))
        if not pressed:
            return False

    def OK_dialog_btn_on_click(self, x, y, button, pressed):
        if self.OK_dialog_btn_position is None:
            print(f"滑鼠在 ({int(x)}, {int(y)}) 按下 確認視窗的 OK。")
            self.OK_dialog_btn_position = (int(x), int(y))
        if not pressed:
            return False

    def complete_chk_btn_on_click(self, x, y, button, pressed):
        if self.complete_chk_btn is None:
            print(f"滑鼠在 ({int(x)}, {int(y)}) 按下 製作完成 的 確認。")
            self.complete_chk_btn = (int(x), int(y))
        if not pressed:
            return False
    #================================================

    def get_make_btn_position_x_y(self):
        if self.make_btn_position is None:
            return -1, -1
        return self.make_btn_position[0], self.make_btn_position[1]

    def get_OK_dialog_btn_position_x_y(self):
        if self.OK_dialog_btn_position is None:
            return -1, -1
        return self.OK_dialog_btn_position[0], self.OK_dialog_btn_position[1]

    def get_complete_chk_btn_x_y(self):
        if self.complete_chk_btn is None:
            return -1, -1
        return self.complete_chk_btn[0], self.complete_chk_btn[1]
