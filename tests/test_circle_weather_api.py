import requests
import src.helper as Helper

config = Helper.Helper.get_config()
api_key = config['api_key']
base_url = config['base_url']
weather_list = Helper.Helper.weather_list()


def test_get_circle_area_200():
    URL = base_url + '/find?lat=55.5&lon=37.5&cnt=10&appid=' + api_key
    response = requests.get(URL)
    assert response.status_code == 200
    body = response.json()
    assert body['cod'] == '200'
    assert body['count'] == 10
    assert body['message'] == 'accurate'
    assert len(body['list']) == body['count']
    for i in range(0, len(body['list'])):
        assert body['list'][i]['id'] is not None
        assert body['list'][i]['name'] is not None
        assert body['list'][i]['main'] is not None
        assert body['list'][i]['weather'][0]['id'] in weather_list
 
def test_delete_method_not_allowed_405():
    URL = base_url + '/find?lat=55.5&lon=37.5&cnt=10&appid=' + api_key
    response = requests.delete(URL)
    assert response.status_code == 405
    body = response.json()
    assert body['cod'] == '405'
    assert body['message'] == 'Internal error'

def test_put_method_not_allowed_405():
    URL = base_url + '/find?lat=55.5&lon=37.5&cnt=10&appid=' + api_key
    data = {"name": "CITY_NAME"}
    response = requests.put(URL,data)
    assert response.status_code == 405
    body = response.json()
    assert body['cod'] == '405'
    assert body['message'] == 'Internal error'

def test_patch_method_not_allowed_405():
    URL = base_url + '/find?lat=55.5&lon=37.5&cnt=10&appid=' + api_key
    data = {"name": "CITY_NAME"}
    response = requests.patch(URL,data)
    assert response.status_code == 405
    body = response.json()
    assert body['cod'] == '405'
    assert body['message'] == 'Internal error'

def test_get_circle_area_count_above_50_400():
    URL = base_url + '/find?lat=55.5&lon=37.5&cnt=51&appid=' + api_key
    response = requests.get(URL)
    assert response.status_code == 400
    body = response.json()
    assert body['cod'] == '400'
    assert body['message'] == 'cnt from 1 to 50'

def test_get_circle_area_count_under_1_400():
    URL = base_url + '/find?lat=55.5&lon=37.5&cnt=0&appid=' + api_key
    response = requests.get(URL)
    assert response.status_code == 400
    body = response.json()
    assert body['cod'] == '400'
    assert body['message'] == 'cnt from 1 to 50'

def test_get_circle_area_wrong_latitude_400():
    URL = base_url + '/find?lat=abc&lon=37.5&cnt=10&appid=' + api_key
    response = requests.get(URL)
    assert response.status_code == 400
    body = response.json()
    assert body['cod'] == '400'
    assert body['message'] == 'wrong latitude'

def test_get_circle_area_wrong_longitude_400():
    URL = base_url + '/find?lat=55.5&lon=asdffs&cnt=10&appid=' + api_key
    response = requests.get(URL)
    assert response.status_code == 400
    body = response.json()
    assert body['cod'] == '400'
    assert body['message'] == 'wrong longitude'