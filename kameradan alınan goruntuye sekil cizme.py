import cv2 as cv
kamera = cv.VideoCapture(0)
while True:
    ret,canli = kamera.read()
    cv.rectangle(canli,(100,100),(200,200),(0,0,255),2) #dikdörtgen için rectangle(değişken ismi,solüst köşe,sağ alt köşe,BGR,kalınlığı)
   
    cv.line(canli,(100,100),(200,200),(0,255,0),2) #çizgi için rectangle(değişken ismi,başlangıç yeri,bitiş yeri,BGR,kalınlığı)
   
    cv.circle(canli,(150,150),50,(255,0,0),2) #daire için circle(değişken ismi,merkez konumu,yarıçap,BGR,kalınlığı)
    
    cv.putText(canli,"TEXT",(300,300),cv.FONT_HERSHEY_DUPLEX,2,(255,255,255),2) #yazı için line(değişken ismi,yazının başlangıç konumu,yazı fontu,yazı büyüklüğü,rengi,kalınlığı)
    
    cv.imshow("action",canli)
    
    if cv.waitKey(30) & 0xFF == ord("q"):
        break
kamera.relase()#kamerayı kapatır
cv.destroyAllWindows()#tüm pencereleri kapatır