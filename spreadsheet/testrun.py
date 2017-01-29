
from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None
# -*- coding: utf-8 -*-

import requests
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup


def thorlabs_scrapper(weblink):
    r = urlopen(weblink)
    soup = BeautifulSoup(r)
    print(type(soup))
    #content = str(soup.prettify()[0:-1])
    content = str(soup)
    #print(content)

    image_re = re.compile(r'src="\S+" style="width:200; height:200;" width="200"')
    image_link_re = re.compile(r'src="\S+"')
    image_sentence = image_re.findall(content)
    image_link = image_link_re.findall(image_sentence[0])
    image_link = image_link[0].split('"')
    image_link = 'https://www.thorlabs.com/'+image_link[1]

    price_re = re.compile(r'£\d+.\d+')
    price = price_re.findall(content)
    price = price[0]

    #class="PartTitle"><b>MT1B - 1/2" Translation Stage with 1/4"-170 Adjuster, 1/4"-20 Taps</b> 
    part_name_re = re.compile(r'class="PartTitle"><b>.+</b>\s</td></tr><tr><td\salign')
    part_name_redefine_re = re.compile(r'')

    part_name = part_name_re.findall(content)
    part_name = part_name[0]
    part_name = part_name.replace('class="PartTitle"><b>','')
    part_name = part_name.split('</b>')
    part_name = part_name[0]
    
    return image_link, price, part_name

part_id = input('write down part ID: ')
weblink = 'https://www.thorlabs.com/thorproduct.cfm?partnumber=' + part_id
image_link, price, part_name = thorlabs_scrapper(weblink)



# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
#SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
SCOPES = 'https://www.googleapis.com/auth/drive'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Sheets API Python Quickstart'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'sheets.googleapis.com-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def main():
    """Shows basic usage of the Sheets API.

    Creates a Sheets API service object and prints the names and majors of
    students in a sample spreadsheet:
    https://docs.google.com/spreadsheets/d/1dfrzoezsSf_yXID1eLf4INDz6-vwzxqqanTsYb2EtXU/edit
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', http=http,
                              discoveryServiceUrl=discoveryUrl)

    spreadsheet_id = '1dfrzoezsSf_yXID1eLf4INDz6-vwzxqqanTsYb2EtXU'
    range_name = 'Sheet1!A2:E'
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id, range=range_name).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        print('Name, Major:')
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            print('%s, %s' % (row[0], row[1]))

    # whether to use equations
    value_input_option = 'RAW'
    
    # values row by row
    values = [
    [part_name, weblink, image_link, price, part_id],
    # Additional rows ...
    ]
    
    body = {
    'values': values
    }
    result = service.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id, range=range_name,
        valueInputOption=value_input_option, body=body).execute()


if __name__ == '__main__':
    main()
