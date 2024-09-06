from API_Requests.Lib.Rest_Client import RestClient
from conf.config import get_config
from conf.logger import logGen
from conf.conftest import setup_teardown

logging = logGen()


class Test_004:
    def test_004(self,setup_teardown):
        """Test to resource is deleted from Backend """
        self.base_url = get_config()['API']['base_url']
        self.client = RestClient(self.base_url)
        self.headers = {
            'Content-Type':'application/json'
        }

        logging.info("*********** executing test_004 ****************")

        # send delete request
        delete_request,status_code = self.client.delete_request(end_point="objects/6",headers=self.headers,json_data_fmt=True,response_with_status_code=True)

        # verify to get response
        assert delete_request is not None, "DELETE request returned None"
        assert status_code == 204