
#nama :Nadya



nama = ["apel","jeruk", "anggur"]
stock = ["20","15", "10"]
harga = ["10_000","15_000", "20_000"]      
index = [0,1,2]
total_harga = 0
keranjang = []



while True: 
    print("=== Selamat datang di pasar buah ===")

    print("List Menu : ")
    print(" 1. Menampilkan daftar buah")
    print(" 2. Menambahkan buah")
    print(" 3. Menghapus buah")
    print(" 4. Mengubah data buah")
    print(" 5. Exit Program")
    angka = input("Masukkan angka menu yang ingin dijalankan : ")
    print("Daftar Buah")
    if angka == "1":
    
        print(f"{'Index':<10} {'|Nama' :<10} {'|Stock':<10} {'|Harga':<10}")
        print("-"*40)
        for i in range(len(nama)):
            print(f"{i:<10} |{nama[i]:<10} |{stock[i]:<10} |{harga[i]:<10}")
    elif angka == "2":
        nama_buah = input("Masukkan nama buah : ")
        stock_buah = input("Masukkan stock buah : ")
        harga_buah = input("Masukkan harga buah : ")
        nama.append(nama_buah)
        stock.append(stock_buah)
        harga.append(harga_buah)
    
        print("daftar buah")
        
        print(f"|{'Index':<10} {'|Nama' :<10} {'|Stock':<10} {'|Harga':<10}")
        print("-"*40)
        for i in range(len(nama)):
            print(f"{i:<10} |{nama[i]:<10} |{stock[i]:<10} |{harga[i]:<10}")
        
            
        while True:
            confir_msg = input ("Lanjut tambah buah (yes:jika lanjut)?")
            if confir_msg.lower() == "yes": 
                nama_buah = input("Masukkan nama buah : ")
                stock_buah = input("Masukkan stock buah : ")
                harga_buah = input("Masukkan harga buah : ")
                nama.append(nama_buah)
                stock.append(stock_buah)
                harga.append(harga_buah)
    
                print("daftar buah")
        
                print(f"|{'Index':<10} {'|Nama' :<10} {'|Stock':<10} {'|Harga':<10}")
                print("-"*40)
                for i in range(len(nama)):
                    print(f"{i:<10} |{nama[i]:<10} |{stock[i]:<10} |{harga[i]:<10}")
            else:
               
                break
                
                
                        
    elif angka == "3":
       
        print(f"{'Index':<10} {'|Nama' :<10} {'|Stock':<10} {'|Harga':<10}")
        print("-"*40)
        for i in range(len(nama)):
            print(f"{i:<10} |{nama[i]:<10} |{stock[i]:<10} |{harga[i]:<10}")
        del_index = int(input("Masukkan index buah yang ingin dihapus :"))
        
        nama.pop(del_index)
        stock.pop(del_index)
        harga.pop(del_index)
    
        print("Daftar Buah")
        for i in range(len(nama)):
            print(f"{i:<10} |{nama[i]:<10} |{stock[i]:<10} |{harga[i]:<10}")
   
    elif angka == "4":
        print(f"{'Indeks':<10} {'|Nama':<10} {'|Stock':<10} {'|Harga':<10}")
        print("-"*40)
        for i in range(len(nama)):
            print(f"{i:<10} |{nama[i]:<10} |{stock[i]:<10} |{harga[i]:<10}")        
        keranjang = []
        beli_index =int(input("Masukkan index buah yang ingin di beli :"))
        jumlah_beli = (input("Masukkan jumlah buah yang ingin di beli :"))
        keranjang.append(nama[beli_index])
        keranjang.append(jumlah_beli)
        keranjang.append(harga[beli_index])
        if jumlah_beli > stock[beli_index]:

                print(f"Maaf stock tidak cukup, stock {nama[beli_index]} tinggal {stock[beli_index]}")
        else:
            print(f"{'Nama':<10} {'|Qty':<10} {'|Harga':<10}")
            print("-"*30)
            print(f"{nama[beli_index]:<10} |{jumlah_beli:<10} |{harga[beli_index]:<10}")
        

        while True:
            lanjut =input("Mau beli yang lain lagi? (ya/tidak)")
            if  lanjut == "ya": 
                keranjang = []
                beli_index =int(input("Masukkan index buah yang ingin di beli :"))
                jumlah_beli = (input("Masukkan jumlah buah yang ingin di beli :"))
                keranjang.append(nama[beli_index])
                keranjang.append(jumlah_beli)
                keranjang.append(harga[beli_index])
                nama_beli = keranjang[0]
                jumlah_beli = keranjang[1]
            if jumlah_beli > stock[beli_index]:
            
                while jumlah_beli > stock[beli_index]:

                    print(f"Maaf stock tidak cukup, stock {nama[beli_index]} tinggal {stock[beli_index]}")
                    break
                else:
                    print(f"{'Nama':<10} {'|Qty':<10} {'|Harga':<10}")
                    print("-"*30)
                    print(f"{nama[beli_index]:<10} |{jumlah_beli:<10} |{harga[beli_index]:<10}")
            else:
                break



           
            