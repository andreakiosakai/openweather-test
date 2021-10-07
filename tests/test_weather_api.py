import requests
import src.helper as Helper

config = Helper.Helper.get_config()
api_key = config['api_key']
base_url = config['base_url']
weather_list = Helper.Helper.weather_list()

def test_invalid_api_key_401():
    URL = base_url + '/weather?q=London&appid=invalidkey'
    response = requests.get(URL)
    assert response.status_code == 401
    body = response.json()
    assert body['cod'] == 401
    assert body['message'] == "Invalid API key. Please see http://openweathermap.org/faq#error401 for more info."

def test_delete_method_not_allowed_405():
    URL = base_url + '/weather?q=London&appid=' + api_key
    response = requests.delete(URL)
    assert response.status_code == 405
    body = response.json()
    assert body['cod'] == '405'
    assert body['message'] == 'Internal error'

def test_put_method_not_allowed_405():
    URL = base_url + '/weather?q=London&appid=' + api_key
    data = {"name": "CITY_NAME"}
    response = requests.put(URL,data)
    assert response.status_code == 405
    body = response.json()
    assert body['cod'] == '405'
    assert body['message'] == 'Internal error'

def test_patch_method_not_allowed_405():
    URL = base_url + '/weather?q=London&appid=' + api_key
    data = {"name": "CITY_NAME"}
    response = requests.patch(URL,data)
    assert response.status_code == 405
    body = response.json()
    assert body['cod'] == '405'
    assert body['message'] == 'Internal error'

def test_get_by_name_200():
    URL = base_url + '/weather?q=London&appid=' + api_key
    response = requests.get(URL)
    assert response.status_code == 200
    body = response.json()
    assert body['cod'] == 200
    assert body['name'] == 'London'
    assert body['sys']['country'] == 'GB'
    assert body['weather'][0]['id'] in weather_list
    assert body['main'] is not None
    
def test_get_by_name_invalid_404():
    URL = base_url + '/weather?q=abc123&appid=' + api_key
    response = requests.get(URL)
    assert response.status_code == 404
    body = response.json()
    assert body['cod'] == '404'
    assert body['message'] == 'city not found'

def test_get_by_id_200():
    URL = base_url + '/weather?id=2172797&appid=' + api_key
    response = requests.get(URL)
    assert response.status_code == 200
    body = response.json()
    assert body['cod'] == 200
    assert body['id'] == 2172797
    assert body['name'] == 'Cairns'
    assert body['sys']['country'] == 'AU'
    assert body['weather'][0]['id'] in weather_list
    assert body['main'] is not None

def test_get_by_id_invalid_alphabetic_400():
    URL = base_url + '/weather?id=asdasd&appid=' + api_key
    response = requests.get(URL)
    assert response.status_code == 400
    body = response.json()
    assert body['cod'] == '400'
    assert body['message'] == 'asdasd is not a city ID'

def test_get_by_id_not_found_404():
    URL = base_url + '/weather?id=123&appid=' + api_key
    response = requests.get(URL)
    assert response.status_code == 404
    body = response.json()
    assert body['cod'] == '404'
    assert body['message'] == 'city not found'

def test_get_by_coordinates_200():
    URL = base_url + '/weather?lat=35&lon=139&appid=' + api_key
    response = requests.get(URL)
    assert response.status_code == 200
    body = response.json()
    assert body['cod'] == 200
    assert body['coord']['lon'] == 139
    assert body['coord']['lat'] == 35
    assert body['name'] == 'Shuzenji'
    assert body['sys']['country'] == 'JP'
    assert body['weather'][0]['id'] in weather_list
    assert body['main'] is not None

def test_get_by_coordinates_wrong_latitude_400():
    URL = base_url + '/weather?lat=asda&lon=139&appid=' + api_key
    response = requests.get(URL)
    assert response.status_code == 400
    body = response.json()
    assert body['cod'] == '400'
    assert body['message'] == 'wrong latitude'

def test_get_by_coordinates_wrong_longitude_400():
    URL = base_url + '/weather?lat=35&lon=asdas&appid=' + api_key
    response = requests.get(URL)
    assert response.status_code == 400
    body = response.json()
    assert body['cod'] == '400'
    assert body['message'] == 'wrong longitude'
 
def test_get_by_zipcode_200():
    URL = base_url + '/weather?zip=94040,us&appid=' + api_key
    response = requests.get(URL)
    assert response.status_code == 200 
    body = response.json()
    assert body['cod'] == 200
    assert body['name'] == 'Mountain View'
    assert body['sys']['country'] == 'US'
    assert body['weather'][0]['id'] in weather_list
    assert body['main'] is not None

def test_get_by_zipcode_wrong_alphabetic_404():
    URL = base_url + '/weather?zip=abcabcusus&appid=' + api_key
    response = requests.get(URL)
    assert response.status_code == 404
    body = response.json()
    assert body['cod'] == '404'
    assert body['message'] == 'city not found'