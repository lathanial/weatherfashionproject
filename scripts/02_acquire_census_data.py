import requests
import pandas as pd
import hashlib
import json
from pathlib import Path
from datetime import datetime

census_api_key = "b07bcbfd7c9865cded1e35b6f99fbecfeffec438"
base_url = "https://api.census.gov/data"

naics_codes = {
    "4481": "Clothing Stores",
    "44811": "Men's Clothing Stores",
    "44812": "Women's Clothing Stores", 
    "44813": "Children's Clothing Stores",
    "44814": "Family Clothing Stores",
    "44815": "Clothing Accessories Stores",
    "4482": "Shoe Stores",
    "4483": "Jewelry and Luggage Stores"
}

start_year = 2013
end_year = 2022

output_dir = Path("data/raw/census")
output_dir.mkdir(parents=True, exist_ok=True)

def fetch_mrts_data(year):
    print(f"fetching retail sales for {year}...")
    
    url = f"{base_url}/{year}/marts/monthly"
    params = {
        "get": "NAICS,NAICS_TTL,PER,PER_TTL,MRTSSALES",
        "for": "us:*",
        "NAICS": "4481,44811,44812,44813,44814,44815,4482,4483",
        "key": census_api_key
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        
        if len(data) > 1:
            df = pd.DataFrame(data[1:], columns=data[0])
            print(f"  got {len(df)} records")
            return df
        return None
    except:
        print(f"  failed for {year}")
        return None

def fetch_annual_retail_trade(year):
    print(f"fetching annual retail for {year}...")
    
    url = f"{base_url}/{year}/arts/state"
    state_codes = ["36", "06", "17", "48", "04", "42"]
    
    params = {
        "get": "NAICS2017,NAICS2017_TTL,ESTAB,RCPTOT,PAYANN",
        "for": f"state:{','.join(state_codes)}",
        "NAICS2017": "4481",
        "key": census_api_key
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        
        if len(data) > 1:
            df = pd.DataFrame(data[1:], columns=data[0])
            print(f"  got {len(df)} records")
            return df
        return None
    except:
        print(f"  failed for {year}")
        return None

def save_data(name, df):
    filename = f"{name}.csv"
    filepath = output_dir / filename
    
    df.to_csv(filepath, index=False)
    print(f"  saved {filename}")
    
    sha256 = hashlib.sha256()
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    
    checksum_file = filepath.with_suffix('.csv.sha256')
    with open(checksum_file, 'w') as f:
        f.write(f"{sha256.hexdigest()}  {filename}\n")
    
    return filepath

if __name__ == "__main__":
    if census_api_key == "YOUR_CENSUS_API_KEY_HERE":
        print("need to set Census API key!")
        print("get one at: https://api.census.gov/data/key_signup.html")
    else:
        all_monthly = []
        all_annual = []
        
        for year in range(start_year, end_year + 1):
            monthly_df = fetch_mrts_data(year)
            if monthly_df is not None:
                monthly_df['year'] = year
                all_monthly.append(monthly_df)
            
            annual_df = fetch_annual_retail_trade(year)
            if annual_df is not None:
                annual_df['year'] = year
                all_annual.append(annual_df)
        
        if all_monthly:
            monthly_combined = pd.concat(all_monthly, ignore_index=True)
            save_data("monthly_retail_sales", monthly_combined)
        
        if all_annual:
            annual_combined = pd.concat(all_annual, ignore_index=True)
            save_data("annual_retail_sales", annual_combined)
        
        metadata = {
            "collection_date": datetime.now().isoformat(),
            "date_range": {"start": start_year, "end": end_year},
            "naics_codes": naics_codes,
            "monthly_records": len(monthly_combined) if all_monthly else 0,
            "annual_records": len(annual_combined) if all_annual else 0
        }
        
        metadata_file = output_dir / "collection_metadata.json"
        with open(metadata_file, 'w') as f:
            json.dump(metadata, f, indent=2)
        
        print(f"\ndone! saved metadata to {metadata_file}")
