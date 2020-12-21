import shutil
import os
dict_extenstions={
    'audio_extenstions':('.mp3','.mp4'),
    'video_extenstions':('.pm4','.mkv'),
    'document_extenstions':('.txt','.pdf'),
}
folderpath=input('enter the path : ')
def file_finder(folder_path,file_extentions):
    files=[]
    for file in os.listdir(folder_path):
        for extenstion in file_extentions:
            if file.endswith(extenstion):
                files.append(file)
    return files

for extenstion_type, extenstion_tuple in dict_extenstions.items():
    folder_name = extenstion_type.split('_')[0] + 'Files'
    folder_path = os.path.join(folderpath,folder_name)
    os.mkdir(folder_path)
    for item in file_finder(folderpath,extenstion_tuple):
        item_path=os.path.join(folderpath,item)
        item_new_path=os.path.join(folder_path,item)
        shutil.move(item_path,item_new_path)                