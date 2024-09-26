class Calisan:
    
    def __init__(self, ad, soyad, yas, pozisyon, maas):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        self.pozisyon = pozisyon
        self.maas = maas
        
    def bilgileri_goster(self):
        print(f"Ad: {self.ad}, Soyad: {self.soyad}, Yaş: {self.yas}, Pozisyon: {self.pozisyon}, Maaş: {self.maas}")


class Fabrika:
    
    def __init__(self):
        self.calisanlar = []
        
    def calisan_ekle(self, calisan):
        self.calisanlar.append(calisan)
        print(f"{calisan.ad} {calisan.soyad} fabrikaya eklendi...")
        
    def tum_calisanlari_goster(self):
        if not self.calisanlar:
            print("Henüz eklenmiş bir çalışan yok.")
        else:
            print("\nTüm Çalışanlar: ")
            for calisan in self.calisanlar:
                calisan.bilgileri_goster()



def calisan_bilgilerini_al_ve_ekle(fabrika):
    
    ad = input("Çalışanın adı: ")
    soyad = input("Çalışanın soyadı: ")
    yas = int(input("Çalışanın yaşı: "))
    pozisyon = input("Çalışanın pozisyonu: ")
    maas = float(input("Çalışanın maaşı: "))
    yeni_calisan = Calisan(ad, soyad, yas, pozisyon, maas)
    fabrika.calisan_ekle(yeni_calisan)



fabrika = Fabrika()


while True:
    
    cevap = input("Yeni bir çalışan eklemek ister misiniz? (E/H): ").lower()
    if cevap == 'e':
        calisan_bilgilerini_al_ve_ekle(fabrika)
    elif cevap == 'h':
        break
    else:
        print("Geçersiz giriş, lütfen 'E' ya da 'H' tuşlayın.")


fabrika.tum_calisanlari_goster()
