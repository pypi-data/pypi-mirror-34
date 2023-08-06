#自定义的dataset，用来存储数据，通过append(list)的形式存储数据
from torch.utils.data import Dataset
import h5py
import torch as tc
class dataset(Dataset):
    def __init__(self,h5name,opt,auto_save=True):
        self.h5 = h5py.File(h5name,opt)
        self.auto_save = auto_save
        self.opt = opt
        if opt=='r':
            self.nkeys = self.h5['nkeys'].value
            self.length = (len(list(self.h5.keys())) - 1) // self.nkeys
        else:
            self.length = 0
            self.nkeys = 0
    def append(self,data:tuple):
        if not data:
            return
        if self.nkeys == 0:
            self.nkeys = len(data)
            self.h5.create_dataset('nkeys',data=self.nkeys)
        assert len(data) == self.nkeys, '数组大小不一'
        for i,v in enumerate(data):
            self.h5.create_dataset('{}_{}'.format(self.length,i),data=v)
        self.length += 1
        if self.auto_save: 
            self.h5.flush()
    def __iter__(self):
        self.n_iter=0
        return self
    def __next__(self):
        self.n_iter+=1
        return self[self.n_iter-1]
    def __len__(self):
        return self.length
    def __getitem__(self,n):
        return [self.h5['{}_{}'.format(n,i)].value for i in range(self.nkeys)]
    def cat(self,data):
        return [tc.cat(list(i),0) for i in data]
    def __del__(self):
        try:
            self.h5.close()
        except:
            pass


