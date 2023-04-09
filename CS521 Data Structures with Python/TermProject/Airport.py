# -*- coding: utf-8 -*-
"""
Airport.py
Jefferson Parker
Class: CS 521 - Spring 1
Date: February 27, 2022

Airport object class to hold data and methods for Airport objects.
"""
import AirportException

class Airport (object):
    """
    Airport class to hold names, codes, coordinates and other useful 
    information about airports.
    
    REQUIRES an IATA code.
    """
    def __init__(self, airportline: str) -> None:
        """
        Initialize a new Airport object with a row of data from the 
        OpenFlights Airport airline database.

        Parameters
        ----------
        airportline : str
            A line from the airport.dat file with one complete record of an 
            airport in comma delimited text.

        Returns
        -------
        None
        """
        # Parse the line of data into the airport object components.
        airport_list = list()
        airport_list = airportline.split(",")
        
        # The IATA three letter code will be used by other data objects in the
        # program, so they are required.
        if airport_list[4] == '\\N':
            raise AirportException ("Airport object requires three letter" +\
                                    "IATA code")
        elif len(airport_list[4]) > 5:
            raise AirportException("Airport data line did not parse correctly.")
        else:
            # Capture the useful bits.
            self.name = airport_list[1].strip('"')
            self.city = airport_list[2].strip('"')
            self.country = airport_list[3].strip('"')
            self.code3 = airport_list[4].strip('"')
            self.lat = airport_list[6]
            self.lon = airport_list[7]
            self.alt = airport_list[8]
    # End __init__
        
    def get_name(self) -> tuple:
        """
        Returns the name, city, country and IATA (three letter) code of the 
        Airport object.

        Returns
        -------
        tuple
            Tuple of name, city, country and IATA code of the Airport.
        """
        return tuple(self.name, self.city, self.country, self.code3)
    # End get_name
        
    def get_coordinates(self) -> tuple:
        """
        Return the coordinates (lattitude, longitude and altitude) of the 
        Airport.

        Returns
        -------
        tuple
            Tuple of latitude, longitude and altitude of the airport.
        """
        return tuple(self.lat, self.lon, self.alt)
    # End get_cordinates
    
    def get_airport(self) -> dict:
        """
        Return a dict object keyed to the IATA airport code. 
        Returns ALL airport attributes.

        Returns
        -------
        dict
            Dict object with IATA code as key and all other airport
            attributes as a list of values.
        """
        return {self.code3: [self.name, self.city, self.country, self.lat, \
                             self.lon, self.alt]}
    # End get_airport
    
    def __repr__(self) -> str:
        """
        Return a printable representation of the Airport object using the 
        built in function.

        Returns
        -------
        str
            A string representation of an airport object.
        """
        return str(self.code3 + ":" + self.name + "(" + self.city + ","\
                   + self.country + ")")
    # End repr
# End class Airport