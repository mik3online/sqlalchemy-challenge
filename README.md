# sqlalchemy-challenge

--------------------------------------------------------------------
Michael Strati // Module 10 Challenge
--------------------------------------------------------------------
In Folder “SurfsUp” are 2 Files:
- File 1: climate_starter.ipynb → fulfills “Part 1: Analyze and Explore Climate Data”
- File 2: app.py → fulfills “Part 2: Design Your Climate App”
--------------------------------------------------------------------
How to run “app.py”

1. In TERMINAL, Navigate to Folder “SurfsUp” in “sqlalchemy-challenge” Folder  

2. Once Navigated to Folder “SurfsUp”, run Code:  python3 app.py

3. Once “python3 app.py” is running, should receive message:
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000

4. In Browser, Navigate to:
- http://127.0.0.1:5000/  ← for Homepage
- http://127.0.0.1:5000/api/v1.0/precipitation ←for Precipitation Route
- http://127.0.0.1:5000/api/v1.0/stations ← for Station Route
- http://127.0.0.1:5000/api/v1.0/tobs ← for TOBS Route
- http://127.0.0.1:5000/api/v1.0/2017-01-01 ← For Start/End route. Type in “YYYY-MM-DD” you would like to see data on a Specific Date. Data will populate as such below:
  
-TAVG:  ##.###
-TMAX:  ##.#
-TMIN:  ##.#
