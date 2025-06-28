from config import endpoints
from helpers import request_handler


def get_products(endpoint_factory, endpoint,request_type,data=None):
    url = endpoint_factory(endpoint)
    response = request_type(url,data)
    json_data = response.json()
    return json_data

def check_product_detail(product_list):
    titles = ["id","name","price","brand","category"]
    for product in product_list:
            assert all(title in product for title in titles)
            assert all(product[title]!= None for title in titles)


class TestProductProcesses:
    
    def test_get_all_product_list(self,endpoint_factory):
        result = get_products(endpoint_factory,endpoints.product_list,request_handler.get_request)
        assert result["responseCode"] == 200
        assert len(result["products"]) > 0
        products = result["products"][:5]
        check_product_detail(products)
    
    def test_get_brands_list(self,endpoint_factory):
        result = get_products(endpoint_factory,endpoints.brand_list,request_handler.get_request)
        assert result["responseCode"] == 200
        assert len(result["brands"]) > 0
        brands = result["brands"][:5]
        titles = ["id","brand"]
        for brand in brands:
            assert all(title in brand for title in titles)
            assert all(brand[title]!= None for title in titles)

    
    def test_post_to_search_product(self,endpoint_factory):
        data = {
         "search_product": "jean"}
        result = get_products(endpoint_factory,endpoints.search_product,request_handler.post_request,data)
        assert result["responseCode"] ==200
        assert len(result["products"]) > 0 
        products = result["products"][:5]
        check_product_detail(products) 