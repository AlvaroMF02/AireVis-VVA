import cdsapi

dataset = "cams-europe-air-quality-forecasts"
request = {
    "variable": [
        "carbon_monoxide",
        "nitrogen_monoxide",
        "ozone",
        "particulate_matter_2.5um",
        "pm2.5_ammonium",
        "pm2.5_nitrate",
        "secondary_inorganic_aerosol",
        "pm2.5_sulphate",
        "pm2.5_total_organic_matter",
        "particulate_matter_10um",
        "sulphur_dioxide"
    ],
    "model": ["ensemble"],
    "level": ["0"],
    "date": ["2025-07-01/2025-07-19"],
    "type": ["analysis"],
    "time": [
        "00:00", "06:00", "07:00",
        "08:00", "10:00", "12:00",
        "13:00", "14:00", "16:00",
        "18:00", "20:00", "21:00",
        "22:00", "23:00"
    ],
    "leadtime_hour": ["0"],
    "data_format": "netcdf_zip",
    "area": [38.3, -3, 38, -2.6]
}

client = cdsapi.Client()
client.retrieve(dataset, request).download()
