from python_practice.jinx import jinx1
from python_practice.ez import EZ
class Hero_Factory:

    def create_hero(self,name):

        if name =='jinx':

            return jinx1()
        elif name =='EZ':

            return  EZ()
        else:
            raise Exception("此英雄不在英雄工厂里面")


hero = Hero_Factory()
jinx=hero.create_hero("jinx")
EZ=hero.create_hero("EZ")
jinx.fight(EZ.hp,EZ.power)