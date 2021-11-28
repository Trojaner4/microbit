import microbit
from pynput.keyboard import Key, Controller
import os
keyboard = Controller()


while True:
 if microbit.button_a.is_pressed():
    keyboard.press(".")
    keyboard.release(".")
    microbit.sleep(200)
 if microbit.button_b.is_pressed():
    keyboard.press("_")
    keyboard.release("_")
    microbit.sleep(200)
 if microbit.pin0.is_touched():
     keyboard.press(Key.enter)
     keyboard.release(Key.enter)
     microbit.sleep(200)
 if microbit.pin2.is_touched():
     keyboard.press(Key.backspace)
     keyboard.release(Key.backspace)
     microbit.sleep(200)


     

