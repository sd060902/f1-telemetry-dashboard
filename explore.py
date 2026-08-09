import fastf1
fastf1.Cache.enable_cache('cache')

session = fastf1.get_session(2024, 'Monza', 'R')
session.load()

def find_driver_fastest_lap(session,driver_name):
    driver_laps = session.laps.pick_drivers([driver_name])
    driver_fastest_lap = driver_laps.pick_fastest()
    print(f"\n{driver_name}'s fastest lap: ",driver_fastest_lap)
    driver_tel = driver_fastest_lap.get_car_data().add_distance()
    return driver_tel

ver_tel = find_driver_fastest_lap(session,'VER')
ham_tel = find_driver_fastest_lap(session,'HAM')

print("\nTelemetry of VER: ",ver_tel.shape)
print("\nTelemetry of HAM: ",ham_tel.shape)