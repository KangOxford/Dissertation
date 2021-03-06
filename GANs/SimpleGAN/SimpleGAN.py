from turtle import forward
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.datasets as datasets
import torchvision.transforms as transforms
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

class Discriminator(nn.Module):
    def __init__(self, input):
        super(Discriminator, self).__init__()
        self.discriminator = nn.Sequential(
            nn.Linear(input, 256), nn.LeakyReLU(0.01),
            nn.Linear(256,1)     , nn.Sigmoid()
        )
    def forward(self, input):
        return self.discriminator(input)

class Generator(nn.Module):
    def __init__(self, latent_dim, generated_dim):
        super(Generator, self).__init__()
        self.generator = nn.Sequential(
            nn.Linear(latent_dim, 256),    nn.LeakyReLU(0.01),
            nn.Linear(256, generated_dim), nn.Tanh()
        )
    def forward(self, input_lanten, input_generate):
        return self.generator(input_lanten, input_generate)