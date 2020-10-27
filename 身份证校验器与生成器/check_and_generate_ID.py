import re
import time
import random
import datetime

class Check_ID:
    def __init__(self):
        self.regex=r'^[1-9]\d{16}[1-9xX]$'
        self.id=input("请输入需要检验的身份证:")
    def check_number(self):
        """检验格式是否合格,return True or False"""
        if re.fullmatch(self.regex,self.id) is None:
            print("格式错误")
            return False
        else :
            return True
    def check_region_code(self):
        """检验地址码,return True or False"""
        with open('region.txt','r',encoding='utf-8') as f:
            data = f.readlines()
            for info in data:
                if self.id[0:6] in info:
                    print('出生地:',info[7:])
            if self.id=='':
                print("地址码错误")
                return False
            else :
                return False

    def check_birthday(self):
        """检验出生日期是否合法,return True or False"""
        try:
            birth_time=time.strptime (self.id[6:14],'%Y%m%d')
            print('出生日期:',time.strftime("%Y/%m/%d",birth_time))
        except:
            print("出生日期错误")
    def check_sex(self):
        """检验性别"""
        if int(self.id[14:18])%2==0:
            print("性别:女")
        else :print("性别:男")

    def check_check_code(self):
        """第18位校验码校验,return True or False"""
        if self.id[17] == 'x': self.id[17]='X'#把第18位的小写x换成大写X方便处理
        wi = (7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2)#前17位验证码权重系数
        ui = (1,0,'X',9,8,7,6,5,4,3,2)#校验码对照数字
        weighted_sum = 0
        for i in range(0,17):
            weighted_sum+=wi[i]*int(self.id[i])
        if str(ui[weighted_sum%11])!=self.id[17]:
            print("校验码错误")
            return False
        else :return True

    def check_id(self):
        self.check_number()
        self.check_region_code()
        self.check_birthday()
        self.check_sex()
        self.check_check_code()

class Generate_ID:
    def __init__(self):
        self.id=''
    def generate_region_code(self,region=''):
        if region=='':
            n=random.randint(0,3465)
            with open ('region.txt','r',encoding='utf-8') as f:
                for i in range(n):
                    data = f.readline()
                self.id+=data[0:6]
        else :
            with open ('region.txt','r',encoding='utf-8') as f:
                data = f.readlines()
                for info in data:
                    if region in info:
                        self.id+=info[0:6]
                        break
                if self.id=='':
                    print("地址错误")
                    quit()

    def generate_birthday_code(self,years):
        if years=='':
            years=random.randint(0,100)
        else:
            years=int(years)
        now_year=datetime.datetime.now().strftime("%Y")
        year_code=int(now_year)-years
        while True:
            try:
                birthday=datetime.date(year_code,random.randint(1,12),random.randint(1,31))
                birthday_code=birthday.strftime("%Y%m%d")
                break
            except:
                pass
        self.id+=birthday_code

    def generate_order_code(self,sex=''):
        if sex=='男':
            self.id+=str(random.randint(0,499)*2).ljust(3,'0')
        elif sex=='女':
            self.id+=str(random.randint(0,499)*2+1).ljust(3,'0')
        elif sex=='' :
            self.id+=str(random.randint(0,999)).ljust(3,'0')
        else:
            print("性别错误")
            quit()

    def generate_check_code(self):
        wi = (7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2)  # 前17位验证码系数
        ui = (1,0,'X',9,8,7,6,5,4,3,2)  # 校验码对照数字
        weighted_sum = 0
        for i in range (0,17):
            weighted_sum += wi[i] * int (self.id[i])
        self.id+=str(ui[weighted_sum%11])
    def generate_id(self):
        birth_place = input ("请输入籍贯或者不输入(随机地址):")
        self.generate_region_code (region=birth_place)
        years = input ("请输入年龄或者不输入(随机年龄):")
        self.generate_birthday_code (years=years)
        sex = input ("请输入性别或者不输入(随机性别):")
        self.generate_order_code (sex=sex)
        self.generate_check_code ()
        print ("生成身份证号码:",self.id)

if __name__=='__main__':
    ans=input("需要检验身份证或者生成身份证，请输入0或者1：")
    if ans=='0':
        Check_ID().check_id()
    elif ans=='1':
        Generate_ID().generate_id()
    else :
        print("请重新运行")
