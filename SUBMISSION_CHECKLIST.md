# Final Project Submission Checklist

Use this checklist to ensure your project meets all IS477 requirements before submission.

## Pre-Submission Requirements

### ✅ Repository Setup

- [ ] GitHub repository created and accessible
- [ ] All team members added as collaborators (if applicable)
- [ ] Clear Git commit history showing contributions
- [ ] Repository is public or instructor has access
- [ ] .gitignore properly configured to exclude data files

### ✅ API Configuration

- [ ] NOAA API token obtained and configured
- [ ] Census API key obtained and configured
- [ ] API keys tested and working
- [ ] API keys removed from code before committing
- [ ] Instructions for adding API keys included in documentation

### ✅ Data Acquisition and Storage

- [ ] Data successfully acquired from both sources
- [ ] Checksums generated for all data files
- [ ] Data organized in proper directory structure
- [ ] Box folder created and data uploaded
- [ ] Box sharing link generated and tested
- [ ] Box link added to README.md

### ✅ Code and Scripts

- [ ] All 6 analysis scripts created and functional
- [ ] Scripts follow numbered naming convention
- [ ] Each script has logging capability
- [ ] Error handling implemented
- [ ] Code is well-commented
- [ ] No hardcoded paths (uses relative paths)

### ✅ Workflow Automation

- [ ] Snakefile created and tested
- [ ] All rules execute successfully
- [ ] run_all.sh script created and tested
- [ ] Workflow can be executed end-to-end
- [ ] Logs generated for each step

### ✅ Documentation - README.md

Required sections (all present and complete):

- [ ] **Title**: Project title clearly stated
- [ ] **Contributors**: Names with ORCIDs (if available)
- [ ] **Summary** (500-1000 words):
  - [ ] Overview of project
  - [ ] Research questions
  - [ ] Motivation
  - [ ] Key findings
- [ ] **Data Profile** (500-1000 words):
  - [ ] Description of each dataset
  - [ ] Ethical/legal constraints documented
  - [ ] Licenses and terms of use specified
  - [ ] Privacy considerations addressed
- [ ] **Data Quality** (500-1000 words):
  - [ ] Quality assessment methodology
  - [ ] Findings for each dataset
  - [ ] Cleaning actions documented
- [ ] **Findings** (~500 words):
  - [ ] Numeric results presented
  - [ ] Visualizations included/referenced
- [ ] **Future Work** (~500-1000 words):
  - [ ] Lessons learned
  - [ ] Potential extensions
- [ ] **Reproducing**:
  - [ ] Step-by-step instructions
  - [ ] Prerequisites listed
  - [ ] Expected runtime documented
  - [ ] Troubleshooting guidance
- [ ] **References**:
  - [ ] All datasets cited properly
  - [ ] All software cited
  - [ ] Formatted citations

### ✅ Data Documentation

- [ ] Data dictionary created (DATA_DICTIONARY.md)
- [ ] All variables defined
- [ ] Units specified for numeric variables
- [ ] Value ranges documented
- [ ] Missing value handling explained
- [ ] Data provenance documented

### ✅ Metadata

- [ ] metadata.json created
- [ ] Schema.org format used
- [ ] All required fields populated
- [ ] DOI placeholder added (update after Zenodo)
- [ ] Keywords comprehensive
- [ ] Spatial/temporal coverage specified

### ✅ Data Quality Artifacts

- [ ] Quality assessment script functional
- [ ] quality_assessment_report.json generated
- [ ] quality_summary.txt generated
- [ ] Completeness metrics calculated
- [ ] Consistency checks performed
- [ ] Accuracy assessment (outliers) completed
- [ ] Validity checks executed

### ✅ Data Cleaning Artifacts

- [ ] Cleaning script functional
- [ ] Cleaned datasets generated
- [ ] cleaning_log.json created
- [ ] All transformations documented
- [ ] Missing value strategy implemented
- [ ] Outlier handling strategy implemented

### ✅ Analysis and Visualization

- [ ] Analysis script functional
- [ ] All required visualizations generated:
  - [ ] temperature_analysis.png
  - [ ] precipitation_analysis.png
  - [ ] extreme_weather_analysis.png
  - [ ] correlation_matrix.png
  - [ ] seasonal_comparison.png
- [ ] analysis_summary.json generated
- [ ] Findings documented in README

### ✅ Reproducibility

- [ ] requirements.txt created with pinned versions
- [ ] environment.yaml created
- [ ] pip freeze output captured
- [ ] All dependencies documented
- [ ] Workflow can be reproduced from scratch
- [ ] Expected outputs match actual outputs
- [ ] Reproduction instructions tested

### ✅ Licensing

- [ ] LICENSE file created (MIT for code)
- [ ] Code license specified in README
- [ ] Data license documented
- [ ] Documentation license specified (CC BY 4.0)
- [ ] CITATION.cff file created
- [ ] Citation format provided in README

### ✅ Compliance and Ethics

- [ ] Terms of use respected for all data sources
- [ ] Attribution requirements met
- [ ] Privacy considerations addressed
- [ ] No PII in datasets
- [ ] Consent requirements satisfied (N/A for government data)
- [ ] Copyright respected
- [ ] Licenses compatible

### ✅ Module Coverage

Module requirements addressed:

- [ ] **Module 1 - Data Lifecycle**: Lifecycle model discussed in README
- [ ] **Module 2 - Ethics**: Ethical constraints documented
- [ ] **Module 3 - Acquisition**: 2+ datasets from distinct sources
- [ ] **Module 4-5 - Storage**: Storage strategy documented
- [ ] **Module 6 - Extraction**: Data extraction implemented
- [ ] **Module 7-8 - Integration**: Datasets integrated
- [ ] **Module 9 - Quality**: Quality assessment performed
- [ ] **Module 10 - Cleaning**: Cleaning methods applied
- [ ] **Module 11-12 - Workflow**: Automated workflow provided
- [ ] **Module 13 - Reproducibility**: Reproducible package created
- [ ] **Module 15 - Metadata**: Metadata provided

## Submission Process

### 1. Final Code Review

- [ ] All scripts execute without errors
- [ ] No API keys in committed code
- [ ] Comments are clear and helpful
- [ ] Variable names are descriptive
- [ ] Code follows consistent style

### 2. Final Testing

- [ ] Clean environment test:
  ```bash
  rm -rf data/ logs/
  ./run_all.sh
  ```
- [ ] Verify all outputs generated
- [ ] Check Box link accessibility
- [ ] Test reproduction instructions

### 3. Create Release

```bash
# Ensure all changes committed
git add .
git commit -m "Final project submission"
git push origin main

# Create tag
git tag -a final-project -m "Final project submission for IS477 FA25"
git push origin final-project

# Create GitHub release
# Go to GitHub > Releases > Create new release
# Select "final-project" tag
# Add release notes
# Publish release
```

- [ ] Git tag created: `final-project`
- [ ] All files committed and pushed
- [ ] GitHub release created
- [ ] Release notes added
- [ ] Release URL obtained

### 4. Box Data Sharing

- [ ] All required data uploaded to Box
- [ ] Folder structure matches project structure
- [ ] Sharing link created
- [ ] Link tested (accessible to TAs)
- [ ] Link added to README.md
- [ ] Data paths documented for where to extract

### 5. Canvas Submission

- [ ] GitHub release URL submitted to Canvas
- [ ] Submission made before deadline
- [ ] Correct Canvas assignment selected

### 6. Optional: Zenodo Archival (FAIR bonus points)

- [ ] Zenodo account created
- [ ] Project uploaded to Zenodo
- [ ] DOI obtained
- [ ] DOI added to README.md
- [ ] DOI added to metadata.json
- [ ] DOI added to CITATION.cff

## Grading Criteria Review

### Reproducibility (20 points)

- [ ] Complete workflow can be reproduced
- [ ] Clear documentation of all steps
- [ ] Dependencies properly specified
- [ ] Data acquisition documented
- [ ] Expected vs. actual outputs verified

### Transparency (20 points)

- [ ] Artifacts for each workflow step
- [ ] Data acquisition scripts
- [ ] Integration documentation
- [ ] Quality assessment results
- [ ] Cleaning documentation
- [ ] Analysis code
- [ ] Workflow automation

### Compliance (10 points)

- [ ] All licenses respected
- [ ] Terms of use followed
- [ ] Attribution provided
- [ ] Ethical requirements met

### Citation (10 points)

- [ ] All data sources cited
- [ ] All software cited
- [ ] Proper citation format
- [ ] CITATION.cff provided

### FAIR (10 points)

- [ ] Findable: GitHub + optional Zenodo
- [ ] Accessible: Public repository + Box sharing
- [ ] Interoperable: Standard formats (CSV, JSON)
- [ ] Reusable: Clear license + documentation

### Documentation (10 points)

- [ ] README complete
- [ ] Data dictionary provided
- [ ] Setup instructions clear
- [ ] Reproduction steps documented
- [ ] All manual steps described

### Quality (20 points)

- [ ] Well-organized repository
- [ ] Clear file naming
- [ ] No unnecessary artifacts
- [ ] Complete and well-written report
- [ ] Professional presentation

## Pre-Submission Verification

Run this final check before submitting:

```bash
# 1. Clean environment
rm -rf data/ logs/ .snakemake/

# 2. Run complete workflow
./run_all.sh

# 3. Verify outputs
ls data/output/

# Expected files:
# - quality_assessment_report.json
# - quality_summary.txt
# - analysis_summary.json
# - temperature_analysis.png
# - precipitation_analysis.png
# - extreme_weather_analysis.png
# - correlation_matrix.png
# - seasonal_comparison.png

# 4. Check Box link
# Open Box link in incognito/private browser
# Verify data is accessible

# 5. Create release
git tag -a final-project -m "Final submission"
git push origin final-project
```

## Common Issues to Avoid

- [ ] ❌ API keys in committed code
- [ ] ❌ Data files in Git repository
- [ ] ❌ Hardcoded absolute paths
- [ ] ❌ Missing Box link in README
- [ ] ❌ Inaccessible Box folder
- [ ] ❌ Missing required sections in README
- [ ] ❌ No contribution statement (for teams)
- [ ] ❌ Unclear reproduction instructions
- [ ] ❌ Missing citations
- [ ] ❌ No software dependencies listed

## Final Submission Details

**Project Title**: Weather Patterns and Seasonal Fashion Sales

**Submission Date**: December 10, 2025

**GitHub Release Tag**: final-project

**GitHub Release URL**: https://github.com/lynnpepin/weatherfashion/releases/tag/final-project

**Box Data Link**: [INSERT YOUR BOX LINK HERE]

**Zenodo DOI** (optional): 10.5281/zenodo.XXXXXXX

---

## Completion Sign-off

I confirm that:

- [ ] All checklist items above are completed
- [ ] The project meets all IS477 requirements
- [ ] All data sources are properly cited and licensed
- [ ] The workflow is fully reproducible
- [ ] Documentation is complete and accurate
- [ ] Code is clean, commented, and functional

**Submitted by**: Lynn  
**Date**: December 7, 2025  
**Course**: IS477 Fall 2025
