import math 
def define_quarter(delta_X, delta_Y):  

    fi = math.atan(abs(delta_Y/delta_X))

    if delta_X == 0 or delta_Y == 0:
        if delta_X == 0 and delta_Y > 0:
            azimuth = math.pi/2
        elif delta_X == 0 and delta_Y < 0:
            azimuth = math.pi * 3/2
        elif delta_Y == 0 and delta_X > 0:
            azimuth = 0
        elif delta_Y == 0 and delta_X < 0:
            azimuth = math.pi
    else:
        if delta_Y > 0 and delta_X > 0:
            azimuth = fi 
        elif delta_Y > 0 and delta_X < 0:
            azimuth = math.pi - fi 
        elif delta_Y < 0 and delta_X < 0:
            azimuth = math.pi + fi
        elif delta_Y < 0 and delta_X > 0:
            azimuth = 2 * math.pi - fi 
    return azimuth
