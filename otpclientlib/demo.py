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

from otpclientlib.otpclient import OtpServer

def main():
    otp = OtpServer()
    r = otp.plan(fromPlace="45.948523,-0.974349", toPlace="45.989806,-1.091079")
    if r.error():
        err = r.error()
        print("Error %d: %s" % (err.id(), err.msg()))
    else:
        iti = r.itinerary()
        print("Itinerary: %s -> %s (%d seconds), %d transfers" % (iti.startTime(), iti.endTime(), iti.duration(), iti.transfers()))
        for leg in iti.legs():
            print("  Leg %s: %s -> %s (%d seconds, %d meters)" % (leg.mode(), leg.startTime(), leg.endTime(), leg.duration(), leg.distance()))

if __name__ == '__main__':
    main()
