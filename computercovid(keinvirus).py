from pynput.mouse import Button, Controller
from time import sleep
mouse = Controller()
while True:
 ein = input()
 if ein == "b":
  while True:
    mouse.press(Button.left)
    mouse.release(Button.left)
    
