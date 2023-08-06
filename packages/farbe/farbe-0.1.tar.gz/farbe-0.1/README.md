# farbe

![Hello Colors](https://github.com/morinokami/farbe/blob/master/docs/hello.png)

## Installation
```sh
$ pip install farbe
```

## Test
Just type in these commands and check if your terminal can print colors properly:
```sh
>>> import farbe
>>> farbe.test()
```
It prints the supported combinations of colors and effects:
![Test](https://github.com/morinokami/farbe/blob/master/docs/test.png)

## Basic Usage
Specify the color you want to use and feed a string to the `Farbe` object's `print` method.
```sh
>>> from farbe import Color, Farbe
>>> bb = Farbe(Color.Fg.BrightBlue)
>>> bb.print('Hello, Bright Blue')
Hello, Bright Blue
>>> white_fg_red_bg = Farbe(Color.Fg.White, Color.Bg.Red)
>>> white_fg_red_bg.print('White characters on red background')
White characters on red background
>>> italic = Farbe(Color.Fg.Normal, effects=[Color.Effect.Italic])
>>> italic.print('Characters in italic')
Characters in italic
```
![Basic](https://github.com/morinokami/farbe/blob/master/docs/basic.png)

## Using Colored objects
`Colored` objects can be used in combination with normal strings.
```sh
>>> red = Farbe(Color.Fg.Red)
>>> yellow = Farbe(Color.Fg.Yellow)
>>> error = red.colored('Error')
>>> warning = yellow.colored('Warning')
>>> print('[' + error + '] Something went wrong!')
[Error] Something went wrong!
>>> print('🐍 ' + warning + '! 🐍')
🐍 Warning! 🐍
```
![Colored](https://github.com/morinokami/farbe/blob/master/docs/colored.png)

## Supported Colors and Effects

### Foreground Colors
Color Name | Code
--- | ---
Normal | `Color.Fg.Normal`
Black | `Color.Fg.Black`
Red | `Color.Fg.Red`
Green | `Color.Fg.Green`
Yellow | `Color.Fg.Yellow`
Blue | `Color.Fg.Blue`
Magenta | `Color.Fg.Magenta`
Cyan | `Color.Fg.Cyan`
White | `Color.Fg.White`
BrightBlack | `Color.Fg.BrightBlack`
BrightRed | `Color.Fg.BrightRed`
BrightGreen | `Color.Fg.BrightGreen`
BrightYellow | `Color.Fg.BrightYellow`
BrightBlue | `Color.Fg.BrightBlue`
BrightMagenta | `Color.Fg.BrightMagenta`
BrightCyan | `Color.Fg.BrightCyan`
BrightWhite | `Color.Fg.BrightWhite`

### Background Colors
Color Name | Code
--- | ---
Normal | `Color.Bg.Normal`
Black | `Color.Bg.Black`
Red | `Color.Bg.Red`
Green | `Color.Bg.Green`
Yellow | `Color.Bg.Yellow`
Blue | `Color.Bg.Blue`
Magenta | `Color.Bg.Magenta`
Cyan | `Color.Bg.Cyan`
White | `Color.Bg.White`
BrightBlack | `Color.Bg.BrightBlack`
BrightRed | `Color.Bg.BrightRed`
BrightGreen | `Color.Bg.BrightGreen`
BrightYellow | `Color.Bg.BrightYellow`
BrightBlue | `Color.Bg.BrightBlue`
BrightMagenta | `Color.Bg.BrightMagenta`
BrightCyan | `Color.Bg.BrightCyan`
BrightWhite | `Color.Bg.BrightWhite`

### Effects
Effect | Code
--- | ---
Bold | `Color.Effect.Bold`
Faint | `Color.Effect.Faint`
Italic | `Color.Effect.Italic`
Underline | `Color.Effect.Underline`
SlowBlink | `Color.Effect.SlowBlink`
RapidBlink | `Color.Effect.RapidBlink`
Reverse | `Color.Effect.Reverse`
Conceal | `Color.Effect.Conceal`
CrossOut | `Color.Effect.CrossOut`
