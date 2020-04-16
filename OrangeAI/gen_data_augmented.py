from PIL import Image
import os, glob
import numpy as np
from sklearn import model_selection

classes = ["Orange", "OrangeTree"]
num_classes = len(classes)
image_size = 50
num_testdata = 100

# 画像の読み込み
X_train = []
X_test =[]
Y_train = []
Y_test = []

for index, classlabel in enumerate(classes):
    photos_dir = "./Image/" + classlabel
    files = glob.glob(photos_dir + "/*.jpg")

    for i, file in enumerate(files):
        if i >= 200: break
        image = Image.open(file)
        image = image.convert("RGB")
        image = image.resize((image_size, image_size))
        data = np.asarray(image)

        if i < num_testdata:
            X_test.append(data)
            Y_test.append(index)
        else:
            X_train.append(data)
            Y_train.append(index)

            for angle in range(-20, 20, 5):
                #kaiten
                img_r = image.rotate(angle)
                data =  np.asarray(img_r)
                X_train.append(data)
                Y_train.append(index)

                #hanten
                img_trans = image.transpose(Image.FLIP_LEFT_RIGHT)
                data = np.asarray(img_trans)
                X_train.append(data)
                Y_train.append(index)

#X = np.array(X)
#Y = np.array(Y)

X_train = np.asarray(X_train)
X_test = np.asarray(X_test)
y_train = np.asarray(Y_train)
y_test = np.asarray(Y_test)


#X_train, X_test, y_train, y_test = model_selection.train_test_split(X, Y, test_size=0.20)
xy = (X_train, X_test, y_train, y_test)
np.save('./orangeai_aug.npy', xy)