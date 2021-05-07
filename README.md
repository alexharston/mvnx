# mvnx

### A lightweight python library for parsing the MVNX motion capture file format.

```python
from mvnx.mvnx import MVNX
mvnx = MVNX('path/to/file.mvnx')
mvnx.orientation
mvnx.jointAngle
mxnv.segments
mvnx.joints
```
or you can parse individual modalities (all in camelCase) , as below:

```
mvnx = MVNX('path/to/file.mvnx')
mvnx.parse_modality('orientation')
mvnx.parse_modality('angularVelocity')
mvnx.orientation
mvnx.angularVelocity
```

Alternatively, you can run from the command line, using the modality of your choice (in this case, `jointAngle`):

`python3 mvnx.py --file path/to/file.mvnx --modality jointAngle`
