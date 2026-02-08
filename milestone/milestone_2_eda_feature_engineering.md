# 🔬 Milestone 2: EDA, Feature Engineering & Data Engineering

## Objective
Perform comprehensive exploratory data analysis and engineer features for optimal model performance.

## Exploratory Data Analysis (EDA)

### Distribution Analysis
- **Target Variable Distribution**:
  - Approved: 72.4%
  - RFE (Request for Evidence): 18.2%
  - Denied: 9.4%

### Key Insights Discovered
1. **Nationality Impact**: Approval rates vary significantly by country (60-85% range)
2. **Wage Level Correlation**: Higher wage levels strongly correlate with approval
3. **Premium Processing**: 15% faster processing, similar approval rates
4. **Seasonality**: Q1 filings have slightly higher RFE rates

### Visualizations Created
- Approval rate trends by visa type
- Processing time distributions
- Feature correlation heatmaps
- Geographic analysis by consulate

## Feature Engineering

### New Features Created

| Feature | Type | Description |
|---------|------|-------------|
| `wage_ratio` | Numerical | Offered wage / prevailing wage |
| `company_approval_history` | Numerical | Employer's historical approval rate |
| `consulate_load` | Numerical | Relative case volume at consulate |
| `days_since_filing` | Numerical | Application age |
| `is_stem` | Binary | STEM occupation classification |
| `education_score` | Ordinal | Encoded education level (1-5) |

### Encoding Strategies
- **Categorical**: Target encoding for high-cardinality features
- **Numerical**: StandardScaler for continuous variables
- **Temporal**: Cyclical encoding for date features

## Data Engineering Pipeline

```
Raw Data → Cleaning → Feature Engineering → Train/Val/Test Split → Model Ready
   │           │              │                    │
   └── Logs    └── Reports    └── Feature Store    └── Versioned Datasets
```

### Data Splits
- **Training**: 70% (35,000 records)
- **Validation**: 15% (7,500 records)
- **Test**: 15% (7,500 records)

## Deliverables
- [x] EDA notebook with visualizations
- [x] Feature engineering pipeline
- [x] Data preprocessing scripts
- [x] Feature importance analysis
