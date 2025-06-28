from config import endpoints
from helpers import request_handler

class TestNegativeScenarios:
    
    def test_post_to_all_product_list(self,endpoint_factory):
        url = endpoint_factory(endpoints.product_list)
        response = request_handler.post_request(url)
        json_data = response.json()
        assert json_data["responseCode"] == 405
        assert json_data["message"] =="This request method is not supported."


    def test_put_to_all_brands_list(self,endpoint_factory):
        url = endpoint_factory(endpoints.brand_list)
        response = request_handler.put_request(url)
        json_data = response.json()
        assert json_data["responseCode"] == 405
        assert json_data["message"] =="This request method is not supported."

    def test_post_to_search_without_parameter(self,endpoint_factory):
        url = endpoint_factory(endpoints.search_product)
        response  =request_handler.post_request(url)
        json_data = response.json()
        assert json_data["responseCode"] == 400
        assert json_data["message"] == "Bad request, search_product parameter is missing in POST request."  

    def test_login_without_email(self,endpoint_factory):
        url = endpoint_factory(endpoints.login)
        credentials = {
            "password" : "TestPass!2025"
        }
        response = request_handler.post_request(url,data=credentials)
        json_data = response.json()
        assert json_data["responseCode"] == 400
        assert json_data["message"] == "Bad request, email or password parameter is missing in POST request."

    def test_delete_to_verify_login(self,endpoint_factory):
        url = endpoint_factory(endpoints.login)
        response = request_handler.delete_request(url)
        json_data = response.json()
        assert json_data["responseCode"] == 405
        assert json_data["message"] == "This request method is not supported."

    def test_login_invalid_credentials(self,endpoint_factory):
        url = endpoint_factory(endpoints.login)
        credentials = {
            "email" : "test-test@example.com",
            "password" : "A88b55"
        }
        response = request_handler.post_request(url,data=credentials)
        json_data = response.json()
        assert json_data["responseCode"] == 404
        assert json_data["message"] == "User not found!"