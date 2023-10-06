import os
import shutil

def clean_map_folder(path):
    map_folders=os.listdir(path)
    i=0
    for map in map_folders:
        map_folder_path=os.path.join(path,map)
        files_in_folder=os.listdir(map_folder_path)
        for file in files_in_folder:
            to_remove=os.path.join(map_folder_path,file)
            if to_remove.endswith(".mp3")  or file.endswith(".osu"):
                pass
            else:
                if os.path.isfile(to_remove):
                    os.remove(to_remove)
                if os.path.isdir(to_remove):
                     shutil.rmtree(to_remove)
    print("done")

                
path="C:\\Users\\Uzytkownik\\Desktop\\folder" #insert folder path
clean_map_folder(path)
    

    

