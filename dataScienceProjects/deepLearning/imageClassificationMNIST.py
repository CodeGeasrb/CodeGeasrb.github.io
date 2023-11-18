
## Creación de una NN básica para clasificación de imágenes

"""**1. Importar Librerías**"""

import tensorflow as tf
import tensorflow_datasets as tfds
import matplotlib.pyplot as plt
import cv2
import numpy as np
from sklearn.metrics import confusion_matrix
import seaborn as sb
import os

"""**2. Descargar el dataset Mnist de digitos escritos a mano**

"""

mnist = tf.keras.datasets.mnist
(X_train,y_train), (X_test,y_test) = mnist.load_data()

"""**3. Exploramos los datos y la metadata**"""

X_train[:2]  # numpy array de las matrices de las imagenes

y_train # array de etiquetas

"""**4. Escalamiento de las imágenes**"""

X_train = X_train/255
X_test = X_test/255

"""**5. Mostrar el dataset:**
Podemos mostrar algunas imágenes que componen el dataset
"""

plt.figure(figsize=(8,6))
plt.suptitle('HandWritten Digits',fontsize=20)
for i in range(len(X_train[:9])):
  plt.subplot(3,3,i+1)
  plt.imshow(X_train[i],cmap=plt.cm.binary)
plt.show()

"""**6. Creación de la red neuronal básica**"""

# Arquitectura de la red
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten(input_shape=(28,28)))
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))

# compilación del modelo
model.compile(
    optimizer='adam',
    loss=tf.keras.losses.SparseCategoricalCrossentropy(),
    metrics=['accuracy']
)

"""**7.Entrenamieto**"""

model.fit(X_train,y_train,epochs=5)

"""**8.Rendimiento del modelo**"""

loss, accuracy = model.evaluate(X_test,y_test)
print(f'La exactitud de la NN es de: {round(accuracy,3)}')
print(f'La pérdida de la NN resultó en: {round(loss,3)}')

"""**9.Predicciones de Mnist**"""

predictions = model.predict(X_test)
predictions[0] # predictions es un array de 10 elementos, con una probabilidad por clase

predictions = np.argmax(predictions,axis=1) # seleccinamos la clase con mayor probabilidad

# creamos una matriz de confusión
confusion_mat = confusion_matrix(y_test,predictions)

"""**10.Predicciones de imágenes nuevas**"""

# creamos imagenes de digitos escritos a mano en paint y evaluamos las predicciones
plt.figure(figsize=(14,6))
plt.suptitle('HandWritten Digits Predictions',fontsize=20)
digit_number = 0
while os.path.isfile(f'digit_{digit_number}.png'):
  image = cv2.imread(f'digit_{digit_number}.png')[:,:,0]  # un solo canal
  image = np.invert(np.array([image]))  # invertimos para que el digito sea de color negro
  image = image/255
  prediction = model.predict(image)
  prediction = np.argmax(prediction)
  plt.subplot(2,5,(digit_number+1))
  plt.imshow(image[0],cmap=plt.cm.binary)
  plt.title(f'Es probable que sea: {prediction}')
  plt.axis('off')
  digit_number += 1
plt.show()

"""## Creación de una NN Convolusional  para clasificación de imágenes

**1.Arquitectura de la CNN**
"""

model_CNN =  tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(28, 28,1)),  # Capa convolucional con 32 filtros de 3x3
    tf.keras.layers.MaxPooling2D((2,2)),  # Capa de max pooling
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

model_CNN.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

"""**2.Entrenamiento**"""

model_CNN.fit(X_train,y_train,epochs=5)

"""**3.Rendimiento**"""

loss_CNN, accuracy_CNN = model_CNN.evaluate(X_test,y_test)
print(f'La exactitud de la CNN es de: {round(accuracy_CNN,3)}')
print(f'La pérdida de la CNN resultó en: {round(loss_CNN,3)}')

"""**4.Predicciones Mnist**"""

predictions_CNN = model_CNN.predict(X_test)
predictions_CNN = np.argmax(predictions_CNN,axis=1)

confusion_mat_CNN = confusion_matrix(y_test,predictions_CNN)

plt.figure(figsize=(15,6))
plt.subplot(1,2,1)
sb.heatmap(confusion_mat,annot=True,cmap='YlGnBu',fmt='d',cbar=False)
plt.title('Matrix Confusion')

plt.subplot(1,2,2)
sb.heatmap(confusion_mat_CNN,annot=True,cmap='YlGnBu',fmt='d',cbar=False)
plt.title('Matrix Confusion CNN')

plt.show()

"""**5.Predicciones Imagenes nuevas**"""

plt.figure(figsize=(14,6))
plt.suptitle('HandWritten Digits Predictions with CNN',fontsize=20)
digit_number = 0
while os.path.isfile(f'digit_{digit_number}.png'):
  image = cv2.imread(f'digit_{digit_number}.png')[:,:,0]  # un solo canal
  image = np.invert(np.array([image]))  # invertimos para que el digito sea de color negro
  image = image/255
  prediction = model_CNN.predict(image)
  prediction = np.argmax(prediction)
  plt.subplot(2,5,(digit_number+1))
  plt.imshow(image[0],cmap=plt.cm.binary)
  plt.title(f'Es probable que sea: {prediction}')
  plt.axis('off')
  digit_number += 1
plt.show()