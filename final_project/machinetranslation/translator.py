"""
    This module translates eng <-> french , using Ibm watson
"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator)

language_translator.set_service_url(url)

def englishToFrench(english_text):
    """
    This function returns returns french translation of english Text
    """
    if (isinstance(english_text, str)) and (len(english_text) > 0):
        try:
            translation = language_translator.translate(
            text=english_text,
            model_id='en-fr').get_result()
            return translation["translations"][0]["translation"]
        except:
            return ""
    else:
        return ""

def frenchToEnglish(french_text):
    """
    This function returns  english translation of french Text
    """
    if (isinstance(french_text, str)) and (len(french_text) > 0):
        try:
            translation = language_translator.translate(
            text=french_text,
            model_id='fr-en').get_result()
            return translation["translations"][0]["translation"]
        except:
            return ""
    else:
        return ""
