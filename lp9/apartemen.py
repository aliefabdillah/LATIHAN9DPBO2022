from hunian import Hunian

class Apartemen(Hunian):
    def __init__(self, nama_pemilik, jml_penghuni, jml_kamar, luasBangunan, listrik, status):
        super().__init__("Apartemen", status, jml_penghuni, jml_kamar, luasBangunan, listrik)
        self.nama_pemilik = nama_pemilik

    def get_dokumen(self):
        return "Sertifikat Hak Milik Atas Satuan Rumah Susun (SHMSRS) a/n " + self.nama_pemilik + "."

    def get_nama_pemilik(self):
        return self.nama_pemilik