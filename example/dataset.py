import numpy as np
import os

from torch.utils.data import Dataset, ConcatDataset
from torchvision import datasets, transforms

class Fake_Dataset(Dataset):
    def __init__(self, dataset):
        self.dataset = dataset
        self.index = [i for i in range(len(dataset))]

    def __len__(self):
        return len(self.index)

    def __getitem__(self, item):
        image, label = self.dataset[self.index[item]]
        label = np.random.randint(0, 9)
        return image, label

def get_femnistDatasets(n_nodes):
	apply_transform_train = transforms.Compose(
		[
			transforms.CenterCrop((96,96)),
      transforms.Grayscale(num_output_channels=1),
			transforms.Resize((28,28)),
			transforms.ColorJitter(contrast=3),
			transforms.ToTensor(),
			transforms.Normalize((0.1307,), (0.3081,))]
	)
	total_nodes = len(os.listdir("../data/writer"))
	train_datasets = []
	for nodeIdx in range(n_nodes):
		directory = '../data/writer/{}'.format(nodeIdx)
		train_datasets.append(datasets.ImageFolder(directory, transform=apply_transform_train))

	test_datasets = []
	for nodeIdx in range(int(0.1*total_nodes)):
		directory = '../data/writer/{}'.format(total_nodes-nodeIdx-1)
		test_datasets.append(datasets.ImageFolder(directory, transform=apply_transform_train))
	test_dataset = ConcatDataset(test_datasets)

	return train_datasets, test_dataset

def get_dataset(n_nodes):
	train_datasets, test_dataset = get_femnistDatasets(n_nodes)

	fake_datasets = [Fake_Dataset(train_dataset) for train_dataset in train_datasets]

	return train_datasets, test_dataset, fake_datasets