import requests
import json
import webbrowser


def ocr_space_file(filename, overlay=False, api_key='helloworld', language='eng'):
    """ OCR.space API request with local file.
        Python3.5 - not tested on 2.7
    :param filename: Your file path & name.
    :param overlay: Is OCR.space overlay required in your response.
                    Defaults to False.
    :param api_key: OCR.space API key.
                    Defaults to 'helloworld'.
    :param language: Language code to be used in OCR.
                    List of available language codes can be found on https://ocr.space/OCRAPI
                    Defaults to 'en'.
    :return: Result in JSON format.
    """

    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )
    return r.content.decode()


def ocr_space_url(url, overlay=False, api_key='helloworld', language='eng'):
    """ OCR.space API request with remote file.
        Python3.5 - not tested on 2.7
    :param url: Image url.
    :param overlay: Is OCR.space overlay required in your response.
                    Defaults to False.
    :param api_key: OCR.space API key.
                    Defaults to 'helloworld'.
    :param language: Language code to be used in OCR.
                    List of available language codes can be found on https://ocr.space/OCRAPI
                    Defaults to 'en'.
    :return: Result in JSON format.
    """

    payload = {'url': url,
               'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    r = requests.post('https://api.ocr.space/parse/image',
                      data=payload,
                      )
    return r.content.decode()



def upload_ocr(processed_image_location):

    # if upload local files
    raw_ocr_result = ocr_space_file(
        filename = processed_image_location,
        language='eng',
        api_key='02a0da578b88957')

# if using a direct json string
#raw_ocr_result = r'{"ParsedResults":[{"TextOverlay":{"Lines":[],"HasOverlay":false,"Message":"Text overlay is not provided as it is not requested"},"FileParseExitCode":1,"ParsedText":"DALLAS \r\n18B20 \r\n0442B7 \r\n106ÅC \r\n","ErrorMessage": "","ErrorDetails":""}],"OCRExitCode":1,#"IsErroredOnProcessing":false,"ErrorMessage":null,"ErrorDetails":null,"PocessingTimeInMilliseconds":"310"}'


# if using an url
#raw_ocr_result = ocr_space_url(url='http://i.imgur.com/31d5L5y.jpg', api_key='02a0da578b88957')

# if use GET ocr api 
#raw_ocr_result = requests.get('https://api.ocr.space/parse/imageurl?apikey=helloworld&url=http://i.imgur.com/fwxooMv.png')
#json_string = ocr_result.json()

    json_string = json.loads(raw_ocr_result)
    parsed_ocr_result = json_string["ParsedResults"][0]["ParsedText"]

    part_number = parsed_ocr_result.replace(" \r", "")
    part_number = part_number.split('\n')
    part_number.remove('')
    print(part_number)
    return part_number

    #webbrowser.open(str(alldatasheet_search[i]))
