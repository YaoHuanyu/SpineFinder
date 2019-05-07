from keras.datasets import mnist
from keras.utils import to_categorical
from keras.models import Sequential, load_model
from keras.layers import Dense, Conv2D, Flatten
import sys

_, load_existing = sys.argv

# download mnist data and split into train and test sets
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# reshape data to fit model
X_train = X_train.reshape(60000, 28, 28, 1)
X_test = X_test.reshape(10000, 28, 28, 1)

X_train = X_train / 256.0
X_test = X_test / 256.0

# one-hot encode target column
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

if load_existing == 'False':

    # create model
    model = Sequential()
    # add model layers
    model.add(Conv2D(64, kernel_size=3, activation='relu', input_shape=(28,28,1)))
    model.add(Conv2D(32, kernel_size=3, activation='relu'))
    model.add(Flatten())
    model.add(Dense(10, activation='softmax'))

    # compile model using accuracy to measure model performance
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    # train the model
    model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=3)

    model.save('keras_mnist.h5')

else:

    model = load_model('keras_mnist.h5')

print(model.predict(X_test[:4]))
print(y_test[:4])