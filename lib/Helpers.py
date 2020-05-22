import matplotlib.pyplot as plt
import numpy as np
def plot_image(image, shape=[256, 256], cmap="Greys_r"):
    plt.imshow(image.reshape(shape), cmap=cmap, interpolation="nearest")
    plt.axis("off")
    plt.show()

def movingaverage(values,window):
  weights = np.repeat(1.0,window)/window
  smas = np.convolve(values,weights,'valid')
  return smas
