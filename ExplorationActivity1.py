from astroquery.simbad import Simbad
from astropy.coordinates import SkyCoord, get_icrs_coordinates
from astropy.coordinates.name_resolve import NameResolveError
import astropy.units as u

def get_star_info(s_StarName):
    Simbad.add_votable_fields('main_id', 'plx', 'distance') 

    try:
        coordinates = SkyCoord.from_name(s_StarName) # gets the necessary coordinates
    except NameResolveError as e:
        print("NameResolveError:", e)
        coordinates = None  # Set coordinates to None when name is unfound

    try:
        coords = get_icrs_coordinates(s_StarName)
        coords_str = f"Right Ascension: {coords.ra.deg}, Declination: {coords.dec.deg}"
    except NameResolveError as e:
        print("NameResolveError:", e)
        coords = None
        coords_str = None

    try:
        star_info = Simbad.query_object(s_StarName) # query the identifying information
    except NameResolveError as e:
        print("NameResolveError:", e)
        star_info = None # Set star information to None when star is unfound

    print(f"\n{s_StarName}:") # print star name
    print(f"Coordinates: {coords_str}")

    try:
        if star_info is not None:
            if not star_info['PLX_VALUE'].mask[0]: # if parallax distance available...
                print("Distance from earth is {:0.1f} lightyears.".format((1000./star_info['PLX_VALUE'][0]) * 3.262)) # get parallax distance in light-years
            else: 
                print("No distance available in Simbad.")
        else:
            print("Unable to resolve astronomical coordinates for the given name.\n")
    except NameResolveError as e:
        print("NameResolveError:", e)

    try:
      if star_info is not None:
          if not star_info['MAIN_ID'].mask[0]:  # Check if MAIN_ID is available
              print(f"Main Identifier: {star_info['MAIN_ID'][0]}")  # Print the MAIN_ID
          else:
              print("No ID available in Simbad.")
      else:
          print("Unable to resolve main identifier for the given name.\n")
    except NameResolveError as e:
      print("NameResolveError:", e)

if __name__ == "__main__":
    star_name = input("Enter the name of a star (use underscores if name has spaces): ")
    get_star_info(star_name)