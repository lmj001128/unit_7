
from tools import data_yaml
import pytest
import requests



class Test_wms:

    @pytest.mark.parametrize('data',data_yaml('./lianxi.yaml'))
    def test_login(self,data):
        url = 'http://82.157.138.248:8080/jeewms/rest/pdaapi/login'
        boby = {
            "userName": data['username'],
            "password": data['password'],
        }
        login = requests.post(url=url,json=boby)
        print(login.json())


# if __name__ == '__main__':
#     pytest.main()

