import numpy as np

def x(ab, ac, ad, bc, bd, cd):

    return [ab, ac, ad, bc, bd, cd]

def rot_ab(u):

    c = np.cos(u)
    s = np.sin(u)
    
    M = np.array([[c, -s, 0, 0],
                  [s, c, 0, 0],
                  [0, 0, 1, 0],
                  [0, 0, 0, 1]])
                  
    return M

def rot_ac(u):

    c = np.cos(u)
    s = np.sin(u)
    
    M = np.array([[c, 0, -s, 0],
                  [0, 1, 0, 0],
                  [s, 0, c, 0],
                  [0, 0, 0, 1]])
                  
    return M

def rot_ad(u):

    c = np.cos(u)
    s = np.sin(u)
    
    M = np.array([[c, 0, 0, -s],
                  [0, 1, 0, 0],
                  [0, 0, 1, 0],
                  [s, 0, 0, c]])
                  
    return M

def rot_bc(u):

    c = np.cos(u)
    s = np.sin(u)
    
    M = np.array([[1, 0, 0, 0],
                  [0, c, -s, 0],
                  [0, s, c, 0],
                  [0, 0, 0, 1]])
                  
    return M

def rot_bd(u):

    c = np.cos(u)
    s = np.sin(u)
    
    M = np.array([[1, 0, 0, 0],
                  [0, c, 0, -s],
                  [0, 0, 1, 0],
                  [0, s, 0, c]])
                  
    return M

def rot_cd(u):

    c = np.cos(u)
    s = np.sin(u)
    
    M = np.array([[1, 0, 0, 0],
                  [0, 1, 0, 0],
                  [0, 0, c, -s],
                  [0, 0, s, c]])
                  
    return M

def rotations(u):

    M = [rot_ab(u), rot_ac(u), rot_ad(u), rot_bc(u), rot_bd(u), rot_cd(u)]

    return M


def rotator(n, ab, ac, ad, bc, bd, cd):

    xx = x(ab, ac, ad, bc, bd, cd)

    M = np.asarray([[1, 0, 0, 0],
                    [0, 1, 0, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1]])
                    
    for i in range(6):
        if xx[i] != 0:
            M = rotations(xx[i]*n)[i].dot(M)
            
    return M
                 
def projection1(x, d1):

    u = d1/(d1 - x[3])
    y = x[:3]
    z = u*y
    
    return z

def projection2(x, d2):

    u = d2/(d2 - x[2])
    y = x[:2]
    z = u*y
    
    return z

