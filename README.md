# Bulk image Resizer/Compressor

This is a little script in Python to bulk resize and compress images. 

I use it to create thumbnails for an app. 

## What do you need :

You need Python 3 => https://docs.python.org/fr/3/installing/index.html

After, install Pillow library :

`pip install Pillow`

The documentation is here : https://pillow.readthedocs.io/en/stable/

That's all (normally).

## Script arguments :

You can launch the script without or with arguments, here is the list : 

- `-h` for help
- `-i` to specify the input folder
- `-o` to specify the ouput folder
- `-c` to specify the compresison level (1 to 100)

-----------

- By default, the compression level is set to 50.
- By default, the input folder is the "Images" folder of this repository
- By default, the output folder is the "Thumbnail" folder of this repository

## Image sizes :

By default in the code, the new size of images are set like this in the code : 

```
def determine_size(calculated_ratio):
    # Landscape image
    if calculated_ratio > 1:
        return 1920, 1080
    # Square image
    elif calculated_ratio == 1:
        return 1000, 1000
    # portrait image
    elif calculated_ratio < 1:
        return 1080, 1920
```

Enjoy ! 