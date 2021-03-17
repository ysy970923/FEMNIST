import torch

import dataset as dataset

def getAllDataLoaders(nodeIDs, n_normal):
	nodeDataLoaders = {}
	n_nodes = len(nodeIDs)
	train_datasets, test_dataset, fake_datasets = dataset.get_dataset(n_nodes)
	for i, nodeID in enumerate(nodeIDs):
		if i <= n_normal:
			nodeDataLoaders[nodeID] = torch.utils.data.DataLoader(train_datasets[i], batch_size=10, shuffle=False)
		else:
			nodeDataLoaders[nodeID] = torch.utils.data.DataLoader(fake_datasets[i], batch_size=10, shuffle=False)

	testLoader = torch.utils.data.DataLoader(test_dataset, 10, shuffle=False)

	return nodeDataLoaders, testLoader


if __name__ == "__main__":
	import matplotlib.pyplot as plt
	print("Asdflaskfjlksd")
	nodeIDs = ['node-{}'.format(i) for i in range(10)]
	n_normal = 5
	nodeDataLoaders, testLoader = getAllDataLoaders(nodeIDs, n_normal)
	(image, label) = next(iter(nodeDataLoaders['node-0']))
	print(len(nodeDataLoaders))
	plt.imshow(torch.squeeze(image[1]), cmap='gray')
	plt.savefig("example.png")
	print(label[1])