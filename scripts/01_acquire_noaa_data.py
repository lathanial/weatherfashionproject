import requests
import json
import hashlib
import time
from pathlib import Path
from datetime import datetime

noaa_api_token = "YOUR_NOAA_API_TOKEN_HERE"
base_url = "https://www.ncei.noaa.gov/cdo-web/api/v2"

metro_areas = {
    "New York": "CITY:US360019",
    "Los Angeles": "CITY:US060037",
    "Chicago": "CITY:US170031",
    "Houston": "CITY:US480029",
    "Phoenix": "CITY:US040013",
    "Philadelphia": "CITY:US420045",
    "San Antonio": "CITY:US480065",
    "San Diego": "CITY:US060073"
}

start_date = "2013-01-01"
end_date = "2022-12-31"
datatypes = ["TMAX", "TMIN", "PRCP", "SNOW", "AWND"]

output_dir = Path("data/raw/noaa")
output_dir.mkdir(parents=True, exist_ok=True)

def fetch_data(endpoint, params):
    url = f"{base_url}/{endpoint}"
    time.sleep(0.2)
    response = requests.get(url, headers={"token": noaa_api_token}, params=params)
    if response.status_code == 200:
        return response.json()
    return None

def collect_city_data(city_name, location_id):
    print(f"collecting {city_name}...")
    
    params = {
        "datasetid": "GHCND",
        "locationid": location_id,
        "startdate": start_date,
        "enddate": end_date,
        "datatypeid": ",".join(datatypes),
        "limit": 1000,
        "units": "metric"
    }
    
    all_results = []
    offset = 1
    
    while True:
        params["offset"] = offset
        data = fetch_data("data", params)
        
        if not data or "results" not in data:
            break
        
        all_results.extend(data["results"])
        
        if len(data["results"]) < 1000:
            break
        
        offset += 1000
        print(f"  got {len(all_results)} records")
    
    return all_results

def save_data(city_name, data):
    filename = f"{city_name.lower().replace(' ', '_')}_weather.json"
    filepath = output_dir / filename
    
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)
    
    sha256 = hashlib.sha256()
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    
    checksum_file = filepath.with_suffix('.json.sha256')
    with open(checksum_file, 'w') as f:
        f.write(f"{sha256.hexdigest()}  {filename}\n")
    
    print(f"  saved {filename}")
    return filepath

if __name__ == "__main__":
    if noaa_api_token == "YOUR_NOAA_API_TOKEN_HERE":
        print("need to set NOAA API token!")
        print("get one at: https://www.ncdc.noaa.gov/cdo-web/token")
    else:
        metadata = {
            "collection_date": datetime.now().isoformat(),
            "date_range": {"start": start_date, "end": end_date},
            "data_types": datatypes,
            "cities": {}
        }
        
        for city_name, location_id in metro_areas.items():
            data = collect_city_data(city_name, location_id)
            if data:
                filepath = save_data(city_name, data)
                metadata["cities"][city_name] = {
                    "location_id": location_id,
                    "records": len(data),
                    "file": str(filepath.name)
                }
        
        metadata_file = output_dir / "collection_metadata.json"
        with open(metadata_file, 'w') as f:
            json.dump(metadata, f, indent=2)
        
        print(f"\ndone! saved metadata to {metadata_file}")
