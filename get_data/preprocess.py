import shutil
import os


folders = os.listdir("../data/by_class")

folder2Label = {}

alphabet = 'abcdefghijklmnopqrstuvwxyz'
hexdigit = '0123456789abcdef'

for i in range(10):
  folder2Label[str(30+i)] = str(i)

for i in range(1, len(alphabet)+1):
  folder_name = str(4 + int(i/len(hexdigit))) + hexdigit[i%len(hexdigit)]
  folder2Label[folder_name] = alphabet[i-1].upper()

for i in range(1, len(alphabet)+1):
  folder_name = str(6 + int(i/len(hexdigit))) + hexdigit[i%len(hexdigit)]
  folder2Label[folder_name] = alphabet[i-1].lower()

n_writer = 0
writer2Idx = {}

for folder in folders:
  print(folder)
  subfolderfiles = os.listdir("../data/by_class/{}".format(folder))
  
  subfolders = []
  for subfolderfile in subfolderfiles:
    if '.mit' in subfolderfile:
      subfolders.append(subfolderfile.replace('.mit', ''))
  
  for subfolder in subfolders:
    f = open("../data/by_class/{}/{}.mit".format(folder, subfolder))
    content = f.read()
    content_list = content.split("\n")
    
    pairs = []
    for pair in content_list:
      pair_list = pair.split(" ")
      if len(pair_list) == 2:
        pairs.append(pair_list)
    
    for pair in pairs:
      file_name = pair[0]
      writer = pair[1][1:5]
      if writer not in writer2Idx.keys():
        writer2Idx[writer] = str(n_writer)
        n_writer += 1

      file_dir = "../data/by_class/{}/{}/{}".format(folder, subfolder, file_name)

      if not os.path.isdir("../data/writer/{}".format(writer2Idx[writer])):
        os.mkdir("../data/writer/{}".format(writer2Idx[writer]))
        for fkey in folder2Label.keys():
          os.mkdir("../data/writer/{}/{}".format(writer2Idx[writer], folder2Label[fkey]))

      target_dir = "../data/writer/{}/{}".format(writer2Idx[writer], folder2Label[folder])
      shutil.copy(file_dir, target_dir)