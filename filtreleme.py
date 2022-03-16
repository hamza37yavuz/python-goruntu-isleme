import cv2 as cv
import numpy as np
"""
Burada verilen filtrelerle ilgili filtrelerin nasil kullanildigi ve temel ozellikleri hakkında bilgi verilmistir.
Kullandiginiz ide'de filtreleme fonksiyonlarinin hangi parametreleri aldigi yazmaktadir.
Daha ayrinti bilgi icin orada yazan parametreleri arastirmalisiniz.
"""
a = cv.imread("pyt1.jpg")
b = cv.imread("pyt2.jpg")

meanFilter1 = cv.blur(a,(3,3))#3x3 luk bir alanda renk degerlerinin ortalamasi alinir ve ortadaki piksele yazilir
meanFilter2 = cv.blur(a,(6,6))#Bu piksel bolgelerinde yumusatma ve renk gecislerini yayar
meanFilter3 = cv.blur(a,(9,9))#Piksel bolgelerindeki alan artirilirsa bulaniklik artar (dogrusal bir filtrelemedir)

medianFilter1 = cv.medianBlur(a,1)#Bu filtreleme pikselleri sizin verdiginiz degerde kareler olusturur
medianFilter2 = cv.medianBlur(a,3)#Olusturdugu karenin icinde bulunan pikselleri buyukten kucuğe sıralar ortadaki degeri (mediani) karenin ortasındaki deger yerine verir 
medianFilter3 = cv.medianBlur(a,5)#Bu filtreleme yontemi dogrusal degildir.

gaussFilter1 = cv.GaussianBlur(b,(3,3),0)#Gauss yumuşatma operatörü, görüntüleri 'bulanıklaştırmak', ayrıntı ve gürültüyü ortadan kaldırmak için
gaussFilter2 = cv.GaussianBlur(b,(5,5),0)#kullanılan 2 boyutlu konvolüsyon (çekirdek matris ile resim üzerindeki piksellerin çarpımı işlemi) operatörüdür. 
gaussFilter3 = cv.GaussianBlur(b,(7,7),0)#gaussfilter resmin piksellerini çan şeklindeki grafikle temsil edecek farkli bir sablon kullanir.

cv.imshow("orijinal1",a)
cv.imshow("orijinal2",b)

cv.imshow("meanfilter1",meanFilter1) #filtrelemedeki ortalama alinacak alan ne kadar artarsa resim o kadar bulaniklasir
cv.imshow("meanfilter2",meanFilter2) #meanFilter1 meanFilter2 den daha az bulaniktir
cv.imshow("meanfilter3",meanFilter3) #bunun sebebi yukarida yazilmişti

cv.imshow("medianfilter1",medianFilter1)#Ayrica bu yontemde 5 ten buyuk degerleri giremezsiniz. burasi arastirilacak
cv.imshow("medianfilter2",medianFilter2)#readme dosyasina yazdigim linke bakarak bu soruya cevap bulabilirsiniz
cv.imshow("medianfilter3",medianFilter3)

cv.imshow("gaussfilter1",gaussFilter1)#gauss sablonunda sigmax ve sigmay degerleriyle ilgili merakinizi gidermek icin-
cv.imshow("gaussfilter2",gaussFilter2)#kendiniz arastirma yapmalisiniz
cv.imshow("gaussfilter3",gaussFilter3)

cv.waitKey(0)
cv.destroyAllWindows()
