"""
@author: Dominik Cedro
@resources: https://www.heart.org/en/healthy-living/fitness/fitness-basics/target-heart-rates
"""

def calculate_opinion(age: int, hr: int):
    ''' Examines the hr and appropriate age and returns opinion about the hr
    ARGS:
        age: int - age of the examined person
        hr: int - heart rate of the person
    RETURNS:
        str - opinion about the heart rate
    RAISES:
        ValueError - if age or hr is not integer
        ValueError - if age is not in range 10-100
        ValueError - if hr is not in range 10-200
    '''
    if not isinstance(age, int) or not isinstance(hr, int):
        raise ValueError("Age and hr must be integers")
    dict_ranges = {20:(50,100), 30:(100,170), 35:(95,162), 40:(93,157), 45:(90,153),
                   50:(88,149), 55:(85,145), 60:(83,140), 65:(80,136), 70:(75,132), 100:(75,128)}
    if age == 0 or hr == 0:
        raise ValueError( "Age and hr must not be 0")
    if age > 100 or age < 10:
        raise ValueError("Age out of range 10-100")
    if hr < 10 or hr > 200:
        return "Abnormal heartrate. Measure your heart rate one more time or contact a medical professional"
    for key in dict_ranges:
        if key <= age:
            if hr < dict_ranges[key][0]:
                return "Your heart rate is too low"
            elif hr > dict_ranges[key][1]:
                return "Your heart rate is too high"
            else:
                return "Your heart rate for your age is accurate"