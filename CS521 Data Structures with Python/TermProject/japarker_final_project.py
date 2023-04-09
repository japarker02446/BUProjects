# -*- coding: utf-8 -*-
"""
japarker_final_project.py
Jefferson Parker
Class: CS 521 - Spring 1
Date: February 27, 2022

Load aiport data from https://openflights.org/data.html (airports.dat).
Process the file to calculate global airport statistics.
Classes and methods allow user selection from a selection of airports and
    calculate distance between them.
"""
# Import module(s).
from math import radians, cos, sin, asin, sqrt
import random

# Import custom modules:
# NOTE - You have to open and execute the custom class files in the current
#   session to make them importable.  I don't really understand why this is
#   the case but it is what works.
try:
    import Airport
except ModuleNotFoundError:
    print("Please open and run the AirportException.py and Airport.py" +\
          " modules before trying to import the Airport module.")

# Define program function(s).
def haversine_distance(lat1:float, lon1: float, lat2:float, lon2:float) -> float:
    """
    Haversine distance calculation of great circle arc around the earth as
    defined at https://stackoverflow.com/questions/4913349/haversine-formula-\
        in-python-bearing-and-distance-between-two-gps-points.

    Parameters
    ----------
    lat1 : float
        Latitude of coordinate 1 in decimal degrees.
    lon1 : float
        Longitude of coordinate 1 in decimal degrees.
    lat2 : float
        Latitude of coordinate 2 in decimal degrees.
    lon2 : float
        Longituted of coordinate 2 in decimal degrees.

    Returns
    -------
    float
        Distance between coordinate 1 and coordinate 2 in kilometers.
    """
    EARTHRADIUS = 6371
    
    # Convert decimal degrees to radians.
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)
    
    diff_lat = lat2 - lat1
    diff_lon = lon2 - lon1
    
    a = sin(diff_lat/2)**2 + cos(lat1) * cos(lat2) * sin(diff_lon/2)**2
    c = 2 * asin(sqrt(a))
    
    return c * EARTHRADIUS
# End haversine_distance

# Initialize program variables.
all_airport_dict = dict()
all_code_list = list()
select_airport_set = set()

# Load airport data from the input file "airport.dat".
# For some reason the encoding had to be specified as UTF-8.
try:
    infile = open("airports.dat", "r", encoding="UTF-8")
    
    # Parse the data file to capture airport entries.
    for next_line in infile:
        try:
            next_airport = Airport(next_line)
#            print(next_airport)
            
            # All airports in a dict by IATA code.
            # All airport IATA codes as a LIST.
            all_airport_dict.update(next_airport.get_airport())
            all_code_list.append(next_airport.code3)
            
        except AirportException:
            continue
except FileNotFoundError:
    print("ERROR: Data file airports.dat not found.")

# From the available airports, select 20 for the user to select from for a 
# trip and load them to a SET
select_airport_set = set(random.sample(all_code_list, 20))
print("{:^10}{:<20}{:<20}{:<30}".format(str("Code"), str("City"), \
                                        str("Country"), str("Name")))
print("{:^10}{:<20}{:<20}{:<30}".format(str("----"), str("----"), \
                                        str("-------"), str("----")))

for airport in select_airport_set:
    print("{:^10}{:<20}{:<20}{:<30}".format(airport, 
                                           all_airport_dict[airport][1],
                                           all_airport_dict[airport][2], 
                                           all_airport_dict[airport][0]
                                    )
          )

# Prompt the user to select two airports from the list by Code.
# Confirm that the airports are in the list (select_airport_set).
# Calculate the distance between the airports.
# Report the distance with the names.
airport1 = ''
airport2 = ''

# Select airport1
user_pass = False
while not user_pass:
    user_pass = True
    
    airport1 = input("Please enter the CODE for your DEPARTURE airport from"\
                     " the above list: ")
    if airport1 not in select_airport_set:
        print("I'm sorry, that airport is not in our flight plans, please"\
              "select again")
        user_pass = False
# End select airport1.

# Select airport2
user_pass = False
while not user_pass:
    user_pass = True
    
    airport2 = input("Please enter the CODE for your DESTINATION airport from"\
                     " the above list: ")
    if airport2 not in select_airport_set:
        print("I'm sorry, that airport is not in our flight plans, please"\
              "select again")
        user_pass = False
# End select airport2.

# Pull the airport data.
# Calculate the distance.
# Report to output.
depart_port = all_airport_dict[airport1]
destin_port = all_airport_dict[airport2]

try:
    distance = haversine_distance(float(depart_port[3]), 
                                  float(depart_port[4]), 
                                  float(destin_port[3]), 
                                 float(destin_port[4])
                            )
    print("The distance between {} and {} is {:.2f} miles".format(depart_port[1],
                                                                 destin_port[1],
                                                                 distance
                                                            )
          )
except ValueError:
    print("Distance cannot be calculated for these airports.")
