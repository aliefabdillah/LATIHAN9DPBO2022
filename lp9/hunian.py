class Hunian():
    def __init__(self, jenis, status, jml_penghuni = 1, jml_kamar = 1, luasBangunan=0, listrik=450):
        self.jenis = jenis
        self.jml_penghuni = jml_penghuni
        self.jml_kamar = jml_kamar
        self.luasBangunan = luasBangunan
        self.listrik = listrik
        self.status = status

    def get_jenis(self):
        return self.jenis

    def get_jml_penghuni(self):
        return self.jml_penghuni

    def get_jml_kamar(self):
        return self.jml_kamar

    def get_dokumen(self):
        pass

    def get_luasBangunan(self):
        return str(self.luasBangunan) + " Meter Persegi"

    def get_listrik(self):
        return str(self.listrik) + " VA"

    def get_status(self):
        if self.status != "Permanent":
            return "Mengontrak " + self.status
        else:
            return self.status
            

    def get_summary(self):
        return "Hunian "+ self.jenis +", ditempati oleh " + str(self.jml_penghuni) + " orang."