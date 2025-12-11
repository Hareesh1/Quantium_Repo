import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# -------------------------
# 1. Load and prepare data
# -------------------------

# Adjust path if your file lives somewhere else
df = pd.read_csv("data/formatted_sales_data.csv")

# Ensure Date is datetime and sort
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

# For safety: normalize region case to lowercase
df["Region"] = df["Region"].str.lower()

# -------------------------
# 2. Build Dash app
# -------------------------

app = Dash(__name__)
app.title = "Soul Foods Pink Morsel Sales"

app.layout = html.Div(
    style={
        "backgroundColor": "#0f172a",      # dark blue background
        "color": "#e5e7eb",                # light text
        "minHeight": "100vh",
        "padding": "30px",
        "fontFamily": "Segoe UI, sans-serif",
    },
    children=[
        # Header
        html.Div(
            style={
                "textAlign": "center",
                "marginBottom": "30px",
            },
            children=[
                html.H1(
                    "Soul Foods – Pink Morsel Sales Dashboard",
                    style={
                        "fontSize": "32px",
                        "marginBottom": "10px",
                        "letterSpacing": "0.05em",
                    },
                ),
                html.P(
                    "Explore how Pink Morsel sales changed around the January 15, 2021 price increase.",
                    style={"fontSize": "16px", "color": "#cbd5f5"},
                ),
            ],
        ),

        # Main content card
        html.Div(
            style={
                "maxWidth": "1000px",
                "margin": "0 auto",
                "backgroundColor": "#111827",
                "borderRadius": "16px",
                "padding": "24px 28px 32px 28px",
                "boxShadow": "0 15px 35px rgba(0,0,0,0.45)",
                "border": "1px solid #1f2937",
            },
            children=[
                # Region radio buttons
                html.Div(
                    style={
                        "display": "flex",
                        "justifyContent": "space-between",
                        "alignItems": "center",
                        "marginBottom": "20px",
                        "flexWrap": "wrap",
                        "rowGap": "10px",
                    },
                    children=[
                        html.Div(
                            children=[
                                html.Label(
                                    "Region Filter",
                                    style={
                                        "fontWeight": "600",
                                        "fontSize": "14px",
                                        "textTransform": "uppercase",
                                        "color": "#9ca3af",
                                    },
                                ),
                                html.P(
                                    "Use the radio buttons to focus on a single region or view all.",
                                    style={"fontSize": "12px", "color": "#6b7280", "marginTop": "4px"},
                                ),
                            ]
                        ),
                        dcc.RadioItems(
                            id="region-radio",
                            options=[
                                {"label": "All", "value": "all"},
                                {"label": "North", "value": "north"},
                                {"label": "East", "value": "east"},
                                {"label": "South", "value": "south"},
                                {"label": "West", "value": "west"},
                            ],
                            value="all",
                            inline=True,
                            style={
                                "display": "flex",
                                "gap": "18px",
                                "alignItems": "center",
                                "fontSize": "14px",
                            },
                            labelStyle={
                                "display": "flex",
                                "alignItems": "center",
                                "cursor": "pointer",
                            },
                        ),
                    ],
                ),

                html.Hr(style={"borderColor": "#374151", "margin": "12px 0 20px 0"}),

                # Line chart
                dcc.Graph(
                    id="sales-line-chart",
                    style={"height": "500px"},
                    config={"displayModeBar": False},
                ),

                # Small legend / hint
                html.Div(
                    "Dashed line marks the Pink Morsel price increase on 15 Jan 2021.",
                    style={"fontSize": "12px", "color": "#9ca3af", "marginTop": "10px"},
                ),
            ],
        ),
    ],
)

# -------------------------
# 3. Callback
# -------------------------

@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-radio", "value"),
)
def update_sales_chart(selected_region):
    # Filter by region (or all)
    if selected_region == "all":
        filtered_df = df.copy()
        title_suffix = "All Regions"
    else:
        filtered_df = df[df["Region"] == selected_region]
        title_suffix = selected_region.capitalize()

    # Aggregate daily sales
    daily_sales = (
        filtered_df.groupby("Date", as_index=False)["Sales"]
        .sum()
        .sort_values("Date")
    )

    fig = px.line(
        daily_sales,
        x="Date",
        y="Sales",
        title=f"Daily Pink Morsel Sales – {title_suffix}",
        labels={"Date": "Date", "Sales": "Sales (Quantity × Price)"},
    )

    # Highlight the price change date
    price_change_date = pd.to_datetime("2021-01-15")
    fig.add_vline(
        x=price_change_date,
        line_dash="dash",
        line_width=2,
        annotation_text="Price Increase (15 Jan 2021)",
        annotation_position="top left",
    )

    # Styling for the chart itself
    fig.update_layout(
        plot_bgcolor="#020617",
        paper_bgcolor="#111827",
        font=dict(color="#e5e7eb"),
        xaxis=dict(
            title="Date",
            gridcolor="#1f2937",
            showgrid=True,
        ),
        yaxis=dict(
            title="Total Sales",
            gridcolor="#1f2937",
            showgrid=True,
        ),
        margin=dict(l=40, r=20, t=60, b=40),
        hovermode="x unified",
    )

    fig.update_traces(mode="lines+markers")

    return fig

# -------------------------
# 4. Run app
# -------------------------

if __name__ == "__main__":
    app.run_server(debug=True)
