import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('ZJyw4IQ1ThX-DIbTFSDc8Zy_I-Pd2GRZgH_4YXQIehW3')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator= authenticator
)

language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com/instances/dafb1d1f-45cf-475b-bac8-676d3cef1356')

def english_to_french(english_text):

    translation = language_translator.translate(text=english_text, model_id='en-fr').get_result()

    french_text = translation['translations'][0]['translation']

    return french_text

def french_to_english(french_text):

    translation = language_translator.translate(text=french_text, model_id='fr-en').get_result()

    english_text = translation['translations'][0]['translation']

    return english_text