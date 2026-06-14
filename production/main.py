import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import KeyScanner

keyboard = KMKKeyboard()


#Pin setup or something idk 
keyboard.matrix = KeysScanner(
    pins=[
        board.D0,
        board.D1,
        board.D2,
        board.D3,
    ],
    value_when_pressed=False,
)

#Keymap
keyboard.keymap = [
    [
    KC.LCTL(KC.LALT(KC.S)), #Star Map
    KC.LCTL(KC.LALT(KC.I)), #ISS Tracker
    KC.LCTL(KC.LALT(KC.B)), #BRUH
    KC.LCTL(KC.LALT(KC.N)) #NASA APOD
    ]
]

if __name__ == '__main__':
    keyboard.go()