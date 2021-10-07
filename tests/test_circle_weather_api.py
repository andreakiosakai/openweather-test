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
