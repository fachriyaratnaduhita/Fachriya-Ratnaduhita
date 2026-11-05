def make_car(manufacturer, model, **car_info):
    """Store information about a car in a dictionary."""
    car_info['manufacturer'] = manufacturer.title()
    car_info['model'] = model.title()
    return car_info

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)