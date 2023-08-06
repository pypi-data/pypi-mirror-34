import copy
from enum import Enum
import sys
from typing import List, Union


def test():
    for fg_color in Color.Fg:
        if fg_color == Color.Fg.Normal:
            continue
        for bg_color in Color.Bg:
            if bg_color == Color.Bg.Normal:
                continue
            f = Farbe(fg_color, bg_color)
            f.print('fg={},bg={}'.format(fg_color.name, bg_color.name))
    for effect in Color.Effect:
        f = Farbe(Color.Fg.White, effects=[effect])
        f.print(effect.name)


class Color:

    CSI = '\033[{:d}m'
    END = CSI.format(0)

    class Fg(Enum):
        Normal = 0
        Black = 30
        Red = 31
        Green = 32
        Yellow = 33
        Blue = 34
        Magenta = 35
        Cyan = 36
        White = 37
        BrightBlack = 90
        BrightRed = 91
        BrightGreen = 92
        BrightYellow = 93
        BrightBlue = 94
        BrightMagenta = 95
        BrightCyan = 96
        BrightWhite = 97

    class Bg(Enum):
        Normal = 0
        Black = 40
        Red = 41
        Green = 42
        Yellow = 43
        Blue = 44
        Magenta = 45
        Cyan = 46
        White = 47
        BrightBlack = 100
        BrightRed = 101
        BrightGreen = 102
        BrightYellow = 103
        BrightBlue = 104
        BrightMagenta = 105
        BrightCyan = 106
        BrightWhite = 107

    class Effect(Enum):
        Bold = 1
        Faint = 2
        Italic = 3
        Underline = 4
        SlowBlink = 5
        RapidBlink = 6
        Reverse = 7
        Conceal = 8
        CrossOut = 9


class Farbe:

    def __init__(self, fg: Color.Fg, bg: Color.Bg = None, effects: List[Color.Effect] = None):
        if effects is None:
            effects = []
        self.fg = fg
        self.bg = bg
        self.effects = effects

    def add_effects(self, effects: List[Color.Effect]):
        self.effects += [e for e in effects if e not in self.effects]

    def remove_effects(self, effects: List[Color.Effect]):
        self.effects = [e for e in self.effects if e not in effects]

    def print(self, string: str, end: str = '\n', file=sys.stdout):
        self.colored(string).print(end=end, file=file)

    def colored(self, string: str):
        return Colored(self, string)


class Colored:

    @classmethod
    def build_effect_string(cls, effects: [Color.Effect] = None) -> str:
        if effects is None:
            effects = []
        if len(effects) == 0:
            return ''
        return ''.join(map(lambda x: Color.CSI.format(x.value), effects))

    def __init__(self, farbe: Farbe, string: str):
        self.farbe = [farbe]
        self.string = [string]

    def __str__(self):
        res = ''

        for f, s in zip(self.farbe, self.string):
            effects = Colored.build_effect_string(f.effects)
            fg = Color.CSI.format(f.fg.value)
            bg = Color.CSI.format(f.bg.value) if f.bg else ''
            res += effects + fg + bg + s + Color.END

        return res

    def __len__(self):
        return len(''.join(self.string))

    def __add__(self, other: Union[str, 'Colored']):
        new_colored = copy.deepcopy(self)

        if type(other) == str:
            new_colored.farbe.append(Farbe(Color.Fg.Normal))
            new_colored.string.append(other)
        else:
            new_colored.farbe += copy.deepcopy(other.farbe)
            new_colored.string += copy.deepcopy(other.string)

        return new_colored

    def __radd__(self, other):
        normal = Farbe(Color.Fg.Normal)
        colored_other = normal.colored(other)
        return colored_other + self

    def add_effects(self, effects: List[Color.Effect]):
        for f in self.farbe:
            f.add_effects(effects)

    def remove(self, effects: List[Color.Effect]):
        for f in self.farbe:
            f.remove_effects(effects)

    def plain(self) -> str:
        return ''.join(self.string)

    def print(self, end: str = '\n', file=sys.stdout):
        print(str(self), end=end, file=file)
