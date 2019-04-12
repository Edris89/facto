import os
import time


saves_directory_path = "/opt/factorio/saves"



while not os.listdir(saves_directory_path):
    time.sleep(1)


data = {
    
}
if (os.listdir(saves_directory_path)):
    detected_files_list = os.listdir(saves_directory_path)
    print("detected files" + str(detected_files_list))
    files = []
    for file in detected_files_list:
        files.append({"name" : file})
    
    print(files)
    # data has to be
    # data = {
    #     "name": "filename1",
    #     "name": "filename2"
    # }


