import math
def azimuth_calculation():
    coordinate_database = {}
    axis = ['X','Y']
    id = [1,2]

    def coordinate_save(axis, id):
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
        delta_X = database['X2'] - database['X1']
        delta_Y = database['Y2'] - database['Y1']

        print(delta_Y)
        print(delta_X)
        print(delta_Y/delta_X)
        print(abs((delta_Y/delta_X)))
        fi = math.degrees(math.atan(abs(delta_Y/delta_X)))
        print(fi)

    # invoke of user coordinate input
    for i in id:
        for j in axis:
            coordinate_save(j, i)

    # invoke of calculation 
    calculation(coordinate_database)

azimuth_calculation()
