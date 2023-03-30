


import math
def azimuth_calculation():
    """
    Function to calculate azimuth between two point based on their coordinate
    :return: azmiuth (in degrees)
    """
    coordinate_database = {}
    axis = ['X','Y']
    id = [1,2]
    results = {}

    def coordinate_save(axis, id):
        """
        Function that saves data provided by the user for using it in the further calculation
        """
        while True:
            print(f'Please provide {axis} axis coordinate for point #{id}')
            value = input()
            try:
                value = float(value)
            except ValueError:
                print('Provided value isn\'t a number')
            else:
                coordinate_database.update({f'{axis}{id}':value})
                break

    def calculation(database):
        """
        Base function that calculate value of fi and decide how to use in calculation base on value for delta X and Y 
        """
        delta_X = database['X2'] - database['X1']
        delta_Y = database['Y2'] - database['Y1']

        fi = math.degrees(math.atan(abs(delta_Y/delta_X)))

        distance = round(math.sqrt((delta_X)**2+(delta_Y**2)),2)

        if delta_X == 0:
            if delta_Y == 0:
                azimuth = 'Special case - same place'
            elif delta_Y > 0:
                azimuth = 90
            else:
                azimuth = 240 
        elif delta_X > 0:
            if delta_Y == 0:
                azimuth = 0
            elif delta_Y > 0:
                azimuth = fi 
            else:
                azimuth = 360- fi
        elif delta_X < 0:
            if delta_Y == 0:
                azimuth = 180
            elif delta_Y > 0:
                azimuth = 180 - fi 
            else:
                azimuth = 180 + fi

        results.update({'Azimuth':float(round(azimuth,6))})
        results.update({'Distance': distance})
        return results
    
    # invoke of user coordinate input
    for i in id:
        for j in axis:
            coordinate_save(j, i)

    # invoke of calculation 
    print(calculation(coordinate_database))
    
azimuth_calculation()
