import mendeleev as md
from flask import Flask
from flask_cors import CORS
app=Flask(__name__)
cors=CORS(app)

@app.route('/data/<element>')
def print_element_properties(element):
    element=md.element(element.capitalize())
    # print(f'Element Name: {element.name.capitalize()}')
    # print(f'Element Symbol: {element.symbol}')
    # print(f'Atomic Number: {element.atomic_number}')
    # print(f'Atomic Weight: {element.atomic_weight}')
    # print(f'Density: {element.density} g/cm³')
    # print(f'Melting Point: {element.melting_point} K')
    # print(f'Boiling Point: {element.boiling_point} K')
    # print(f'Atomic Radius: {element.atomic_radius} pm')
    # print(f'Heat of Fusion: {element.heat_of_formation} kJ/mol')
    # print(f'Specific Heat Capacity: {element.specific_heat_capacity} J/g·K')
    # print(f'Thermal Conductivity: {element.thermal_conductivity} W/m·K')
    # print(f'Discovered By: {element.discoverers}')
    # print(f'Description: {element.description}')
    return({
         "Name":element.name.capitalize(),
         "Symbol":element.symbol,
         "Atomic Number":element.atomic_number,
         "Atomic Weight":element.atomic_weight,
         "Density":element.density,
         "Melting Point":element.melting_point,
         "Boiling Point":element.boiling_point,
         "Atomic Radius":element.atomic_radius,
         "Heat of Fusion":element.heat_of_formation,
         "Specific Heat Capacity":element.specific_heat_capacity,
         "Thermal Conductivity":element.thermal_conductivity,
         "Discovered By":element.discoverers,
         "Description":element.description,
    })



@app.route('/data2/<sym>')
def printeledet(sym):
     element=md.element(sym.capitalize())
     return({
         "Name":element.name.capitalize(),
         "Symbol":element.symbol,
         "Atomic Number":element.atomic_number,
         "Atomic Weight":element.atomic_weight,
         "Density":element.density,
         "Melting Point":element.melting_point,
         "Boiling Point":element.boiling_point,
         "Atomic Radius":element.atomic_radius,
         "Heat of Fusion":element.heat_of_formation,
         "Specific Heat Capacity":element.specific_heat_capacity,
         "Thermal Conductivity":element.thermal_conductivity,
         "Discovered By":element.discoverers,
         "Description":element.description,
    })

@app.route('/data1/<num>')
def printeledeta(num):
     element=md.element(int(num))
     return({
         "Name":element.name.capitalize(),
         "Symbol":element.symbol,
         "Atomic Number":element.atomic_number,
         "Atomic Weight":element.atomic_weight,
         "Density":element.density,
         "Melting Point":element.melting_point,
         "Boiling Point":element.boiling_point,
         "Atomic Radius":element.atomic_radius,
         "Heat of Fusion":element.heat_of_formation,
         "Specific Heat Capacity":element.specific_heat_capacity,
         "Thermal Conductivity":element.thermal_conductivity,
         "Discovered By":element.discoverers,
         "Description":element.description,
    })








# r = 1
# while r == 1:
#             option = int(input("\nEnter 1 To Search By Name.\nEnter 2 To Search By Symbol.\nEnter 3 To Search By Atomic Number.\nSelect an option: \n"))

#             if option == 1:
#                 name = input("Enter the Name Of The Element: ")
#                 element = md.element(name.capitalize())
#                 if element:
#                     print_element_properties(element)
#                 else:
#                     print("Element not found.")
                
#             elif option == 2:
#                 symbol = input("Enter the Symbol Of The Element: ")
#                 element = md.element(symbol.capitalize())
#                 if element:
#                     print_element_properties(element)
#                 else:
#                     print("Element not found.")
                
#             elif option == 3:
#                 number = int(input("Enter the Atomic Number Of The Element: "))
#                 element = md.element(number)
#                 if element:
#                     print_element_properties(element)
#                 else:
#                     print("Element not found.")
                
#             else:
#                 print("Invalid option.")


if __name__ =='__main__':
     app.run(debug=True)