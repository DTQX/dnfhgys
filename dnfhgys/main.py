from time import sleep

from ascript.android import action
from dnfhgys.actions import decomposeObject
from dnfhgys.utils.index import waitUntilFindTxt, waitUntilFindTxtAndClick


def main():
    # UI 设置

    # TODO打开游戏，
    # TODO判断当前游戏处于什么状态

    # 进入游戏
    # print("加载游戏中...")
    # assert waitUntilFindTxt(
    #     [552, 560, 770, 610], "角色选择界面快速前往"
    # ), "加载游戏失败"
    # action.click(642, 642)

    # print("进入角色选择界面")
    # assert waitUntilFindTxt(
    #     rect=[201, 674, 300, 712], pattern="创建角色"
    # ), "进入角色选择界面失败"
    # # 选择第一个角色 TODO 支持选择1~10 个角色
    # action.click(152, 330)
    # sleep(0.2)
    # action.click(640, 672)

    print("进入主房间")
    decomposeObject()
