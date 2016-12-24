import exifread
import os

file = open('Path\\test.jpg', 'rb')
tags = exifread.process_file(file, stop_tag="EXIF DateTimeOriginal")
dateTaken = tags["EXIF DateTimeOriginal"]
file.close()
