import exifread
import os
import time
import re

#Make sure and set your path
def photo_metadata(path):
    for root, dirs, files in os.walk(path):
        for photo in files:
            # Is it a Jpeg?
            if photo.lower().endswith(('.jpg', '.jpeg')):
                print (photo)
                photo_src_path = (os.path.join(root, photo))

                #We're going to skip files that are already formatted correctly
                skip_file = ("^\d{8}_\d{6}")
                if re.match(skip_file, photo):
                    print ("Skipping " + (photo_src_path))
                else:
                    #Magic to get the DateTime into a variable
                    with open((photo_src_path), 'rb') as fh:
                        tags = exifread.process_file(fh, stop_tag="EXIF DateTimeOriginal")
                        dateTaken = tags.get("EXIF DateTimeOriginal")
                        fh.close()

                    # If there is no Exif data, change from none to the current date
                    if not (dateTaken):
                        dateTaken = (time.strftime('%Y%m%d_%H%M%S'))

                    # Convert to a string value
                    dateTaken = str(dateTaken)

                    # Remove : as it is invalid naming character
                    dateTaken = dateTaken.replace(":", "")
                    dateTaken = dateTaken.replace(" ", "_")

                    # Prep the destination file and path
                    filename = dateTaken + '.jpg'
                    photo_dst_path = (os.path.join(root, filename))

                    # Check to see if a collision will occur, e.g. the file already exists
                    # If so, we're going to add an underscore and a number, then recheck
                    counter = 0
                    while True:
                        if os.path.isfile(photo_dst_path):
                            #print ("I'm found a file conflict", counter)
                            counter += 1
                            filename = (dateTaken) + '_' + str(counter) + '.jpg'
                            photo_dst_path = (os.path.join(root, filename))
                        else:
                            break

                    #Rename the file
                    print(photo_src_path, dateTaken)
                    os.rename(photo_src_path, photo_dst_path)


path = 'ADD PATH HERE'
photo_metadata(path)
