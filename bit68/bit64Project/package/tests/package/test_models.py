import pytest


pytestmark = pytest.mark.django_db

class TestPackageModel:
    def test_str_return(self,package_factory):
        package = package_factory(product_price = 1200) # test will fail if product_price changed
        assert package.__str__() == 1200
def application(env , start_response):
    start_response('200 ok' , [('content-type','text/html')])
    return [b"Hola"]