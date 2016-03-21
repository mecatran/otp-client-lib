# -*- coding: utf-8 -*-
#    This file is part of otp-client-lib.
#
#    otp-client-lib is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    otp-client-lib is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with otp-client-lib.  If not, see <http://www.gnu.org/licenses/>.
"""
@author: Laurent GRÉGOIRE <laurent.gregoire@mecatran.com>
"""
import datetime
from time import strftime, localtime
import requests
import json

class OtpLeg(object):

    def __init__(self, data):
        self._data = data

    def mode(self):
        return self._data.get('mode')

    def duration(self):
        return self._data.get('duration')

    def startTime(self):
        return datetime.datetime.fromtimestamp(self._data.get('startTime') / 1000.)

    def endTime(self):
        return datetime.datetime.fromtimestamp(self._data.get('endTime') / 1000.)

    def distance(self):
        return self._data.get('distance')

    def transitLeg(self):
        return self._data.get('transitLeg')

class OtpItinerary(object):

    def __init__(self, data):
        self._data = data
        self._legs = [ OtpLeg(leg) for leg in self._data.get('legs', []) ]

    def duration(self):
        return self._data.get('duration')

    def startTime(self):
        return datetime.datetime.fromtimestamp(self._data.get('startTime') / 1000.)

    def endTime(self):
        return datetime.datetime.fromtimestamp(self._data.get('endTime') / 1000.)

    def transfers(self):
        return self._data.get('transfers')

    def walkTime(self):
        return self._data.get('walkTime')

    def walkDistance(self):
        return self._data.get('walkDistance')

    def walkLimitExceeded(self):
        return self._data.get('walkLimitExceeded')

    def legs(self):
        return self._legs

class OtpError(object):

    def __init__(self, data):
        self._data = data

    def msg(self):
        return self._data.get('msg')

    def id(self):
        return self._data.get('id')

    def noPath(self):
        return self._data.get('noPath')

class OtpResponse(object):

    def __init__(self, data):
        self._data = data
        self._itineraries = []
        self._error = OtpError(self._data.get('error')) if self._data.get('error') else None
        plan = self._data.get('plan')
        if plan:
            itis = plan.get('itineraries')
            if itis:
                self._itineraries = [ OtpItinerary(iti) for iti in itis ]

    def error(self):
        return self._error

    def itinerary(self):
        return self._itineraries[0] if self._itineraries else None

    def itineraries(self):
        return self._itineraries

class OtpServer(object):

    def __init__(self, url="http://localhost:8080/otp", router="default"):
        self._otpurl = url
        self._router = router

    def plan(self, fromPlace, toPlace, datetime=localtime(), numItineraries=1, **kwargs):
        params = {
                'fromPlace':        fromPlace,
                'toPlace':          toPlace,
                'numItineraries':   numItineraries,
                'time':             strftime("%H:%M:%S", datetime),
                'date':             strftime("%m-%d-%Y", datetime)
        }
        params.update(kwargs)
        resp = requests.get(self._otpurl + "/routers/%s/plan" % self._router, params=params)
        return OtpResponse(json.loads(resp.text))