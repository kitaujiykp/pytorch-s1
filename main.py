import torch
from model import CNN
from dataset import myDataloader
from pathlib import Path

dataloader = myDataloader()
# print(next(iter(dataloader)))


LEARNING_RATE = 0.001
model = CNN()
# print the model summery
print(model)  

#Initialize optimizer
optimizer = torch.optim.SGD(model.parameters(), lr=LEARNING_RATE)

#Initialize loss function
loss_fun = torch.nn.BCELoss()
criterion = torch.nn.CrossEntropyLoss()

NUM_EPOCHS = 10
for i in range(NUM_EPOCHS):
    for x_batch, y_batch in dataloader:
        model.train()
        y_pred = model(x_batch)
        loss = loss_fun(y_pred, y_batch.float())
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()
    print('After {} epoch training loss is {}'.format(i, loss.item()))

PATH = Path(__file__).parent / './model/cifar_net.pth'
torch.save(model.state_dict(), PATH)
