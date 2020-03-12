# Automatic update of the C3G software stack catalog
**parser.py**: Generate the `result.json`.
**result.json**: the result.
**scratch.py**: scratch the `url` & `description` of modules from websites, and then output the data to `other.json`
**tmp.html**: temp file

## Usage
* Environment: Python 3.8.1
* Run `python scratch.py` && `python parser.py`