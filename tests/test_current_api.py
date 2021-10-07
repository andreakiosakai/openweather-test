import requests
import src.helper as Helper

config = Helper.Helper.get_config()
api_key = config['api_key']
base_url = config['base_url']

def test_invalid_api_key_401():
    URL = base_url + '/weather?q=London&appid=invalidkey'
    response = requests.get(URL)
    assert response.status_code == 401
    body = response.json()
    assert body['cod'] == 401
    assert body['message'] == "Invalid API key. Please see http://openweathermap.org/faq#error401 for more info."

def test_get_by_name_200():
    URL = base_url + '/weather?q=London&appid=' + api_key
    response = requests.get(URL)
    assert response.status_code == 200
    body = response.json()
    assert body['name'] == 'London'

def test_get_by_id_200():
    URL = base_url + '/weather?id=2172797&appid=' + api_key
    response = requests.get(URL)
    assert response.status_code == 200

def test_get_by_coordinates_200():
    URL = base_url + '/weather?lat=35&lon=139&appid=' + api_key
    response = requests.get(URL)
    assert response.status_code == 200

def test_get_valid_city_by_zip_200():
    URL = base_url + '/weather?zip=94040,us&appid=' + api_key
    response = requests.get(URL)
    assert response.status_code == 200

def test_get_rectangle_box_200():
    URL = base_url + '/box/city?bbox=12,32,15,37,10&appid=' + api_key
    response = requests.get(URL)
    assert response.status_code == 200

def test_get_circle_area_200():
    URL = base_url + '/find?lat=55.5&lon=37.5&cnt=10&appid=' + api_key
    response = requests.get(URL)
    assert response.status_code == 200