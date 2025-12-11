import pandas as pd
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# -------------------------
# 1. Load and prepare data
# -------------------------

# Adjust the path if your file is in a different folder
df = pd.read_csv("data/formatted_sales_data.csv")

# Ensure Date is a proper datetime and sort
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

# -------------------------
# 2. Build Dash app
# -------------------------

app = Dash(__name__)
app.title = "Soul Foods Pink Morsel Sales"

# Region options for dropdown (plus 'All')
region_options = [{"label": "All Regions", "value": "ALL"}]
region_options += [
    {"label": region.title(), "value": region}
    for region in sorted(df["Region"].unique())
]

app.layout = html.Div(
    children=[
        # Header
        html.H1(
            "Soul Foods Pink Morsel Sales Visualiser",
            style={"textAlign": "center", "marginBottom": "20px"},
        ),

        # Region filter
        html.Div(
            [
                html.Label("Filter by Region:"),
                dcc.Dropdown(
                    id="region-dropdown",
                    options=region_options,
                    value="ALL",  # default: all regions combined
                    clearable=False,
                    style={"width": "300px"},
                ),
            ],
            style={"display": "flex", "justifyContent": "center", "marginBottom": "20px"},
        ),

        # Line chart
        dcc.Graph(id="sales-line-chart"),
    ],
    style={"fontFamily": "Arial, sans-serif", "margin": "40px"},
)

# -------------------------
# 3. Callbacks
# -------------------------

@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-dropdown", "value"),
)
def update_sales_chart(selected_region):
    # Filter by region if needed
    if selected_region == "ALL":
        filtered_df = df.copy()
        title_suffix = " (All Regions)"
    else:
        filtered_df = df[df["Region"] == selected_region]
        title_suffix = f" ({selected_region.title()})"

    # Aggregate sales by day
    daily_sales = (
        filtered_df.groupby("Date", as_index=False)["Sales"]
        .sum()
        .sort_values("Date")
    )

    # Create line chart
    fig = px.line(
        daily_sales,
        x="Date",
        y="Sales",
        title=f"Daily Pink Morsel Sales{title_suffix}",
        labels={"Date": "Date", "Sales": "Sales (Quantity × Price)"},
    )

    # Add a vertical line to highlight the price change date
    price_change_date = pd.to_datetime("2021-01-15")
    fig.add_vline(
        x=price_change_date,
        line_dash="dash",
        annotation_text="Price Increase (15 Jan 2021)",
        annotation_position="top left",
    )

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Total Sales",
        hovermode="x unified",
    )

    return fig

# -------------------------
# 4. Run the app
# -------------------------

if __name__ == "__main__":
    app.run_server(debug=True)
