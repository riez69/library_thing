import classProcces as mdl

modul = mdl.LibDataBase
def perintah(jalurfile):
    info_dict = {}
    command = ["buka file","cari judul", "cari kata", "jangka waktu", "list file"]
    info = ["membuka file \"harap masukkan format file\"","mencari file berdasarkan judul\"harap masukkan format file\"", "cari kata dari setiap file didalam folder", "cari file berdasarkan waktu pembuatan", "menampilkan semua file" ]
    for com, inf in zip(command, info):
        print("[{}] {}".format(command.index(com), com))
        info_dict[com] = inf

    print("ketik info untuk info command")
    comm = input("masukkan command>>> ")
    if comm =="info":
        inp = int(input("masukkan command? "))
        inp_inf = command[inp]
        print(info_dict[inp_inf])

    elif comm == "0":
        inp = input("masukkan nama file? ")
        if modul(jalurfile,0000,0,00,9999,9999,99,inp,"").isthere():
            file = modul(jalurfile,0000,0,00,9999,9999,99,inp,"").bukafile()
            for row in file:
                print(row)
        else:
            print("file tidak ditemukan")

    elif comm == "1":
        inp = input("masukkan judul file?  ")
        file = modul(jalurfile,0000,0,00,9999,9999,99,inp,"").isthere()
        if file:
            print("file {} ditemukan".format(inp))
        else:
            print("file tidak ditemukan")
    elif comm == "2":
        try:
            file = modul(jalurfile,0000,0,00,9999,9999,99,"",input("masukkan kata? ")).words()
            for i in file:
                print(i)
        except (TypeError):
            print("kata tidak ditemukan")

    elif comm == "3":
        file = modul(jalurfile,int(input("masukkan tahun awal ketik \"0\" untuk skip")),int(input("masukkan bulan awal ketik \"0\" untuk skip")),int(input("masukkan tanggal awal ketik \"0\" untuk skip")),int(input("masukkan tahun khir ketik \"9999\" untuk skip")),int(input("masukkan bulan akhir ketik \"9999\" untuk skip")),int(input("masukkan tanggal akhir ketik \"9999\" untuk skip")),"","").jangkawaktu()
        if len(file) > 0:
            for i in file:
                print(i)
        else:
            print("file tidak ditemukan")
    elif comm == "4":
        file = modul(jalurfile,0000,0000,0000,9999,9999,9999,"","").dict()
        max = 0
        for jalur in file.keys():
            if len(jalur) > max:
                max = len(jalur)
            else:
                pass
        for jalur, info in file.items():
            l = max-len(jalur)
            print(jalur," "*l, "= ", info)

    else:
        print("command salah")