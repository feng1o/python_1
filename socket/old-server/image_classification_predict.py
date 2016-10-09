
import sys
mxnet_root = '/root/mxnet/'
sys.path.insert(0, mxnet_root + 'python')

import mxnet as mx
import logging
import numpy as np
from skimage import io, transform

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Load the pre-trained model
prefix = "/root/mxnet/model/Inception/Inception_BN"
num_round = 39
model = mx.model.FeedForward.load(prefix, num_round, ctx=mx.cpu(), numpy_batch_size=1)

# load mean image
mean_img = mx.nd.load("/root/mxnet/model/Inception/mean_224.nd")["mean_img"]

# load synset (text label)
synset = [l.strip() for l in open('/root/mxnet/model/Inception/synset.txt').readlines()]

def PreprocessImage(path, show_img=False):
    # load image
    img = io.imread(path)
    print("Original Image Shape: ", img.shape)
    # we crop image from center
    short_egde = min(img.shape[:2])
    yy = int((img.shape[0] - short_egde) / 2)
    xx = int((img.shape[1] - short_egde) / 2)
    crop_img = img[yy : yy + short_egde, xx : xx + short_egde]
    # resize to 224, 224
    resized_img = transform.resize(crop_img, (224, 224))
    if show_img:
        io.imshow(resized_img)
    # convert to numpy.ndarray
    sample = np.asarray(resized_img) * 256
    # swap axes to make image from (224, 224, 4) to (3, 224, 224)
    sample = np.swapaxes(sample, 0, 2)
    sample = np.swapaxes(sample, 1, 2)
    # sub mean 
    normed_img = sample - mean_img.asnumpy()
    normed_img.resize(1, 3, 224, 224)
    return normed_img

def Main(path):
    batch = PreprocessImage(path, True)
    prob = model.predict(batch)[0]
    pred = np.argsort(prob)[::-1]
    top1 = synset[pred[0]]
    return top1[9:]



if __name__ == '__main__':
	print Main("111.jpg")
