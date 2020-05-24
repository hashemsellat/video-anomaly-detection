import shelve
from os import listdir
from os.path import join, isdir
import numpy as np
import Config
from PIL import Image

def get_clips_by_stride(stride, frames_list):
    """
    Parameters
    ----------
    stride : int
        The distance between two consecutive frames
    frames_list : list
        A list of sorted frames of shape 256*256
    Returns
    -------
    list
        A list of clips , 10 frames each
    """
    clips = []
    sz = len(frames_list)
    clip = np.zeros(shape=(256, 256, 10))
    cnt = 0
    for start in range(0, stride):
        for i in range(start, sz, stride):
            clip[:, :, cnt] = frames_list[i]
            cnt = cnt + 1
            if cnt == 10:
                clips.append(clip)
                cnt = 0

    return clips


def get_dataset(re=Config.RELOAD_DATASET):
    """
    Parameters
    ----------
    re : bool
        Reload the dataset or load it from cache
    Returns
    -------

    """
    cache = shelve.open(Config.CACHE_PATH + "dataset")
    if not re:
        return cache["dataset"]
    sz = 20
    clips = []
    cnt = 0
    container = np.zeros(shape=(256, 256, 10))
    for f in sorted(listdir(Config.DATASET_PATH)):
        if isdir(join(Config.DATASET_PATH, f)):
            print(f)
            all_frames = []
            for c in sorted(listdir(join(Config.DATASET_PATH, f))):
                if str(join(join(Config.DATASET_PATH, f), c))[-3:] == "tif":
                    img = Image.open(join(join(Config.DATASET_PATH, f), c))
                    img = img.resize((256, 256))
                    img = np.array(img, dtype=np.float32)
                    img = img / 256.0
                    all_frames.append(img)
            for stride in range(1, 2):
                clips.extend(get_clips_by_stride(stride, all_frames))
    cache["dataset"] = clips
    cache.close()
    return clips


def get_testset(re=Config.RELOAD_TESTSET):
    cache = shelve.open(Config.CACHE_PATH + "testset")
    if not re:
        return cache["testset"]
    sz = 200
    images = np.zeros(shape=(sz, 256, 256, 10))
    cnt = 0
    cnt_container = 0
    container = np.zeros(shape=(256, 256, 10))
    for f in sorted(listdir(Config.SINGLE_TEST_PATH)):
        if str(join(Config.SINGLE_TEST_PATH, f))[-3:] == "tif":
            img = Image.open(join(Config.SINGLE_TEST_PATH, f))
            img = img.resize((256, 256))
            img = np.array(img, dtype=np.float32)
            img = img / 256.0
            container[:, :, cnt] = img
            cnt = cnt + 1
            if cnt % 10 == 0:
                cnt = 0
                images[cnt_container, :, :, :] = container
                container = np.zeros(shape=(256, 256, 10))
                cnt_container = cnt_container + 1
    cache["testset"] = images
    print(images.shape)
    print(cnt_container)
    return images