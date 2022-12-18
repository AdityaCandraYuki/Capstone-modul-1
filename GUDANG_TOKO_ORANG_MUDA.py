listbarang = {
    "WineImport": {
        "WI1": {
            "merek": "Angciu",
            "Rasa": "Rose",
            "Asal": "Perancis",
            "Alkohol": 15,
            "Stock": 15,
            "Distributor": "Pt. Matahari"
        },
        "WI2": {
            "merek": "Angciu",
            "Rasa": "Jeruk",
            "Asal": "Perancis",
            "Alkohol": 15,
            "Stock": 20,
            "Distributor": "Pt. Nusantara"
        },
        "WI3": {
            "merek": "Smirf",
            "Rasa": "Mixed",
            "Asal": "Rusia",
            "Alkohol": 30,
            "Stock": 8,
            "Distributor": "Pt. Arangkayu"
        }
    },
    "Winedomestik": {
        "WD1": {
            "merek": "Opa",
            "Rasa": "Berry",
            "Asal": "Pasuruan",
            "Alkohol": 25,
            "Stock": 6,
            "Distributor": "Pt. Matahari"
        }
    }
}


def ReadDataGudang(kadar=None):
    if kadar is None:
        if len(listbarang) == 0:
            print('\t Belum ada data')
        else:
            print(120 * "+")
            print('DAFTAR GUDANG MINUMAN TOKO ORANG MUDA'.center(125))
            print(120 * "+")
            print('| Import/lokal \t| Kode\t| merek\t| Rasa\t|  Asal\t\t|  Alkohol\t| Stock| Distributor\t|')
            print(3 * "--------------------------------------".center(20))
            for keyitems in listbarang:
                # print(keyitems)
                for kode in listbarang[keyitems]:
                    # print([keyitems])
                    print(
                        f"|{keyitems:>5}\t|{kode:>1} \t|{listbarang[keyitems][kode]['merek']}\t| {listbarang[keyitems][kode]['Rasa']}\t| {listbarang[keyitems][kode]['Asal']} \t| {listbarang[keyitems][kode]['Alkohol']}%\t\t| {listbarang[keyitems][kode]['Stock']}\t| {listbarang[keyitems][kode]['Distributor']}\t|\t")
    else:
        if len(listbarang) == 0:
            print('\t Belum ada data')
        else:
            print(125 * "+")
            print('DAFTAR GUDANG MINUMAN TOKO ORANG MUDA'.center(125))
            print(125 * "+")
            print('| Import/lokal \t| Kode\t| merek\t| Rasa\t|  Asal\t\t|  Alkohol\t| Stock| Distributor\t|')
            print(3 * "--------------------------------------".center(25))
            for keyitems in listbarang:
                # print(keyitems)
                for kode in listbarang[keyitems]:
                    splitkadar = str(kadar).split("-")
                    # print(splitkadar)
                    if int(splitkadar[0]) <= listbarang[keyitems][kode]['Alkohol'] <= int(splitkadar[1]):
                        print(
                            f"|{keyitems:>5}\t|{kode:>1} \t|{listbarang[keyitems][kode]['merek']}\t| {listbarang[keyitems][kode]['Rasa']}\t| {listbarang[keyitems][kode]['Asal']} \t| {listbarang[keyitems][kode]['Alkohol']}%\t\t| {listbarang[keyitems][kode]['Stock']}\t| {listbarang[keyitems][kode]['Distributor']}\t|\t")


def menambahMinuman():
    while True:
        ImportLokal = input('Tipe minuman [Import / Lokal] (Case sensitive) : ')
        if ImportLokal == 'Import' or ImportLokal == 'Lokal':
            break

    kode = input('Masukkan kode : ')
    if kode in listbarang['Winedomestik']:
        print(120 * "+")
        print("Data sudah ada".center(125))
        print(120 * "+")
    elif kode in listbarang['WineImport']:
        print(120 * "+")
        print("Data sudah ada".center(125))
        print(120 * "+")
    else:
        merk = input('Masukkan Merk Minuman yang akan disimpan : ')
        rasa = input('Masukkan Rasa Minuman yang akan disimpan : ')
        asal = input('Masukkan Asal pembuatan minumannya : ')
        kadar = int(input('Berapa persen kadar alkoholnya? : '))
        stok = int(input('Masukkan Stock Minuman yang akan disimpan : '))
        distributor = input('Masukkan perusahaan distributornya [Maksimal 13 karakter] : ')
    
        if ImportLokal == 'Import':
            listbarang['WineImport'][kode] = {}
            listbarang['WineImport'][kode]['merek'] = merk
            listbarang['WineImport'][kode]['Rasa'] = rasa
            listbarang['WineImport'][kode]['Asal'] = asal
            listbarang['WineImport'][kode]['Alkohol'] = kadar
            listbarang['WineImport'][kode]['Stock'] = stok
            listbarang['WineImport'][kode]['Distributor'] = distributor
        else:
            listbarang['Winedomestik'][kode] = {}
            listbarang['Winedomestik'][kode]['merek'] = merk
            listbarang['Winedomestik'][kode]['Rasa'] = rasa
            listbarang['Winedomestik'][kode]['Asal'] = asal
            listbarang['Winedomestik'][kode]['Alkohol'] = kadar
            listbarang['Winedomestik'][kode]['Stock'] = stok
            listbarang['Winedomestik'][kode]['Distributor'] = distributor
        print(120 * "+")
        print("Data berhasil disimpan".center(125))
        print(120 * "+")


def mengubahMinuman():
    kode = input("Masukkan kode minuman yang akan diubah : ")
    if kode in listbarang['Winedomestik']:
        merk = input('Masukkan Merk Minuman yang akan diubah : ')
        rasa = input('Masukkan Rasa Minuman yang akan diubah  : ')
        asal = input('Masukkan Asal pembuatan minumannya : ')
        kadar = int(input('Berapa persen kadar alkoholnya? : '))
        stok = int(input('Masukkan Stock Minuman yang akan disimpan : '))
        distributor = input('Masukkan perusahaan distributornya : ')
        while True:
            print("Apakah anda yakin ingin mengubah data minuman dengan kode", kode, "[Ya / Tidak]? ", end='')
            yesno = input()
            if yesno.lower() == 'ya':
                listbarang['Winedomestik'][kode]['merek'] = merk
                listbarang['Winedomestik'][kode]['Rasa'] = rasa
                listbarang['Winedomestik'][kode]['Asal'] = asal
                listbarang['Winedomestik'][kode]['Alkohol'] = kadar
                listbarang['Winedomestik'][kode]['Stock'] = stok
                listbarang['Winedomestik'][kode]['Distributor'] = distributor
                print("Data Sudah Diubah.")
                break
            elif yesno.lower() == "tidak":
                break
    elif kode in listbarang['WineImport']:
        merk = input('Masukkan Merk Minuman yang akan diubah : ')
        rasa = input('Masukkan Rasa Minuman yang akan diubah : ')
        asal = input('Masukkan Asal pembuatan minumannya : ')
        kadar = int(input('Berapa persen kadar alkoholnya? : '))
        stok = int(input('Masukkan Stock Minuman yang akan diubah : '))
        distributor = input('Masukkan perusahaan distributornya : ')
        while True:
            print("Apakah anda yakin ingin mengubah data minuman dengan kode", kode, "[Ya / Tidak]? ", end='')
            yesno = input()
            if yesno.lower() == 'ya':
                listbarang['WineImport'][kode]['merek'] = merk
                listbarang['WineImport'][kode]['Rasa'] = rasa
                listbarang['WineImport'][kode]['Asal'] = asal
                listbarang['WineImport'][kode]['Alkohol'] = kadar
                listbarang['WineImport'][kode]['Stock'] = stok
                listbarang['WineImport'][kode]['Distributor'] = distributor
                print("Data Terupdate")
                break
            elif yesno.lower() == "tidak":
                break
    else:
        print(120 * "+")
        print("Data yang anda cari tidak ada".center(125))
        print(120 * "+")


def menghapusMinuman():
    kode = input("Masukkan kode minuman yang akan dihapus : ")
    if kode in listbarang['Winedomestik']:
        while True:
            print("Apakah anda yakin ingin menghapus data minuman dengan kode", kode, "[Ya / Tidak]? ", end='')
            yesno = input()
            if yesno.lower() == 'ya':
                listbarang['Winedomestik'].pop(kode)
                print(120 * "+")
                print("Data Dihapus".center(125))
                print(120 * "+")
                break
            elif yesno.lower() == "tidak":
                break
    elif kode in listbarang['WineImport']:
        while True:
            print("Apakah anda yakin ingin menghapus data minuman dengan kode", kode, "[Ya / Tidak]? ", end='')
            yesno = input()
            if yesno.lower() == 'ya':
                listbarang['WineImport'].pop(kode)
                print(120 * "+")
                print("Data Dihapus".center(125))
                print(120 * "+")
                break
            elif yesno.lower() == "tidak":
                break
    else:
        print("Data yang anda cari tidak ada")


def main():
    while True:
        print(120 * "+")
        print("Selamat Datang di Sistem Pergudangan Toko Orang Muda".center(125))
        print(120 * "+")
        print("1. Menampilkan Stok Gudang")
        print("2. Menambah Stok Gudang")
        print("3. Menghapus Stok Gudang")
        print("4. Mengedit Stok Gudang")
        print("5. Exit Program")
        while True:
            menu = int(input("Masukkan angka menu yang ingin dijalankan [1-5] : "))
            if menu > 5 or menu < 1:
                print("Pilihan yang anda masukkan salah\n")
            else:
                print("")
                break

        if menu == 1:
            print("1. Menampilkan Semua Stok Gudang")
            print("2. Menampilkan Stok Gudang berdasarkan Kadar Alkohol")
            print("3. Kembali Ke Menu Utama")
            while True:
                menusatu = int(input("Masukkan angka menu yang ingin dijalankan [1-3] : "))
                if menusatu > 3 or menusatu < 1:
                    print(120 * "+")
                    print("Pilihan yang anda masukkan salah\n".center(125))
                    print(120 * "+")
                else:
                    print("")
                    break

            if menusatu == 1:
                ReadDataGudang()
            elif menusatu == 2:
                kadar = input("Masukkan range nilai kadar alkohol. Contoh:(1-25) : ")
                ReadDataGudang(kadar)
            elif menusatu == 3:
                main()
        elif menu == 2:
            ReadDataGudang()
            menambahMinuman()
        elif menu == 3:
            ReadDataGudang()
            menghapusMinuman()
        elif menu == 4:
            ReadDataGudang()
            mengubahMinuman()
        elif menu == 5:
            print(120 * "+")
            print("Terimakasih telah menggunakan program ini".center(125))
            print(120 * "+")
            break

main()
