# Persontyle Workshop for Applied Deep Learning

This repository contains several ipython notebooks with machine learning tutorials using python, keras and tensorflow.

## Contents

1. [Installation](#installation)
2. [Setup](#setup)
3. [Sessions](#sessions)
4. [Usage](#usage)


## Installation

- This code has been tested in a Linux machine with python 2.7. It should work on Mac OS X as well.
- Follow [these instructions](https://github.com/tensorflow/tensorflow/blob/r0.10/tensorflow/g3doc/get_started/os_setup.md#pip-installation) to install tensorflow 0.10 with pip.
- Install other dependencies ```pip install -r requirements.txt```.

## Setup

Run ``` python setup.py``` to collect datasets and models before we begin, to avoid problems if notebooks freeze at some point.

## Sessions

- AWS Setup
- [Logistic Regression](sessions/2-3_classify.ipynb)
- [Multiclass Classification](sessions/2-3_classify.ipynb)
- [Deep models](sessions/4_deep.ipynb)
- [Convolutional Neural Networks](sessions/5_convnets.ipynb)
- [Visualization](sessions/6_visualization.ipynb)
- [GAN](sessions/7_gan.ipynb)
- [Deep Dream](sessions/8_dream.ipynb)
- [Neural Style](sessions/8_style.ipynb)
- [Object Detection I](sessions/detection/ssd_keras/testing.ipynb)
- [Object Detection II](sessions/detection/ssd_keras/testing_video.ipynb)
- [Object Tracking I](sessions/tracking/tracking_siamese.ipynb)
- [Object Tracking II](sessions/tracking/tracking_kalman.ipynb)
- [LSTM char generation](sessions/13_lstm.ipynb)
- [Embeddings](sessions/14_embeddings.ipynb)
- [20news](sessions/15_news20.ipynb)
- [Question Answering](sessions/16_QA.ipynb)

## Usage

### Run a notebook

```shell
jupyter notebook
```

Then navigate to:

```
http://localhost:8888
```

and start editing the notebooks.
