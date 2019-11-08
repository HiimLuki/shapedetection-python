import cv2
import numpy as np

cap = cv2.VideoCapture(0)

##bsp aus der open CV dokumentation
#img = cv2.imread("shapes.jpg", cv2.IMREAD_GRAYSCALE)
#imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
#ret, thresh = cv.threshold(imgray, 127, 255, 0)
#contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

def nothing(x):
    # any operation
    pass

frameCount = 0

#zum ausrpobieren von werten nur thresh wird genutzt
cv2.namedWindow("Trackbars")
cv2.createTrackbar("thresh", "Trackbars", 211, 255, nothing)
cv2.createTrackbar("maxval", "Trackbars", 200, 255, nothing)

while True:
    thresh = cv2.getTrackbarPos("thresh", "Trackbars")
    maxval = cv2.getTrackbarPos("maxval", "Trackbars")

    _, frame = cap.read()
    imgray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #1.frame merken
  # if frameCount == 0:
    #     firstFrame = imgray
    # frameCount += 1
    
    #Betrag der Differenz berechnen:absDiff()
    #absDiff= cv2.absdiff(imgray, firstFrame)

    #irgendso ein filter geht auch ohne aber hatte das gefühl so ist besser
    gray = cv2.bilateralFilter(imgray, 11, 17, 17)
    
    #thresh bestimmt wie viel erkannt wird --> je keiner desto mehr wird erkannt, Wert der am besten funktioniert bei mir: 219(tageslicht)
    #wenn etwas dunkler geht 211 ganz gut
    #maxval (da wo 255 steht) gibt den kontrast vom neuen bild an --> 255 heißt alles komplett schwarz und weiß
    #egal ob THRESH_BINARY_INV  oder nur THRESH_BINARY --> dann sit nur schwarz und weiß vertauscht
    #_, threshold = cv2.threshold(gray, thresh, 255, cv2.THRESH_BINARY_INV)
    _, threshold = cv2.threshold(absDiff, thresh, 255, cv2.THRESH_BINARY_INV)

    #original werte aus dem video
    #_, threshold = cv2.threshold(imgray, 240, 255, cv2.THRESH_BINARY)

 
    #threshold = cv2.Canny(gray, 30, 200)

    contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    font = cv2.FONT_HERSHEY_COMPLEX

    for cnt in contours:
        area = cv2.contourArea(cnt)

        #if bedingung sorgt dafür das nur große sachen erkannt werden (aus realtime_shape_detection geklaut)
        if area > 3000:
            approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
            cv2.drawContours(frame, [approx], 0, (0), 5)
            x = approx.ravel()[0]
            y = approx.ravel()[1]

            if len(approx) == 3:
                cv2.putText(frame, "Dreiech", (x, y), font, 1, (0))
            elif len(approx) == 4:
                cv2.putText(frame, "Rechteck", (x, y), font, 1, (0))
            elif len(approx) == 5:
                cv2.putText(frame, "Pentagon", (x, y), font, 1, (0))
            #elif 6 < len(approx) < 15:
             #   cv2.putText(frame, "Ellipse", (x, y), font, 1, (0))
            else:
                cv2.putText(frame, "Kreis", (x, y), font, 1, (0))

            cv2.imshow("shapes", frame)
            cv2.imshow("Threshold", threshold)
    key = cv2.waitKey(1)
    #esc zum beenden drücken
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()