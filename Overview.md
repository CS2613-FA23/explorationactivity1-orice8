# Overview
## 1. Which package or library did you select?
I selected the [AstroPy Python Library](https://docs.astropy.org/en/stable/) for Exploration Activity 1.

## 2. What is the package or library?
### What purpose does it serve?
The purpose of the AstroPy library is to provide tools and constants to do astronomy based calculations and observations. According to the official [AstroPy Website](https://docs.astropy.org/en/stable/#:~:text=It%20is%20at%20the%20core%20of%20the%20Astropy%20Project%2C%20which%20aims%20to%20enable%20the%20community%20to%20develop%20a%20robust%20ecosystem%20of%20affiliated%20packages%20covering%20a%20broad%20range%20of%20needs%20for%20astronomical%20research%2C%20data%20processing%2C%20and%20data%20analysis.):
> "It is at the core of the Astropy Project, which aims to enable the community to develop a robust ecosystem of affiliated packages covering a broad range of needs for astronomical research, data processing, and data analysis."

### How do you use it?
In my sample program I use it to do manipulations and calculations to star data. For example, I wanted to calculate the distance from the earth to different stars, I had to get the [parallax distance](https://skyserver.sdss.org/dr1/en/proj/advanced/hr/hipparcos2.asp#:~:text=d%20%3D%201%2Fp%2C,parallax%20angle%20in%20arc%20seconds.) which uses parsec units, and then convert that distance to [light-years](https://skyserver.sdss.org/dr1/en/proj/advanced/hr/hipparcos2.asp#:~:text=d%20%3D%201%2Fp%2C,parallax%20angle%20in%20arc%20seconds.). In addition, I have used this package in other projects to use solar data as a way to understand abnormalities in sensor data relating to temperature. This package has many uses in the environmental reasearch sector as well as data manipulation/science. I also used [this](https://gist.github.com/elnjensen/ce2367faf0d876def1ff68b6154e102b) tutorial to help me calculate some of the distances.

## 3. What are the functionalities of the package or library?
The [functionalities](https://docs.astropy.org/en/stable/index.html) of the AstroPy library includes:
### [Astrology Constants](https://docs.astropy.org/en/stable/constants/index.html)
  ```
  from astropy.constants import M_sun
  print(M_sun)
  ```
  ```
  Output:
  Name   = Solar mass
  Value  = 1.988409870698051e+30
  Uncertainty  = 4.468805426856864e+25
  Unit  = kg
  Reference = IAU 2015 Resolution B 3 + CODATA 2018
  ```
### Data Tables, Datasets, and [Timeseries](https://docs.astropy.org/en/stable/timeseries/index.html)
  ```
  from astropy.utils.data import get_pkg_data_filename
  from astropy.timeseries import TimeSeries

  filename = get_pkg_data_filename('timeseries/kplr010666592-2009131110544_slc.fits')  
  ts = TimeSeries.read(filename, format='kepler.fits')
  print(ts)
  ```
  ```
  Output:
            time             timecorr   ...   pos_corr1      pos_corr2   
                                d       ...      pix            pix      
----------------------- ------------- ... -------------- --------------
2009-05-02T00:41:40.338  6.630610e-04 ...  1.5822421e-03 -1.4463664e-03
2009-05-02T00:42:39.188  6.630857e-04 ...  1.5743829e-03 -1.4540013e-03
2009-05-02T00:43:38.045  6.631103e-04 ...  1.5665225e-03 -1.4616371e-03
2009-05-02T00:44:36.894  6.631350e-04 ...  1.5586632e-03 -1.4692718e-03
2009-05-02T00:45:35.752  6.631597e-04 ...  1.5508028e-03 -1.4769078e-03
2009-05-02T00:46:34.601  6.631844e-04 ...  1.5429436e-03 -1.4845425e-03
2009-05-02T00:47:33.451  6.632091e-04 ...  1.5350844e-03 -1.4921773e-03
2009-05-02T00:48:32.291  6.632337e-04 ...  1.5272264e-03 -1.4998110e-03
2009-05-02T00:49:31.149  6.632584e-04 ...  1.5193661e-03 -1.5074468e-03
2009-05-02T00:50:29.998  6.632830e-04 ...  1.5115069e-03 -1.5150816e-03
                      ...           ... ...            ...            ...
2009-05-11T17:58:22.526  1.014493e-03 ...  3.6121816e-03  3.1950327e-03
2009-05-11T17:59:21.376  1.014518e-03 ...  3.6102540e-03  3.1872767e-03
2009-05-11T18:00:20.225  1.014542e-03 ...  3.6083264e-03  3.1795206e-03
2009-05-11T18:01:19.065  1.014567e-03 ...  3.6063993e-03  3.1717657e-03
2009-05-11T18:02:17.923  1.014591e-03 ...  3.6044715e-03  3.1640085e-03
2009-05-11T18:03:16.772  1.014615e-03 ...  3.6025438e-03  3.1562524e-03
2009-05-11T18:04:15.630  1.014640e-03 ...  3.6006160e-03  3.1484952e-03
2009-05-11T18:05:14.479  1.014664e-03 ...  3.5986886e-03  3.1407392e-03
2009-05-11T18:06:13.328  1.014689e-03 ...  3.5967610e-03  3.1329831e-03
2009-05-11T18:07:12.186  1.014713e-03 ...  3.5948332e-03  3.1252259e-03
Length = 14280 rows
  ```
### Handling various time formats
  ```
  from astropy.time import Time

  currentDate = Time.now()
  julianDate = Time(currentDate, format='jd', scale='utc')
  print("Today's Julian Date: " + str(julianDate))
  ```
  ```
  Output:
  Today's Julian Date: 2460228.095269535
  ```
### Astronomical and World Coordinates
  ```
  from astropy.coordinates import get_icrs_coordinates

  star_name = "Sirius"
  coords = get_icrs_coordinates(star_name)
  print(f"Right Ascension: {coords.ra.deg}, Declination: {coords.dec.deg}")
  ```
  ```
  Output:
  Right Ascension: 101.287155333, Declination: -16.716115861
  ```
### Machine Learning Modeling and Data Visualization
   Reference this tutorial: [LINK](https://docs.astropy.org/en/stable/modeling/index.html)
  
### Several Statistical Metrics
Simplified tutorial of this: [LINK](https://docs.astropy.org/en/stable/stats/index.html)
  ```
  from astropy.stats import sigma_clip
  import numpy as np
  
  x = np.array([1, 0, 0, 1, 99, 0, 0, 1, 0])
  print(x.mean())
  y = sigma_clip(x)
  print(y.mean())
  ```
  ```
  Output:
  11.333333333333334
  0.375
  ```

## 4. When was it created?
AstroPy was [initially released](https://docs.astropy.org/en/stable/changelog.html) on June 16, 2012.

## 5. Why did you select this package or library?
I selected this library because I've always had an interest in space. I wanted to learn about some of the ways distances between celestial bodies were calculated. This exploration activity also gave me the chance to research different stars and their values and why some values would be useful in certain scenarios.
  
## 6. How did learning the package or library influence your learning of the language?
This package taught me to parse data better and use data tables. In addition, I also learned how to use masking to read "dataframe" data. Masking, as I've learned, is used by AstroPy to check if data is missing by looking at a hidden "masked" array that runs along the length of the existing row. This row indicates whether data exists (False, not masking) or data is non-existant (True, being masked) and returns accordingly.

## 7. How was your overall experience with the package/library?
### When would you recommend this package or library to someone?
As previously stated, I would recommend this library to someone working in data science or in the environmental/astro-science fields. I suppose it could also be used in several physics-based projects as well.

### Would you continue using this package or library? Why or why not?
I would continue using this package. I plan to take an astronomy course to complete my basic science requirement and I think this library will come in handy.
