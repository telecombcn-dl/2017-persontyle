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
- [Logistic Regression]()
- [Multiclass Classification]()
- [Deep models](sessions/deep.ipynb)
- [Convolutional Neural Networks](sessions/convnets.ipynb)
- [Visualization](sessions/visualization.ipynb)
- [GAN]()
- [Deep Dream](sessions/dream.ipynb)
- [Neural Style](sessions/style.ipynb)
- [Object Detection I](sessions/detection/ssd_keras/detection_1.ipynb)
- [Object Detection II](sessions/detection/ssd_keras/detection_2.ipynb)
- [Detection for Video](sessions/detection/ssd_keras/video_detection.ipynb)
- [Object Tracking II](sessions/tracking/tracking.ipynb)
- [LSTM char generation]()
- [Embeddings]()
- [20news]()
- [Question Answering]()

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
