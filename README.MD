# Image Compression

### Requirements

##### Python

Download lastest version of Python 3 from:

[https://www.python.org/downloads/release/latest](https://www.python.org/downloads/release/latest)

##### PIL

Install Pillow by running the following command:

```Python
pip install Pillow
```

### Running the project

Put the ```compress.py``` file in the directory where all the images you want to compress and/or resize are. In the command line go to the root of that directory:

```
cd path/to/the/image/folder
```

And run the file:

```
python compress.py
```

or

```
python3 compress.py
```

depending on how you set up your Python installation.

### Options

#### Rezising the images

Uncomment the line 13, and change the 'width' and 'height' to your desired size. Example:

```Python
img = img.resize((1080, 720), Image.ANTIALIAS)
```