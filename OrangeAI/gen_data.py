from PIL import Image
import os, glob
import numpy as np
from sklearn import model_selection

classes = ["Orange", "OrangeTree", "NoOrange"]
num_classes = len(classes)
image_size = 50

#画像の読み込み
X = []
Y = []
for index, classlabel in enumerate(classes):
    photos_dir = "./Image/" + classlabel
    files = glob.glob(photos_dir + "/*.jpg")
    
    for i, file in enumerate(files):
        if i >= 200: break
        image = Image.open(file)
        image = image.convert("RGB")
        image = image.resize((image_size, image_size))
        data = np.asarray(image)
        X.append(data)
        Y.append(index)

X = np.array(X)
Y = np.array(Y)


X_train, X_test, y_train, y_test = model_selection.train_test_split(X, Y, test_size=0.20)
xy = (X_train, X_test, y_train, y_test)
np.save('./orangeai.npy', xy)

