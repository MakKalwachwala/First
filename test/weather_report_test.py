from app.weather_report import display_forecast

def test_display_forecast():
    assert display_forecast(zip_code = "08648", country_code="US") == 200

    
