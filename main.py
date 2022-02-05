from datavaksin import* 

def main () :
    jumlah_data = int (input ("Jumlah Data : "))
    daftar = [] 
    nomor = 1
    for x in range (jumlah_data) :
        print ("Data Mahasiswa ke-", nomor)
        nomor += 1
        
        nama = input ("Nama  : ")
        npm = input ("Npm  : ")
        telepon = input("Telepon : ")
        nik = input ("Nik  : ")
        vaksin = input ("Vaksin ke  : ")

        mahasiswa = datavaksin (nama,npm,telepon,nik,vaksin)

        daftar.append (mahasiswa)
        print("")


    
    #menampilakn data
    i = 1
    display = input ("Apakah Anda Ingin Menampilkan Data ? (y/n)")
    if display == "y" :   
        print ("|No\t |Nama\t| Npm\t| Telepon\t| NIK\t| Vaksin\t|")
        print ("-------------------------------------------")
        for x in daftar :
            print ("| {}\t |{}\t |{}\t |{}\t |{}\t |{}\t".format(i,nama,npm,telepon,nik,vaksin))
            i += 1


    #hapus
    delete = input ("apakah anda ingin menghapus data (y/n)?")
    if delete == "y" :
        pilih = int(input("Data Nomor ?"))
        del daftar[pilih-1]
    else :
        print ("Data tidak di hapus")

    i = 1
    print ("|Nama\t| Npm\t| Telepon\t| NIK\t| Vaksin\t|")
    print ("-------------------------------------------")

    for x in daftar :
        print ("| {}\t |{}\t |{}\t |{}\t |{}\t |{}\t".format(i,nama,npm,telepon,nik,vaksin))
        i += 1
        
if __name__ == "__main__" :
    main()