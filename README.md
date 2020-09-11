# Omdena Aerial

Based on :- https://github.com/jmather625/predicting-poverty-replication

The above repository involves a lot of manual work to get the data. Using hub, we can eliminate all these tedious tasks.
Hub also allows you to stream data insteading of loading all of it your RAM, thus allowing you to train models on large dataset.
It's ideal for distributed teams that work on shared datasets.

Running the entire repository is now as simple as running the following 3 notebooks in order.
```
train_cnn_hub.ipynb
feature_extract_hub.ipynb
predict_consumption.ipynb
```

PS Ensure that the data folder is present in the base directory.


Understanding how the data was stored is important in case you want to adapt this approach for future models or make modifications to the current one. Go through "store_omdena.py" for the same. 

If you want to try out the storage code:-
```
Install hub, register and login 
> pip3 install hub
> hub register
> hub login
Create a new folder in data folder named "countries". 
In the countries folder create 3 folders, namely ethiopia_2015, malawi_2016 and nigeria_2015.
Create a subfolder images in each of the three folders. 
Place the images that need to be stored in the images folder of their corresponding country.
> python3 store_omdena.py"
```
