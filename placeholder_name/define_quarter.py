
def define_quarter(delta_X, delta_Y, fi):  
    if delta_X == 0 or delta_Y == 0:
        if delta_X == 0 and delta_Y > 0:
            azimuth = 90
        elif delta_X == 0 and delta_Y < 0:
            azimuth = 240
        elif delta_Y == 0 and delta_X > 0:
            azimuth = 0
        elif delta_Y == 0 and delta_X < 0:
            azimuth = 180
    else:
        if delta_Y > 0 and delta_X > 0:
            azimuth = fi 
        elif delta_Y < 0 and delta_X > 0:
            azimuth = 180 - fi 
        elif delta_Y < 0 and delta_X < 0:
            azimuth = 180 + fi
        elif delta_Y > 0 and delta_X < 0:
            azimuth = 360 - fi 
    return azimuth
