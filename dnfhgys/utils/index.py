from time import sleep, time
from ascript.android.screen import Ocr
from ascript.android import action


def waitUntilFindTxt(rect: list, pattern: str, maxSecond=5):
    start = time()
    res = Ocr.paddleocr_v2(rect=rect, pattern=pattern)
    while not res and time() - start < maxSecond:
        sleep(0.5)
    return res


def waitUntilFindTxtAndClick(rect: list, pattern: str, maxSecond=5):
    res = waitUntilFindTxt(rect=rect, pattern=pattern, maxSecond=maxSecond)
    if res:
        action.click(res[0].x, res[0].y)
        return True
    return False
