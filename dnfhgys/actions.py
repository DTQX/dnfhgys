from dnfhgys.utils.index import waitUntilFindTxtAndClick


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
