# Stock_Forecast
# Model1  
![10batch_20epochs_resprop](https://user-images.githubusercontent.com/45307224/59323304-181e9d80-8d15-11e9-98c6-1d26a7637bcd.jpg)  
loss = 'mean_square_error'  
optimizer = 'rmsprop'  
batch_size = 10  
epochs = 20  
![10batch_20epochs_resprop_2](https://user-images.githubusercontent.com/45307224/59323652-8748c180-8d16-11e9-9e02-3410bf863f93.jpg)  

# Model2  
![20batch_20epochs_resprop](https://user-images.githubusercontent.com/45307224/59323844-60d75600-8d17-11e9-9d8a-026d6d843817.jpg)  
loss = 'mean_square_error'  
optimizer = 'rmsprop'  
batch_size = 20  
epochs = 20  
![20batch_20epochs_resprop_2](https://user-images.githubusercontent.com/45307224/59323816-3a191f80-8d17-11e9-8bdc-99cf192f42b0.jpg)  


# Model3  
![20batch_20epochs_resprop_mean_absolute_error](https://user-images.githubusercontent.com/45307224/59324374-9bda8900-8d19-11e9-8811-4507ba7168ca.jpg)  
loss = 'mean_absolute_error'  
optimizer = 'rmsprop'  
batch_size = 20  
epochs = 20  
![20batch_20epochs_resprop_mean_absolute_error_2](https://user-images.githubusercontent.com/45307224/59324371-92e9b780-8d19-11e9-89c7-faad7a81bc7f.jpg)  


# Model4  
![10batch_20epochs_resprop_mean_absolute_error](https://user-images.githubusercontent.com/45307224/59324665-df81c280-8d1a-11e9-8c94-1453f990f5b4.jpg)  
loss = 'mean_absolute_error'  
optimizer = 'rmsprop'  
batch_size = 10  
epochs = 20  
![10batch_20epochs_resprop_mean_absolute_error_2](https://user-images.githubusercontent.com/45307224/59324658-d55fc400-8d1a-11e9-8f47-6968b4c0d71f.jpg)  


# Model5  
![20batch_20epochs_adam_mean_absolute_error](https://user-images.githubusercontent.com/45307224/59324448-efe56d80-8d19-11e9-9d7f-2b4617fcaa82.jpg)  
loss = 'mean_absolute_error'  
optimizer = 'adam'  
batch_size = 10  
epochs = 20  
![20batch_20epochs_adam_mean_absolute_error_2](https://user-images.githubusercontent.com/45307224/59324438-e78d3280-8d19-11e9-9a9a-f89dcf200dee.jpg)  


# Model6  
![20batch_20epochs_resprop_mean_squared_logarithmic_error](https://user-images.githubusercontent.com/45307224/59324944-012f7980-8d1c-11e9-8450-f055f392e60b.jpg)  
loss = 'mean_squared_logarithmic_error'  
optimizer = 'rmsprop'  
batch_size = 20  
epochs = 20  
![20batch_20epochs_resprop_mean_squared_logarithmic_error_2](https://user-images.githubusercontent.com/45307224/59324915-e0ffba80-8d1b-11e9-9bf1-2939a3276596.jpg)  


# Model7  
![10batch_20epochs_adagrad_mena_square_error](https://user-images.githubusercontent.com/45307224/59325842-849e9a00-8d1f-11e9-90f5-c8025982750c.jpg)  
loss = 'mean_squared_logarithmic_error'  
optimizer = 'adagrad'  
batch_size = 10  
epochs = 20  
![10batch_20epochs_adagrad_mena_square_error_2](https://user-images.githubusercontent.com/45307224/59325855-8ff1c580-8d1f-11e9-960e-2cd7f2d9c202.jpg)  


# RESULT
## optimizer adagrad 는 rmsprop과 유사 하지만 주식데이터에는  
## rmsprop이 더 적합하고,

## loss function = 'mean_square_error'  
## optimizer = 'rmsprop' 을 가진 Model1 이 가장 잘 예측 한다.
