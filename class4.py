##Function
# def add():
#     print(5 + 5)
# add() #เรียกออกมา

##Parameters ตัวแปรในฟังก์ชั่น
#Arguments ค่าที่เอาเข้า
# def grade(score):
#     if score >= 80:
#         print("Grade A")
#     elif score >= 70:
#         print("Grade B")
#     elif score >= 60:
#         print("Grade C")
# grade(60)

# def my_sum(a,b):
#     print(a+b)
# my_sum(5,5)
#ใช้ type ไรก็ได้

#Return Value
# def my_sum(a,b):
#      return a + b
# print(my_sum(5,5))

# def my_sum(a,b):
#      return a + b
# result = my_sum(5,5)
# print(result)
#จะได้เอาไปใช้ต่อได้

# def price(a,b): #Business Logic ไม่มีการ Input Output
#     return a*b

#     ##result = qua*price_per
#     ##total = result + (result * 0.07)
#     ##return total

# def menu(): #User Interface
#     while True:
#         choice = int(input("1.เลือกคำนวณราคาสินค้า ,2.ออก : "))
#         if choice == 1:
#             qua = int(input("จำนวนสินค้า: "))
#             price_per = int(input("ราคา: "))
#             result = price(qua, price_per)
#             vat = result + (result*7/100)
#             print(vat)

#             ##print(price(qua*price_per))
            
#         if choice ==2:
#             print("ออก")
#             break

# menu()

#List เก็บได้ทุก type
#เริ่มต้นที่ 0 ไล่ไป
# my_list = [1, 2, "Da"]
# print("Before" ,my_list[0])
# #แก้ไข List
# my_list[0] = "3"
# print("After" , my_list[0])

# print("Before" , my_list)

#เพิ่มข้อมูล
# my_list.append("DDD")

#ลบข้อมูล ใส่เลขลบตำแหน่งนั้น ไม่ใส่ลบตัวสุดท้าย
# my_list.pop(0)
# print("After", my_list)

#for loop ข้อมูลในลิสต์
# for i in my_list:
#     print(i)

#Dictionary
my_dict = {"name" : "Da" , "age" : 18}
print("Before" ,my_dict)
#เพิ่มข้อมูล
my_dict["IT"] = 31
#แทนที่ เหมือนเปลี่ยน เปลี่ยนได้ทุก type
my_dict["name"] = "Ked"
print("After" ,my_dict)

students = [
    {"name":"Da" , "age":"18"},
    {"name":"Ked" , "age":"18"}
]
for i in students:
    print(i["age"])
