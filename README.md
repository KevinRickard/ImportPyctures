# ImportPyctures
A simple Python script for importing pictures from a digital camera. Originally created for my Mom and other non-tech-savvy people.

### How it works

Grabs all the new media files off of your camera or sd card and then copies them into folders on your computer organized by season.

Follows the [DCF 2.0 (2010) standard](https://web.archive.org/web/20180517065732/http://cipa.jp/std/documents/e/DC-009-2010_E.pdf) for detecting media files on a given volume.

Creates a file on the root of your volume: imported.txt ; which is used for keeping track of which files have already been imported (by checking the creation date of files compared to the modification date of imported.txt). Will also check to not overwrite files on your computer in the unlikely case where the program thinks it should import a file that already exists.

### OS compatibility

The script is currently only designed and tested for *Windows (10)* machines, but should be able to be updated to Linux/Mac if you so desire. You'll want to replace all the ctime uses with mtime in that case as ctime is only used by windows.

### Getting started

You'll need to edit some things in the script to make it work for your system. 
1. camera_path - Set this to the drive letter or volume where your camera or sd_card shows up on your system.
1. pictures_path - Set this to the folder where you want your season subfolders created.
1. valid_media_filetypes - This is a set that should contain all the different filetypes that can be created by your camera. Please note these strings are case sensitive.
1. month_num_to_season_map - If you want to, you can change how the seasonal folders are decided. Or maybe ditch the seasons all together. It's up to you.

### License

This project uses the MIT license. There's a lot of room for improvement so go crazy. Check the LICENSE file for more information.
