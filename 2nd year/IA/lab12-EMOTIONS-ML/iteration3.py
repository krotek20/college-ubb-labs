import os
import numpy as np
import cv2
from keras.utils import np_utils
from sklearn.utils import shuffle
from keras.models import Sequential
from keras import layers
from sklearn.model_selection import KFold, train_test_split
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import ModelCheckpoint, EarlyStopping
import matplotlib.pyplot as plt

data_dir_list = os.listdir('emotion_images')
print(data_dir_list)

img_data_list = []
labels_lengths = []

for dataset in data_dir_list:
    img_list = os.listdir('emotion_images/' + dataset)
    labels_lengths.append(len(img_list))
    print('Loaded the images of dataset-' + '{}\n'.format(dataset))
    for img in img_list:
        input_img = cv2.imread('emotion_images/' + dataset + '/' + img)
        input_img_resize = cv2.resize(input_img, (48, 48))
        img_data_list.append(input_img_resize)

img_data = np.array(img_data_list)
img_data = img_data.astype('float32')
img_data /= 255
print(img_data.shape)

num_classes = 7
num_of_samples = img_data.shape[0]
labels = np.ones((num_of_samples,), dtype='int64')
# print(labels_lengths)

dp_labels_lengths = [labels_lengths[0]]
for length in labels_lengths[1:]:
    dp_labels_lengths.append(dp_labels_lengths[-1] + length)
# print(dp_labels_lengths)

for i in range(len(dp_labels_lengths)):
    labels[0 if i == 0 else dp_labels_lengths[i - 1]:dp_labels_lengths[i] - 1] = i

classes = ['anger', 'contempt', 'disgust', 'fear', 'happy', 'sadness', 'surprise']


def get_label(id):
    return ['anger', 'contempt', 'disgust', 'fear', 'happy', 'sadness', 'surprise'][id]


def create_model():
    input_shape = (48, 48, 3)

    model = Sequential([
        layers.Conv2D(6, (5, 5), input_shape=input_shape, padding='same', activation='relu'),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Conv2D(16, (5, 5), padding='same', activation='relu'),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D(pool_size=(2, 2)),

        layers.Flatten(),
        layers.Dense(128, activation='relu'),
        layers.Dropout(0.5),
        layers.Dense(num_classes, activation='softmax')
    ])

    model.compile(loss='categorical_crossentropy', metrics=['accuracy'], optimizer='RMSprop')
    return model


Y = np_utils.to_categorical(labels, num_classes)
x, y = shuffle(img_data, Y, random_state=2)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=2)

# cross-validation
kf = KFold(n_splits=5, shuffle=False)
aug = ImageDataGenerator(
    rotation_range=25, width_shift_range=0.1,
    height_shift_range=0.1, shear_range=0.2,
    zoom_range=0.2, horizontal_flip=True,
    fill_mode="nearest")

result = []
scores_loss = []
scores_acc = []
k_no = 0
models = []
histories = []
for train_index, test_index in kf.split(x):
    X_Train = x[train_index]
    Y_Train = y[train_index]
    X_Test = x[test_index]
    Y_Test = y[test_index]

    # file_path = "weights/weights" + str(k_no) + ".hdf5"
    # checkpoint = ModelCheckpoint(file_path, monitor='loss', verbose=0, save_best_only=True, mode='min')
    # early = EarlyStopping(monitor="loss", mode="min", patience=8)
    #
    # callbacks_list = [checkpoint, early]

    model = create_model()
    # history = model.fit_generator(aug.flow(X_Train, Y_Train), epochs=200, validation_data=(X_Test, Y_Test),
    #                               callbacks=callbacks_list, verbose=0)
    history = model.fit(X_Train, Y_Train, batch_size=20, epochs=150, verbose=1)

    print(f'Training for fold {k_no} ...')
    # model.load_weights(file_path)
    score = model.evaluate(X_Test, Y_Test, verbose=0)
    print(
        f'Score for fold {k_no}: {model.metrics_names[0]} of {score[0]}; {model.metrics_names[1]} of {score[1]}')
    scores_loss.append(score[0])
    scores_acc.append(score[1])

    histories.append(history)
    models.append(model)
    k_no += 1

print("Scores acc and scores loss:")
print(scores_acc, scores_loss)

# taking the best model
value_min = min(scores_loss)
value_index = scores_loss.index(value_min)
best_model = models[value_index]
best_history = histories[value_index]

score = best_model.evaluate(x_test, y_test, verbose=0)
print('Test Loss:', score[0])
print('Test accuracy:', score[1])

test_image = x_test[0:1]

print(best_model.predict(test_image))
print(best_model.predict_classes(test_image))
print(y_test[0:1])

# predict
y_pred = best_model.predict(x_test)

# diagrams
acc = best_history.history['accuracy']
val_acc = best_history.history['val_accuracy']
loss = best_history.history['loss']
val_loss = best_history.history['val_loss']

epochs_range = range(len(acc))

plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.plot(epochs_range, acc, label='Training Accuracy')
plt.plot(epochs_range, val_acc, label='Validation Accuracy')
plt.legend(loc='lower right')
plt.title('Training and Validation Accuracy')

plt.subplot(1, 2, 2)
plt.plot(epochs_range, loss, label='Training Loss')
plt.plot(epochs_range, val_loss, label='Validation Loss')
plt.legend(loc='upper right')
plt.title('Training and Validation Loss')
plt.show()
