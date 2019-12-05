import numpy as np
import keras.backend as K
from keras.models import load_model
from keras.layers import Input
from yolo import YOLO
from PIL import Image
import tensorflow as tf

if __name__ == '__main__':
    yolo = YOLO()
    path = 'the image path'
    try:
        image = Image.open(path)
    except:
        print('Open Error! Try again!')
    else:
        r_image = yolo.detect_image(image)
        r_image.show()

    yolo.close_session()
