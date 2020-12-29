# landscape-pdf
Utility to convert a pdf for viewing in landscape mode using
[PyPDF2](https://pypi.org/project/PyPDF2/) package. This makes
it easier to read papers and other documents meant to a4 or
letter format on ereader devices like the remarkable2 which
do not make it easy to read content in landscape. Each
page is converted to two overlapping pages covering the
top and bottom of the original page.

[before](imgs/before.png)
[after](imgs/after.png)

# Installation
Can be installed using pip with

```
pip install landscape_pdf
```

# Running
Installation places a script called `landscape-pdf` in the path which takes two arguments, the name of the pdf file to convert and the name of the output file. For example

```
landscape-pdf 2012.13391.pdf 2012.13391_landscape.pdf
```


