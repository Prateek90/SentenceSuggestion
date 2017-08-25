import unittest
import SentenceSuggestions
from flask import json
from DataUpload import service_data
import random
from random import randint

#Testing class
class MyTestClass(unittest.TestCase):

    # Initialization during set up
    def setUp(self):
        SentenceSuggestions.app.testing = True
        self.app = SentenceSuggestions.app.test_client()

    # Test case for testing response
    # This test case checks for the presence of query inside the results
        def test_response(self):

        # Selecting 100 random sentences from the corpus
        index = random.sample(range(0,len(service_data)),100)

        # Checking results for those 100 sentences
        for counter in range(100):
            val1=service_data[index[counter]]

            pos = randint(1,len(val1))
            val1= val1[:pos]
            val1 = val1.encode("utf-8")

            response = self.app.get('/autocomplete?q={}'.format(val1))
            data=json.loads(response.get_data(as_text=True))

            # Flag variable check for the validity of received response
            flag=True
            for key in data['Completions']:
                key=key.lower()
                key=key.replace(" ","")
                val1 = val1.replace(" ","")
                if val1.lower() not in key.lower():
                    print val1
                    print key
                    flag=False
                    break

            if flag==False:
                break

        # If flag is False means result received is not correct
        self.assertEquals(True,flag)


if __name__ == "__main__":
    unittest.main()
