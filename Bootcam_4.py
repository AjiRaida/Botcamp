class car:

    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
        self.pintu = "terbuka"
        self.mobil = "mati"
        
    def membuka_pintu(self):
        if  self.pintu == 'tertutup':
            print("pintu berehasil dibuka")
            self.pintu = 'terbuka'
        else:
            print("pintu terbuka")
            
    def menutup_pintu(self):
        if  self.pintu == 'terbuka':
            print("pintu berhasil di tutup")
            self.pintu = 'tertutup'
        else:
            print("pintu tertutup")
            
    def mobil_Dinyalakan(self):
        if  self.mobil == 'mematikan':
            print("mobil berehasil dihdupkan")
            self.mobil = 'dihidupkan'
        else:
            print("mobil dihidupkan")   
       
    def mobil_Dimatikan(self):
        if  self.mobil == 'dihidupkan':
            print("mobil berehasil diamtikan")
            self.moobil = 'dimatikan'
        else:
            print("mobil dimatikan")


car_1 = car('toyota', 1998)


car_1.membuka_pintu()
car_1.menutup_pintu()
car_1.mobil_Dinyalakan()
car_1.mobil_Dimatikan()