import math
def time_to_travel_around_planet(robot_speed: float, planet_diameter: float):
    if robot_speed <= 0 or planet_diameter <= 0:
        return "Скорость и диаметр должны быть положительными числами!"
    PI = math.pi 
    circumference = PI * planet_diameter
    travel_time = circumference / robot_speed
    return travel_time
robot_speed = 50.0 # км/ч
planet_diameter = 6371.0 # Диаметр Земли в км
robot_name = "Igor_bot V.2.0"
planet_name = "Земля"
calculation_1 = time_to_travel_around_planet(robot_speed, planet_diameter)
if isinstance(calculation_1, float) or isinstance(calculation_1, int):
    print(f"Роботу {robot_name} необходимо {calculation_1:.2f} часов, чтобы объехать вокруг планеты {planet_name}.")
else:
    print(calculation_1)
print("-" * 50)
error_calculation = time_to_travel_around_planet(-10, 1000)
print(f"Попытка расчета с некорректной скоростью: {error_calculation}")
