Micral (MICROstructure anALysis)

Grain separation module - core module

-----

Description :

The aim is to distinguish between coarse and ultrafine graine microstructure.
This tools output the pourcentage of coarse grain.
This tools doesn't plot anything, it just return raw data that could be get by an user, or use with the graphic module

-----

Installation :

pip install micral_grain_core

-----

Usage :

In a python file or directly in the interpreter, type :

import micral_grain_core
print(micral_grain_core.analyse(<your image>))

Where <your image> is the name of the image to analyse (with extension (ie jpg, png, bmp etc...))
The output is an unique value.

It's also possible to send multiple image at once : in that case, provide a list of name :
<your image> = [<image1>, <image2>, ...]
And the return will be also a list of all the results

Note that the image must be in the same directory than the python file (or in the current directory of the command)