import tensorflow as tf
import numpy as np

# Задаем входные данные и соответствующие им метки
input_data = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=np.float32)
labels = np.array([[0], [0], [0], [1]], dtype=np.float32)

# Создаем модель нейронной сети
model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=1, activation='sigmoid', input_shape=(2,))
])

# Компилируем модель
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Обучаем модель
model.fit(input_data, labels, epochs=1000, verbose=2)

# Предсказываем результаты
predictions = model.predict(input_data)

# Выводим результаты
print("Предсказания:")
print(predictions)

# Округляем результаты до 0 или 1
rounded_predictions = np.round(predictions,1)
print("Округленные предсказания:")
print(rounded_predictions)