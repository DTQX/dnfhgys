from time import sleep
from dnfhgys.utils.index import (
    findTxtAndClick,
    waitUntilFindColors,
    waitUntilFindImages,
    waitUntilFindImagesAndClick,
    waitUntilFindTxt,
    waitUntilFindTxtAndClick,
)
from ascript.android.screen import FindColors, FindImages
from ascript.android.system import R
from ascript.android.screen import Ocr, FindColors, FindImages
from ascript.android import action


def decomposeObject():
    print("分解物品")
    # assert waitUntilFindTxtAndClick(
    #     rect=[1183, 680, 1274, 716], pattern="物品背包"
    # ), "打开背包"
    assert waitUntilFindTxtAndClick(
        rect=[1181, 656, 1270, 700], pattern="分解"
    ), "点击分解"
    # TODO 根据配置文件查看物品等级的勾选
    selectedLevel = [1, 2, 3]
    for level in selectedLevel:
        FindColors.find("272,633,#FCEFB5", rect=[254, 609, 292, 647])


def saleObject():
    print("出售物品")


def setSetting():
    print("重置设置")
    # TODO 确认是否需要关闭
    # 消耗品快捷使用
    # 消耗品快捷配置
    # 技能学会通知
    # 装备快速穿戴


def task():
    print("开始主线任务")
    isInTask = True
    while True:
        # isInTask = False
        print("点击任务")
        waitUntilFindTxtAndClick(
            rect=[65, 138, 123, 167], pattern="[主线]", maxSecond=3
        )

        # TODO 排除加载框
        print("正在移动")
        while waitUntilFindTxt(rect=[61, 134, 180, 192], pattern="正在移动"):
            print("正在移动")
            sleep(5)
        isInTask = isInTask or waitUntilFindTxtAndClick(
            rect=[1165, 23, 1225, 63], pattern="跳过", maxSecond=3
        )
        isInTask = isInTask or waitUntilFindTxtAndClick(
            rect=[301, 107, 989, 518], pattern="确认", maxSecond=3
        )
        waitUntilFindTxtAndClick(rect=[965, 572, 1183, 630], pattern="战斗开始")
        if waitUntilFindTxt(rect=[592, 203, 685, 260], pattern="惩罚", maxSecond=3):
            print("游戏收到处罚，无法继续进行")
            return
    print("任务结束")


# 已测试
def switchRole(roleIndex):
    print("切换角色")
    waitUntilFindImagesAndClick(R.img("设置.png"), rect=[1203, 5, 1267, 74])
    sleep(0.5)
    waitUntilFindImagesAndClick(R.img("选择角色.png"), rect=[1070, 621, 1165, 710])
    assert waitUntilFindTxt(
        rect=[561, 638, 709, 700], pattern="开始游戏", maxSecond=20
    ), "进入角色选择界面失败"
    while roleIndex > 5:
        action.swipe(730, 470, 730, 10, 1000)
        roleIndex -= 5

    roles = waitUntilFindTxt(rect=[49, 161, 1250, 616], pattern="等级")
    action.click(roles[roleIndex].x, roles[roleIndex].y)
    waitUntilFindTxtAndClick(rect=[561, 638, 709, 700], pattern="开始游戏")
    assert waitUntilFindImages(
        R.img("设置.png"), rect=[1203, 5, 1267, 74], maxSecond=20
    ), "进入游戏房间失败"
    print("进入游戏房间成功")
