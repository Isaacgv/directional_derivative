import numpy as np

def input_vectors():    

    while(True):
        try:
            point_x = float(input("Coordinates x : "))
            break
        except:
            print("Insert only numerical value")
            
    while(True):
        try:  
            point_y = float(input("Coordinates y : "))
            break
        except:
            print("Insert only numerical value")

    while(True):
        try:
            u_x = float(input("Vector u component x : "))
            break
        except:
            print("Insert only numerical value")
            
    while(True):
        try:
            u_y = float(input("Vector u component y : "))
            break
        except:
            print("Insert only numerical value")
    
    return np.array([point_x, point_y]), np.array([u_x, u_y])

