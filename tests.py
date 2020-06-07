import tensorflow as tf
import time
import matplotlib.pyplot as plt
print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))
config = tf.ConfigProto()
config.gpu_options.allow_growth = True
session = tf.Session(config=config)
#sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))

from tensorflow.keras.datasets import cifar10
(X_train,y_train),(X_test,y_test) = cifar10.load_data()

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import *



model = Sequential()
model.add(Conv2D(32,kernel_size=(3,3),input_shape=(32,32,3)))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(128,activation="relu"))

model.add(Dense(1,activation="sigmoid"))

model.compile(optimizer="rmsprop",loss="binary_crossentropy",metrics=["accuracy"])

timeline = []

print(X_train.shape)
y_train_car = y_train == 1 
for i in range(5):
    tic = time.perf_counter()
    model.fit(X_train,y_train_car,batch_size=256,epochs=1,shuffle=True)
    toc = time.perf_counter()
    toc = float(toc - tic)
    timeline.append(toc)


bar_list1 = []
bar_list2 = []
progress = 0
for i in range(len(timeline)):
    timeline[i] = round(timeline[i],3)*1000
    if i%2 == 0:
        bar_list1.append((progress,timeline[i]))
    else:
        bar_list2.append((progress,timeline[i]))
    progress = progress + timeline[i]

print(bar_list1)



fig, gra = plt.subplots()

gra.set_ylim(0,40)
gra.set_xlim(0,10000)

gra.set_xlabel("seconds since start")
gra.set_ylabel("durchführung")

gra.set_yticks([15,30])
gra.set_yticklabels(["selfplay","netzwerktraining"])

gra.broken_barh(bar_list1,(15,9),facecolors='tab:blue')
gra.broken_barh(bar_list2,(30,9),facecolors='tab:red')
plt.show()


