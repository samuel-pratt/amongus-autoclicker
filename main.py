import pyautogui

from screen_search import *

# Search for the github logo on the whole screen
# note that the search only works on your primary screen.
search = Search("./images/manifolds/1.png")


pos = search.imagesearch()

if pos[0] != -1:
    print("position : ", pos[0], pos[1])
    pyautogui.moveTo(pos[0], pos[1])
else:
    print("image not found")