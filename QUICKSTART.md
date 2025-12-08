# Quick Start Guide

Get up and running with the Weather and Fashion Sales Analysis project in minutes!

## Prerequisites

- Python 3.11+
- NOAA API Token: https://www.ncdc.noaa.gov/cdo-web/token
- Census API Key: https://api.census.gov/data/key_signup.html

## 5-Minute Setup

### 1. Clone and Setup (2 minutes)

```bash
# Clone repository
git clone https://github.com/lynnpepin/weatherfashion.git
cd weatherfashion

# Create environment
conda env create -f environment.yaml
conda activate weatherfashion
```

### 2. Configure API Keys (1 minute)

Edit these files and add your credentials:
- `scripts/01_acquire_noaa_data.py` → Add NOAA_API_TOKEN
- `scripts/02_acquire_census_data.py` → Add CENSUS_API_KEY

### 3. Run Analysis (2 minutes to start, 15-30 minutes total)

**Option A - Full Automation**:
```bash
snakemake --cores 1
```

**Option B - Simple Script**:
```bash
./run_all.sh
```

**Option C - Using Pre-Collected Data**:
```bash
# Download from Box: [INSERT LINK]
# Extract to project directory
# Then run only analysis:
python scripts/06_analyze_visualize.py
```

## What You Get

After running, you'll have:

📊 **Visualizations** in `data/output/`:
- Temperature trends across cities
- Precipitation patterns
- Extreme weather events
- Correlation matrices
- Seasonal comparisons

📈 **Analysis Results**:
- Quality assessment reports
- Statistical summaries
- Cleaned datasets ready for further analysis

📝 **Documentation**:
- Complete data dictionary
- Quality assessment findings
- Reproducible workflow

## Viewing Results

```bash
# View analysis summary
cat data/output/analysis_summary.json | python -m json.tool

# View quality report
cat data/output/quality_summary.txt

# Open visualizations
open data/output/*.png  # macOS
xdg-open data/output/*.png  # Linux
```

## Common Commands

```bash
# Clean everything and start fresh
snakemake clean_all
./run_all.sh

# Run only data acquisition
python scripts/01_acquire_noaa_data.py
python scripts/02_acquire_census_data.py

# Run only analysis (after having data)
python scripts/06_analyze_visualize.py

# Check what would run
snakemake --dry-run

# See workflow diagram
snakemake --dag | dot -Tpng > workflow.png
```

## Troubleshooting

**Issue**: Module not found
```bash
pip install -r requirements.txt
```

**Issue**: API rate limit
- Wait 1 hour and retry
- NOAA allows 5 requests/second

**Issue**: Permission denied on scripts
```bash
chmod +x run_all.sh
```

## Next Steps

1. 📖 Read the full [README.md](README.md)
2. 📊 Explore outputs in `data/output/`
3. 📚 Check the [Data Dictionary](docs/DATA_DICTIONARY.md)
4. 🔧 Customize parameters in `config.yaml`
5. 📦 Upload your data to Box for sharing

## Getting Help

- 📋 Review [SUBMISSION_CHECKLIST.md](SUBMISSION_CHECKLIST.md)
- 🔧 See [docs/SETUP.md](docs/SETUP.md) for detailed setup
- 📁 Check [docs/PROJECT_STRUCTURE.md](docs/PROJECT_STRUCTURE.md) for organization
- 🐛 Open an issue on GitHub

## Project Structure at a Glance

```
weatherfashion/
├── scripts/          # 6 numbered analysis scripts
├── data/            # Raw, processed, and output data (in .gitignore)
├── docs/            # Documentation
├── README.md        # Main documentation
├── Snakefile        # Workflow automation
└── run_all.sh       # Simple execution script
```

## Time Estimates

| Task | Time |
|------|------|
| Setup environment | 2-3 minutes |
| Configure API keys | 1 minute |
| Data acquisition | 10-20 minutes |
| Data processing | 5-10 minutes |
| Analysis | 2-3 minutes |
| **Total** | **15-35 minutes** |

## Success Indicators

✅ No errors during execution  
✅ All 8 PNG visualizations created  
✅ Quality reports generated  
✅ Analysis summary contains findings  
✅ Cleaned datasets in `data/processed/cleaned/`

---

**Ready to dive deeper?** Check out the full [README.md](README.md) for comprehensive documentation!
