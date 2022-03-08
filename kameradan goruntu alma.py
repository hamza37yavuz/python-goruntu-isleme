import cv2 as cv
kamera = cv.VideoCapture(0)#0 bilgisayarın kamerasıdır 1 usb ye bağlı kamera olabilir buraya video da tanımlanabilir
while True:
#ret değişkeni, kameranın çalışıp çalışmadığını kontrol etmek için tanımlanır
#goruntu döngü içerisinde kameradan çekilen fotografın atıldığı değişken
    ret,canli = kamera.read()
    cv.imshow("action",canli)#burada çekilen fotoğraf gosterilir
    #print(ret) #true değeri ile işlem devam eder
    if cv.waitKey(30) & 0xFF == ord("q"):#wiatkey(20) 20 milisaniyede bir bir foto çekiyor 0xFF burada çıkış anlamına gelir
        break
kamera.relase()#kamerayı kapatır
cv.destroyAllWindows()#tüm pencereleri kapatır