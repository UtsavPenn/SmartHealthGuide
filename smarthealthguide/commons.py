'''TO DO Nikhil : Add utility method here to parse suggestion source data'''

"""
Functions:

Score: 1 - best, 2 - okay, 3 - worst
    sleep_score(age, hrs)
    weight_score(weight, height)
    calorie_score(age, calories)
    
Score: 1 - best, 2 - worst
    heart_rate_score(heart_rate)
"""

def sleep_score(age, hrs):
    """
    Input:
        age - In years
        hrs - Sleep hours
    
    Returns:
        score - 1: Recommended sleep
                2: Appropriate sleep
                3: Not Recommended sleep
    """
    if age < 15:
        if 9 <= hrs <= 12:
            return 1
        elif hrs in [8,13]:
            return 2
        else:
            return 3

    elif age < 20:
        if 8 <= hrs <= 10:
            return 1
        elif hrs in [7,11]:
            return 2
        else:
            return 3

    elif age < 25:
        if 7 <= hrs <= 9:
            return 1
        elif hrs in [6,10,11]:
            return 2
        else:
            return 3
        
    elif age < 65:
        if 7 <= hrs <= 9:
            return 1
        elif hrs in [6,10]:
            return 2
        else:
            return 3
        
    elif age >= 65:
        if 7 <= hrs <= 8:
            return 1
        elif hrs in [5,6,9]:
            return 2
        else:
            return 3

def weight_score(weight, height):
    """
    Input:
        weight - lbs
        height - inches (58 - 72)
    Returns: 
        Score - 1: Normal
                2: Overweight/underweight
                3: Obese
    """
    if height == 58 :
        if 91 <= weight <= 115:
            return 1
        elif weight < 138:
            return 2
        else:
            return 3
    
    elif height == 59 :
        if 94 <= weight <= 119:
            return 1
        elif weight < 143:
            return 2
        else:
            return 3
        
    elif height == 60 :
        if 97 <= weight <= 123:
            return 1
        elif weight < 148:
            return 2
        else:
            return 3
    
    elif height == 61 :
        if 100 <= weight <= 127:
            return 1
        elif weight < 153:
            return 2
        else:
            return 3
        
    elif height == 62 :
        if 104 <= weight <= 131:
            return 1
        elif weight < 158:
            return 2
        else:
            return 3
        
    elif height == 63 :
        if 107 <= weight <= 135:
            return 1
        elif weight < 163:
            return 2
        else:
            return 3
        
    elif height == 64 :
        if 110 <= weight <= 140:
            return 1
        elif weight < 169:
            return 2
        else:
            return 3
        
    elif height == 65 :
        if 114 <= weight <= 144:
            return 1
        elif weight < 174:
            return 2
        else:
            return 3
        
    elif height == 66 :
        if 118 <= weight <= 148:
            return 1
        elif weight < 179:
            return 2
        else:
            return 3
    
    elif height == 67 :
        if 121 <= weight <= 153:
            return 1
        elif weight < 185:
            return 2
        else:
            return 3
        
    elif height == 68 :
        if 125 <= weight <= 158:
            return 1
        elif weight < 190:
            return 2
        else:
            return 3
        
    elif height == 69 :
        if 128 <= weight <= 162:
            return 1
        elif weight < 196:
            return 2
        else:
            return 3
        
    elif height == 70 :
        if 132 <= weight <= 167:
            return 1
        elif weight < 202:
            return 2
        else:
            return 3
        
    elif height == 71 :
        if 136 <= weight <= 172:
            return 1
        elif weight < 208:
            return 2
        else:
            return 3
        
    elif height == 72 :
        if 140 <= weight <= 177:
            return 1
        elif weight < 213:
            return 2
        else:
            return 3
        
    elif height == 73 :
        if 144 <= weight <= 182:
            return 1
        elif weight < 219:
            return 2
        else:
            return 3
        
    elif height == 74 :
        if 148 <= weight <= 186:
            return 1
        elif weight < 225:
            return 2
        else:
            return 3
        
    elif height == 75 :
        if 152 <= weight <= 192:
            return 1
        elif weight < 232:
            return 2
        else:
            return 3
        
    elif height == 76 :
        if 156 <= weight <= 197:
            return 1
        elif weight < 238:
            return 2
        else:
            return 3
    
    else:
        return 2

def calorie_score(age, calories):
    """
    Input:
        age - In years
        calories - calories burned
    
    Returns:
        score - 1: Active
                2: Modertely active
                3: Sedentary
    """

    if age < 20:
        if calories > 2800:
            return 1
        elif calories > 2600:
            return 2
        else:
            return 3

    elif age < 25:
        if calories > 2800:
            return 1
        elif calories > 2400:
            return 2
        else:
            return 3
        

    elif age < 45:
        if calories > 2600:
            return 1
        elif calories > 2200:
            return 2
        else:
            return 3
        
    else:
        if calories > 2400:
            return 1
        elif calories > 2200:
            return 2
        else:
            return 3

def heart_rate_score(heart_rate):
    """
    Input:
        heart_rate - Resting heart_rate
    
    Returns:
        score - 1: Safe
                2: Needs attention
    """

    if  60 <= heart_rate <= 100:
        return 1
    else:
        return 2