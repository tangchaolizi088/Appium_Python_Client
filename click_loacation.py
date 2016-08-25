#-*- coding:utf-8 -*-

class GetValues():

    def __init__(self,x,y):
        self.location =  {'q':('1','4'),'w':('2','4'),'e':('3','4'),'r':('4','4'),'t':('5','4'),'y':('6','4'),'u':('7','4'),'i':('8','4'),'o':('9','4'),'p':('10','4'),'a':('1','3'),
            's':('2','3'),'d':('3','3'),'f':('4','3'),'g':('5','3'),'h':('6','3'),'j':('7','3'),'k':('8','3'),'l':('9','3'),'z':('1','2'),'x':('2','2'),'c':('3','2'),
             'v':('4','2'),'b':('5','2'),'n':('6','2'),'m':('7','2'),'1':('1','4'),'transf':('1','1'),'2':('2','4'),'3':('3','4'),'4':('4','4'),'5':('5','4'),'6':('6','4'),
            '7':('7','4'),'8':('8','4'),'9':('9','4'),'0':('10','4'),'return':('10','1')}
        self.width = x
        self.height = y
        #根据手机高度判断机型，再设置顶部到键盘的距离
        if self.height == 736:
            self.keyboard_height = 510
        elif self.height == 480:
            self.keyboard_height = 265
        elif self.height == 1812:
            self.keyboard_height = 1110

    def get_value(self,x,y):
        if y == 4 :
            y = (float(self.keyboard_height)+((self.height-float(self.keyboard_height))/4/2))
            if x ==1:
                x = x*(float(self.width)/10/2)
            else:
                x = x*(float(self.width)/10)-(float(self.width)/10/2)
            return x,y
        elif y == 3:
            y = (float(self.keyboard_height)+((self.height-float(self.keyboard_height))/4/2))+((self.height-float(self.keyboard_height))/4)
            if x == 1:
                x = x*(float(self.width)/10)
            else:
                x =x*(float(self.width)/10)
            return x,y
        elif y == 2:
            y = float(self.keyboard_height)+(self.height-float(self.keyboard_height))/4*2.5
            if x == 1:
                x = 2*(float(self.width)/10)
            else:
                x = ((x+1)*(float(self.width)/10))
        elif y == 1:
            y = float(self.keyboard_height)+(self.height-float(self.keyboard_height))/4*3.5
            if x == 1:
                x = (float(self.width)/10)
            else:
                x = (float(self.width)/10)*9

        return x,y

    def get_location(self,*numbers):
        l = []
        for i in numbers[0]:
            locations = {}
            if i.isdigit():
                #切换按钮的坐标获取
                values = self.get_value(int(self.location['transf'][0]),int(self.location['transf'][1]))
                locations_trf = {'x':round(values[0],1),'y':round(values[1],1)}
                #获取该数字的坐标
                i_location = self.location[i]
                values = self.get_value(int(i_location[0]),int(i_location[1]))
                locations = {'x':round(values[0],1),'y':round(values[1],1)}
                l.append(locations_trf)
                l.append(locations)
                l.append(locations_trf)
            elif i.isalpha():
                i = i.lower()
                i_location = self.location[i]
                values = self.get_value(int(i_location[0]),int(i_location[1]))
                locations = {'x':round(values[0],1),'y':round(values[1],1)}
                l.append(locations)
         #增加键盘收回动作
        r_keyboard = self.get_value(int(self.location['return'][0]),int(self.location['return'][1]))
        locations_r_keyboard = {'x':round(r_keyboard[0],1),'y':round(r_keyboard[1],1)}
        l.append(locations_r_keyboard)
        return l
