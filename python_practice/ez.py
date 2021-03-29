
from python_practice.hero import hero
from python_practice.jinx import jinx1
class EZ(hero):
    hp = 1000
    power = 210
    name = "EZ"

ez= EZ()
#
ez.fight(jinx1.hp,jinx1.power)