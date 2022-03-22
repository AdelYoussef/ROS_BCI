# ROS_BCI

The aim of this project is to develop a generic BCI system that can help physically impaired patients to increase their degree of independency

in this project an interface technique called steady state viusal envoked potentials was used (SSVEP)

SSVEP uses the envoked potentials from visual stimulation to acquire meaningful data that could be used later to interact with computers.

![image](https://user-images.githubusercontent.com/63298005/159416650-45ab121f-4401-4e78-8f6c-cb98181bbdae.png)

# Data Acquisition

![image](https://user-images.githubusercontent.com/63298005/159416391-946b2a7a-c519-471c-9308-57f6c4af45c9.png)

the process of data acquistion was done by using OPENBCI's [Cyton Biosensing Board](https://shop.openbci.com/products/cyton-biosensing-board-8-channel?variant=38958638542)

the process of visual stimulation is done by an array of LEDs where is LED is flashing with a uinque frequency 
![image](https://user-images.githubusercontent.com/63298005/159416500-8bdc8b5e-2159-4c66-aafc-fe250f5c8776.png)


# Filtering

the collected data is characterised with low voltage values therefore it experiences big deformalities form the surrounding noise signals.
so before going forward with the model the data must be first filtered. 
![image](https://user-images.githubusercontent.com/63298005/159417946-727c7817-e89b-46c6-85c5-703ab2a15cbc.png)


# Feature extraction and classification
aquired data experience feature extraction process to decrease dimensionality and decrease training time for the classification model.

for this project Principal component analysis (PCA) was used as a feature extraction algorithm.

the best classification algorithms used for (SSVEP) data are support-vector machine (SVM) and artifical neural networks (ANN).
<img src="https://user-images.githubusercontent.com/63298005/159419842-c120c65b-319c-4f00-8afb-8030bf5d1447.jpeg" width="250" height="250">    <img src="https://user-images.githubusercontent.com/63298005/159419409-62ddc86d-8d04-4a55-aac7-d6e7ce4916be.png" width="250" height="250">


