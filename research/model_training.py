from keras.models import Model
from keras.layers import Dense, Input
from keras.utils import to_categorical
from keras.callbacks import ModelCheckpoint
import numpy as np
import pandas as pd

np.random.seed(42)
num_class = 4


inputs = Input(shape=(16, ))
x = Dense(32, activation='relu')(inputs)
x = Dense(16, activation='relu')(x)
predictions = Dense(num_class, activation='softmax')(x)
model = Model(inputs=[inputs], outputs=predictions)

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['acc'])

model.summary()

checkpointer = ModelCheckpoint('models_saved/weights-simple.hdf5',
                               monitor='val_acc', verbose=1, save_best_only=True, mode='max')

history = model.fit([X_train],
                    y=to_categorical(y_train), verbose=1,
                    batch_size=64,
                    validation_split=0.25,
                    shuffle=True, epochs=5,
                    callbacks=[checkpointer])
