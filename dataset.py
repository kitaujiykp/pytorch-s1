#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/4/16
# @Author : YKP

import torch
from torch.utils.data import Dataset, DataLoader
from dataset_pre import load_data


class MyDataset(Dataset):
    
    def __init__(self):
        base_path = './data'
    
        data, label = load_data(base_path)
        
        self._x = data
        self._y = label
        self._len = len(data)
        
    def __getitem__(self, item):
        return torch.from_numpy(self._x[item]).float()[0] , torch.from_numpy(self._y[item])
    
    def __len__(self):
        return self._len
        
dataset = MyDataset()

dataloader = DataLoader(dataset, batch_size=1, shuffle=True, drop_last=True, num_workers=0)

def myDataloader():
    return dataloader
    
if __name__ == '__main__':
    
    print(len(dataset))
    first = next(iter(dataset))
    print(first)
    n = 0
    
    for data_val, label_val in dataloader:
        print('x:', data_val)
        print('y:', label_val)
        n += 1
    
    print('iteration:', n)