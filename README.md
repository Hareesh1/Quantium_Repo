# Soul Foods Pink Morsel Sales Dashboard

## Overview

This project provides an interactive Dash web application for exploring sales of Pink Morsels across different regions and dates. It also includes automated tests and a continuous integration workflow. The primary business goal is to determine whether Pink Morsel sales were higher before or after the price increase on January 15, 2021.

The project includes:

* Data cleaning and processing to generate a unified dataset
* A Dash application with a styled interface
* Region-based filtering using radio buttons
* A line chart visualising sales over time
* Automated testing with Pytest
* A GitHub Actions workflow to run tests automatically

---

## Data Processing

The original dataset consists of three CSV files containing daily sales data.
A preprocessing script was used to:

1. Filter the data to include only rows where the product is "pink morsel".
2. Convert prices to numeric values.
3. Compute the `Sales` field using `quantity × price`.
4. Retain only the fields: `Sales`, `Date`, and `Region`.

The cleaned and combined dataset is saved as:

```
formatted_sales_data.csv
```

---

## Dash Application

The Dash app displays an interactive dashboard that includes:

### Header

A clear title at the top of the page.

### Region Picker

A set of radio buttons that allow filtering by region:

```
all, north, east, south, west
```

### Line Chart

A time-series visualisation of daily Pink Morsel sales.
The chart includes:

* Chronological sorting
* A vertical marker indicating the price increase on 15 January 2021
* Custom CSS styling for a more polished layout

To run the application locally:

```bash
python app.py
```

Then open the browser at:

```
http://127.0.0.1:8050/
```

---

## Test Suite

The project includes a Pytest test suite (`test_app.py`) to verify that:

1. The header renders correctly
2. The line chart is present
3. The region picker is visible

Tests use Dash’s built-in `dash_duo` fixture.

Run tests with:

```bash
pytest -v
```

---

## Test Runner Script

A test automation script named `run_tests.sh` is included. It:

1. Activates the project’s virtual environment
2. Executes the Pytest suite
3. Returns exit code `0` if all tests pass, otherwise `1`

This makes it suitable for integration with CI tools.

Run it with:

```bash
./run_tests.sh
```

---

## Continuous Integration

A GitHub Actions workflow file is included at:

```
.github/workflows/test.yml
```

This workflow:

* Sets up Python
* Creates a virtual environment
* Installs dependencies
* Runs the test automation script
* Reports pass/fail status on every push and pull request

This ensures that the project remains stable as changes are introduced.

---

## Installation

Clone the repository and enter the project folder:

```bash
git clone <repository-url>
cd <project-directory>
```

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the Dash app:

```bash
python app.py
```

Open in a browser:

```
http://127.0.0.1:8050/
```

---

## Running Tests

Via Pytest:

```bash
pytest -v
```

Via the test script:

```bash
./run_tests.sh
```


