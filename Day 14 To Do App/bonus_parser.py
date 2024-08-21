def paras(feet_inches):
    """ This function takes Feet and inches as a String
     Formate split both values and convert both values to
      float and finally return both values as Dictionary data type """
    part = feet_inches.split(' ')
    feet1 = float(part[0])
    inch  = float(part[1])
    return {"Feet":feet1, "Inches":inch}

def convert(feet_local,inches_local):
    """ This fn take two argument feet and inches convert them into meters
     and return the result """
    meter = feet_local * 0.3048 + inches_local * 0.0254

    return meter