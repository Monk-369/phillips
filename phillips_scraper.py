# coding=utf-8

import os
import pathlib

import requests
from bs4 import BeautifulSoup


def download_image(img_url, folder_name):
    try:
        response = requests.get(img_url)
        file_name = os.path.basename(img_url)
        file_path = os.path.join(folder_name, file_name)
        with open(file_path, 'wb') as f:
            f.write(response.content)
        print("Image downloaded successfully:", file_path)
    except Exception as e:
        print("Error downloading image:", e)


def get_image_content(url, directory):
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, "lxml")
    images = soup.find_all("figure", class_="p-product-image p-grid-item p-one-third p-m-one-whole")
    directory_name = directory
    directory_name.mkdir(parents=True, exist_ok=True)

    for image in images:
        img_url = image['src']
        download_image(img_url, directory_name)


if __name__ == "__main__":
    directory = pathlib.Path("Bulbs/")
    url = (u"https://www.lighting.philips.co.za/consumer/choose-a-bulb/products#filters=REFLECTOR_BULB_SU%2CCANDLE_BULB_SU%2CSPOT_BULB_SU%2CSTANDARD_BULB_SU%2CLINEAR_BULB_SU%2CSMARTLIGHTING_BULB_SU&sliders=&support=&price=&priceBoxes=&page=&layout=12.subcategory.p-grid-icon")
    get_image_content(url, directory)
