# Stock_Forecast
Model1

Layer (type)               |  Output Shape        |      Param  

lstm_5 (LSTM)              |  (None, 50, 50)      |      10400     

lstm_6 (LSTM)              |  (None, 64)          |      29440     

dense_3 (Dense)            |  (None, 1)           |      65        

loss = 'mse'  
optimizer = 'rmsprop'  
batch_size = 10  
epochs = 20  

![10batch_20epochs_resprop](https://user-images.githubusercontent.com/45307224/59323304-181e9d80-8d15-11e9-98c6-1d26a7637bcd.jpg)

