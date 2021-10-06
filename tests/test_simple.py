import requests

def test_get_by_name_200():
    response = requests.get('http://api.openweathermap.org/data/2.5/weather?q=London&appid=b6cc41aedbbd439a8a2b6a9b6190c7e7')
    assert response.status_code == 200
    body = response.json()
    assert body['name'] == 'London'


def test_get_by_id_200():
    response = requests.get('http://api.openweathermap.org/data/2.5/weather?id=2172797&appid=b6cc41aedbbd439a8a2b6a9b6190c7e7')
    assert response.status_code == 200

def test_get_by_coordinates_200():
    response = requests.get('http://api.openweathermap.org/data/2.5/weather?lat=35&lon=139&appid=b6cc41aedbbd439a8a2b6a9b6190c7e7')
    assert response.status_code == 200

def test_get_valid_city_by_zip_200():
    response = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=94040,us&appid=b6cc41aedbbd439a8a2b6a9b6190c7e7')
    assert response.status_code == 200

def test_get_rectangle_box_200():
    response = requests.get('http://api.openweathermap.org/data/2.5/box/city?bbox=12,32,15,37,10&appid=b6cc41aedbbd439a8a2b6a9b6190c7e7')
    assert response.status_code == 200

def test_get_circle_area_200():
    response = requests.get('http://api.openweathermap.org/data/2.5/find?lat=55.5&lon=37.5&cnt=10&appid=b6cc41aedbbd439a8a2b6a9b6190c7e7')
    assert response.status_code == 200