import numpy as np

xlimdict = {
    3: 2e-5,    #Sirio
    1: 3.5e-5,
    2: 3.5e-5,
    16: 2e-5,
    17:1.5e-5,
    19:2e-5,
    20:1.5e-5,
    21:1.5e-5,
    22:1.5e-5,
    23:1.5e-5,
    4:2.5e-5,    #Rigel
    6:2.5e-5,
    7:2.5e-5,
    13:2.5e-5,
    24:2.5e-5,    #GAmmaleo
    8:2.5e-5,            #betelgeuse  
    9:2.5e-5          
}

xlimdef=6*(np.pi/180/3600)

if __name__=="__main__":
    print(xlimdict)
    