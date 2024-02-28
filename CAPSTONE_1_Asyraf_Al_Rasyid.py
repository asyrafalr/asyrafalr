from tabulate import tabulate
import datetime as  dt

data_pesanan = {
    '12001':{'No HP' : '088712345678', 'Nama Pemesan':'Arsyil Malik','Alamat': 'jl. sarimanis blok 13','Quantity':2, 'Jenis Tabung Gas': '12kg', 'Tanggal Order': dt.date(2024,1,12), 'Total Biaya': 404000},
    '12002':{'No HP' : '081212337232', 'Nama Pemesan':'Andi F','Alamat':'jl.purwakarta V no.3','Quantity':1, 'Jenis Tabung Gas': '5kg', 'Tanggal Order': dt.date(2024,2,15), 'Total Biaya': 90000},
    '12003':{'No HP' : '085722388700', 'Nama Pemesan':'Alma S M','Alamat': 'jl. cijerah 3 no.24','Quantity':1, 'Jenis Tabung Gas': '12kg', 'Tanggal Order': dt.date(2024,1,10), 'Total Biaya': 202000},
    '12004':{'No HP' : '083369001444', 'Nama Pemesan':'Erik R Z','Alamat':'jl. kacapiring no.10','Quantity':3, 'Jenis Tabung Gas': '5kg', 'Tanggal Order': dt.date(2024,2,20),'Total Biaya': 270000 }}

harga_5kg = 90000
harga_12kg = 202000

#==========================================FUNGSI MAIN MENU=======================================================================================================================================
def main_menu():
    ''' Fungsi untuk memanggil menu utama dari program Data Tabung Gas Delivery Service
    '''
    print('''==================== Data Tabung Gas Delivery Service =====================\n
                1. Report Data Tabung Gas Delivery Service
                2. Menambahkan Tabung Gas Delivery Service
                3. Mengubah Data Tabung Gas Delivery Service
                4. Menghapus Data Tabung Gas Delivery Service
                5. Keluar''')
    choice = input('\nSilahkan pilih salah satu opsi berikut(1/2/3/4/5): ')
    return choice
    
def menu_read():
    '''Fungsi untuk memanggil menu utama read dari program Data Tabung Gas Delivery Service 
    '''
    print('''\n==================== Report Data Tabung Gas Delivery Service =====================\n
                1. Tampilkan Data Keseluruhan Tabung Gas Delivery Service
                2. Tampilkan Data Tertentu Tabung Gas Delivery Service
                3. Kembali ke Menu Utama''')
    read_choice = input('\nSilahkan pilih salah satu opsi berikut (1/2/3): ')
    return read_choice

def menu_create():
    '''Fungsi untuk memanggil menu utama create dari program Data Tabung Gas Delivery Service
    '''
    print('''==================== Menambahkan Data Tabung Gas Delivery Service =====================\n
                1. Tambahkan satu data pesanan
                2. Tambahkan banyak data pesanan
                3. Kembali ke Menu Utama''')
    create_choice = input('Silahkan pilih salah satu opsi berikut (1/2/3): ')
    return create_choice

def menu_update():
    '''Fungsi untuk memanggil menu utama update dari program Data Tabung Gas Delivery Service 
    '''
    print('''==================== Mengubah Data Tabung Gas Delivery Service =====================\n
                1. Ubah Data pesanan berdasarkan kolom
                2. Ubah Data pesanan satu baris berdasarkan kode pesanan
                3. Kembali ke menu ''')
    update_choice = input('\nSilahkan pilih salah satu opsi berikut (1/2/3): ') 
    return update_choice

def menu_delete():
    '''Fungsi untuk memanggil menu utama update dari program Data Tabung Gas Delivery Service 
    '''
    print('''==================== Menghapus Data Tabung Gas Delivery Service =====================\n
                1. Hapus Satu Data Tabung Gas Delivery Service
                2. Hapus Semua Data Tabung Gas Delivery Service
                3. Kembali ke Menu Utama''')
    delete_choice = input('Silahkan pilih salah satu opsi berikut (1/2/3): ')
    return delete_choice

#========================================FUNGSI SUB MENU READ==============================================================================
def report_all():
    '''Fungsi untuk menampilkan semua data dari program Data Tabung Gas Delivery Service 
    '''
    if not data_pesanan:
        print ('\nTidak ada data pesanan yang tersedia\n')
    
    else :
        list_kosong= []                                 # Tabulate digunakan untuk mengembalikkan hasil print dalam bentuk tabel agar outputnya lebih mudah untuk dibaca, perlu dimunculkan dalam bentuk list
        for key,value in data_pesanan.items() :
            list_baru = [key,value['No HP'],value['Nama Pemesan'],value['Alamat'],value['Quantity'],value['Jenis Tabung Gas'], value['Tanggal Order'],value['Total Biaya']]
            list_kosong.append(list_baru)
        print(tabulate(list_kosong, headers=['Kode Pesanan','No HP','Nama Pemesan','Alamat','Quantity','Jenis Tabung Gas','Tanggal Order','Total Biaya'], tablefmt="fancy_grid"))

def search_data():
    '''Fungsi untuk menampilkan data tertentu program Data Tabung Gas Delivery Service 
    '''
    if not data_pesanan:
        print ('\nTidak ada data pesanan yang tersedia\n')
    else :
     while True:
        print('''
                1. Tampilkan Pesanan dengan kode pesanan tertentu
                2. Tampilkan Pesanan Berdasarkan Tanggal Order
                3. Kembali ke Menu Data Report''')
        choice = input("\nMasukkan pilihan Anda (1/2/3): ")
        if choice =='1':
            choice_pesanan = input('\n Harap masukkan Kode Pesanan yang ingin Anda cari: ').upper()

            if choice_pesanan in data_pesanan:
                print(f'\nInformasi Kode Pesanan: {choice_pesanan} adalah:')
                value = data_pesanan[choice_pesanan]
                list_kosong = [[choice_pesanan, value['No HP'],value['Nama Pemesan'],value['Alamat'],value['Quantity'],value['Jenis Tabung Gas'], value['Tanggal Order'],value['Total Biaya']]]
                print(tabulate(list_kosong, headers=['Kode Pesanan','No HP','Nama Pemesan','Alamat','Quantity','Jenis Tabung Gas','Tanggal Order','Total Biaya'], tablefmt="fancy_grid"))

            else:
                print('Kode Pesanan tidak ditemukan')

        elif choice =='2':
                choice2 = input('Pilih urutan berdasarkan: 1.tanggal terbaru / 2.tanggal terlampau ')
                if choice2  == '1':
                    sort_by_Tanggal_Desc = sorted(data_pesanan.items(), key=lambda item:item[1]['Tanggal Order'], reverse=True)
                    print('\nDaftar Pesanan berdasarkan Tanggal Order')
                    list_kosong =[]
                    for key,value in sort_by_Tanggal_Desc:
                        list_baru = [key,value['No HP'],value['Nama Pemesan'],value['Alamat'],value['Quantity'],value['Jenis Tabung Gas'], value['Tanggal Order'],value['Total Biaya']] 
                        list_kosong.append(list_baru)
                    print(tabulate(list_kosong, headers=['Kode Pesanan','No HP','Nama Pemesan','Alamat','Quantity','Jenis Tabung Gas','Tanggal Order','Total Biaya'], tablefmt="fancy_grid"))
                elif choice2 == '2':
                    sort_by_Tanggal_Asc = sorted(data_pesanan.items(), key=lambda item:item[1]['Tanggal Order'])
                    print('\nDaftar Pesanan berdasarkan Tanggal Order')
                    list_kosong =[]
                    for key,value in sort_by_Tanggal_Asc:
                        list_baru = [key,value['No HP'],value['Nama Pemesan'],value['Alamat'],value['Quantity'],value['Jenis Tabung Gas'], value['Tanggal Order'],value['Total Biaya']] 
                        list_kosong.append(list_baru)
                    print(tabulate(list_kosong, headers=['Kode Pesanan','No HP','Nama Pemesan','Alamat','Quantity','Jenis Tabung Gas','Tanggal Order','Total Biaya'], tablefmt="fancy_grid"))
                else : 
                    print('\nMohon masukkan input yang benar\n')
                
        elif choice == '3':
             break
        
        else:
             print('Mohon masukkan input yang benar')
    
#========================================FUNGSI SUB MENU CREATE==============================================================================
def add_data():
    '''Fungsi untuk menambahkan satu data ke program Data Tabung Gas Delivery Service 
    '''
    data_temp = {
          'No HP': '080012341234',                      # data_temp digunakan untuk memanggil key nya saja dalam dictionary
          'Nama Pemesan' : 'Nama template',
          'Alamat' : 'Jalan jalan',
          'Quantity':3, 
          'Jenis Tabung Gas':'12kg',
          'Tanggal Order':dt.date(1111,1,11),
          'Total Biaya': 999990
     }
    data_kosong = dict.fromkeys(data_temp.keys())
    report_all()

    while True:
        key = (input('Masukkan kode pesanan:'))
        if key in data_pesanan or key.isdigit() == False or len(key)<5:
            print('\nMasukkan kode pesanan yang benar\n')
            
        else:
            data_kosong['No HP'] = input('Nomor HP Pelanggan (min. 11 angka):')
            if data_kosong['No HP'].isdigit()== False or len(data_kosong['No HP']) < 11 or len(data_kosong['No HP']) > 13 or data_kosong['No HP'].startswith('08') == False:
                print('\nMasukkan input yang benar\n')
                break

            data_kosong['Nama Pemesan'] = input('Nama Pelanggan:').title()
            if data_kosong['Nama Pemesan'].replace(' ','').isalpha() == False:
                print('Hanya boleh menginput alphabet')
                break
            
            data_kosong['Alamat'] = input('Alamat Pelanggan:').title()
            if len(data_kosong['Alamat']) < 3 or data_kosong['Alamat'].isdigit() :
                print('Mohon ketikkan yang sesuai (ex: Jl. jalan no.00)')
                break
                            
            data_kosong['Quantity'] = (input('Jumlah Barang:'))
            if data_kosong['Quantity'].isdigit() == False:
                print ('Mohon masukkan input yang benar')
                break
                                    
    
            data_kosong['Jenis Tabung Gas'] = input('Silahkan pilih 1. 5kg / 2. 12kg (ketik 1/2):')
            if data_kosong['Jenis Tabung Gas'] == '1':
                data_kosong['Jenis Tabung Gas'] =  '5kg'
                quantity = int(data_kosong['Quantity'])
                total_biaya = quantity * harga_5kg
                data_kosong['Total Biaya'] = total_biaya

            elif data_kosong['Jenis Tabung Gas'] == '2':
                data_kosong['Jenis Tabung Gas'] = '12kg'
                quantity = int(data_kosong['Quantity'])
                total_biaya = quantity * harga_12kg
                data_kosong['Total Biaya'] = total_biaya
            else: 
                print('Mohon Masukkan input yang benar')
                break
            try:
                tanggal_pemesanan = input('Masukkan  tanggal order(yyyy-mm-dd):')
                tahun, bulan, hari = map(int, tanggal_pemesanan.split('-'))
                tanggal_pemesanan = dt.date(tahun, bulan, hari)
                data_kosong['Tanggal Order'] = tanggal_pemesanan
            except Exception as x:
                print('Mohon gunakan penulisan tanggal yang sesuai (yyyy-mm-dd)',x) 
                break

            while True:
                save = input('Apakah data yang dimasukkan sudah benar? (y/n):').upper()
                if save  == 'Y':
                    data_pesanan.update({key:data_kosong})
                    print('Data sudah tersimpan')
                    break
                elif save == 'N':
                    print('Data tidak tersimpan. Kembali ke menu sebelumnya')
                    break
                else:
                    print('Input tidak valid')
        report_all()
        break
                

def add_many():
    '''Fungsi untuk menambahkan data sesuai jumlah data yang ingin diinput program Data Tabung Gas Delivery Service 
    '''
    report_all()

    data_kosong = []
    for key,value in data_pesanan.items():
        kode_pesanan = key
        nomor = value['No HP']
        nama_pemesan = value['Nama Pemesan']
        alamat = value['Alamat']
        jumlah = value['Quantity']
        jenis = value['Jenis Tabung Gas']
        tanggal = value['Tanggal Order']
        total = value['Total Biaya']
        data_kosong.append([kode_pesanan,nomor,nama_pemesan,alamat,jumlah,jenis,tanggal,total])
    try:
        banyak_pesanan = int(input('Masukkan jumlah pesanan yang ingin ditambahkan:'))      # Untuk menambahkan data sesuai input yang diinginkan 
     
        for banyak in range(banyak_pesanan):
            kode_pesanan = input('Masukkan kode pesanan:')
            if kode_pesanan in data_pesanan:
                print('\nKode pesanan sudah tersedia\n')
                break

            elif kode_pesanan.isdigit() == False:
                print('Mohon masukkan hanya angka')  
                break

            else:
                nomor = input('Nomor HP Pelanggan (Min. 11 Angka):')
                if nomor.isdigit() == False or len(nomor) < 11 or len(nomor) > 13 or nomor.startswith('08') == False  :
                    print('\nMasukkan input yang benar\n')
                    break

                nama_pemesan = input('Nama Pelanggan:').title()
                if nama_pemesan.replace(' ','').isalpha() == False:
                    print('Hanya boleh menginput alphabet')
                    break
                
                alamat = input('Alamat Pelanggan:').title()
                if len(alamat) < 3 or alamat.isdigit() :
                    print('Mohon ketikkan yang sesuai (ex: Jl. jalan no.00)')
                    break
                                
                quantity = (input('Jumlah Barang:'))
                if quantity.isdigit == False:
                    print ('Mohon masukkan input yang benar')
                    break
                                        
        
                jenis = input('Silahkan pilih jenis tabung gas 1. 5kg / 2. 12kg (ketik 1/2):')
                if jenis == '1':
                    jenis =  '5kg'
                    jumlah= int(quantity)
                    total_biaya = jumlah * harga_5kg
                    total = total_biaya

                elif jenis == '2':
                    jenis = '12kg'
                    jumlah = int(quantity)
                    total_biaya = jumlah * harga_12kg
                    total = total_biaya

                else: 
                    print('Mohon Masukkan input yang benar')
                    break
                try:
                    tanggal_pemesanan = input('Masukkan  tanggal order(yyyy-mm-dd):')
                    tahun, bulan, hari = map(int, tanggal_pemesanan.split('-'))
                    tanggal_pemesanan = dt.date(tahun, bulan, hari)
                    tanggal = tanggal_pemesanan
                except Exception as x:
                    print('Mohon gunakan penulisan tanggal yang sesuai (yyyy-mm-dd)',x)
                    break
                        
                while True:
                    save = input('Apakah data yang dimasukkan sudah benar? (y/n):').upper()
                    if save  == 'Y':
                        data_pesanan[kode_pesanan] = {
                        'No HP': nomor,                      # data_temp digunakan untuk memanggil key nya saja dalam dictionary
                        'Nama Pemesan' : nama_pemesan,
                        'Alamat' : alamat,
                        'Quantity': quantity, 
                        'Jenis Tabung Gas':jenis,
                        'Tanggal Order': tanggal,
                        'Total Biaya': total
                        }
                        print('Data sudah tersimpan')
                        break
                    elif save == 'N':
                        print('Data tidak tersimpan. Kembali ke menu sebelumnya')
                        break
                    else:
                        print('Input tidak valid')
            report_all()
    except Exception as x:
            print('Mohon hanya masukkan angka',x)                


#==================================================== FUNGSI MENU UPDATE ===========================================================================================================

def modify_one_column():
    '''Fungsi untuk mengubah satu data di program Data Tabung Gas Delivery Service 
    '''
    if not data_pesanan:
        print ('\nTidak ada data pesanan yang tersedia\n')
    
    else :
        report_all()

        while True:
            key = input('Silahkan pilih kode pesanan yang akan diubah:')
            if key in data_pesanan:
                print(f'\nKode Pesanan {key} ada di data pesanan. Pilih kolom yang akan anda ubah:')
                print('''
                        1. Ubah Nomor HP Pemesan
                        2. Ubah Nama Pemesan
                        3. Ubah Alamat Pemesan
                        4. Ubah Jumlah Pesanan
                        5. Ubah Jenis Tabung Gas
                        6. Ubah Tanggal Pemesanan
                        7. Kembali ke Menu''')
                
                update_pesanan = input('\nMasukan pilihan data yang ingin diubah:')
                
                if update_pesanan == '1':
                        nomor_baru = input('Masukan Nomor HP baru pemesan: ')
                        if nomor_baru.isdigit()== False or len(nomor_baru) < 11 or len(nomor_baru) > 13 or nomor_baru.startswith('08') == False :
                            print('\nMasukkan input yang benar\n')
                            
                        else:
                            while True:
                                save = input('Apakah anda ingin menyimpan data(Y/N)?: ').upper()
                                if save == 'Y':
                                    print('Data berhasil disimpan')
                                    data_pesanan[key]['No HP'] = nomor_baru
                                    break
                                elif save == 'N':
                                    print('Data tidak disimpan')
                                    break
                                else: 
                                    print('Masukkan input yang benar')
                            break

                elif update_pesanan == '2':
                        nama_baru = input('Masukan nama baru pemesan: ').title()
                        if nama_baru.replace(' ','').isalpha() == False:
                            print('Hanya boleh menginput alphabet')
                            
                        else:
                            while True:
                                save = input('Apakah anda ingin menyimpan data(Y/N)?: ').upper()
                                if save == 'Y':
                                    print('Data berhasil disimpan')
                                    data_pesanan[key]['Nama Pemesan'] = nama_baru 
                                elif save == 'N':
                                    print('Data tidak disimpan')
                                    break
                                else: 
                                    print('Masukkan input yang benar')
                            break

                elif update_pesanan == '3':
                        alamat_baru= input('Masukan Alamat baru pemesan: ').title()
                        if len(alamat_baru) < 3 or alamat_baru.isdigit() :
                            print('Mohon ketikkan yang sesuai (ex: Jl. jalan no.00)')

                        else:
                            while True:
                                save = input('Apakah anda ingin menyimpan data(Y/N)?: ').upper()
                                if save == 'Y':
                                    print('Data berhasil disimpan')
                                    data_pesanan[key]['Alamat'] = alamat_baru 
                                    break
                                elif save == 'N':
                                    print('Data tidak disimpan')
                                    break
                                else: 
                                    print('Masukkan input yang benar')
                            break
                                
                elif update_pesanan == '4':
                    jumlah_baru = input('Masukan jumlah pesanan baru: ')
                    if jumlah_baru.isdigit() == False:
                        print ('Mohon masukkan input yang benar')
                    else:
                        while True:
                            save = input('Apakah anda ingin menyimpan data(Y/N)?: ').upper()
                            if save == 'Y':
                                print('Data berhasil disimpan')
                                data_pesanan[key]['Quantity'] = jumlah_baru
                                quantity = int(jumlah_baru)
                                if data_pesanan[key]['Jenis Tabung Gas'] == '5kg':
                                    total_biaya = quantity * harga_5kg
                                    data_pesanan[key]['Total Biaya'] = total_biaya
                                elif data_pesanan[key]['Jenis Tabung Gas'] == '12kg':
                                    total_biaya = quantity * harga_12kg
                                    data_pesanan[key]['Total Biaya'] = total_biaya
                                break
                            elif save == 'N':
                                print('Data tidak disimpan')
                                break
                            else: 
                                print('Masukkan input yang benar')
                            break
                                
                elif update_pesanan == '5':
                    jenis_baru = input('Masukan Jenis tabung gas baru (1. 5kg/ 2. 12kg): ')
                    if jenis_baru != '1' and jenis_baru != '2':
                        print('Mohon input 1 / 2')
                    else:
                        while True:
                            save = input('Apakah anda ingin menyimpan data(Y/N)?: ').upper()
                            if save == 'Y':
                                if jenis_baru == '1':
                                    print('Data berhasil disimpan')
                                    jenis_baru = data_pesanan[key]['Jenis Tabung Gas']
                                    data_pesanan[key]['Jenis Tabung Gas'] = '5kg'
                                    total_biaya = harga_5kg * int(data_pesanan[key]['Quantity'])
                                    data_pesanan[key]['Total Biaya'] = total_biaya
                                    break
                                elif jenis_baru == '2':
                                    jenis_baru = data_pesanan[key]['Jenis Tabung Gas']
                                    data_pesanan[key]['Jenis Tabung Gas'] = '12kg'
                                    total_biaya = harga_12kg * int(data_pesanan[key]['Quantity'])
                                    data_pesanan[key]['Total Biaya'] = total_biaya
                                    break
                            elif save == 'N':
                                print ('Data tidak disimpan')
                                break
                            else:
                                print('Mohon masukkan input yang benar')
                                    
                elif update_pesanan == '6':
                    try:
                        tanggal_daftar = input("Masukkan Tanggal Pendaftaran (YYYY-MM-DD): ")
                        tahun, bulan, hari = map(int, tanggal_daftar.split('-'))
                        tanggal_daftar = dt.date(tahun, bulan, hari)
                        data_pesanan[key]['Tanggal Order'] = tanggal_daftar
                    except Exception as x:
                        print('Mohon gunakan penulisan tanggal yang sesuai (yyyy-mm-dd)',x)
                        break                
                elif update_pesanan == '7':
                    break
                else:
                    print('Input tidak valid')

            else:
                print('Data pesanan tidak ditemukan')
            report_all()
            break

def modify_one_data():
    '''Fungsi untuk mengubah data satu baris berdasarkan kode pesanan di program Data Tabung Gas Delivery Service 
    '''
    if not data_pesanan:
        print ('\nTidak ada data pesanan yang tersedia\n')
    
    else :
        data_temp = {                           # data_temp digunakan untuk memanggil key nya saja dalam dictionary
            'No HP': '080012341234',
            'Nama Pemesan' : 'Nama template',
            'Alamat' : 'Jalan jalan',
            'Quantity':3, 
            'Jenis Tabung Gas':'12kg',
            'Tanggal Order':dt.date(1111,1,11),
            'Total Biaya':999999
        }
        data_kosong = dict.fromkeys(data_temp.keys())
        report_all()

        while True:
            key = (input('Masukkan kode pesanan:'))
            if key in data_pesanan:
                    print(f'\nInformasi Kode Pesanan: {key} adalah:')
                    list_kosong =[]
                    value = data_pesanan[key]
                    list_kosong = [[key, value['No HP'],value['Nama Pemesan'],value['Alamat'],value['Quantity'],value['Jenis Tabung Gas'], value['Tanggal Order'],value['Total Biaya']]]
                    print(tabulate(list_kosong, headers=['Kode Pesanan','No HP','Nama Pemesan','Alamat','Quantity','Jenis Tabung Gas','Tanggal Order','Total Biaya'], tablefmt="fancy_grid"))
                    
                    while True: 
                        save = input('Apakah anda ingin melanjutkan ubah data?(y/n):').upper()
                        if save == 'Y':
                            data_kosong['No HP'] = input('Nomor HP Pelanggan (Min. 11 angka):')
                            if data_kosong['No HP'].isdigit()== False or len(data_kosong['No HP']) < 11 or len(data_kosong['No HP']) > 13 or data_kosong['No HP'].startswith('08') == False :
                                print('\nMasukkan input yang benar\n')
                                break

                            data_kosong['Nama Pemesan'] = input('Nama Pelanggan:').title()
                            if data_kosong['Nama Pemesan'].replace(' ','').isalpha() == False:
                                print('Hanya boleh menginput alphabet')
                                break
                            
                            data_kosong['Alamat'] = input('Alamat Pelanggan:').title()
                            if len(data_kosong['Alamat']) < 3 or data_kosong['Alamat'].isdigit() :
                                print('Mohon ketikkan yang sesuai (ex: Jl. jalan no.00)')
                                break
                                            
                            data_kosong['Quantity'] = (input('Jumlah Barang:'))
                            if data_kosong['Quantity'].isdigit() == False:
                                print ('Mohon masukkan input yang benar')
                                break
                                                    
                    
                            data_kosong['Jenis Tabung Gas'] = input('Silahkan pilih 1. 5kg / 2. 12kg (ketik 1/2):')
                            if data_kosong['Jenis Tabung Gas'] == '1':
                                data_kosong['Jenis Tabung Gas'] =  '5kg'
                                quantity = int(data_kosong['Quantity'])
                                if data_kosong['Jenis Tabung Gas'] == '5kg':
                                    total_biaya = quantity * harga_5kg
                                    data_kosong['Total Biaya'] = total_biaya
                                
                            elif data_kosong['Jenis Tabung Gas'] == '2':
                                data_kosong['Jenis Tabung Gas'] =  '12kg'
                                quantity = int(data_kosong['Quantity'])
                                if data_kosong['Jenis Tabung Gas'] == '12kg':
                                    total_biaya = quantity * harga_12kg
                                    data_kosong['Total Biaya'] = total_biaya

                            else: 
                                print('Mohon Masukkan input yang benar')
                                break
                            try:
                                tanggal_pemesanan = input('Masukkan  tanggal order(yyyy-mm-dd):')
                                tahun, bulan, hari = map(int, tanggal_pemesanan.split('-'))
                                tanggal_pemesanan = dt.date(tahun, bulan, hari)
                                data_kosong['Tanggal Order'] = tanggal_pemesanan
                            except Exception as x:
                                print('Mohon gunakan penulisan tanggal yang sesuai (yyyy-mm-dd)',x)
                                break
                            while True:
                                save = input('Apakah data yang dimasukkan sudah benar? (y/n):').upper()
                                if save  == 'Y':
                                    data_pesanan.update({key:data_kosong})
                                    print('Data sudah tersimpan')
                                    report_all()
                                    break
                                elif save == 'N':
                                    print('Data tidak tersimpan. Kembali ke menu sebelumnya')
                                    break
                                else:
                                    print('Input tidak valid')
                            break
                        elif save == 'N':
                            print('Data tidak jadi diubah')
                            break
                        else:
                            print('Mohon masukkan input y/n')
            else:
                print('\nMasukkan kode pesanan yang benar\n')
            break

#====================================================== FUNGSI SUB MENU DELETE =================================================================================================================================
def delete_one ():
    '''Fungsi untuk menghapus satu data berdasarkan kode pesanan di program Data Tabung Gas Delivery Service 
    '''
    if not data_pesanan:
        print ('\nTidak ada data pesanan yang tersedia\n')
    
    else :
        report_all()

        key = input('Masukan data pesanan yang akan di hapus berdasarkan kode pesanan: ')
        if key in data_pesanan:
            print(f'Data {key} Terdapat di data pesanan. Data dapat di Hapus')
            while True:
                user_delete = input(f'Apakah Anda ingin menghapus data pesanan {key} ?(Y/N): ').upper()
                if user_delete == 'Y':
                    del data_pesanan[key]
                    print(f'\nData pesanan{key} telah berhasil dihapus\n')
                    break
                elif user_delete == 'N':
                    print(f'Data pesanan {key} tidak di hapus') 
                    break
                else:
                    print('Input tidak valid, silahkan masukkan Y / N')
                    
        else:
            print('data tidak di temukan')

def delete_all():
    '''Fungsi untuk menghapus seluruh data yang tersedia di program Data Tabung Gas Delivery Service 
    '''
    if not data_pesanan:
        print ('\nTidak ada data pesanan yang tersedia\n')
    
    else :
        report_all()

        passwordKey = 'hapus'
        
        while True:
            hapus_semua = input('apakah anda yakin ingin menghapus semua data pesanan? (y/n): ').upper()
            if hapus_semua == 'Y':
                password = input('Masukkan password untuk menghapus semua data:')
                if password == passwordKey:
                    data_pesanan.clear()
                    print('Semua data pesanan sudah di hapus')
                    report_all()
                    break
                else :
                    print('\nPassword salah. Kembali ke menu sebelumnya\n')
                    break
            elif hapus_semua == 'N':
                print('Data pesanan tidak jadi dihapus') 
                break
            else:
                print('Masukkan input y/n')

#====================================================== FUNGSI START=============================================================================================================================================
def start():
    '''Fungsi untuk memulai program Data Tabung Gas Delivery Service 
    '''
    while True:
        choice = main_menu()
        if choice == '1':
            while True:    
                read_choice = menu_read()
                if read_choice == '1':
                      report_all()
                elif read_choice == '2':
                      search_data()
                elif read_choice == '3':
                      break
                else:
                    print("Pilihan tidak valid. Silakan coba lagi.")

        elif choice == '2':
            while True:  
                create_choice = menu_create()
                if create_choice == '1':
                     add_data()
                elif create_choice == '2':
                     add_many()
                elif create_choice == '3':
                     break
                else:
                    print("Pilihan tidak valid. Silakan coba lagi.")


        elif choice == '3':
            while True:  
                update_choice = menu_update()
                if update_choice == '1':
                       modify_one_column()
                elif update_choice == '2':
                       modify_one_data()
                elif update_choice == '3':
                       break
                else:
                    print("Pilihan tidak valid. Silakan coba lagi.")
        
        elif choice == '4':
            while True:  
                delete_choice = menu_delete()
                if delete_choice == '1':
                       delete_one()
                elif delete_choice == '2':
                       delete_all()
                elif delete_choice == '3':
                      break
                else:
                    print("Pilihan tidak valid. Silakan coba lagi.")

        elif choice == '5':
                print("Keluar dari program...")
                break
        
        else:
                print("\nPilihan tidak valid. Silakan coba lagi.\n")


start()