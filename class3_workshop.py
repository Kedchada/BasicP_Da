
# Bubbles = 450
# Buttercup = 350


while True:
    Blossom = 550
    sword = 50
    bow_arrow = 75
    revolver = 100

    choice = int(input("กรอก 1 เพื่อต่อสู้มอนเตอร์, กรอก 2 เพื่อออก : "))
    print("Blossom HP = 550")
    if choice == 1:
        num = int(input("กรอกจำนวนเลือกว่าจะตีกี่รอบ : "))
        sumation = 0
            

        for i in range(num):
            weapon = int(input("กรอก 1 เพื่อใช้ sword(damage = 50) ,กรอก 2 เพื่อใช้ bow&arrow(damage = 75) , กรอก 3 เพื่อใช้ revolver(damage = 100) : "))
            
            if weapon == 1:
                Blossom = Blossom - sword
                print("HP Blossom : " , Blossom)
            elif weapon == 2:
                Blossom = Blossom - bow_arrow
                print("HP Blossom : " ,Blossom)
            elif weapon == 3:
                Blossom = Blossom - revolver
                print("HP Blossom : " ,Blossom)

            if Blossom == 0:
                print("ตาย")
            elif Blossom < 0:
                print("ยังไม่ตาย")
                Blossom = 20
            else:
                print(Blossom)
                
    if Blossom != 0:
        print("ผู้เล่นตาย")

    if choice ==2:
        print("ออก")
        break