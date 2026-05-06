
#nama :Nadya
print("=== Fruits Market ===")
#price
apple_price = 10_000
orange_price = 15_000
grape_price = 20_000

#stock
apple_stock = 10
orange_stock = 10
grape_stock = 10


#input user
while True :
    apple_qty = input("masukkan jumlah apel: ")
    apple_qty = int(apple_qty)
    if  apple_stock >= apple_qty:
        break

    print("Jumlah yang dimasukkan terlalu banyak. Stock tinggal: ", apple_stock)
    apple_qty = int(input("Masukkan jumlah apel: "))
while True :
    orange_qty = input("masukkan jumlah jeruk: ")
    orange_qty = int(orange_qty)
    if  orange_stock >= orange_qty:
        break

    print("Jumlah yang dimasukkan terlalu banyak. Stock tinggal: ", orange_stock)
while True :
    grape_qty= input("masukkan jumlah anggur: ")
    grape_qty = int(grape_qty)
    if  grape_stock >= grape_qty:
        break

    print("Jumlah yang dimasukkan terlalu banyak. Stock tinggal: ", grape_stock)
    
apple_total_price = apple_qty * apple_price
orange_total_price = orange_qty * orange_price
grape_total_price = grape_qty * grape_price

print("Total Belanja")
print()
print(f"Apel    : {apple_qty} x {apple_price} = {apple_total_price}")
print(f"jeruk    : {orange_qty} x {orange_price} = {orange_total_price}")
print(f"anggur    : {grape_qty} x {grape_price} = {grape_total_price}")
total = apple_total_price + orange_total_price + grape_total_price
print()
print(f"Total belanja: {total}")

money = input("Masukkan Jumlah Uang")
money = int(money) 

if money < total : 
    kurang = total - money
    hasil = "dibatalkan"
    print(f"Transaksi anda {hasil} uang nya kurang sebesar {kurang}")
elif money == total :
    print("Terima Kasih")
else:
    kembali = money - total
    print(f"Terima Kasih \n Uang kembali anda sebesar {kembali}")
    
    
