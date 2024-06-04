import requests
import os
from bs4 import BeautifulSoup
import re
from typing import Optional
from pathlib import Path

class Extractor:

    name = "arxdown"

    def __init__(self,
                 ref: float,
                 path: Optional[str] = None,
                 name: Optional[str] = None) -> None:
        self.ref = str(ref)
        if path is not None:
            self.path = os.path.abspath(path)
        else:
            self.path = Path.home()/'Documents'
        if name is not None:
            self.name = name
        else:
            url = 'https://arxiv.org/abs/' + str(ref)
            response = requests.get(url)
            soup = BeautifulSoup(response.text, features="xml")
            self.name = soup.title.text

    def extract(self) -> None:
        url = 'https://arxiv.org/abs/' + self.ref
        urlpdf = 'http://arxiv.org/pdf/' + self.ref
        response = requests.get(url)
        responsepdf = requests.get(urlpdf)
        soup = BeautifulSoup(response.text, features="xml")

        try:
            os.chdir(self.path)
        except FileNotFoundError:
            print('Folder does not exist. Create it ? [Y/n]')
            ans = input().lower().strip()
            if ans == "y":
                os.mkdir(self.path)
            elif ans == "n":
                print("Disappointing.")
                exit(1)
            else:
                print("Not a valid input, exiting")
                exit(1)
        if 'arXiv_downloads' not in os.listdir():
            os.mkdir('arXiv_downloads')
        os.chdir('arxiv_downloads')

        subject_name = soup.find('td', class_='tablecell subjects').find('span', class_='primary-subject').text
        pattern = r'\([^)]*\)'
        directory = re.sub(pattern, '', subject_name).strip()

        if directory not in os.listdir():
            os.mkdir(directory)
        os.chdir(directory)

        destination_file_name = self.name + '.pdf'

        if destination_file_name in os.listdir():
            print(f"File name already exists: {self.name}")
        else:
            with open(destination_file_name, 'wb') as file:
                file.write(responsepdf.content)
                print("File downloaded successfully")