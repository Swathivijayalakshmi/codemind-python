class mounika:
    def __init__(self,sankrit,english,m1,m2,phy,chem):
        self.sankrit=sankrit
        self.english=english
        self.m1=m1
        self.m2=m2
        self.phy=phy
        self.chem=chem
    def printing(self):
        print(f"sankrit marks: {self.sankrit}")
        print(f"English marks: {self.english}")
        print(f"Maths1 marks: {self.m1}")
        print(f"Maths2 marks: {self.m2}")
        print(f"Physics marks: {self.phy}")
        print(f"Chemistry marks: {self.chem}")
    def avg(self):
        return f"Percentage of Mounika is {(self.sankrit+self.english+self.m1+self.m2+self.phy+self.chem)/6} %"


sankrit=int(input("Enter Sankrit marks: "))
english=int(input("Enter English marks: "))
m1=int(input("Enter m1 marks: "))
m2=int(input("Enter m2 marks: "))
phy=int(input("Enter Physics marks: "))
chem=int(input("Enter Chemistry marks: "))

percentage=mounika(sankrit,english,m1,m2,phy,chem)
percentage.printing()
print(percentage.avg())
