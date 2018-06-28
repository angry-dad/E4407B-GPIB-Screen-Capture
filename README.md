# E4407B GPIB Screen Capture

A simple python script/example to save a screenshot from the E4407B spectrum analyzer via GPIB. It was written because it was the only spectrum analzyer I had access to at the time. This model has no USB interface, and the floppy drive was broken, so I had no interface to save data other than GPIB.

### Prerequisites

* Python 2.7 or 3.4+
* NI-VISA. Version 17.5 was used for testing, available at http://www.ni.com/download/ni-visa-17.5/7220/en/
**Note: NI-VISA and Python must match in bitness i.e. both 32 or both 64 bit**
* [PyVISA](http://pyvisa.readthedocs.io/en/stable/index.html)  - Control your instruments with Python
* [Pipenv](https://docs.pipenv.org/) - Python Dev Workflow for Humans

### Installing

Python and NI-VISA are installed from their binaries. A system restart is needed after installing NI-VISA.

PyVISA and Pipenv are installed via pip:

```
pip install PyVISA Pipenv
```

Next, install the Pipenv requirements from the Pipfile:

```
pipenv install
```

### Running

```
pipenv run python main.py 
```
Or run/double-click 'capture.bat'

## Authors

* **Joshua Wright**

## License

This project is licensed under the MIT License.