Soul Foods Pink Morsel Sales Dashboard
A Dash Data Visualisation, Automated Testing, and Continuous Integration Project

Project Overview
This project delivers an interactive Dash web application that allows Soul Foods to analyse sales of Pink Morsels across different regions and over time. The primary business objective is to answer the question:

“Were Pink Morsel sales higher before or after the price increase on January 15th, 2021?”

Using the provided sales data, the project:

Extracts only "Pink Morsel" records.

Calculates total sales using Sales = Quantity × Price.

Produces a combined, cleaned CSV file.

Displays sales trends in a line chart.

Allows region-level filtering using a radio button.

Highlights the price increase date for comparison.

The project also incorporates:

Automated testing with Pytest and Dash's testing utilities.

A GitHub Actions continuous integration pipeline.

A portable test runner script for CI engines.

Data Processing
The original dataset consists of three CSV files representing daily sales records. The preprocessing script:

Filters rows for the product "pink morsel".

Converts the price column to numeric values.

Computes the total Sales column.

Retains only the fields: Sales, Date, and Region.

The cleaned dataset is written to:

Plaintext

formatted_sales_data.csv
Dash Application
The application includes the following components:

1. Header
A title describing the dashboard and its purpose.

2. Line Chart
A time series plot of daily Pink Morsel sales, sorted by date.

The chart includes a vertical dashed line representing the price increase on 15 January 2021.

3. Region Picker
A radio button that allows filtering by:

all

north

east

south

west

4. Custom Styling
The UI uses custom CSS to improve layout, spacing, and visual appeal. This includes styled containers, a dark theme, and enhanced readability.

Run the application locally using:

Bash

python app.py
The app will be hosted at: http://127.0.0.1:8050/

Testing
A test suite (test_app.py) validates the core components of the Dash application. The suite checks that:

The header is rendered.

The line chart element is present.

The region picker (radio buttons) appears in the layout.

All tests are written using Pytest and Dash’s dash_duo testing fixture.

Run tests locally with:

Bash

pytest -v
Continuous Integration (GitHub Actions)
A CI workflow is provided at .github/workflows/test.yml.

The workflow performs the following:

Checks out the repository.

Sets up Python.

Creates a virtual environment.

Installs all dependencies including testing tools.

Runs the test runner script (run_tests.sh).

Passes or fails the workflow based on test results.

This ensures that every commit and pull request is automatically validated.

Test Runner Script
The file run_tests.sh is used for both local and CI-based test execution. It:

Activates the virtual environment.

Executes the Pytest suite.

Returns exit code 0 if all tests pass.

Returns exit code 1 if any test fails.

This makes the project CI-compatible and portable.

Installation Instructions
1. Clone the repository
Bash

git clone <your-repo-url>
cd <project-directory>
2. Create and activate a virtual environment
Bash

python -m venv venv
source venv/bin/activate
# On Windows use: venv\Scripts\activate
3. Install dependencies
Bash

pip install -r requirements.txt
Usage
Running the Visualiser
Bash

python app.py
Then open the browser at: http://127.0.0.1:8050/

Running Tests
Via Pytest:

Bash

pytest -v
Via the test script:

Bash

./run_tests.sh
Continuous Integration
All tests run automatically on GitHub Actions when code is pushed or a pull request is opened. Results can be viewed in the repository’s "Actions" tab.
