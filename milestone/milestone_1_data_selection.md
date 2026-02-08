# 📊 Milestone 1: Data Selection & Collection

## Objective
Acquire and prepare high-quality visa application data for training predictive models.

## Dataset Overview

### Data Sources
1. **USCIS H-1B Disclosure Data** - Historical visa application records
2. **Department of State Wait Time Data** - Consulate processing times
3. **Synthetic Augmentation** - Generated data to balance edge cases

### Key Features Collected

| Category | Features |
|----------|----------|
| **Applicant** | Nationality, Education Level, Prior Travel History |
| **Employer** | Industry, Company Size, Wage Level, NAICS Code |
| **Application** | Visa Type (H-1B, L-1, O-1), Filing Date, Premium Processing |
| **Processing** | Service Center, Consulate Location, Case Status |

### Dataset Statistics
- **Total Records**: 50,000+ visa applications
- **Time Period**: 2018-2025
- **Visa Types**: H-1B, L-1A, L-1B, O-1, EB-1, EB-2, EB-3
- **Target Variables**: 
  - `status` (Approved, RFE, Denied)
  - `processing_days` (Time to decision)

## Data Quality Checks
- ✅ Missing value analysis completed
- ✅ Duplicate records removed
- ✅ Date format standardization
- ✅ Categorical encoding validated

## Deliverables
- [x] Raw dataset acquisition
- [x] Data schema definition
- [x] Initial data cleaning scripts
- [x] Data dictionary documentation
