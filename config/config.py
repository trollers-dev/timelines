import json
import logging
from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

IS_DEV_MODE = os.environ.get('TIMELINES_DEVELOPMENT_MODE') == 'true'

# Directories
BASE_DIR = Path(__file__).parent.parent.absolute()
CONFIG_DIR = Path(BASE_DIR, 'config')
BACKEND_DIR = Path(BASE_DIR, 'backend')
ML_DIR = Path(BASE_DIR, 'ml')
TESTS_DIR = Path(BASE_DIR, 'tests')
FIXTURES_DIR = Path(TESTS_DIR, 'fixtures')

# API Keys
NEWS_API_KEY = os.environ['NEWS_API_KEY']

# CORS
ALLOWED_HOSTS = [os.environ.get('ALLOWED_HOST')]

# Constants
SOURCES = ['economist.com', 'apnews.com','reuters.com','theguardian.com',
           'washingtonpost.com','aljazeera.com', 'npr.org', 'nytimes.com',
           'bbc.co.uk', 'straitstimes.com']

ARTICLES_TO_REMOVE = (
    'Russia-Ukraine war: what we know on day',  # The Guardian
    'Russia-Ukraine war latest: what we know on day',  # The Guardian
    'Timeline: Week',  # Al Jazeera
    'Russia-Ukraine war: List of key events',  # Al Jazeera
    'Russia-Ukraine war: What happened today',  # NPR
    'Russia-Ukraine war: A weekly recap and look ahead',  # NPR
)

# Ref: https://github.com/dipanjanS/text-analytics-with-python/blob/master/New-Second-Edition/Ch05%20-%20Text%20Classification/contractions.py
with open('config/contractions.json', 'r') as f:
    CONTRACTION_MAP = json.loads(f.read())

# Augment contraction map with alternative apostrophe used by some news outlets
for contraction in list(CONTRACTION_MAP):
    CONTRACTION_MAP[contraction.replace("'", "’")] = CONTRACTION_MAP[contraction]

# Cache
assert "AWS_ACCESS_KEY_ID" in os.environ
assert "AWS_SECRET_ACCESS_KEY" in os.environ
CACHE_TABLE_NAME = os.environ['CACHE_TABLE_NAME']
CACHE_TABLE_REGION = os.environ['CACHE_TABLE_REGION']
CACHE_TABLE_KEY_PREFIX = os.environ['CACHE_TABLE_KEY_PREFIX']

# Sentry
SENTRY_DSN = os.environ["SENTRY_DSN"]
SENTRY_SAMPLE_RATE = 1.0

# Development settings

if IS_DEV_MODE:
    ALLOWED_HOSTS = ['*']
    logging.basicConfig(level=logging.DEBUG)
