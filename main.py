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

"""Verilen kod zaten temel bir müzikal playlist uygulaması için gerekli işlevselliği içeriyor. Ancak, kodu daha da geliştirmek ve yeni özellikler eklemek isterseniz aşağıdaki bazı önerileri değerlendirebilirsiniz:

Arama fonksiyonları: Şu anda sadece şarkı adına göre sorgulama yapabilen bir fonksiyon mevcut. Bunun yanı sıra, sanatçıya, albüme veya şirkete göre şarkı sorgulama yapabilen fonksiyonlar ekleyebilirsiniz.

Şarkı güncelleme: Mevcut şarkı bilgilerini güncellemek için bir fonksiyon ekleyebilirsiniz. Kullanıcıya şarkı adını sormak ve yeni bilgileri girmesini istemek gibi bir yöntem kullanabilirsiniz.

Puana göre sıralama: Şarkıları puanlarına göre sıralayabilen bir fonksiyon ekleyebilirsiniz. Böylece kullanıcılar en yüksek puanlı şarkıları görüntüleyebilirler.

Favori şarkılar: Kullanıcılara favori şarkılarını işaretleyebilecekleri bir seçenek ekleyebilirsiniz. Böylece favori şarkıları daha kolay bulabilirler.

Şarkı istatistikleri: Toplam şarkı süresi dışında, örneğin albüm bazında şarkı sayısı veya sanatçı bazında ortalama şarkı süresi gibi istatistikler sağlayan fonksiyonlar ekleyebilirsiniz.

GUI (Grafiksel Kullanıcı Arayüzü): Mevcut konsol tabanlı arayüzü daha kullanıcı dostu bir grafiksel arayüz ile değiştirebilirsiniz. Bu, kullanıcıların şarkıları daha kolay yönetmelerini sağlayacaktır.

Bu öneriler, kodunuzu daha işlevsel ve kullanıcı dostu hale getirmeniz için başlangıç noktası olabilir. İhtiyaçlarınıza ve tercihlerinize göre, daha fazla özellik ve geliştirmeler ekleyebilirsiniz.
"""