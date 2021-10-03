{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "d9cc66f9",
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "import json\n",
    "import datetime\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "url = \"https://modis.ornl.gov/rst/api/v1/\"\n",
    "header = {'Accept': 'application/json'}\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "79a8a2f3",
   "metadata": {},
   "outputs": [],
   "source": [
    "from datetime import datetime\n",
    "day_of_year = datetime.now().timetuple().tm_yday\n",
    "start_day = day_of_year - 60\n",
    "end_day = day_of_year\n",
    "year = datetime.today().year\n",
    "\n",
    "modis_start_date = f\"A{year}{start_day}\"\n",
    "modis_end_date = f\"A{year}{end_day}\"\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "711331f1",
   "metadata": {},
   "outputs": [],
   "source": [
    "lat = 39.56499 # Input latitude\n",
    "lon = -121.55527 # Input longitude\n",
    "prod = ['MOD13Q1','MOD11A2','MOD14A2'] # MODIS product for LST data, NDVI, Thermal anomalies\n",
    "data_band = ['250m_16_days_NDVI','LST_Day_1km','FireMask'] \n",
    "above_below = 10 # km above/below\n",
    "left_right = 10 # km left/right"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "69597f5a",
   "metadata": {},
   "outputs": [],
   "source": [
    "lst_response = requests.get(\"\".join([\n",
    "        url, prod[1], \"/subset?\",\n",
    "        \"latitude=\", str(lat),\n",
    "        \"&longitude=\", str(lon),\n",
    "        \"&band=\", data_band[1],\n",
    "        \"&startDate=\", modis_start_date,\n",
    "        \"&endDate=\", modis_end_date,\n",
    "        \"&kmAboveBelow=\", str(above_below),\n",
    "        \"&kmLeftRight=\", str(left_right)\n",
    "    ]), headers=header)\n",
    "\n",
    "ndvi_response = requests.get(\"\".join([\n",
    "        url, prod[0], \"/subset?\",\n",
    "        \"latitude=\", str(lat),\n",
    "        \"&longitude=\", str(lon),\n",
    "        \"&band=\", data_band[0],\n",
    "        \"&startDate=\", modis_start_date,\n",
    "        \"&endDate=\", modis_end_date,\n",
    "        \"&kmAboveBelow=\", str(above_below),\n",
    "        \"&kmLeftRight=\", str(left_right)\n",
    "    ]), headers=header)\n",
    "\n",
    "thermal_anomaly_response = requests.get(\"\".join([\n",
    "        url, prod[2], \"/subset?\",\n",
    "        \"latitude=\", str(lat),\n",
    "        \"&longitude=\", str(lon),\n",
    "        \"&band=\", data_band[2],\n",
    "        \"&startDate=\", modis_start_date,\n",
    "        \"&endDate=\", modis_end_date,\n",
    "        \"&kmAboveBelow=\", str(above_below),\n",
    "        \"&kmLeftRight=\", str(left_right)\n",
    "    ]), headers=header)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "1796fe2b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0.37608477366255144, 15574.321995464852, 4.918367346938775]\n"
     ]
    }
   ],
   "source": [
    "from statistics import mean\n",
    "subset= [0,0,0]\n",
    "means=[0,0,0]\n",
    "subset[0] = json.loads(ndvi_response.text)\n",
    "data = subset[0]['subset'][0]['data']\n",
    "means[0] = mean(data)*0.0001\n",
    "\n",
    "subset[1] = json.loads(lst_response.text)\n",
    "data = subset[1]['subset'][0]['data']\n",
    "means[1] = mean(data)\n",
    "\n",
    "subset[2] = json.loads(thermal_anomaly_response.text)\n",
    "data = subset[2]['subset'][0]['data']\n",
    "means[2] = mean(data)\n",
    "# ndvi_response.text\n",
    "\n",
    "print(means)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
