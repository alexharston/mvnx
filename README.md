# mvnx

### A lightweight python library for parsing the MVNX motion capture file format.

To run the MVNX parser, create an MVNX object, and run `parse_all()`, which will then parse all the modalities into the object's attributes, which you can then access with standard dot notation:

```python
from mvnx import MVNX
mvnx = MVNX('path/to/file.mvnx')
mvnx.parse_all()
mvnx.orientation
mvnx.jointAngle
```
or you can parse individual modalities (all in camelCase) , as below:

```
mvnx = MVNX('path/to/file.mvnx')
mvnx.parse_modality('orientation')
mvnx.parse_modality('jointAngle')
mvnx.orientation
mvnx.angularVelocity
```

Alternatively, you can run from the command line, using the modality of your choice (in this case, `jointAngle`):

`python3 mvnx.py --file path/to/file.mvnx --modality jointAngle`
