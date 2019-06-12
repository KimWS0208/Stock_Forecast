#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd  #  0.23.0
import numpy as np # 1.16.2
import matplotlib.pyplot as plt  #  2.2.2

# Keras                              2.2.4
# Keras-Applications                 1.0.7
# Keras-Preprocessing                1.0.9
# tensorflow                         1.13.1
from keras.models import Sequential
from keras.layers import LSTM, Dropout, Dense, Activation

import datetime

data = pd.read_csv(r"C:\Users\user\Desktop\VSC\StockForecast\data\Ss.csv")
data.head()

high_prices = data['High'].values
low_prices = data['Low'].values
mid_prices = (high_prices + low_prices) / 2

seq_len = 50 #Window size (최근 50일 간 데이터)
sequence_length = seq_len + 1

result = []
for index in range(len(mid_prices) - sequence_length):
    result.append(mid_prices[index:index + sequence_length])
    
# Normalize
normalized_data = []
for window in result:
    normalized_window = [((float(p)/float(window[0])) - 1) for p in window]
    normalized_data.append(normalized_window)
    
result = np.array(normalized_data)

row = int(round(result.shape[0]*0.8))
train = result[:row, :]
np.random.shuffle(train)

x_train = train[:, :-1] #50
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
y_train = train[:, -1] #1

x_test = result[row:, :-1]
x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1],1))
y_test = result[row:, -1]

x_train.shape, x_test.shape


model = Sequential()
model.add(LSTM(50, return_sequences=True, input_shape=(50,1)))
model.add(LSTM(64, return_sequences=False))
model.add(Dense(1, activation='linear')) #다음날 하루 예측
model.compile(loss='mse', optimizer='rmsprop')
model.summary()

model.fit(x_train, y_train,
         validation_data = (x_test, y_test),
         batch_size = 10,
         epochs = 20)

pred = model.predict(x_test)

fig = plt.figure(facecolor='white')
aa = fig.add_subplot(111)
aa.plot(y_test, label='True')
aa.plot(pred, label='Prediction')
aa.legend()
plt.show()