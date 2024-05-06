from time import sleep, time
import time
from ascript.android.screen import Ocr


def waitUntilFindTxt(rect: list, txt: str, maxSecond=5):
    start = time()
    res = Ocr.paddleocr_v2(rect=rect, pattern=txt)
    while not res and time() - start < maxSecond:
        sleep(0.5)
    return res
