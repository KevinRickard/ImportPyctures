#! python3

import os
import shutil
from datetime import datetime

camera_path = 'D:\\'  # must end with a trailing slash (or two backslashes on windows)
pictures_path = 'C:\\Users\\Kevin\\Pictures\\'  # must exist and end with appropriate slash(es)
valid_media_filetypes = {'JPG','MOV'}  # case sensitive
dcim_path = camera_path + 'DCIM\\'  # windows specific backslashes, must be changed for other os'
imported_txt_path = camera_path + 'imported.txt'
month_num_to_season_map = {
    1: 'Winter',
    2: 'Winter',
    3: 'Spring',
    4: 'Spring',
    5: 'Spring',
    6: 'Summer',
    7: 'Summer',
    8: 'Summer',
    9: 'Fall',
    10: 'Fall',
    11: 'Fall',
    12: 'Fall'
}

if not (os.path.exists(camera_path) and os.path.exists(dcim_path)):
    print('WARNING: Could not find the camera and/or DCIM directory.',
          'Please make sure the SD card is inserted or the camera is connected.')
else:
    last_import_time = None
    if os.path.exists(imported_txt_path):
        last_import_time = datetime.fromtimestamp(os.stat(imported_txt_path).st_mtime_ns // 1000000000)
        print("Media on this card was last imported on " + str(last_import_time))
    else:
        print("Media on this card has never been imported before; Everything will be imported.")
        last_import_time = datetime.min

    media_files = []
    for entry in os.scandir(dcim_path):
        if entry.is_dir() and len(entry.name) == 8 and entry.name[0:3].isdigit():  # if entry is a camera directory
            for subentry in os.scandir(entry.path):
                if (not subentry.is_dir()) and \
                        len(subentry.name) > 8 and \
                        subentry.name.find('.') == 8 and \
                        subentry.name[4:8].isdigit() and \
                        subentry.name[9:] in valid_media_filetypes:
                    # if subentry is a media file
                    media_files.append(subentry)

    imported_file_count = 0
    for media_file in media_files:
        creation_time = datetime.fromtimestamp(media_file.stat().st_ctime_ns // 1000000000)
        if creation_time > last_import_time:
            destination_folder_name = str(creation_time.year) + ' ' + month_num_to_season_map[creation_time.month]
            destination_folder_path = pictures_path + destination_folder_name
            if not os.path.exists(destination_folder_path):
                os.makedirs(destination_folder_path)
            destination_path = destination_folder_path + '\\' + media_file.name
            if os.path.exists(destination_path):
                print('WARNING: I want to copy ' + media_file.path, '->', destination_path,
                      'but the destination file already exists.',
                      'I must skip this file now, and it will not be attempted to be imported in the future.',
                      'If you want to import this file, you must do it manually.')
            else:
                print('Copying ' + media_file.path, '->', destination_path)
                shutil.copyfile(media_file.path, destination_path)
                imported_file_count += 1

    print('Imported ' + str(imported_file_count) + ' files')

    print('Creating new imported.txt file in the camera directory')
    f = open(imported_txt_path, "w")
    f.write("Media on this card was last imported on " + str(datetime.now()))
    f.close()

input('\nPress enter to close this window')
