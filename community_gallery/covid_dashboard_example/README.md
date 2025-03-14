# COVID-19 Dashboard Example

## 📌 Overview
This interactive dashboard analyzes **COVID-19 trends worldwide** using data from the **OWID COVID-19 Dataset**.

## 📊 Features
- Filters COVID-19 cases using a **slider**.
- Displays **tables** of COVID-19 data.
- Generates **interactive scatter plots** using **Plotly**.

## 📂 Folder Structure
community_gallery/covid_dashboard_example/ ├── hello.py # The Preswald script ├── data/ │ ├── owid-covid-latest.csv # Local dataset (less than 2MB) ├── README.md # Documentation

## [LIVE LINK](https://my-project-287626-49ciiygs-ndjz2ws6la-ue.a.run.app)

##  Dataset Source
- [OWID COVID-19 Data](https://github.com/owid/covid-19-data)
-[link](https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/latest/owid-covid-latest.csv)

## 🚀 How to Run Locally
```bash
# Navigate to the project directory
cd community_gallery/covid_dashboard_example/

# Run with Preswald
preswald run hello.py

```

## Deployment
To deploy on Preswald, run:
```bash
preswald deploy --target structured --github <your_github_username> --api-key <your_api_key> hello.py

