from operator import ge
from hunian import Hunian

class Indekos(Hunian):

    def __init__(self, nama_pemilik, nama_penghuni, luasBangunan, listrik, status, noKtp, tglLahir, gender, pekerjaan):
        super().__init__("Indekos", status, 1, 1, luasBangunan, listrik)
        self.nama_pemilik = nama_pemilik
        self.nama_penghuni = nama_penghuni
        self.noKtp = noKtp
        self.tglLahir = tglLahir
        self.gender = gender
        self.pekerjaan = pekerjaan

    def get_dokumen(self):
        return "Bukti kontrak indekos oleh " + self.nama_penghuni + " dari " + self.nama_pemilik + "."

    def get_nama_pemilik(self):
        return self.nama_pemilik

    def get_nama_penghuni(self):
        return self.nama_penghuni

    def get_summary(self):
        return "Hunian Indekos."

    def getDataPenghuni(self):
        return "No KTP Penghuni: " + self.noKtp + "\n" + "Nama Penghuni: " + self.nama_penghuni + "\n" + "Tgl. Lahir Penghuni: " + self.tglLahir + "\n" + "Pekerjaan Penghuni: " + self.pekerjaan
