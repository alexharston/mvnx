# mvnx

### A Python parser for the MVNX motion capture file format (.mvnx)
[![Downloads](https://static.pepy.tech/personalized-badge/mvnx?period=total&units=international_system&left_color=black&right_color=orange&left_text=Downloads)](https://pepy.tech/project/mvnx)
[![Downloads](https://pepy.tech/badge/mvnx/month)](https://pepy.tech/project/mvnx)
[![Downloads](https://pepy.tech/badge/mvnx/week)](https://pepy.tech/project/mvnx)

You can install the library using `pip install mvnx`

The simplest way to run the tool is in the following way:

```python
import mvnx
yourfile = mvnx.load('path/to/file.mvnx')
```
This creates an MVNX object, the data in which can then be read using standard Python dot notation, like so:

```python
yourfile.orientation 
yourfile.jointAngle
yourfile.angularVelocity
yourfile.segments
yourfile.joints
```
### Alternatively, once installed, you can run the tool from the command line, using `mvnx`.
You can provide `mvnx` a filepath to your .mvnx file and an output path, and it will read the info into a .npy file

Run it using: `mvnx --file path/to/file.mvnx --output /path/to/output.npy`

Note: the parser at present is doing no batch processing or multiprocessing when parsing the file into an object - it will read directly into memory, so be careful when parsing larger files as it can put load on your system.
