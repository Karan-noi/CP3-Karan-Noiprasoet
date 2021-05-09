Username =input("Username :")
Password =input("Password :")
if Username == "karan" and Password == "12345":
    print("Login Success")
    print("Welcome To Shop")
    print("1.Egg = 10 THB")
    print("2.Juice = 15 THB")
    print("3.Milk = 10 THB")
    userOder =int(input("กรุณาใส่หมายเลขสินค้า"))
    if userOder == 1:
        price = 10
        print("จำนวนสินค้าที่ท่านต้องการซื้อ")
        Amountprice =int(input(">>: "))
    elif userOder == 2:
         price = 15
         print("จำนวนสินค้าที่ท่านต้องการซื้อ")
         Amountprice =int(input())
    elif userOder == 3:
         price = 10
         print("จำนวนสินค้าที่ท่านต้องการซื้อ")
         Amountprice =int(input())
    print("----------------------------")
    print("Total Price")
    print(price * Amountprice)
    print("ขอบพระคุณที่อุดหนุน")
    print("-----------------------------")