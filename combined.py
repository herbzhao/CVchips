from image_processing import image_process
from ocr import upload_ocr
from google_scrapper import google_scrape
from resistor_analyser import resistor_analyse
from resistor_colour_code import resistor_output

colour_output = resistor_analyse()
resistor_output(colour_output)


input_image_location = r'resources\DS18B20.jpg'
processed_image_location = r'resources\processed_image.png'
processed_image = image_process(input_image_location, processed_image_location)

part_number = upload_ocr(processed_image_location)
for i in range(len(part_number)):
    google_scrape(part_number[i])


