#coding=utf-8

class Bicycle:
    def run(self,miles):

        print (f"用脚踩了{miles}公里，好累的")
        pass


class Ebicycle(Bicycle):
    #构造函数
    def __init__(self,valume):

        self.valume = valume
    def fill_charge(self,add_valume):
        if isinstance(add_valume,int):
            self.valume = self.valume+add_valume


    def run_e(self,miles):


        ele_miles = self.valume * 10
        res_miles = ele_miles - miles
        if res_miles >=0:
            print (f"使用电量总公里数为{miles}")
        else:
            print (f"使用电动车骑行的公里数为{ele_miles}")
            self.run(miles-ele_miles)
        pass

ebike = Ebicycle(100)
ebike.run_e(10000)

