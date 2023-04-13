
def define_quarter(delta_X, delta_Y, fi):  
    if delta_X == 0 or delta_Y == 0:
        if delta_X == 0 and delta_Y > 0:
            azimuth = 100
        elif delta_X == 0 and delta_Y < 0:
            azimuth = 300
        elif delta_Y == 0 and delta_X > 0:
            azimuth = 0
        elif delta_Y == 0 and delta_X < 0:
            azimuth = 200
    else:
        if delta_Y > 0 and delta_X > 0:
            azimuth = fi 
        elif delta_Y > 0 and delta_X < 0:
            azimuth = 200 - fi 
        elif delta_Y < 0 and delta_X < 0:
            azimuth = 20 + fi
        else:
            azimuth = 400 - fi 
    return azimuth
