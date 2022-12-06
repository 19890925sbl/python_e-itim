"""
müşteri adı
müşteri soyadı
müşteri adı+soyadı
müşteri cinsiyet
müşteri tc kimlik
müşteri doğum yılı
müşteri adres bilgisi
müşteri yaşı
"""
müşteriAdı='Sibel'
müşteriSoyadı='Mercan'
müşteriAdSoyad=müşteriAdı+' '+müşteriSoyadı
müşteriCinsiyet='Kadın'
müşteriTc='12345678911'
müşteriDoğumYılı='1989'
müşteriAdresi='İstanbulEsenyurt'
müşteriYaşı=2022-(müşteriDoğumYılı)

"""
AŞAĞIDAKİ SİPARİŞLERİN TOPLAM BİLGİSİNİ HESAPLAYINIZ
sipariş1=>110TL
sipariş2=>1100.5TL
sipariş3=>356.95TL


"""
order1=110
order2=1100.5
order3=356.95
total=order1+order2+order3
print("Total:",total)
