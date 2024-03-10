import os
from pathlib import Path

# Specify the input folder containing the PDF files
input_folder = "./Optimize"

# Specify the output folder where renamed files will be moved
output_folder = "./renamecut_output"

# Iterate through each file in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith("_Compress.pdf"):  # Check if the file ends with "_Compress.pdf"
        # Remove the "_Compress" suffix
        new_filename = filename.replace("_Compress", "")

        # Create full paths for the old and new filenames
        old_path = os.path.join(input_folder, filename)
        new_path = os.path.join(output_folder, new_filename)

        # Rename the file
        os.rename(old_path, new_path)
        print(f"Renamed: {filename} -> {new_filename}")

print("All files renamed and moved to the 'Output' folder.")