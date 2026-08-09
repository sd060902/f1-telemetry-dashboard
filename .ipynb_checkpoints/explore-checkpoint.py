import fastf1
fastf1.Cache.enable_cache('cache')

session = fastf1.get_session(2024, 'Monza', 'R')
session.load()

# 1. Laps dataframe — see the columns available
print("LAP COLUMNS:", list(session.laps.columns))

# 2. Pick one driver's laps
ver_laps = session.laps.pick_drivers(['VER','HAM'])
print("\nVER total laps:", len(ver_laps))

# 3. Get VER's fastest lap
fastest = ver_laps.pick_fastest()
print("\nFastest lap time:", fastest['LapTime'])

# 4. Pull telemetry for JUST that one lap
tel = fastest.get_car_data().add_distance()
print("\nTelemetry rows for ONE lap:", len(tel))
print(tel[['Distance', 'Speed', 'Throttle', 'Brake', 'nGear']].head())

# 5. Now estimate the full session telemetry size
all_tel_rows = 0
for drv in session.drivers:
    drv_laps = session.laps.pick_drivers([drv])
    for _, lap in drv_laps.iterrows():
        pass  # don't actually loop-fetch every lap yet, that's slow — just eyeball step 4's number × laps × drivers
print("\nRough estimate: ~", len(tel), "rows/lap ×", len(session.laps), "total laps in session =",
      len(tel) * len(session.laps), "telemetry rows if pulled for every lap")