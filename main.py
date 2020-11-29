import pyautogui
import time

while(True):
    isDownloadVisible = pyautogui.locateOnScreen("./images/uploaddata/download.png",  grayscale=True, confidence=0.9)
    isUploadVisible = pyautogui.locateOnScreen("./images/uploaddata/upload.png", grayscale=True, confidence=0.9)
    manifolds1 = pyautogui.locateOnScreen("./images/manifolds/1.png", grayscale=True, confidence=0.9)
    fuelEngines = pyautogui.locateOnScreen("./images/fuel/fuelButton.png", grayscale=True, confidence=0.9)
    divertPower1 = pyautogui.locateOnScreen("./images/divertPower/divertPower1.png", confidence=0.9)
    divertPower2 = pyautogui.locateOnScreen("./images/divertPower/divertPower2.png", confidence=0.9)
    swipeCard = pyautogui.locateOnScreen("./images/swipeCard/card.png", confidence=0.9)

    if swipeCard:
        clickLocation = pyautogui.center(swipeCard)
        pyautogui.click(clickLocation)
        time.sleep(2)
        swipeCard = pyautogui.locateOnScreen("./images/swipeCard/swipe.png", grayscale=True, confidence=0.9)
        clickLocation = pyautogui.center(swipeCard)
        pyautogui.click(clickLocation)
        pyautogui.dragRel(1500, 0, duration=1.5)

    if divertPower2:
        clickLocation = pyautogui.center(divertPower2)
        pyautogui.click(clickLocation)

    if divertPower1:
        pyautogui.click(divertPower1)
        pyautogui.dragRel(0, -200, duration=0.2)

    if fuelEngines:
        clickLocation = pyautogui.center(fuelEngines)
        pyautogui.mouseDown(clickLocation)
        time.sleep(3)
        pyautogui.mouseUp()

    if manifolds1:
        clickLocation = pyautogui.center(manifolds1)
        pyautogui.click(clickLocation)

        manifolds2 = pyautogui.locateOnScreen("./images/manifolds/2.png", confidence=0.9)
        clickLocation = pyautogui.center(manifolds2)
        pyautogui.click(clickLocation)

        manifolds3 = pyautogui.locateOnScreen("./images/manifolds/3.png", confidence=0.9)
        clickLocation = pyautogui.center(manifolds3)
        pyautogui.click(clickLocation)

        manifolds4 = pyautogui.locateOnScreen("./images/manifolds/4.png", confidence=0.9)
        clickLocation = pyautogui.center(manifolds4)
        pyautogui.click(clickLocation)

        manifolds5 = pyautogui.locateOnScreen("./images/manifolds/5.png", confidence=0.9)
        clickLocation = pyautogui.center(manifolds5)
        pyautogui.click(clickLocation)

        manifolds6 = pyautogui.locateOnScreen("./images/manifolds/6.png", confidence=0.9)
        clickLocation = pyautogui.center(manifolds6)
        pyautogui.click(clickLocation)

        manifolds7 = pyautogui.locateOnScreen("./images/manifolds/7.png", confidence=0.9)
        clickLocation = pyautogui.center(manifolds7)
        pyautogui.click(clickLocation)

        manifolds8 = pyautogui.locateOnScreen("./images/manifolds/8.png",confidence=0.9)
        clickLocation = pyautogui.center(manifolds8)
        pyautogui.click(clickLocation)

        manifolds9 = pyautogui.locateOnScreen("./images/manifolds/9.png", confidence=0.9)
        clickLocation = pyautogui.center(manifolds9)
        pyautogui.click(clickLocation)

        manifolds10 = pyautogui.locateOnScreen("./images/manifolds/10.png", confidence=0.9)
        clickLocation = pyautogui.center(manifolds10)
        pyautogui.click(clickLocation)


    if isDownloadVisible:
        clickLocation = pyautogui.center(isDownloadVisible)

        pyautogui.click(clickLocation)

    if isUploadVisible:
        clickLocation = pyautogui.center(isUploadVisible)

        pyautogui.click(clickLocation)