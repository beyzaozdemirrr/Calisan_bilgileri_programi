class Calisan:
    def __init__(self, ad ,soyad, yas, pozisyon, maas):
        self.ad= ad
        self.soyad=soyad
        self.yas=yas
        self.pozisyon=pozisyon
        self.maas=maas
        
    def bilgileri_goster(self):
        print(f"Ad: {self.ad}, Soyad: {self.soyad},Yaş: {self.yas},Pozisyon: {self.pozisyon},Maaş: {self.maas}")


class Fabrika:
    def __init__(self):
        self.calisanlar =[]
        
    def calisan_ekle(self,calisan) :
        self.calisanlar.append(calisan)
        print(f"{calisan.ad} {calisan.soyad} fabrikaya eklendi...")
        
    def tum_calisanlari_goster(self):
        print("\nTüm Çalışanlar: ")
        for calisan in self.calisanlar:
            calisan.bilgileri_goster()

fabrika=Fabrika()


calisan1 = Calisan("Ahmet", "Yılmaz", 30, "Mühendis", 5000)
calisan2 = Calisan("Ayşe", "Kaya", 25, "Teknisyen", 4000)

fabrika.calisan_ekle(calisan1)
fabrika.calisan_ekle(calisan2)

fabrika.tum_calisanlari_goster()      