from keras.datasets import mnist, cifar10
from keras.applications.vgg16 import VGG16
import time

print ("Downloading datasets...")
t = time.time()
mnist.load_data()
cifar10.load_data()

print (time.time() - t,'seconds.')

print("Downloading VGG-16...")
t = time.time()
model = VGG16(weights='imagenet', include_top=False)
model = VGG16(weights='imagenet', include_top=True)
print (time.time() - t,'seconds.')
