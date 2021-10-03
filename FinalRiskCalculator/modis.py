import sys
import requests
import json
import datetime

lat = float(sys.argv[1]) # Input latitude - to be given
lon = float(sys.argv[2]) # Input longitude - to be given


url = "https://modis.ornl.gov/rst/api/v1/"
header = {'Accept': 'application/json'}

from datetime import datetime
day_of_year = datetime.now().timetuple().tm_yday
start_day = day_of_year - 60
end_day = day_of_year
year = datetime.today().year

modis_start_date = f"A{year}{start_day}"
modis_end_date = f"A{year}{end_day}"

prod = ['MOD13Q1','MOD11A2','MOD14A2'] # MODIS product for LST data, NDVI, Thermal anomalies
data_band = ['250m_16_days_NDVI','LST_Day_1km','FireMask'] 
above_below = 10 # km above/below
left_right = 10 # km left/right

lst_response = requests.get("".join([
        url, prod[1], "/subset?",
        "latitude=", str(lat),
        "&longitude=", str(lon),
        "&band=", data_band[1],
        "&startDate=", modis_start_date,
        "&endDate=", modis_end_date,
        "&kmAboveBelow=", str(above_below),
        "&kmLeftRight=", str(left_right)
    ]), headers=header)

ndvi_response = requests.get("".join([
        url, prod[0], "/subset?",
        "latitude=", str(lat),
        "&longitude=", str(lon),
        "&band=", data_band[0],
        "&startDate=", modis_start_date,
        "&endDate=", modis_end_date,
        "&kmAboveBelow=", str(above_below),
        "&kmLeftRight=", str(left_right)
    ]), headers=header)

thermal_anomaly_response = requests.get("".join([
        url, prod[2], "/subset?",
        "latitude=", str(lat),
        "&longitude=", str(lon),
        "&band=", data_band[2],
        "&startDate=", modis_start_date,
        "&endDate=", modis_end_date,
        "&kmAboveBelow=", str(above_below),
        "&kmLeftRight=", str(left_right)
    ]), headers=header)


from statistics import mean
subset= [0,0,0]
means=[0,0,0]
subset[0] = json.loads(ndvi_response.text)
data = subset[0]['subset'][0]['data']
means[0] = mean(data)*0.0001

subset[1] = json.loads(lst_response.text)
data = subset[1]['subset'][0]['data']
means[1] = mean(data)

subset[2] = json.loads(thermal_anomaly_response.text)
data = subset[2]['subset'][0]['data']
means[2] = mean(data)
# ndvi_response.text

print(means[0])
print(means[1])
print(means[2])
sys.stdout.flush()
