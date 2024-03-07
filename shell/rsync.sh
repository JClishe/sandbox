rsync [OPTION]... SRC [SRC]... DEST


# The following command will copy all files and directories from the current working directory to the specified destination. -v (verbose) is optional. 
rsync -v -r --progress * '/Volumes/Seagate 5TB/'

Common arguments:
--remove-source-files Removes the source files but not the directories 
--progress Show progress during transfer