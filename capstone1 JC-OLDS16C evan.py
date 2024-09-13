data = [
{
    'kodeindex' : '01',
    'bidang'    : 'Kesehatan',
    'nama'      : 'Evan',
    'telephone' : '08975107611',
    'alamat'    : 'Jalan mulyosari prima 20',
    'pekerjaan' : 'dokter umum'
},
{
    'kodeindex' : '02',
    'bidang'    : 'Kesehatan',
    'nama'      : 'Alvin',
    'telephone' : '08876107621',
    'alamat'    : 'Jalan ketintang timur 101',
    'pekerjaan' : 'dokter mata'
},
{
    'kodeindex' : '03',
    'bidang'    : 'Keamanan',
    'nama'      : 'Stevin',
    'telephone' : '085261076223',
    'alamat'    : 'Jalan wonorejo v/ D-10',
    'pekerjaan' : 'Polisi'
},
{
    'kodeindex' : '04',
    'bidang'    : 'Keamanan',
    'nama'      : 'Carlo',
    'telephone' : '085388819333',
    'alamat'    : 'Jalan sutorejo tengah 56',
    'pekerjaan' : 'Pemadam kebakaran'
},
{   'kodeindex' : '05',
    'bidang'    : 'Pendidikan',
    'nama'      : 'Budi',
    'telephone' : '087830002433',
    'alamat'    : 'Jalan prapen indah 56',
    'pekerjaan' : 'Guru'
},
{
    'kodeindex' : '06',
    'bidang'    : 'Pendidikan',
    'nama'      : 'Hans',
    'telephone' : '085683922512',
    'alamat'    : 'Jalan mayjen sungkono 58',
    'pekerjaan' : 'Dosen'
},
{
    'kodeindex' : '07',
    'bidang'    : 'Konstruksi',
    'nama'      : 'Allan',
    'telephone' : '089876309223',
    'alamat'    : 'Jlan dupak megah jaya 38',
    'pekerjaan' : 'Arsitek'
},
{
    'kodeindex' : '08',
    'bidang'    : 'Konstruksi',
    'nama'      : 'Ruben',
    'telephone' : '085683922512',
    'alamat'    : 'Jalan ahmad yani v / 58',
    'pekerjaan' : 'Kontraktor'
},
{
    'kodeindex' : '09',
    'bidang'    : 'Perbankan',
    'nama'      : 'Steffi',
    'telephone' : '088676321529',
    'alamat'    : 'Jalan panjang jiwo 101',
    'pekerjaan' : 'Customer service'
},
{
    'kodeindex' : '10',
    'bidang'    : 'Perbankan',
    'nama'      : 'Citra',
    'telephone' : '085236894760',
    'alamat'    : 'Jalan embong malang 22',
    'pekerjaan' : 'Marketing kredit'
}
]

def lihatdaftar():
    print('Daftar Semua Data Pada Yellow Page :\n')
    print('Kode index\t| Bidang \t| Nama  \t| Telephone \t| Alamat                    \t| Pekerjaan')
    for i in range(len(data)):
        print(f'{data[i]["kodeindex"]}       \t| {data[i]["bidang"]} \t| {data[i]["nama"]}   \t| {data[i]["telephone"]} \t| {data[i]["alamat"]} \t| {data[i]["pekerjaan"]}')

def lihatdaftar_filter():
    while True:
        print('Pilih filter untuk menampilkan data:')
        print('1. Berdasarkan Kode Index')
        print('2. Berdasarkan Nama')
        print('3. Berdasarkan Bidang')
        print('4. Berdasarkan Pekerjaan')
        print('5. Kembali ke Menu sebelumnya')

        pilihan = input('Masukkan angka pilihan: ')

        if pilihan == '1':
            kodeindex = input('Masukkan kode index yang dicari: ')
            filtered_data = [d for d in data if d["kodeindex"] == kodeindex]
        elif pilihan == '2':
            nama = input('Masukkan nama yang dicari: ')
            filtered_data = [d for d in data if d["nama"].lower() == nama.lower()]
        elif pilihan == '3':
            bidang = input('Masukkan bidang yang dicari: ')
            filtered_data = [d for d in data if d["bidang"].lower() == bidang.lower()]
        elif pilihan == '4':
            pekerjaan = input('Masukkan pekerjaan yang dicari: ')
            filtered_data = [d for d in data if d["pekerjaan"].lower() == pekerjaan.lower()]
        elif pilihan == '5':
            break
        else:
            print("Pilihan tidak valid. Silakan pilih angka dari 1 hingga 5.")
            continue

        if filtered_data:
            print('Hasil Pencarian:\n')
            print('Kode index\t| Bidang \t| Nama  \t| Telephone \t| Alamat                    \t| Pekerjaan')
            for item in filtered_data:
                print(f'{item["kodeindex"]}       \t| {item["bidang"]} \t| {item["nama"]}   \t| {item["telephone"]} \t| {item["alamat"]} \t| {item["pekerjaan"]}')
        else:
            print("Data tidak ditemukan.")

def cekkodeindex(kodeindex):
    return any(d["kodeindex"] == kodeindex for d in data)

def cektelephone(telephone):
    return any(d["telephone"] == telephone for d in data)

def tambahdata():
    while True:
        print('Menu Tambah Data:')
        print('1. Cek Kode Index')
        print('2. Tambah Data Baru')
        print('3. Kembali ke Menu Utama')

        pilihan = input('Masukkan angka pilihan: ')

        if pilihan == '1':
            kodeindex = input('Masukkan kode index yang ingin dicek: ')
            if cekkodeindex(kodeindex):
                print(f"Kode index {kodeindex} sudah ada.")
            else:
                print(f"Kode index {kodeindex} tersedia.")
        elif pilihan == '2':
            while True:
                kodeindextambah = input('Masukkan Kodeindex tambahan : ')
                if cekkodeindex(kodeindextambah):
                    print("Kode index sudah ada. Tidak dapat menambahkan data.")
                else:
                    bidangtambah = input('Masukkan Bidang tambahan : ')
                    namatambah = input('Masukkan Nama tambahan : ')
                    
                    while True:
                        telephonetambah = input('Masukkan Telephone tambahan : ')
                        if cektelephone(telephonetambah):
                            print("Nomor telephone sudah ada dalam data. Silakan masukkan nomor telephone yang berbeda.")
                        else:
                            break
                    
                    alamattambah = input('Masukkan Alamat tambahan : ')
                    pekerjaantambah = input('Masukkan Pekerjaan tambahan : ')
                    data.append({
                        'kodeindex': kodeindextambah,
                        'bidang': bidangtambah,
                        'nama': namatambah,
                        'telephone': telephonetambah,
                        'alamat': alamattambah,
                        'pekerjaan': pekerjaantambah
                    })
                    print("Data berhasil ditambahkan")
                    lihatdaftar()
                    break
        elif pilihan == '3':
            break
        else:
            print("Pilihan tidak valid. Silakan pilih angka dari 1 hingga 3.")

def hapusdata():
    while True:
        lihatdaftar()
        print('Menu Hapus Data:')
        print('1. Hapus Data')
        print('2. Kembali ke Menu Utama')

        pilihan = input('Masukkan angka pilihan: ')

        if pilihan == '1':
            kodeindex = input('Masukkan kode index yang ingin dihapus : ')
            for i in range(len(data)):
                if data[i]["kodeindex"] == kodeindex:
                    del data[i]
                    print(f"Data dengan kode index {kodeindex} berhasil dihapus.")
                    break
            else:
                print(f"Kode index {kodeindex} tidak ditemukan.")
        elif pilihan == '2':
            break
        else:
            print("Pilihan tidak valid. Silakan pilih angka 1 atau 2.")

import copy

def ubahdata():
    while True:
        lihatdaftar()
        print('Menu Ubah Data:')
        print('1. Ubah Data Berdasarkan Kode Index')
        print('2. Kembali ke Menu Utama')

        pilihan = input('Masukkan angka pilihan: ')

        if pilihan == '1':
            kodeindex = input('Masukkan kode index yang ingin diubah: ')
            for item in data:
                if item['kodeindex'] == kodeindex:
                    data_asli = copy.deepcopy(item)

                    print('Data yang ada:')
                    print(f'Bidang: {item["bidang"]}')
                    print(f'Nama: {item["nama"]}')
                    print(f'Telephone: {item["telephone"]}')
                    print(f'Alamat: {item["alamat"]}')
                    print(f'Pekerjaan: {item["pekerjaan"]}')

                    while True:
                        print('\nPilihan:')
                        print('1. Ubah Bidang')
                        print('2. Ubah Nama')
                        print('3. Ubah Telephone')
                        print('4. Ubah Alamat')
                        print('5. Ubah Pekerjaan')
                        print('6. Selesai Mengubah')
                        print('7. Batalkan Pengubahan')
                        
                        subpilihan = input('Masukkan angka pilihan: ')
                        
                        if subpilihan == '1':
                            item['bidang'] = input('Masukkan bidang baru: ')
                        elif subpilihan == '2':
                            item['nama'] = input('Masukkan nama baru: ')
                        elif subpilihan == '3':
                            while True:
                                telephonetambah = input('Masukkan nomor telephone baru: ')
                                if telephonetambah == item['telephone']:
                                    print("Nomor telephone tidak berubah.")
                                    break
                                elif cektelephone(telephonetambah):
                                    print("Nomor telephone sudah ada dalam data. Silakan masukkan nomor telephone yang berbeda.")
                                else:
                                    item['telephone'] = telephonetambah
                                    print("Nomor telephone berhasil diubah.")
                                    break
                        elif subpilihan == '4':
                            item['alamat'] = input('Masukkan alamat baru: ')
                        elif subpilihan == '5':
                            item['pekerjaan'] = input('Masukkan pekerjaan baru: ')
                        elif subpilihan == '6':
                            print("\nData setelah diubah:")
                            lihatdaftar()
                            input("\nTekan Enter untuk kembali ke menu utama...")
                            break
                        elif subpilihan == '7':
                            item.clear()
                            item.update(data_asli)
                            print("Pengubahan data dibatalkan.")
                            break
                        else:
                            print("Pilihan tidak valid. Silakan pilih angka dari 1 hingga 7.")
                        
                        if subpilihan == '7':
                            break
                    break
            else:
                print(f"Kode index {kodeindex} tidak ditemukan.")
        elif pilihan == '2':
            break
        else:
            print("Pilihan tidak valid. Silakan pilih angka 1 atau 2.")

def main():
    while True:
        print('''
Selamat Datang di Yellow Page 'Komunitas Sehat Bersama'

Berikut Merupakan Daftar Informasi Anggota :
1. Menampilkan Daftar Data
2. Menambah Daftar
3. Menghapus Daftar
4. Mengubah Daftar
5. Exit Program
        ''')

        pilihanMenu = input('Masukkan angka Menu yang ingin dijalankan : ')

        if pilihanMenu == '1':
            while True:
                print('Menu Lihat Daftar:')
                print('1. Lihat Semua Data')
                print('2. Lihat Data Berdasarkan Kriteria')
                print('3. Kembali ke Menu Utama')

                subpilihan = input('Masukkan angka pilihan: ')

                if subpilihan == '1':
                    lihatdaftar()
                elif subpilihan == '2':
                    lihatdaftar_filter()
                elif subpilihan == '3':
                    break
                else:
                    print("Pilihan tidak valid. Silakan pilih angka dari 1 hingga 3.")
        elif pilihanMenu == '2':
            tambahdata()
        elif pilihanMenu == '3':
            hapusdata()
        elif pilihanMenu == '4':
            ubahdata()
        elif pilihanMenu == '5':
            print("Terima kasih telah menggunakan program Yellow Page. Selamat tinggal!")
            break
        else:
            print("Pilihan tidak valid, silakan pilih angka dari 1 hingga 5.")

main()