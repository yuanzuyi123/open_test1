


class hero:
    # def __init__(self,name):
    #     self.name = name
    hp = 0
    power = 0
    name = ""
    def fight(self,enemy_hp, enemy_power):

        final_hp = self.hp - enemy_power

        enemy_final_hp = enemy_hp - self.power
        if final_hp > enemy_final_hp:
            print(f"{self.name}赢了")
        elif final_hp < enemy_power:
            print("敌人赢了")
        else:
            print("我们大平了")
