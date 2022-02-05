class datavaksin (object) :
    def __init__(self ,nama ,npm ,nTelepon ,nNik, nVaksin ) :
        self.nama = nama
        self.npm = npm
        self.nTelepon = nTelepon
        self.nNik = nNik
        self.nVaksin = nVaksin

    def Telepon (self) :
        return self.nTelepon ()

    def Nik (self) :
        return self.nNik ()

    def Vaksin (self) :
        return self.nNik ()
        