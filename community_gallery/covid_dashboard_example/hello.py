from preswald import text, table, plotly, connect, get_df, slider
import pandas as pd
import plotly.express as px

# Display Title
text("# COVID-19 Data Analysis ")
text("An interactive dashboard exploring COVID-19 trends worldwide.")

# Load a small dataset (less than 2MB)
data_url = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/latest/owid-covid-latest.csv"

def load_data():
    return pd.read_csv(data_url)

df = load_data()

# Check if the dataset loaded properly
if df.empty:
    text("⚠️ Error loading data. Please check the data source.")
else:
    text("Covid Data Loaded Successfully!")
    table(df.head(10), title="Sample COVID-19 Data")

    # Ensure required columns exist
    if "total_cases" not in df.columns or "new_cases" not in df.columns:
        text("⚠️ Missing required columns: `total_cases` or `new_cases`. Check your dataset!")
    else:
        # Slider to filter by total cases
        min_cases = slider(
            "Filter by Total Cases",
            min_val=int(df["total_cases"].min(skipna=True) or 0),
            max_val=int(df["total_cases"].max(skipna=True) or 100000),
            default=10000
        )

        # Apply filter
        filtered_df = df[df["total_cases"] > min_cases]

        # Display filtered data
        table(filtered_df.head(10), title="Filtered COVID-19 Data")

        # Create an interactive scatter plot
        fig = px.scatter(
            filtered_df, x="total_cases", y="new_cases", color="continent",
            hover_name="location", title="New Cases vs. Total Cases"
        )

        # Show the plot
        plotly(fig)
