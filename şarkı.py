import sqlite3
import time
class Şarkı():
    def __init__(self,isim,sanatçı,albüm,şirket,süre,puan):
         self.isim=isim
         self.sanatçı=sanatçı
         self.albüm=albüm
         self.şirket=şirket
         self.süre=süre
         self.puan=puan
    def __str__(self):
        return"şarkı_ismi= {} \nsanatçı={} \nalbüm= {} \nşirket={} \nsüre={} \npuan{} \n".format(self.isim,self.sanatçı,self.albüm,self.şirket,self.süre,self.puan)

class Playlist():
    def __init__(self):
        self.baglantı_olustur()
    def baglantı_olustur(self):
        self.baglantı=sqlite3.connect("müzikal.db")
        self.cursor=self.baglantı.cursor()
        sorgu="Create Table If not exists şarkılar (isim TEXT,sanatçı TEXT,albüm TEXT,şirket TEXT, süre INT,puan INT)"
        self.cursor.execute(sorgu)
        self.baglantı.commit()
    def baglantı_kapa(self):
        self.baglantı.close()
    def şarkıları_göster(self):
        sorgu="Select * From şarkılar"
        self.cursor.execute(sorgu)
        şarkılar=self.cursor.fetchall()
        if(len(şarkılar)==0):
            print("henüz bir şarkı eklenmedi")
        else:
            for i in şarkılar:
                şarkı=Şarkı(i[0],i[1],i[2],i[3],i[4],i[5])
                print(şarkı)

    def şarkı_sorgula(self,isim):
        sorgu="Select * From şarkılar where isim= ?"
        self.cursor.execute(sorgu,(isim,))
        şarkılar=self.cursor.fetchall()
        if(len(şarkılar)==0):
            print("şuan hiç şarkı bulunmamaktadır")
        else:
            şarkı=Şarkı(şarkılar[0][0],şarkılar[0][1],şarkılar[0][2],şarkılar[0][3],şarkılar[0][4],şarkılar[0][5])
            print(şarkı)
    def şarkı_ekle(self,şarkı):
       sorgu="Insert into şarkılar Values (?,?,?,?,?,?)"
       self.cursor.execute(sorgu,(şarkı.isim,şarkı.sanatçı,şarkı.albüm,şarkı.şirket,şarkı.süre,şarkı.puan))
       self.baglantı.commit()
    def şarkı_sil(self,isim):
        sorgu="Delete From şarkılar where isim=?"
        self.cursor.execute(sorgu,(isim,))
        self.baglantı.commit()
    def toplam_süre(self):
        sorgu="Select * From şarkılar"
        self.cursor.execute(sorgu)
        şarkılar=self.cursor.fetchall()
        toplam=0
        for i in şarkılar:
            şarkı = Şarkı(i[0], i[1], i[2], i[3], i[4], i[5])
            toplam+= int(şarkı.süre)
        print("playlist toplam şarkı süresi==",toplam)
