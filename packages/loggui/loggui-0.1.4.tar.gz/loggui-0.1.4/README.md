# LogGui

## GUI for Python logging

## Installation

1. Install requirements
`pip3 install -r requirements.txt`

2. Install LogGui!
`python3 setup.py install`

3. (Optionally) Try it out!
`python3 -m loggui example/just_logging.py`

![LogGui](pics/LogGui.png)

## Usage

### Run script

`python3 -m loggui path_to_script`

### Include in your code

Add this in place where you want the GUI to show up:

```
import logging
from loggui import GUILoggerHandler
rlogger = logging.getLogger()
rlogger.setLevel(logging.DEBUG)
rlogger.addHandler(GUILoggerHandler())
```
