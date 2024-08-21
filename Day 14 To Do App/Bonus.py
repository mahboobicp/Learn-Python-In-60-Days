# This simple code take inches and feets and convert them to meters
import bonus_parser
feet = input("Enter Feet and Inches : ")
parased = bonus_parser.paras(feet)
meter = bonus_parser.convert(parased["Feet"],parased["Inches"])
print(f"{parased["Feet"]} Feet and {parased['Inches']} Inches is equal :{meter}")

                  
