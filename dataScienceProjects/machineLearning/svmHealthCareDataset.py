
""" **INTRODUCCIÓN**

El presente trabajo busca la implementación de un modelo de machine learning que pueda predecir con buena precisión la posibilidad de que un paciente pueda presentar un derrame cerebral. El dataset se obtuvo de: https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset?select=healthcare-dataset-stroke-data.csv

**INFORMACIÓN DE LOS ATRIBUTOS**

1. id: identificador único

2. género: "Masculino", "Femenino" u "Otro"

3. edad: edad del paciente

4. hipertensión: 0 si el paciente no tiene hipertensión, 1 si el paciente tiene
hipertensión

5. enfermedad cardíaca: 0 si el paciente no tiene ninguna enfermedad cardíaca, 1 si el paciente tiene una enfermedad cardíaca

6. alguna vez casado: "No" o "Sí"

7. tipo de trabajo: "niños", "trabajo gubernamental", "nunca ha trabajado", "privado" o "autónomo"

8. tipo de residencia: "rural" o "urbana"

9. nivel promedio de glucosa: nivel promedio de glucosa en sangre

10. IMC: índice de masa corporal

11. estado de tabaquismo: "fumaba anteriormente", "nunca fumó", "fuma" o "Desconocido"

12. accidente cerebrovascular: 1 si el paciente tuvo un accidente cerebrovascular o 0 si no

**IMPORTANDO LIBRERÍAS**
"""

import pandas as pd # data exploration and data analysis
import numpy as np  # linear algebra
import matplotlib.pyplot as plt # ploting
import seaborn as sns  # plotting data
from sklearn.model_selection import train_test_split  # data split in train and test data
from sklearn.preprocessing import MinMaxScaler  # scaling data
from sklearn.svm import SVC # SVM model
from sklearn.metrics import confusion_matrix  # confusion matrix
from sklearn.metrics import precision_score
from imblearn.under_sampling import RandomUnderSampler
from imblearn.over_sampling import RandomOverSampler

"""**CARGANDO EL DATASET**"""

data_set = pd.read_csv('healthcare-dataset-stroke-data.csv')
data_set.head(3)

"""**DATA ANÁLISIS**

1. Exploramos el dataset, es posible que existan espacios que deben omitirse o llenar (elementos nulos) o que existan elementos de tipo "categorical"
"""

data_set.info()

"""2. Se observan elementos nulos en el atributo "bmi" , por tanto, decidí rellenar los elementos con el valor medio de este atributo. Usamos el método "decribe( )" para acceder a esta información."""

data_set.describe().T

bmi_mean = data_set['bmi'].mean()
data_set['bmi'].fillna(bmi_mean,inplace=True)
data_set.info()

data_set.head(3)

"""3. Podemos visualizar la cuenta de los datos para conocer más nuestro data set ya sea con gráficos de barras o histogramas."""

for column in data_set.columns:
  if column in ['age','id','avg_glucose_level','bmi']:
    continue
  plt.figure(figsize=(6,5))
  ax = sns.countplot(x=data_set[column])
  plt.title(f'Conteo de datos para {column}')
  plt.show(ax)

for column in data_set.columns:
  if column in ['age','avg_glucose_level','bmi']:
    plt.figure(figsize=(10,8))
    histogram = data_set.hist(column,edgecolor='black')
    plt.show(histogram)
  else:
    continue

"""4. Observamos que existen elementos de tipo "categorical" en los atributos: gender, ever_married, work_type, residence_type y smoking_status, así que decidí cambiarlos por valores numéricos."""

stroke = data_set['stroke'] # saving labels
dummies = pd.get_dummies(data_set[['gender','ever_married','work_type','Residence_type','smoking_status']],dtype=int)
data_set_preprocessed = data_set.drop(['gender','ever_married','work_type','Residence_type','smoking_status','stroke'],axis=1) # creating a new variable to saved dataset pre-processed
data_set_preprocessed = pd.concat([data_set_preprocessed,dummies,stroke],axis=1)
data_set_preprocessed.head(3)

"""5. Creo una matriz de correlación para visualizar la relavancia de los atributos con respecto al label o target."""

plt.figure(figsize=(20,20))
corr_matrix = data_set_preprocessed.corr()
heat_map = sns.heatmap(corr_matrix,cmap='YlGnBu',annot=True)
plt.show(heat_map)

"""**PROCESAMIENTO DE DATOS**

1. Escalamos los datos, esto puede ayudar a mejorar el rendimiento de los modelos de clasificación, en este caso, utilizo minMaxScaler para escalar los valores a números entre 0 y 1.
"""

data_set_processed = data_set_preprocessed
minMax_scaler = MinMaxScaler()  # creating minMax scaler
data_set_processed.iloc[:,1:-1] = minMax_scaler.fit_transform(data_set_preprocessed.iloc[:,1:-1]) # scaling data
data_set_processed.head(3)

"""2. Definimos las variables independientes y dependiente X e y"""

X = data_set_processed.iloc[:,1:-1]
y = data_set_processed.iloc[:,-1]

"""3. También pudimos percatarnos del desbalance que existe entre las clases sí(1) y no(0) en las etiquetas "stroke", por tanto decidí aplicar un remuestreo para equilibrar las instancias entre clase. En este caso aumentamos el número de instancias de la clase minoritaria"""

sampler = RandomOverSampler(random_state=42)
X_resampled,y_resampled = sampler.fit_resample(X,y)

"""**IMPLEMENTACIÓN DE SVM CLASSIFIER**

1. Hacemos un split de los datos para dividir entre datos de entrenamiento y datos de prueba
"""

X_train,X_test,y_train,y_test = train_test_split(X_resampled,y_resampled,test_size=0.2,random_state=42)

"""2. Creamos el modelo de SVM"""

svm_model = SVC(kernel='linear')

"""3. Entrenamos el modelo"""

svm_model.fit(X_train,y_train)

"""4. Realizamos predicciones del conjunto de prueba"""

predictions = svm_model.predict(X_test)

"""5. Evaluamos la exactitud del modelo"""

print(f'La exactitud del modelo es de {svm_model.score(X_test,y_test)}')

"""6. Creamos la matriz de confusión para visualizar gráficamente la comparación entre las predicciones y los valores reales"""

plt.figure(figsize=(8,6))
mat_confussion = confusion_matrix(y_test,predictions)
heat_map_2 = sns.heatmap(mat_confussion, annot=True, cmap='Blues',cbar=False)
plt.title('Matriz de confusión')
plt.xlabel('Predicción')
plt.ylabel('Real')
plt.show()

"""7. Medimos ahora la exactitud del modelo con los resultados de la matriz de confusión."""

print(f'La precisión del modelo es: {precision_score(y_test,predictions)}')