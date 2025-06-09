"""
A single-file implementation of a GPT-2 inspired language model.

References:
    * https://github.com/karpathy/minGPT/blob/master/mingpt/model.py
    * https://github.com/karpathy/nanoGPT/blob/master/model.py
"""

import torch
import torch.nn as nn
import torch.nn.functional as F

