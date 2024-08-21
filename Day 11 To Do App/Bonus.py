feet = input("Enter Feet and Inches : ")


def convert(feet_l):
    part = feet_l.split(' ')
    feet1 = float(part[0])
    inch  = float(part[1])

    meter = feet1 * 0.3048 + inch * 0.0254

    return f"{feet1} Feet and {inch} is equal to : {round(meter)} Meters"


print(convert(feet))
                  
