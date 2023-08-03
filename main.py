from şarkı import *
print("""
****************************************
1-Playlist göster
2-Playlist şarkı sorgulama
3-şarkı ekleme
4-Şarkı silme
5-Playlist şarkı süresi hesaplama
q-çıkış

****************************************
""")
şarkı=Playlist()
while True:
    işlem=input("yapacağınız işlemi giriniz")

    if(işlem=="q"):
        print("programdan çıkılıyor")
        break
    elif(işlem=="1"):
        şarkı.şarkıları_göster()


    elif(işlem=="2"):
        isim=input("sorgulamak istediğiniz şarkı ismi\t")
        şarkı.şarkı_sorgula(isim)

    elif(işlem=="3"):
        isim=input("şarkı ismi")
        sanatçı=input("sanatçı ismi")
        albüm=input("albüm ismi")
        şirket=input("şirket ismi")
        süre=int(input("şarkı süresi"))
        puan=int(input("şarkı kaç puan verirsiniz"))
        yeni_şarkı=Şarkı(isim,sanatçı,albüm,şirket,süre,puan)
        şarkı.şarkı_ekle(yeni_şarkı)

    elif (işlem == "4"):
        isim=input("silinecek şarkıın ismi")
        şarkı.şarkı_sil(isim)

    elif (işlem == "5"):
        şarkı.toplam_süre()

