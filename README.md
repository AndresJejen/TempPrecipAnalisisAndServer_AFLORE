# TempPrecipAnalisisAndServer_AFLORE

This repo is result of a technical test for Aflore.

## How to use it

1. Clone the repo

```
    git clone https://github.com/AndresJejen/TempPrecipAnalisisAndServer_AFLORE.git
    cd TempPrecipAnalisisAndServer_AFLORE
```
2. Create virtual environment, activate it and install all the dependencies
```
virtualenv env
source ./env/Scripts/activate
pip install -r requirements.txt
```
**Note** If you are using Visual Studio code please install Python Extension   

3. For Data Analysis open the folder ``DataAnalysis`` and open the Python notebook.   
4. For Server Open the Server folder (honoluluserver) in another VS Code Window and press F5
5. The server shoud start to run and you can open any browser and use this querys

route     |Description
----------|--------------------------------------------------------------------------------
/         | "Shows all the available routes"
/api/v1.0/precipitation |"Shows all the precitation data from measures table last 12 months"
/api/v1.0/stations|"Shows all the stations"
/api/v1.0/tobs|"Shows all the temperatures for the last 12 months"
/api/v1.0/\<start>|"Shows Max, min and average value of temperatures from start date to last saved measurement in data"
/api/v1.0/\<start>/\<end>|"Shows Max, min and average value of temperatures from start date to end date saved measurement in data"






# Author
Andres Jejen Cortes [@andres_jejen on twitter](https://twitter.com/andres_jejen)

# Internet Sources
1. [Clean Architecture with python](https://www.thedigitalcatonline.com/blog/2016/11/14/clean-architectures-in-python-a-step-by-step-example/#requests-and-responses)
