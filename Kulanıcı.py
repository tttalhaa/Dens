import cv2
import numpy as np
import requests

def capture_image():
    cap = cv2.VideoCapture(0)
    while(True):
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    return frame

def send_image_to_telegram(image):
    url = 'https://api.telegram.org/bot<TELEGRAM_BOT_TOKEN>/sendPhoto'
    files = {'photo': open('image.jpg', 'rb')}
    params = {'chat_id': '<TELEGRAM_CHAT_ID>'}
    response = requests.post(url, files=files, params=params)
    print(response.json())

def main():
    image = capture_image()
    cv2.imwrite('image.jpg', image)
    send_image_to_telegram(image)

if __name__ == "__main__":
    main()
