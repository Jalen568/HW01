import json # to parse JSON
import requests # to make HTTP requests
import argparse # to parse command-line arguments
import time

if __name__ == "__main__":
  url_1 = "https://api.github.com/users/emaadmanzoor/repos?page=1"
  url_2 = "https://api.github.com/users/emaadmanzoor/repos?page=2"
  url_3 = "https://api.github.com/users/emaadmanzoor/repos?page=3"
  url_4 = "https://api.github.com/users/emaadmanzoor/repos?page=4"
  u1 = requests.get(url_1)
  u2 = requests.get(url_2)
  u3 = requests.get(url_3)
  u4 = requests.get(url_4)
  u1new = u1.json()
  u2new = u2.json()
  u3new = u3.json()
  u4new = u4.json()
  u = u1new+u2new+u3new+u4new
  count = 0
  for i in u:
    count += i["stargazers_count"]
  print(count)
