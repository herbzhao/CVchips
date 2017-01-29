digits_colour_code = {'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4, 'green': 5, 'blue': 6, 'purple': 7, 'grey': 8, 'white': 9}
multiplier_colour_code = {'silver': 0.01, 'gold': 0.1, 'black': 10**0, 'brown': 10**1, 'red': 10**2, 'orange': 10**3, 'yellow': 10**4, 'green': 10**5, 'blue': 10**6, 'purple': 10**7}
tolerance_colour_code = {'no band': 20, 'silver': 10, 'gold': 5,'brown': 1, 'red': 2, 'green': 0.5, 'blue': 0.25, 'purple': 0.1}
temperature_coefficient_colour_code = {'brown': 100, 'red': 50, 'orange': 15, 'yellow': 25}

input_colour_code = ('brown', 'black', 'green', 'gold')
band_number = len(input_colour_code)

def colour_code_recognition(input_colour_code):
    input_colour_code = input_colour_code
    if band_number == 4:
        resistor_digit_1 = digits_colour_code[input_colour_code[0]]*10
        resistor_digit_2 = digits_colour_code[input_colour_code[1]]
        resistor_multiplier = multiplier_colour_code[input_colour_code[2]]
        total_resistance = (resistor_digit_1 + resistor_digit_2) * resistor_multiplier
        resistor_tolerance = tolerance_colour_code[input_colour_code[3]]
        temperature_coefficient = 'unspecified'

    if band_number == 5:
        resistor_digit_1 = digits_colour_code[input_colour_code[0]]*100
        resistor_digit_2 = digits_colour_code[input_colour_code[1]]*10
        resistor_digit_3 = digits_colour_code[input_colour_code[2]]
        resistor_multiplier = multiplier_colour_code[input_colour_code[3]]
        total_resistance = (resistor_digit_1 + resistor_digit_2+ resistor_digit_3 ) * resistor_multiplier
        resistor_tolerance = tolerance_colour_code[input_colour_code[4]]
        temperature_coefficient = 'unspecified'
    
    if band_number == 6:
        resistor_digit_1 = digits_colour_code[input_colour_code[0]]*100
        resistor_digit_2 = digits_colour_code[input_colour_code[1]]*10
        resistor_digit_3 = digits_colour_code[input_colour_code[2]]
        resistor_multiplier = multiplier_colour_code[input_colour_code[3]]
        total_resistance = (resistor_digit_1 + resistor_digit_2+ resistor_digit_3 ) * resistor_multiplier
        resistor_tolerance = tolerance_colour_code[input_colour_code[4]]
        thermal_coefficient = temperature_coefficient_colour_code[input_colour_code[5]]
    return (total_resistance, resistor_tolerance, temperature_coefficient)


def resistor_output(colour_output):
    resistor_info = colour_code_recognition((colour_output))
    print(resistor_info[0])
    print('tolerance: ±{}%'.format(resistor_info[1]))
    print('thermal coefficient: {}'.format(resistor_info[2]))