# Run inside the directory where the images are
import os
import sys

# Get Pillow --> pip install Pillow
from PIL import Image

def compressImg(file):
	filepath = os.path.join(os.getcwd(), file)
	img = Image.open(filepath)

	# Image resizing
	# img = img.resize((width, height), Image.ANTIALIAS)

	# Image compression
	# Set quality= to the preferred quality.
	# 85 has no difference in low size (MB) files and 65 is the lowest reasonable number
	img.save("Compressed_"+file,"JPEG",optimize=True,quality=85)

def main():
	# Gets current working directory
	dir = os.getcwd()
	for file in os.listdir(dir):
		if os.path.splitext(file)[1].lower() in ('.jpg', '.jpeg'):
			compressImg(file)

if __name__ == "__main__":
	main()
