# mvnx

### A Python parser for the MVNX motion capture file format (.mvnx)

You can install the library using `pip install mvnx`

The simplest way to run the tool is in the following way:

```python
from mvnx import MVNX
yourfile = MVNX('path/to/file.mvnx')
```
This creates an MVNX object, the data in which can then be read using standard Python dot notation:

```python
mvnx.orientation 
mvnx.jointAngle
mvnx.angularVelocity
mxnv.segments
mvnx.joints
```
or you can parse individual modalities (all in camelCase) , as below:
```
yourfile = MVNX('path/to/file.mvnx')
yourfile.parse_modality('orientation')
yourfile.parse_modality('angularVelocity')
```

### Alternatively, once installed, you can run the tool from the command line, using `mvnx`.
You can provide `mvnx` a filepath to your .mvnx file and an output path, and it will read the info into `.npy` file

Run it using: `mvnx --file path/to/file.mvnx --output /path/to/output.npy`
