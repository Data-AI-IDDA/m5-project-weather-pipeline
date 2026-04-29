# Topic: Azerbaijan Cotton Yield & Risk Prediction 
 
## Problem Definition

This project integrates 25 years of historical weather data (2000–2024) with district-level cotton production records to build an explainable prediction system. Low yield predictions are linked to specific agronomic risks across four biological growth stages: planting, growing, boll forming, and harvest. 

### Why it matters 

This matters because it replaces guesswork with data-driven planning for cotton production. By predicting yield across districts, stakeholders can better plan supply, logistics, and exports. The risk estimates highlight vulnerable growth stages, allowing early preventive actions. Overall, it helps reduce losses and improve decision-making. 

# Risk Masters

## Team Division & Daily Schedule

### Roles and Responsibilities 

| Task | Member 1 (Ahmadova Esli) | Member 2 (Dirayeva Narmin) | Member 3 (Gasimova Khaver) | Member 4 (Aliyeva Ulviyye) |
|---|---|---|---|---|
| **Role** | Data Engineer | Agro-Analyst & Feature Engineer | ML Engineer | Data Analyst & Visualizer |
| **Files** | `config.py` `ingestion.py` `cleaning.py` | `features.py` | `quality_checks.py` `models.py` | `reports.py` |
| **Task 1** | Project setup & folder structure | Define growth stage windows | Run pre-modelling quality checks | EDA — heatmaps & scatter plots |
| **Task 2** | Fetch 25 years weather data via API | Calculate GDD (base 15.5°C) | Train 4 risk classifiers (one per stage) | Regional yield comparisons |
| **Task 3** | Reshape cotton data wide → long | Compute heat stress, frost, dry streak days | Train yield regressor (XGBoost/Ridge) | Generate 2025 prediction dashboard |
| **Task 4** | Clean nulls, outliers, align datasets | Build risk labels (0/1) and risk scores (0–100%) | Evaluate models (MAE, RMSE, R²) & save via joblib | Export CSV report & write final documentation |
| **Notebooks** | `day_01` `day_02` `day_03` `day_05` | `day_04` `day_07` | `day_08` | `day_06` | 

### Project Timeline (10-Day Plan)

The project follows a structured 10-day roadmap to ensure internal readiness:

| Day | Date | Brief | Focus |
|-----|------|-------|-------|
| 1 | 20 Apr | Kick-Off | Repo setup, API exploration, and project planning |
| 2 | 21 Apr | Data Ingestion | Building the ingestion module and fetching 24 years of historical data |
| 3 | 22 Apr | Database Design | Schema design and data validation queries |
| 4 | 23 Apr | Feature Engineering | Cleaning pipeline and transforming weather data into agro-features |
| 5 | 24 Apr | Automation | Orchestration, incremental loading, and quality gates |
| 6 | 27 Apr | EDA | Descriptive statistics and cross-city comparisons |
| 7 | 28 Apr | Statistical Analysis | Hypothesis testing and final feature selection |
| 8 | 29 Apr | Modeling | Training and evaluating 5 total models |
| 9 | 30 Apr | Dress Rehearsal | Full timed run-through and feedback loop |
| 10 | 01 May | Internal Readiness | Repo freeze and generation of the final PDF report |

### Additional information; 

## 2. Data Sources

Source 1 — Cotton Production Dataset  

- 29 districts × 25 years (2000–2024) = 725 observations
- Values are annual cotton yield in tonnes per district
- Had 191 missing values and we deleted all districts with at least one missing value, and there are 15 districts left. 


Source 2 — Open-Meteo Historical Weather API 

- We pulled daily weather for 5 weather station locations across Azerbaijan: Ganja, Sabirabad, Lankaran, Shamkir, Nakhchivan
- Variables collected: max/min/mean temperature, precipitation, humidity, wind speed, evapotranspiration (ET0)
- 25 years × 365 days × 5 locations = ~45,000 daily rows 