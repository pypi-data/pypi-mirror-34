dicomraw
=======

Code for encoding/decoding arbitrary non-imaging data as `Raw Data Storage IOD` DICOM series by wrapping and unwrapping it into private DICOM `Encapsulated Document`.

Unwrapping with command-line tool
-----
To unwrap non-imaging data from a DICOM file, use `bin/dicomunwrap`:

```
git clone https://gitlab.com/cfmm/DicomRaw
cd DicomRaw
pip install -r requirements.txt
./bin/dicomunwrap --input_file=/path/to/file.dcm --output_directory=/out/dir --decompress
```

This will write the encapsulated file or files, with original names/directory structure, into `/out/dir`, or keep those inside a `zip` file if `--decompress` option is omitted.

Identifying `DicomRaw` datasets
------

An instance of `DicomRaw` encoded `Raw Data Storage` DICOM can be identified by examining it for the private creator tag `(0177, 1000)`.

```
import pydicom
ds = pydicom.read_file('/path/to/file.dcm',stop_before_pixels=True)
is_dicomraw_wrapped = (0x0177, 0x0010) in ds and ds[(0x0177, 0x0010)].value.startswith('Robarts^CFMM')
```