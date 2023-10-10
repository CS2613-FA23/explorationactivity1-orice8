# Overview
## 1. Which package or library did you select?
I selected the [AstroPy Python Library](https://docs.astropy.org/en/stable/) for Exploration Activity 1.

## 2. What is the package or library?
### What purpose does it serve?
The purpose of the AstroPy library is to provide tools and constants to do astronomy based calculations and observations. According to the official [AstroPy Website](https://docs.astropy.org/en/stable/#:~:text=It%20is%20at%20the%20core%20of%20the%20Astropy%20Project%2C%20which%20aims%20to%20enable%20the%20community%20to%20develop%20a%20robust%20ecosystem%20of%20affiliated%20packages%20covering%20a%20broad%20range%20of%20needs%20for%20astronomical%20research%2C%20data%20processing%2C%20and%20data%20analysis.):
> "It is at the core of the Astropy Project, which aims to enable the community to develop a robust ecosystem of affiliated packages covering a broad range of needs for astronomical research, data processing, and data analysis."

### How do you use it?
In my sample program I use it to do manipulations and calculations to star data. For example, I wanted to calculate the distance from the earth to different stars, I had to get the [parallax distance](https://skyserver.sdss.org/dr1/en/proj/advanced/hr/hipparcos2.asp#:~:text=d%20%3D%201%2Fp%2C,parallax%20angle%20in%20arc%20seconds.) which uses parsec units, and then convert that distance to [light-years](https://skyserver.sdss.org/dr1/en/proj/advanced/hr/hipparcos2.asp#:~:text=d%20%3D%201%2Fp%2C,parallax%20angle%20in%20arc%20seconds.). In addition, I have used this package in other projects to use solar data as a way to understand abnormalities in sensor data relating to temperature. This package has many uses in the environmental reasearch sector as well as data manipulation/science.

## 3. What are the functionalities of the package or library?
The functionalities of the AstroPy library includes:
- Astrology Constants
- Data Tables, Datasets, and Timeseries
- Handling various time formats
- Astronomical and World Coordinates
- Machine Learning Modeling
- Several Statistical Metrics
- File I/O
- Data Visualization, Filtering, and Convolution
- Calculation Functions

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
