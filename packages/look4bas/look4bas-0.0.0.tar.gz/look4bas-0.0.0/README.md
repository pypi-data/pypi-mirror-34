# look4bas

``look4bas`` is a Python script to search and obtain Gaussian basis sets.
Currently we only use the data of the
[EMSL basis set exchange](https://bse.pnl.gov/bse/portal).

On the first invocation (and from there on in regular intervals) the script
consults the EMSL BSE website to download the current catalogue
of known basis sets.
Note, that the actual basis set data is not downloaded.
This is only done if the user uses the flag ``--download``, see below.

## Features
- Use **regular expressions** (``grep``) for basis set names and descriptions:
  ```bash
  look4bas  "double zeta"
  ```
- **Ignore case** when searching for patterns:
  ```bash
  look4bas "cc-pv.z" -i
  ```
- Limit to basis sets which **contain** basis definitions for specific **elements**
  (e.g. helium, neon and argon):
  ```bash
  look4bas --elements He Ne Ar
  ```
- Combine various filters:
  ```bash
  look4bas --elements H --regex "cc-pv.z" -i "zeta"
  ```
- Not only list the matching basis sets by name and give a short description
  for them, but also **list the elements** for which this basis set defines
  basis functions:
  ```bash
  look4bas "double zeta" --format elements
  ```
  The same thing can be achied by using the pre-defined ``--extra`` output
  format style, i.e
  ```bash
  look4bas --extra "double zeta"
  ```
- **Download** the findings in Gaussian94 basis format to the current working directory:
  ```bash
  look4bas --elements H --regex "cc-pv.z" -i "zeta" --download
  ```
- For more info about the commandline flags ``look4bas`` understands,
  see the output of ``look4bas -h``

## Requirements and Python dependencies
- Python >= 3.4
- argparse
- [Beautiful Soup](https://pypi.python.org/pypi/beautifulsoup4) >= 4.2
- [PyYAML](https://pypi.python.org/pypi/PyYAML) >= 3.10
- [requests](https://pypi.python.org/pypi/requests) >= 2.2
- shutil
