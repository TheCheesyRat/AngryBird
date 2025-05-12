from math import *
def vecteur(souris_x, souris_y, x_poteau_haut, y_poteau_haut, nb_executions):
    '''
    calcule les coordonnées du vecteur que suivrat le bird
    '''
    vect_AB_x = souris_x - x_poteau_haut
    vect_AB_y = y_poteau_haut - souris_y
    norme = sqrt(vect_AB_x**2 + vect_AB_y**2)
    return(round(norme * (nb_executions*0.5), 0), round((vect_AB_y - (nb_executions*0.5)*(-10))*nb_executions*0.5, 0)) #10 est l'arrondit de 9.81 mais -1 rends la trajectoire plus 'jouable' et le *0.5 pour que les pointillets apparaîssent plus souvent

###
"""
def Vy(t):
    '''
    prd en argt le tmps (t en nmbr de frames) et renvoie la position y de l'objet
    '''
    G = -10
    dt = t - pyxel.frame_count()
    if t == 0:
        return 0 #vitesse initiale sur l'axe Y (modifiable) (ici tt les 0 ds les formules)
    else:
        Vy = 0 + G * dt
        return Vy

def Y(t):
    '''
    prds en argt le tmps (t en nmbr de frames) et renvoie la coordonée de l'objet en Y
    '''
    delta_t = t - pyxel.frame_count()
    dt =
    Y = Y(t - dt) + Vy(t) * dt + Y(0)
    X = 2 *( sqrt(souris_x**2 + souris_y**2)
"""