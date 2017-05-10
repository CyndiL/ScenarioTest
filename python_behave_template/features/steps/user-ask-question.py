from behave import *
import requests
import unittest

# http://stackoverflow.com/questions/11322430/python-how-to-send-post-request
# http://www.seleniumframework.com/python-basic/first-behave-gherkin/
# http://docs.python-requests.org/en/latest/index.html
# https://github.com/yassFar/api-question/blob/master/question_server.py

use_step_matcher("re")


class TestUserQuestion(unittest.TestCase):
    @when("Utilisateur pose une question")
    def step_impl(self):
        r = requests.post("http://poridore.pythonanywhere.com/question/maquestion")
        self.assertEqual("2")

        print(r)

    @then("La question est enregistrée")
    def step_impl(request):
        print (request.status_code)

    @then("Le serveur répond où la réponse sera disponible")
    def step_impl(context):
        context = ""



