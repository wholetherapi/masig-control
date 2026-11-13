"""Model definition for masig-control."""

import torch
from torch import nn


class Model(nn.Module):
    def __init__(self, hidden=256):
        super().__init__()
        self.proj = nn.Linear(128, hidden)
        self.head = nn.Linear(hidden, 1)

    def forward(self, x):
        return self.head(torch.relu(self.proj(x)))
