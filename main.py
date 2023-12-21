"""
ออกแบบโปรแกรมรับข้อมูลจากผู้ใช้งานเป็นตัวเลขจากนั้นตรวจสอบดังนี้
- ถ้าเลขเป็นบวก แสดง The number you entered is positive
- ถ้าเลขเป็นลบ แสดง The number you entered is negative
- ถ้าเลขเป็นศูนย์ แสดง The number you entered is zero

""" 
num_1 = int(input("Enter number : "))
if num_1 > 0 :
    print("The number you entered is positive")
elif num_1 < 0 :
    print("The number you entered is negative")
else:
    print("The number you entered is zero")

git config --global user.email "andythongkipt26@gmail.com"
git config --global user.name "andythongkipt"