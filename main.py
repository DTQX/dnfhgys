from time import sleep

from utils.index import waitUntilFindTxt
from ascript.android import action


def main():
    # UI 设置

    # TODO打开游戏

    # 进入游戏

    res = waitUntilFindTxt([552, 560, 770, 610], "角色选择界面快速前往")
    print("res", res)
    if res:
        action.click(642, 642)


main()
