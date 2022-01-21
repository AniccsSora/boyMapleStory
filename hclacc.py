from random import randint, uniform


class SkillNoter:

    def __init__(self):
        self.loop_position = None
        self.fire_position = None
        self.yami_position = None
        self._loop_each = 480   # 輪施放的基本週期
        self._fire_each = 1800  # 燒的基本週期
        self._yami_each = 3  # 幽暗的基本週期
        self.loop_each = 480
        self.next_fireUse = 0
        self.yami_each = 3

    # ================================================
    def update_yami_each(self):
        self.yami_each = self._yami_each

    def update_loop_each(self):
        self.loop_each = self._loop_each + randint(10, 20)

    def update_fire_nextUseTime(self):
        self.next_fireUse = self._fire_each + randint(1, 5)

    # ================================================
    def have_yami_position(self):
        return self.yami_position is not None

    def have_loop_position(self):
        return self.loop_position is not None

    def have_fire_position(self):
        return self.fire_position is not None

    # ================================================
    def yami_on_click(self, x, y, button, pressed):
        if self.yami_position is None:
            print(f"滑鼠在 ({int(x)}, {int(y)}) 按下 幽暗。")
            self.yami_position = (int(x), int(y))

        if not pressed:
            return False

    def loop_on_click(self, x, y, button, pressed):

        if self.loop_position is None:
            print(f"滑鼠在 ({int(x)}, {int(y)}) 按下 輪迴。")
            self.loop_position = (int(x), int(y))

        if not pressed:
            return False

    def fire_on_click(self, x, y, button, pressed):

        if self.fire_position is None:
            print(f"滑鼠在 ({int(x)}, {int(y)}) 按下 燃燒。")
            self.fire_position = (int(x), int(y))

        if not pressed:
            return False
    #================================================

    def get_yami_x_y(self):
        if self.yami_position is None:
            return -1, -1
        return self.yami_position[0], self.yami_position[1]

    def get_loop_x_y(self):
        if self.loop_position is None:
            return -1, -1
        return self.loop_position[0], self.loop_position[1]

    def get_fire_x_y(self):
        if self.fire_position is None:
            return -1, -1
        return self.fire_position[0], self.fire_position[1]