convert testing.png -border 1x1 -bordercolor black result.png

convert testing.png testing.jpg # not positive this is the correct syntax

convert testing.png -resize 1920 newfile.png 

#convert all files in a directory (extension is case sensitive)
#The new filename will still include the previous extension (file.bmp.jpg). The curly braces will delete everything after the %. 
for f in *.BMP; do convert "$f" "$f.jpg"; done
for f in *.bmp; do convert $f ${f%.bmp}.jpg; done

#same conversion as above, in a script
#!/bin/zsh
cd /path/to/some/working/dir/
for f in *.jpg
do
    /opt/homebrew/bin/convert "$f" "$f.heic"
done

