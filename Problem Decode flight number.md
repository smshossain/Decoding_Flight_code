# 2 - Write a script which processes incoming data about airline flights.  The script should expect to recieve a flight_code as a string.  This string is a coded version of information about that flight. The schema below shows the format: 
# ```
# AA0123.DFWHNL.I0150
# ```
# 
# Example | Name | Possible values
# ------  | ---- | -------
# AA  | Airline | AA = American Airlines<br> JB = Jet Blue<br> SI = Singapore Airlines 
# 0123 | Flight Number | 0000 - 9999 (zero padded)
# DFWHNL | Origin and Destination | Any combination of 3 letter origin and destination IATA airport code.
# I | Status | I = Infight (ENROUTE), G = Ground (departing) 
# 0150 | Time | Can be any integer representing a number of hours and minutes. This will be the time to departure or ETA if enroute.
# 
# Other Notes about the format:
# - All letters in flight code can appear in upper case or lower case.
# - If the two periods (.) are not present the flight code is invalid.
# - Flights departing in less than 30 minutes should including the NOW BOARDING message (see below)
# 
# 
# The script should print the information in a human readable format.  Your script should prompt the user to enter a flight code, print the  result ads shown below:   <Br>
# 
# ```
# Codes to test (see below):
# AA0123.DFWHNL.I0230
# jb1769.JFKGYE.i0336
# Si0023.jfkSIN.G0630
# Si0023.jfkSIN.G0020
# Si0023jfkSIN.G390
# 
# Enter a flight code:
# AA0123.DFWHNL.I0230
# =========================
# American Airlines 123
# DFW -> HNL
# ENROUTE - ETA 2H 30M
# =========================
# 
# Enter a flight code:
# jb1769.JFKGYE.i0336
# =========================
# Jet Blue 1769
# JFK -> GYE
# ENROUTE - ETA 3H 36M
# =========================
# 
# Enter a flight code:
# Si0023.jfkSIN.G0630
# =========================
# Singapore Airlines 23
# JFK -> SIN
# DEPARTING IN 6H 30M
# =========================
# 
# Enter a flight code:
# Si0023.jfkSIN.G0020
# =========================
# Singapore Airlines 23
# JFK -> SIN
# DEPARTING IN 20M
# NOW BOARDING
# =========================
# 
# 
# Enter a flight code:
# Si0023jfkSIN.G0630
# =========================
# Code 'Si0023jfkSIN.G390' is invalid
# =========================
# 
# Enter a flight code:
# Si0023jfkSIN
# =========================
# Code 'Si0023jfkSIN' is invalid
# =========================
# ```

