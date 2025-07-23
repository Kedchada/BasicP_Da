#nested if
# haverice = True
# havespoon = False
# havehand = True

# if haverice:
#     if havespoon:
#         print("กินข้าว")
#     elif havehand:
#         print("กินข้าวเหนียว")

# score = int(input("Enter your score : "))

# if score <= 100:
#     if score >=80:
#        print("A")
#     if 80 < score >=70:
#        print("B")
#     if 70 < score < 60:
#        print("C")
#     if 60 < score < 50:
#        print("D")
               
#ANS
# if score >= 0:
#   if score <= 100:
#     if score >= 80:
#       print("A")
#     if score >= 70:
#        if score < 80:
#           print("B")
#     if score >= 60:
#        if score < 70:
#           print("C")
#     if score >= 50:
#        if score < 60:
#           print("D")
#     if score < 50:
#        print("F")

#Loop
# ต้องใส่ stop เสมอ หยุดเมื่อถึงเลขนั้น ไม่ทำงานเลขนั้น
#step บวกเพิ่มขึ้นทีละเท่าไหร่
# i ตัวแปรอะไรก็ได้ range จำนวนรอบ เริ่มต่นจาก 0 เพิ่มขึ้นทีละ 1
# for i in range(1,10,2):
#     print(i)
# (1,10,2)
#start : 1
#stop : 10
#step : 2
# [1,3,5,7,9] ถึง 9 แล้วทำงานต่อไม่ได้ เป็น 11 ไม่ได้

#While Loop
#วนจนกว่าจะเป็นเท็จ คล้ายif

# i = 0
# while i < 5:
#     print(i)
#     i = i+1 #ต้องมี

while True:
    choice = int(input("กรอก 1 เพื่อบวกเลข, กรอก 2 เพื่อออก"))
    if choice == 1:
        num = int(input("กรอกจำนวนเลขที่ต้องการจะบวก : "))
        sumation = 0

        for i in range(num):
            num1 = int(input("กรอกเลข : "))
            sumation = sumation + num1
        print("ผลลัพธ์ :" , sumation)

    if choice ==2:
        print("บายบาย")
        break