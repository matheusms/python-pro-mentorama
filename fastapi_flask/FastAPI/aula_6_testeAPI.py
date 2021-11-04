import pytest
from requests import get, post
from json import loads


class TestAPI:
    def setup(self):
        self.url = "http://127.0.0.1:8000"

    def test_APIstatus(self):
        resp = get(self.url)
        assert resp.ok
    
    def test_APIresponse(self):
        resp = get(self.url)
        message = loads(resp.text)
        assert message["message"] == "Hello World"

    def test_POSTmethod(self):
        resp = post(self.url + "/novarota"
                    , json= {"curso" : "pythonpro", "modulo" : 6, "tipo" : "POST"})
        message = loads(resp.text)
        resposta_esperada = {
            "curso": "pythonpro",
            "modulo": 6,
            "opt": None,
            "tipo": "POST"
        }
        assert message == resposta_esperada

#python -m pytest aula_6_testeAPI.py
