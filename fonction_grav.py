# max parab: alpha
"""
***FORMATS***

objet[0][0] : taille x (abscice sur un graph)
objet[0][1] : taille y (ordonnée sur un graph)
objet[0][2] : position de la rotation de l'objet
    0: à l'endroit
    1: sur la droite
    2: à l'envers
    3: sur la gauche

objet[1][0] : position x (abscisse sur un graph) de l'objet
objet[1][1] : position y (ordinnée sur un graph) de l'objet


"""
def falling_state(objet):
    '''
    objet[0] : taille x (abscice sur un graph)
    objet[1] : taille y (ordonnée sur un graph)
    objet[2] : état de la rotation de l'objet
    dit si l'objet est en train de tomber et peut toomber ou pas:
    RETOUR = True or False
    '''
    if objet[0][2] == 0 or objet[0][2] == 2:
        if objet[0][1] - objet[1][1] != 0:
            return True
        else:
            return False
    elif objet[0][2] == 1 or objet[0][2] == 3:
        if objet[0][0] - objet[1][1] != 0:
            return True
        else:
            return False

def gravity(objet):
    '''
    pos de forme [x,y]
    objet de forme [[taille x, taille y, rotation], [position x, position y]]
    rotation côté 1 = sur le côté droit du sprite de base, côté 2 = à l'envers du sprite de base, coté 3 = sur le coté gauche du sprite de base, côté 0 = sprite de base
    '''
    while falling_state(objet) == True:
        objet[1][1] -= 1
        falling_state(objet)
        print(falling_state(objet), objet)
    pass

test_object = [[1, 6, 1],[0,14]]

##PYXEL

import pyxel

class App:
    def __init__(self):
        '''
        partie initialisation
        '''
        pyxel.init(160, 120, "Angry Pirds", 30, pyxel.KEY_Q)    #crée la fenêtre de taille 160, 120 px
        pyxel.mouse(True) #conserve la souris qd dans la fenêtre
        self.mouse_x = 0 #initialisation coordonnées de la souris
        self.mouse_y = 0
        pyxel.load("textures.PYXRES")
        pyxel.run(self.update(), self.draw())     #lance les fonctions pyxel


    def update(self):
        """
        permet de quiter la fenêtre en pressant 'Q'
        """
        self.mouse_x = pyxel.mouse_x
        self.mouse_y = pyxel.mouse_y
        #•if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) == True:
            #implémentation code courbe Yohan



    def draw(self):
        """
        permet de 'dessiner' dans la fenetre, ici créant un rectangle bleu
        """
        pyxel.cls(1)
        pyxel.ellib(25, 25, 70, 40, 7)
        #pyxel.
        #pyxel.blt(0, 0, 0, 0, 0, 16, 16, 14)
        #pyxel.circb(60, 60, 40, 7) #crée un cercle format (
        #pyxel.rect(10, 10, 20, 20, 11)
        pyxel.text(10, 10, f"Souris : ({self.mouse_x}, {self.mouse_y})", 7)  # Affiche le texte (couleur 7 = blanc)
        pyxel.show()



App() #permet d'utiliser toutes les fonctions ds cette class, mais pr tt les fonctions ss argts, il faut mettre 'self'