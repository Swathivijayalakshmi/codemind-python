class palindrome:
    def __init__(self,str1):
        self.str1=str1
    def palin(self):
        print(self.str1[::-1])
        
        if self.str1==self.str1[::-1]:
            print("palindrome")
        else:
            print("not palindrome")
str1=input()
pal=palindrome(str1)
pal.palin()
