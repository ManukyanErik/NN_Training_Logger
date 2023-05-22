# # Example usage
from logger import Logger

logger = Logger(email_sender='erik.manukyan.ca@gmail.com', 
                email_password='zjyoxnpjoilfquff') 

logger.add_email_receiver("erik.77233211@gmail.com", 'DEBUG', 'INFO')

import numpy as np
import tensorflow as tf
from keras.layers import Dense, Flatten, Conv2D, MaxPooling2D
from keras.callbacks import ModelCheckpoint

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

x_train = x_train / 255
x_test = x_test / 255

y_train_cat = tf.keras.utils.to_categorical(y_train, 10)
y_test_cat = tf.keras.utils.to_categorical(y_test, 10)

x_train = np.expand_dims(x_train, axis=2)
x_test = np.expand_dims(x_test, axis=2)

x_train = x_train.reshape(-1, 28, 28, 1)
x_test  = x_test.reshape(-1, 28, 28, 1)

model_cnn = tf.keras.Sequential([
    Conv2D(32, (3,3), padding='same', activation='relu', input_shape=(28, 28, 1)),
    MaxPooling2D((2, 2), strides=2),
    Conv2D(64, (3,3), padding='same', activation='relu'),
    MaxPooling2D((2, 2), strides=2),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(10,  activation='softmax')
])

model_cnn.compile(optimizer= tf.keras.optimizers.legacy.Adam(),
                 loss='categorical_crossentropy',
                 metrics=['accuracy'])

def train_neural_model(num_epochs=10, interval=1):
    logger.log("Training started", "INFO")

    checkpoint = ModelCheckpoint('model_weights.h5', monitor='val_loss', save_best_only=True)
    
    for epoch in range(1, num_epochs+1):
        history = model_cnn.fit(x_train, y_train_cat, batch_size=32, epochs=1, validation_split=0.2, callbacks=[checkpoint])
        current_loss = history.history['loss'][0]
        current_accuracy = history.history['accuracy'][0]
        if epoch%interval==0:
            logger.log(f'Epoch: {epoch}, Loss: {current_loss}, Accuracy: {current_accuracy}', "DEBUG")

    logger.log("Training finished", "INFO")

train_neural_model()

# model_cnn.evaluate(x_test, y_test_cat)

# pred = model_cnn.predict(x_test)
# pred = np.argmax(pred, axis=1)
# print(pred[:10])
