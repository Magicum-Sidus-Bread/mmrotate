import os
import shutil

path = '/home/dc/mnt/disk1/niuniu/Mydataset/trainData/video/'
new_path = '/home/dc/mnt/disk1/niuniu/Mydataset/trainData/new_train/'
count = os.listdir(path)
count.sort(key = int)
print(count)
num = 0



for dir in count:
    files = os.listdir(path+dir+'/img/')
    files.sort(key=lambda x: int(x.split('.')[0]))
    #print(files)
    for file in files:
        if file.find('.jpg') != -1:
            shutil.copy(os.path.join(path +'/'+ dir +'/'+ 'img', file),os.path.join(new_path, 'P'+ str(num).zfill(6) + '.jpg'))
            num = num + 1



# for root, dirs, files in os.walk(path):
#     if len(dirs) == 0:
#         for file in files:
#             if file.find('.jpg') != -1:
#                 shutil.copy(os.path.join(path +'/'+ root[-6] + root[-5] +'/'+ 'img', file),os.path.join(new_path, 'P'+ str(num).zfill(4) + '.jpg'))
#                 num = num + 1


