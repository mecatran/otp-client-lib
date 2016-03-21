# otp-client-lib
An open source (GPLv3) client library in python for making HTTP requests to an OpenTripPlanner server.

## Installation

Download and install the lib:

	$ git clone git@github.com:mecatran/otp-client-lib.git
	$ cd otp-client-lib
	$ pip install .

## API tutorial

See [otpclientlib/demo.py](https://github.com/mecatran/otp-client-lib/blob/master/otpclientlib/demo.py) for a minimal example:

```python
from otpclientlib.otpclient import OtpServer

# Default to "http://localhost:8080/otp", use "url" parameter to change
otp = OtpServer(router='bordeaux')

# You can also set other parameters:
# datetime, mode, numItineraries, walkSpeed...
r = otp.request(origin="44.844877,-0.656358",
                destination="44.837789,-0.579180")

if r.error():
	# An error occured
	print("Error %d: %s" % (r.error().id(), r.error().msg()))
else:
	# Get the first itinerary
	iti = r.itinerary()
        print("Itinerary: %s -> %s (%d seconds), %d transfers" % (
		i.startTime(), iti.endTime(),
		i.duration(), iti.transfers()))
        for leg in iti.legs():
            print("  Leg %s: %s -> %s (%d seconds, %d meters)" % (
			g.mode(), leg.startTime(), leg.endTime(),
			g.duration(), leg.distance()))
```
