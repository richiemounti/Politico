import json
import unittest

# Local imports
from app import politico_app


class TestOffice(unittest.TestCase):

    def setUp(self):
        self.app = politico_app() 
        self.client = self.app.test_client()
        self.data = {
          "id": 1,
          "type": "presidential",
          "name": "jubilee"
        }


    """ This class handles methods to test version 1 of the api """

    def test_post_to_office(self):
        """ Tests create an office """

        response = self.client.post(
            'api/v1/offices',
            data=json.dumps(self.data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)

    #
    def test_retrieve_all_offices(self):
        """ Tests retrieve all offices"""

        response = self.client.get('api/v1/offices')
        self.assertEqual(response.status_code, 200)

    def test_retrieve_specific_office(self):
        """ Tests retrieve specific office """

        response = self.client.get('api/v1/offices/1')
        self.assertEqual(response.status_code, 200)

    def test_no_office(self):
        """ Tests the response on a non-existant resource  """

        response = self.client.get('api/v1/offices/10')
        self.assertEqual(response.status_code, 404)

    
    