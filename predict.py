import torch
from model import CNN
from pathlib import Path
from dataset import myDataloader
import numpy as np

PATH = Path(__file__).parent / './model/cifar_net.pth'

model = CNN()
model.load_state_dict(torch.load(PATH))

dataloader = myDataloader()

x = next(iter(dataloader))
print(x)


outputs = model(x[0])

print(outputs.data)

#PREDICTIONS
# pred = np.round(outputs)
# print(pred)
# target = target.float()
# y_true.extend(target.tolist()) 
# y_pred.extend(pred.reshape(-1).tolist())

# _, predicted = torch.max(outputs, 1)