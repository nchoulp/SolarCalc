# Member 1: Ignacio
def get_sun_hours(island: str) -> float:
    """Return average daily peak sun hours (5.0–7.0) for a Canary Island."""
    pass

# Member 2: Leo
def daily_consumption(monthly_kwh: float) -> float:
    """Convert monthly electricity use (kWh > 0) into daily use (kWh)."""
    pass

# Member 3: Jorge
def panels_needed(daily_kwh: float, sun_hours: float) -> int:
    """Calculate the integer number of panels needed (rounded up) from daily kWh and sun hours."""
    pass

# Member 4: Joel
def total_cost(n_panels: int) -> float:
    """Calculate total installation cost in EUR (panels + inverter) for n_panels >= 1."""
    pass

# Member 5: Tarun
def payback_years(cost: float, monthly_kwh: float) -> float:
    """Calculate years (rounded to 1 decimal) to recover the installation cost."""
    pass

# Member 6: Omar
def co2_saved(monthly_kwh: float) -> float:
    """Calculate annual CO2 emissions avoided in kg (rounded) from monthly kWh."""
    pass

print("SolarCalc: panels needed, total cost (EUR), payback years, and annual CO2 saved (kg).")