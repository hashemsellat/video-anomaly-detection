import shelve

import keras
from keras.utils import plot_model
import numpy as np
from keras.layers import Conv2DTranspose, BatchNormalization
from keras.layers.convolutional import Conv2D, MaxPooling2D, UpSampling2D
from keras.models import Sequential
from lib import DataProvider
import Config as Config


# Encoder
def get_model(re=Config.RELOAD_MODEL):
    cache = shelve.open(Config.CACHE_PATH + "model")
    if not re:
        return cache["model"]
    images = DataProvider.get_dataset(Config.RELOAD_DATASET)
    #remove the below line in future executions
    images = np.array((images))
    print(images.shape)
    seq = Sequential()
    seq.add(Conv2D(512, (11, 11), strides=2, padding="same"))
    seq.add(BatchNormalization())
    seq.add(MaxPooling2D((2, 2), padding="same"))
    seq.add(BatchNormalization())
    seq.add(Conv2D(256, (5, 5), padding="same"))
    seq.add(BatchNormalization())
    seq.add(MaxPooling2D((2, 2), padding="same"))
    seq.add(BatchNormalization())
    seq.add(Conv2D(128, (3, 3), padding="same"))
    seq.add(BatchNormalization())
    # # # #
    seq.add(Conv2DTranspose(128, (3, 3), padding="same"))
    seq.add(BatchNormalization())
    seq.add(UpSampling2D((2, 2)))
    seq.add(BatchNormalization())
    seq.add(Conv2DTranspose(256, (5, 5), padding="same"))
    seq.add(BatchNormalization())
    seq.add(UpSampling2D((2, 2)))
    seq.add(BatchNormalization())
    seq.add(Conv2DTranspose(512, (11, 11),strides=2, padding="same"))
    seq.add(BatchNormalization())
    seq.add(Conv2D(10, (11, 11), activation="sigmoid", padding="same"))
    # seq.add(Dense(units=10,activation="sigmoid"))
    seq.compile(loss='mse', optimizer=keras.optimizers.Adam(lr=1e-4,decay=1e-5,epsilon=1e-6))

    # seq.compile(loss='binary_crossentropy', optimizer='adadelta')
    #    plot_model(seq, show_shapes=True, to_file='model.png')
    callback = keras.callbacks.ModelCheckpoint(Config.MODEL_PATH, monitor='val_loss', verbose=0, save_best_only=False,
                                               save_weights_only=False, mode='auto', period=5)
    seq.fit(images, images,
            batch_size=Config.BATCH_SIZE, epochs=Config.EPOCHS, shuffle=False, callbacks=[callback])
    cache["model"] = seq
    cache.close()
    return seq

    # To display the model on jupytor add the following lines
    # from IPython.display import SVG
    # from keras.utils.vis_utils import model_to_dot
    # SVG(model_to_dot(seq).create(prog='dot', format='svg'))
