# mvnx

### A lightweight python library for parsing the MVNX motion capture file format.

To run the MVNX parser, instantiate a ParseObject, and then parse the relevant attributes you want in the following manner:

```python
PO = ParseObject()
PO.parse_mvnx('path/to/file.mvnx')
PO.parse_modality('orientation')
PO.parse_modality('jointAngle')
PO.orientation
PO.jointAngle
```

Alternatively, you can run from the command line, using the modality of your choice (in this case, `jointAngle`):

`python3 mvnx.py --file path/to/file.mvnx --modality jointAngle`
