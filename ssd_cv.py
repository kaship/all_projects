import torch

from torch.autograd import Variable


from ssd import build_ssd

import imageio


from data import BaseTransform , VOC_CLASSES  as labelmap

import torch
precision = 'fp32'
ssd_model = torch.hub.load('NVIDIA/DeepLearningExamples:torchhub', 'nvidia_ssd', model_math=precision)



import os

os.chdir('ssd_model')