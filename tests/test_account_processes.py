from config import endpoints
from helpers import request_handler
import pytest
import json

def send_request(endpoint_factory, endpoint,request_type,data=None,params=None):
    url = endpoint_factory(endpoint)
    response = request_type(url,data,params)
    json_data = response.json()
    return json_data

def load_test_data():
    with open("data/register_data.json") as file:
        return json.load(file)

class TestAccountProcesses:
    
    #kayıt işlemi
    @pytest.mark.parametrize("user_credentials",load_test_data())
    def test_account_processes(self,endpoint_factory,user_credentials):
        register_data = {
            "name":user_credentials["name"] ,"email": user_credentials["email"],
               "password": user_credentials["password"],"title": user_credentials["title"],
               "birth_date": user_credentials["birth_date"],"birth_month": user_credentials["birth_month"],
               "birth_year": user_credentials["birth_year"],"firstname": user_credentials["firstname"],
               "lastname": user_credentials["lastname"], "company": user_credentials["company"],
               "address1": user_credentials["address1"],"address2": user_credentials["address2"],
               "country": user_credentials["country"],"zipcode": user_credentials["zipcode"],
               "state": user_credentials["state"],"city": user_credentials["city"],
               "mobile_number": user_credentials["mobile_number"]
        }
        register_result = send_request(endpoint_factory,endpoints.create_account,request_handler.post_request,register_data)
        assert register_result["responseCode"] == 201
        assert register_result["message"] == "User created!"
        

        #login işlemi
        credentials_for_login = {
            "email": user_credentials["email"],
            "password" : user_credentials["password"]
        }
        login_result = send_request(endpoint_factory,endpoints.login,request_handler.post_request,credentials_for_login)
        assert login_result["responseCode"] == 200
        assert login_result["message"] == "User exists!"



        #günelleme işlemi
        data_for_updating = {
               "name":user_credentials["name"] ,"email": user_credentials["email"],
               "password": user_credentials["password"],"title": user_credentials["title"],
               "birth_date": user_credentials["birth_date"],"birth_month": user_credentials["birth_month"],
               "birth_year": user_credentials["birth_year"],"firstname": "newName",
               "lastname": "newLastname", "company": user_credentials["company"],
               "address1": user_credentials["address1"],"address2": user_credentials["address2"],
               "country": user_credentials["country"],"zipcode": user_credentials["zipcode"],
               "state": user_credentials["state"],"city": user_credentials["city"],
               "mobile_number": user_credentials["mobile_number"]
        }
        update_result = send_request(endpoint_factory,endpoints.update,request_handler.put_request,data=data_for_updating)
        assert update_result["responseCode"] == 200
        assert update_result["message"] ==  "User updated!"
        

        #kullanıcı bilgilerini kontrol et
        check_params = {"email": user_credentials["email"]}
        check_result = send_request(endpoint_factory,endpoints.user_detail,request_handler.get_request,params= check_params)
        assert check_result["responseCode"] == 200
        assert check_result["user"]["first_name"] != user_credentials["firstname"]
        assert check_result["user"]["last_name"] != user_credentials["lastname"]
        assert check_result["user"]["first_name"] == "newName"
        assert check_result["user"]["last_name"] == "newLastname"

        #kullanıcıyı sil
        credentials_for_delete = {
            "email": user_credentials["email"],
            "password": user_credentials["password"]
        }
        delete_result = send_request(endpoint_factory,endpoints.delete,request_handler.delete_request,data=credentials_for_delete)
        assert delete_result["responseCode"] == 200
        assert delete_result["message"] == "Account deleted!"
        

        #silinen kullanıcıyı kontrol et
        check_deleted_account = send_request(endpoint_factory,endpoints.user_detail,request_handler.get_request,params= check_params)
        assert check_deleted_account["responseCode"] == 404
        assert check_deleted_account["message"] == "Account not found with this email, try another email!"