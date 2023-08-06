# Shongololo
## CO2 and Imet sensor ground atation snap
This is the README for the shongololos portion of the VTAgmonitoring applications


## Install:
### Install for testing with web frontend
```bash
$ git clone --recurse-submodules git@gitlab.com:r4space/VTAgMonitoring.git
$ cd VTAgMonitoring/apps/sensor-logger
$ virtualenv --python=python3 .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
$ python server.py
```
Visit localhost:5000 in a browser
ctrl-c to cancle server.py when done

### Install for deployment
.. code-block::bash
sudo aptitude install python3-dev python3-pip virtualenv 
virtualenv --python=python3 .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install setuptools wheel twine


- [Follow this gist for installin flask on ubuntu](https://gist.github.com/swyngaard/296392c427504ce6f7ea81abb87aaee8)

## Operation
**As a stand alone application:**
- Follow install steps
- cd VTAgMonitoring/apps/
- python3 -m shongololo.shongololo
- Data will output to screen and write to file

**In conjuntction with the python flask web interface**
Ass
1. Follow install steps
2. On webpage:
a) Press "Setup Logger" and wait for log to indicated it has concluded testing sensors (it can take a few seconds)
b) When ready to log data for storage press "Start data capture" (This will also take a few seconds to start as it connects to all sensors"
c) When ready to stop capturing press "Stop Data Capture"
d) Repeat if you wish to sample data again
d) When ready to shutdown system press "Shutdown App" 

## Maintenance for developers
``` bash
$ python3 -m pip install --user --upgrade setuptools wheel twine
$ python3 setup.py sdist bdist_wheel
$ twine upload --repository-url  https://upload.pypi.org/legacy/ dist/*
```


### Docs
Generate docs:
``` bash
$ cd docs/
$ make html
```
