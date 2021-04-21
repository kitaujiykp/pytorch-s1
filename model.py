import torch
import torch.nn as nn

# data.shape = 674

#Declare dimensions
VOCAB_SIZE = 674
OUT_CLASSES = 5
HIDDEN_UNITS = 3


class CNN(nn.Module):
    def __init__(self, vocab_size=VOCAB_SIZE ,hidden_units=HIDDEN_UNITS, num_classes=OUT_CLASSES): 
      super().__init__()
      #First fully connected layer
      self.fc1 = torch.nn.Linear(vocab_size, hidden_units)
      #Second fully connected layer
      self.fc2 = torch.nn.Linear(hidden_units, num_classes)
      #Final output of sigmoid function      
      self.output = torch.nn.Sigmoid()

    def forward(self,x):
          fc1 = self.fc1(x)
          fc2 = self.fc2(fc1)
          output = self.output(fc2)
          return output[:, -1]