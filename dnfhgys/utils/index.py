from time import sleep, time
from ascript.android.screen import Ocr, FindColors, FindImages
from ascript.android import action


def waitUntilFindTxt(rect: list, pattern: str, maxSecond=5):
    start = time()
    res = Ocr.paddleocr_v2(rect=rect, pattern=pattern)
    while not res and time() - start < maxSecond:
        sleep(0.3)
        res = Ocr.paddleocr_v2(rect=rect, pattern=pattern)
    print(f"查找{pattern}: {bool(res)}")
    return res


def waitUntilFindTxtAndClick(
    rect: list, pattern: str, maxSecond=5, xOffset=0, yOffset=0
):
    res = waitUntilFindTxt(rect=rect, pattern=pattern, maxSecond=maxSecond)
    if res:
        action.click(res[0].x + xOffset, res[0].y + yOffset)
        print(f"点击：{pattern}")
        return True
    return False


def findTxtAndClick(rect: list, pattern: str):
    waitUntilFindTxtAndClick(rect=rect, pattern=pattern, maxSecond=1)


def waitUntilFindColors(name: str, colorInfo: str, rect: list, maxSecond=5):
    start = time()
    res = FindColors.find(colorInfo, rect=rect)
    while not res and time() - start < maxSecond:
        sleep(0.3)
        res = FindColors.find(colorInfo, rect=rect)
    print(f"查找颜色{name}: {res}")
    print(f"查找颜色{name}: {bool(res)}")
    return res


def waitUntilFindColorsAndClick(
    rect: list, pattern: str, maxSecond=5, xOffset=0, yOffset=0
):
    res = waitUntilFindColors(rect=rect, pattern=pattern, maxSecond=maxSecond)
    if res:
        action.click(res[0].x + xOffset, res[0].y + yOffset)
        print(f"点击：{pattern}")
        return True
    return False


def findColorsAndClick(rect: list, pattern: str):
    waitUntilFindColorsAndClick(rect=rect, pattern=pattern, maxSecond=1)


def waitUntilFindImages(imgSrc: str, rect: list = None, maxSecond=5):
    start = time()
    res = FindImages.find(imgSrc, rect=rect)
    while not res and time() - start < maxSecond:
        sleep(0.3)
        res = FindImages.find(imgSrc, rect=rect)
    print(f"查找图片{imgSrc}: {res}")
    return res


def waitUntilFindImagesAndClick(imgSrc: str, rect: list = None, maxSecond=5):
    res = waitUntilFindImages(imgSrc=imgSrc, rect=rect, maxSecond=maxSecond)
    if res:
        action.click(res["result"][0], res["result"][1])
        print(f"点击：{imgSrc}")
        return True
    return False


def findImagesAndClick(
    imgSrc: str,
    rect: list = None,
):
    waitUntilFindImagesAndClick(imgSrc=imgSrc, rect=rect, maxSecond=1)
