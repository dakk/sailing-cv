# https://www.kaggle.com/miklazarev/boat-types-recognition-with-keras
# https://www.kaggle.com/dgorelik/94-accuracy-with-fast-ai

import kaggle

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from fastai import *
from fastai.vision import *
from fastai.vision.data import *
from fastai.vision.all import *


def test():
    print ("Hello")

def download_dataset():
    kaggle.api.dataset_download_files('clorichel/boat-types-recognition', path='dataset', unzip=True)




data = ImageDataLoaders.from_folder('./dataset', train=".", 
                                  valid_pct=0.2,
                                  item_tfms=Resize(460),
                                  batch_tfms=aug_transforms(size=224),
                                  size=128,
                                  bs=64)
                                #   ds_tfms=get_transforms(flip_vert=False),
                                #   num_workers=0).normalize(imagenet_stats)


data.show_batch()
learn = cnn_learner(data, resnet34, metrics=error_rate)
learn.lr_find()
learn.fine_tune(2, 3e-3)
learn.show_results()

# learn = create_cnn(data, models.resnet34, metrics=accuracy, model_dir="./model")
# learn.fit_one_cycle(4)
# learn.save('stage-1')
# lr = 1e-3
# learn.unfreeze()
# learn.fit_one_cycle(5, slice(lr))
# learn.save('stage-2')


# data = ImageDataBunch.from_folder(path, train=".", 
#                                   valid_pct=0.2,
#                                   ds_tfms=get_transforms(flip_vert=False),
#                                   size=256,bs=64, 
#                                   num_workers=0).normalize(imagenet_stats)

# learn.data = data
# data.train_ds[0][0].shape
# learn.freeze()
# learn.fit_one_cycle(5, slice(1e-3))


# learn.save('stage-3')

