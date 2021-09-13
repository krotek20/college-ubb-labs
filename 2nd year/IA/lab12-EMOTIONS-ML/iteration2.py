import cv2
import numpy as np
import bleedfacedetector as fd


def emotion(image):
    img_copy = image.copy()
    faces = fd.ssd_detect(img_copy, conf=0.2)
    padding = 3
    for x, y, w, h in faces:
        face = img_copy[y - padding:y + h + padding, x - padding:x + w + padding]
        gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        resized_face = cv2.resize(gray, (64, 64))
        processed_face = resized_face.reshape(1, 1, 64, 64)

        net.setInput(processed_face)
        output = net.forward()

        expanded = np.exp(output - np.max(output))
        probablities = expanded / expanded.sum()
        prob = np.squeeze(probablities)
        predicted_emotion = emotions[prob.argmax()]
        print('Predicted Emotion is: {}'.format(predicted_emotion))
        break


emotions = ['Neutral', 'Happy', 'Surprise', 'Sad', 'Anger', 'Disgust', 'Fear', 'Contempt']
net = cv2.dnn.readNetFromONNX("Model/emotion-ferplus-8.onnx")

for i in range(1, 9):
    print(f"Image{i}:")
    image = cv2.imread(f"emotion_pretrained_images/emotion{i}.jpg")
    emotion(image)
