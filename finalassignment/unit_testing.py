import json
import unittest
import requests

class Test(unittest.TestCase):
    ApiURL = 'https://h8ocbc2-milestone1-004.herokuapp.com/api'
    director_url = "{}/directors".format(ApiURL)
    movie_url = "{}/movies".format(ApiURL)
    OBJ = {"department": "abc","gender": 1,"id": 12,"movies":[], "name": "abc","uid": 1}
    updateOBJ = {"department": "Produksi","gender": 1,"id": 12,"movies":[], "name": "Budi","uid": 1}

    def test_getAlldirector (self):
        r = requests.get(Test.director_url)
        self.assertEqual(r.status_code, 200)

    def test_AddNewDirector (self):
        r = requests.post(Test.director_url, json=Test.OBJ)
        self.assertEqual(r.status_code, 201,"ERROR")
        self.assertEqual(r.json(),Test.OBJ,"DATA TIDAK SAMA")

    def test_GetNewDirector (self):
        id = 12
        r = requests.get("{}/{}".format(Test.director_url,id))
        self.assertEqual(r.status_code, 200,"ERROR")
        self.assertEqual(r.json(),Test.OBJ,"DATA TIDAK SAMA")
    
    def test_update(self):
        id = 12
        r = requests.put("{}/{}".format(Test.director_url,12), json=Test.updateOBJ)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json(),Test.updateOBJ,"DATA TIDAK SAMA")
    
    def test_delete(self):
        id = 12
        r = requests.delete("{}/{}".format(Test.director_url,12))
        self.assertEqual(r.status_code, 200)

    def test_getAllMovie (self):
        r = requests.get(Test.movie_url)
        self.assertEqual(r.status_code, 200)
    
    