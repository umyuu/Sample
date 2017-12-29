# -*- coding: utf-8 -*-


def s(w):
    return str(w)


# python 3のクラス宣言
class Human(object):
    # 基本のステータスを宣言
    name = ""
    gender = ""
    length = ""
    weight = ""
    vitality = 0
    magic = 0

    # コンストラクタ
    # def __init__(self):

    #getter,setter 名前--------------------------------------
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = "彼の名前は" + name + "です。"

    # getter,setter 性別--------------------------------------
    def getGender(self):
        return self.gender
    def setGender(self, gender):
        self.gender = gender


    # getter,setter 身長--------------------------------------
    def getLength(self):
        return self.length
    def setLength(self, length):
        self.length = length


    # getter,setter 体重--------------------------------------
    def getWeight(self):
        return self.weight
    def setWeight(self, weight):
        self.weight = weight


    # getter,setter 体力--------------------------------------
    def getvitality(self):
        return self.vitality
    def setvitality(self, vitality):
        self.vitality = vitality

    # getter,setter 魔力--------------------------------------
    def getMagic(self):
        return self.magic
    def setMagic(self, magic):
        self.magic = magic
        print(type(magic))

    # 話す--------------------------------------
    def talk(self, about):
        print(about)

    # 食べる--------------------------------------
    def eatFood(self, food):
        foodType = 0
        if food == "薬草":
            foodType = 1
        elif food == "魔法の水":
            foodType = 2
        else:
            foodType = 3
        # 確認用
        print(foodType)
        self.__digestFood(foodType)
    #
    # # 消化する--------------------------------------
    def __digestFood(self, foodType):
        if foodType == 1:
            self.vitality += 10
            print("HPが10回復した")
        elif foodType == 2:
            print("MPが10回復した")
            self.magic += 10
        else:
            print("お腹を壊してしまった")
            self.vitality -= 1


def main():
    Hero = Human()
    Hero.eatFood("エリクサ")
    #Human.eatFood("hoge", "魔法の水")


if __name__ == '__main__':
    main()
