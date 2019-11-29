
import cv2
import numpy as np

import server
server.start()

cap = cv2.VideoCapture(0)

while True:

    _, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
   
    #Blauer Wertebereich
    lower_blue = np.array([94, 80, 2])
    upper_blue = np.array([126, 255, 255])

    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
    kernel = np.ones((5, 5), np.uint8)
    mask_blue = cv2.erode(mask_blue, kernel)

    #Roter Wertebereich
    lower_red = np.array([1,120,70])
    upper_red = np.array([7,255,255])

    mask_red = cv2.inRange(hsv, lower_red, upper_red)
    mask_red = cv2.erode(mask_red, kernel)

    #Grüner Wertebereich
    lower_green = np.array([25, 52, 72])
    upper_green = np.array([80, 255, 255])

    mask_green = cv2.inRange(hsv, lower_green, upper_green)
    mask_green = cv2.erode(mask_green, kernel)

    contours_green, _ = cv2.findContours(mask_green, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours_red, _ = cv2.findContours(mask_red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours_blue, _ = cv2.findContours(mask_blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    font = cv2.FONT_HERSHEY_COMPLEX

    #Blaue Formen erkennen
    for cnt in contours_blue:
        area = cv2.contourArea(cnt)

        #if bedingung sorgt dafür das nur große sachen erkannt werden
        if area > 3000:

            #je kleiner die 0.01 desto genauer der rand
            approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
            cv2.drawContours(frame, [approx], 0, (0), 5)
            x = approx.ravel()[0]
            y = approx.ravel()[1]

            form = "Keine Form"

            if 20 < len(approx) < 24:
                cv2.putText(frame, "Elefant", (x, y), font, 1, (0))
                form = "Elefant"
          

            server.send(message='position', data={'x': form, 'y': form})

    #Rote Formen erkennen  
    for cnt in contours_red:
        area = cv2.contourArea(cnt)

        #if bedingung sorgt dafür das nur große sachen erkannt werden (aus realtime_shape_detection geklaut)
        if area > 3000:

            #je kleiner die 0.01 desto genauer der rand
            approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
            cv2.drawContours(frame, [approx], 0, (0), 5)
            x = approx.ravel()[0]
            y = approx.ravel()[1]

            form = "Keine Form"

            # if len(approx) == 4:
            #     cv2.putText(frame, "Rechteck", (x, y), font, 1, (0))
            #     form = "Rechteck"
            if 15 < len(approx) < 22:
                cv2.putText(frame, "Ente", (x, y), font, 1, (0))
                form = "Ente"
           
            
            server.send(message='position', data={'x': form, 'y': form})

    #Grüne Formen erkennen 
    for cnt in contours_green:
        area = cv2.contourArea(cnt)

        #if bedingung sorgt dafür das nur große sachen erkannt werden (aus realtime_shape_detection geklaut)
        if area > 3000:

            #je kleiner die 0.01 desto genauer der rand
            approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
            cv2.drawContours(frame, [approx], 0, (0), 5)
            x = approx.ravel()[0]
            y = approx.ravel()[1]

            form = "Keine Form"

            
            if 10 < len(approx) < 19:
                cv2.putText(frame, "Katze", (x, y), font, 1, (0))
                form = "Katze"
            # elif len(approx) == 5:
            #     cv2.putText(frame, "Pentagon", (x, y), font, 1, (0))
            

            server.send(message='position', data={'x': form, 'y': form})

    cv2.imshow("shapes", frame)
    #mask_red, mask_green oder mask_blue nehmen
    cv2.imshow("Mask", mask_red)

    key = cv2.waitKey(1)
    #esc zum beenden drücken
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
