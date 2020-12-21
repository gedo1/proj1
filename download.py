import pandas as pd
import numpy as np
import matplotlib as plt
import json
import re
import requests
import csv

req_URL = 'https://d17h27t6h515a5.cloudfront.net/topher/2017/October/59dd1c4c_tmdb-movies/tmdb-movies.csv'
response = requests.get(req_URL) 

with open('tmdb-movies.csv', 'w') as f:
    writer = csv.writer(f)
    for line in response.iter_lines():
        writer.writerow(line)