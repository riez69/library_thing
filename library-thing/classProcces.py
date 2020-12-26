import os, time
from  datetime import datetime
from os import listdir
from typing import Iterator

class LibDataBase:
    def __init__ (self,file,  tahun_awal=0,bulan_awal=0,tanggal_awal=0, tahun_akhir=9999, bulan_akhir=9999, tanggal_akhir=9999, judul="", kata=""):
        self.file = file
        self.tahun_awal = tahun_awal
        self.bulan_awal = bulan_awal
        self.tanggal_awal = tanggal_awal
        self.tahun_akhir = tahun_akhir
        self.bulan_akhir = bulan_akhir
        self.tanggal_akhir = tanggal_akhir
        self.judul = judul
        self.kata = kata

    # membuat list jalur file [jalurfile]
    def jalurfile(self):
        listindir = []
        file = []
        link = listdir(self.file)
        for i in link:
            listindir.append(self.file+"\\"+i)

        for x in listindir:
            if os.path.isfile(x):
                file.append(x)
        return file

    def listfile(self):
        res = []
        for i in listdir(self.file):
            res.append(i)
        return res
    # membuat list yang berisi [list tahun pembuatan file], [list bulan], [list hari]
    def waktufile(self):
        year = []
        month = []
        day = []
        for i in self.jalurfile():
            humantime = os.stat(i).st_ctime
            tahun,bulan,hari,hour,minute,second=time.localtime(humantime)[:-3]
            year.append(tahun)
            month.append(bulan)
            day.append(hari)
        return year, month, day

    #membuat dictinary yang berisi value {jalurfile = [informasi waktu pembuatan file]}
    def dict(self):
        tahun = self.waktufile()[0]
        bulan = self.waktufile()[1]
        hari = self.waktufile()[2]
        res = {}
        for i in range(len(self.jalurfile())):
            res[self.jalurfile()[i]] = [tahun[i], bulan[i], hari[i]]
        return res

    # cek file berdasarkan jangka waktu 
    # return list dari jalurfile
    def jangkawaktu(self):
        tahunawal = self.tahun_awal
        tahunakhir = self.tahun_akhir
        bulanawal = self.bulan_awal
        bulanakhir = self.bulan_akhir
        tanggalawal = self.tanggal_awal
        tanggalakhir = self.tanggal_akhir
        revtahun = []
        for jalurfile, waktu in self.dict().items():
            tahun = waktu[0]
            bulan = waktu[1]
            tanggal = waktu[2]
            if tahun >= tahunawal and tahun <= tahunakhir and bulan >= bulanawal and bulan <= bulanakhir and tanggal >= tanggalawal and tanggal <= tanggalakhir:
                revtahun.append(jalurfile)

        return revtahun

    # cek jika ada file bernama self.judul
    def isthere(self):
        file = listdir(self.file)
        if self.judul in file:
            return True
        else:
            return False

    
    # mencari kata dari setiap file yang berada dalam jalur self.file
    # output [list]
    def words(self):
        result = []
        for file in listdir(self.file):
            try:
                with open(self.file+"\\"+file, "r") as f:
                    line = 1
                    for string in f:
                        if self.kata in string:
                            result.append("kata ditemukan di file {} baris ke {}".format(file, line))
                        else:
                            pass
                        line += 1
            except(PermissionError):
                pass
        if len(result) > 0:
            return result
        else:
            pass

    # membuka file dan return dalam bentuk list
    def bukafile(self):
        res = []
        with open(self.file+"\\"+self.judul, "r") as file:
            for line in file:
                res.append(line)
        return res
