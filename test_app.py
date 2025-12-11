import pytest
from app import app  # imports the Dash app object from app.py


# 1. Header is present
def test_header_present(dash_duo):
    dash_duo.start_server(app)

    # Wait until the H1 appears
    header = dash_duo.wait_for_element("h1", timeout=10)

    assert header is not None
    assert "Pink Morsel" in header.text or "Soul Foods" in header.text


# 2. Visualisation (line chart) is present
def test_visualisation_present(dash_duo):
    dash_duo.start_server(app)

    # The Graph component has id="sales-line-chart"
    graph = dash_duo.wait_for_element("#sales-line-chart", timeout=10)

    assert graph is not None
    # Dash graphs render into a div; make sure it has some content
    assert graph.get_attribute("id") == "sales-line-chart"


# 3. Region picker (radio buttons) is present
def test_region_picker_present(dash_duo):
    dash_duo.start_server(app)

    # The radio items component has id="region-radio"
    radio = dash_duo.wait_for_element("#region-radio", timeout=10)

    assert radio is not None

    # Optionally, check that the expected labels exist in the page text
    page_text = dash_duo.driver.page_source.lower()
    assert "north" in page_text
    assert "east" in page_text
    assert "south" in page_text
    assert "west" in page_text
    assert "all" in page_text
