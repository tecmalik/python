weight_in_pounds = float(input('Enter weight :'))
hight_in_inches = float(input('Enter height :'))
weight_in_kg = weight_in_pounds *0.45359237
hight_in_meters = hight_in_inches *0.0254
body_mass_index = (weight_in_kg)/(hight_in_meters*hight_in_meters)
print('the body mass index is ', body_mass_index)
