#!/bin/bash

# Set the directory containing your PDFs
pdf_directory="/Users/jasonclishe/JC/.Process/Nirvana/"  

# Check if the directory exists
if [ ! -d "$pdf_directory" ]; then
  echo "Error: The directory '$pdf_directory' does not exist."
  exit 1
fi

# Loop through all PDF files in the directory
for pdf_file in "$pdf_directory"/*.pdf; do
    
    # Check if it's a regular file (not a directory or other type)
    if [ -f "$pdf_file" ]; then
      
        # Extract the base filename (without the extension)
        filename_base=$(basename "$pdf_file" .pdf)

        # Create a directory with the same name as the PDF file
        output_dir="$pdf_directory/$filename_base"
        mkdir -p "$output_dir"

        # Uncomment the appropriate jpg or png lines in the following 2 blocks:

        # Construct the output filename within the new directory
        jpg_file="$output_dir/$filename_base.jpg"
        # png_file="$output_dir/$filename_base.png"
        
        # Use ImageMagick's 'convert' to perform the conversion
        convert -density 300 "$pdf_file" "$jpg_file"
        # convert -density 300 "$pdf_file" "$png_file"
    fi
done

echo "All PDF files in $pdf_directory have been converted."

