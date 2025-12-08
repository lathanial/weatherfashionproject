import pandas as pd
import json
from pathlib import Path
from datetime import datetime

noaa_dir = Path("data/raw/noaa")
census_dir = Path("data/raw/census")
output_dir = Path("data/processed")
output_dir.mkdir(parents=True, exist_ok=True)

def get_season(month):
    if month in [12, 1, 2]:
        return 'Winter'
    elif month in [3, 4, 5]:
        return 'Spring'
    elif month in [6, 7, 8]:
        return 'Summer'
    else:
        return 'Fall'

print("loading weather data...")
all_weather = []

for json_file in noaa_dir.glob("*_weather.json"):
    city_name = json_file.stem.replace("_weather", "").replace("_", " ").title()
    
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    df = pd.DataFrame(data)
    df['city'] = city_name
    all_weather.append(df)

weather_df = pd.concat(all_weather, ignore_index=True)
weather_df['date'] = pd.to_datetime(weather_df['date'])
weather_df['year'] = weather_df['date'].dt.year
weather_df['month'] = weather_df['date'].dt.month
weather_df['season'] = weather_df['month'].map(get_season)

weather_pivot = weather_df.pivot_table(
    index=['city', 'date', 'year', 'month', 'season'],
    columns='datatype',
    values='value',
    aggfunc='first'
).reset_index()

print(f"loaded {len(weather_pivot)} weather records")

print("calculating weather anomalies...")
normals = weather_df.groupby(['city', 'month']).agg({
    'TMAX': 'mean',
    'TMIN': 'mean',
    'PRCP': 'mean'
}).reset_index()

normals.columns = ['city', 'month', 'TMAX_normal', 'TMIN_normal', 'PRCP_normal']

weather_with_normals = weather_pivot.merge(normals, on=['city', 'month'])
weather_with_normals['TMAX_anomaly'] = weather_with_normals['TMAX'] - weather_with_normals['TMAX_normal']
weather_with_normals['TMIN_anomaly'] = weather_with_normals['TMIN'] - weather_with_normals['TMIN_normal']
weather_with_normals['PRCP_anomaly'] = weather_with_normals['PRCP'] - weather_with_normals['PRCP_normal']

print("aggregating to monthly...")
monthly_weather = weather_with_normals.groupby(['city', 'year', 'month', 'season']).agg({
    'TMAX': ['mean', 'max', 'std'],
    'TMIN': ['mean', 'min', 'std'],
    'PRCP': 'sum',
    'SNOW': 'sum',
    'AWND': 'mean',
    'TMAX_anomaly': 'mean',
    'TMIN_anomaly': 'mean',
    'PRCP_anomaly': 'sum'
}).reset_index()

monthly_weather.columns = ['_'.join(col).strip('_') if col[1] else col[0] 
                           for col in monthly_weather.columns.values]

weather_output = output_dir / "weather_monthly.csv"
monthly_weather.to_csv(weather_output, index=False)
print(f"saved weather to {weather_output}")

print("loading retail data...")
monthly_file = census_dir / "monthly_retail_sales.csv"
annual_file = census_dir / "annual_retail_sales.csv"

dfs = []
if monthly_file.exists():
    monthly_df = pd.read_csv(monthly_file)
    monthly_df['frequency'] = 'monthly'
    dfs.append(monthly_df)

if annual_file.exists():
    annual_df = pd.read_csv(annual_file)
    annual_df['frequency'] = 'annual'
    dfs.append(annual_df)

if dfs:
    census_df = pd.concat(dfs, ignore_index=True)
    census_output = output_dir / "retail_sales.csv"
    census_df.to_csv(census_output, index=False)
    print(f"saved retail to {census_output}")

metadata = {
    "integration_date": datetime.now().isoformat(),
    "weather_records": len(monthly_weather),
    "retail_records": len(census_df) if dfs else 0,
    "cities": monthly_weather['city'].unique().tolist(),
    "date_range": {
        "start": int(monthly_weather['year'].min()),
        "end": int(monthly_weather['year'].max())
    }
}

metadata_file = output_dir / "integration_metadata.json"
with open(metadata_file, 'w') as f:
    json.dump(metadata, f, indent=2)

print(f"done! metadata saved to {metadata_file}")
