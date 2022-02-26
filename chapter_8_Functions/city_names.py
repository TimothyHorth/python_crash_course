def city_country(city, country):
    """Takes name of city and its country and returns it as a string"""
    string = f'{city.title()}, {country.title()}'
    return string

example = city_country('akron', 'United States of america')
print(example)
print(romanToInt('MCMXCIV'))