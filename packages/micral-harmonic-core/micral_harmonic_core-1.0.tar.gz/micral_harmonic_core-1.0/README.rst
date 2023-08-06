Micral (MICROstructure anALysis)

Harmonic measurement module - core module

-----

Description :

The aim is to figure out in what extend a given microstrucure could be considered like an harmonic structure or not.
This module don't plot any result, but only raw result to be use in others applications

-----

Installation :

pip install micral_harmonic_core

-----

Usage :

In a python file or directly in the interpreter, type :

import micral_harmonic_core
print(micral_harmonic_core.analyse(<your image>))

Where <your image> is the name of the image to analyse (with extension (ie jpg, png, bmp etc...))
The output is an unique value.

It's also possible to send multiple image at once : in that case, provide a list of name :
<your image> = [<image1>, <image2>, ...]
And the return will be also a list of all the results

Note that the image must be in the same directory than the python file (or in the current directory of the command)