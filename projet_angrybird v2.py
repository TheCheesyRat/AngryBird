import pyxel
from math import *
import code_courbe
class App:
    def __init__(self):
        pyxel.init(160, 120)  # Initialise Pyxel
        self.state = "menu"  # État actuel : "menu" ou "game"
        self.menu_options = ["Jouer", "Quitter", "test"]  # Options du menu
        self.selected_option = 0  # Option sélectionnée dans le menu
        pyxel.mouse(True)
        self.souris_x = 0
        self.souris_y = 0
        pyxel.load("assets.pyxres")  # Charge les ressources (tilemap et sprites)
        pyxel.run(self.update, self.draw)  # Lance l'application

    def update(self):
        if self.state == "menu":
            self.update_menu()
        elif self.state == "game":
            self.update_game()
        self.souris_x = pyxel.mouse_x
        self.souris_y = pyxel.mouse_y


    def update_menu(self):
        '''
        permet la selection d'option dans le menu
        '''
        if pyxel.btnp(pyxel.KEY_DOWN):
            self.selected_option = (self.selected_option + 1) % len(self.menu_options)
        if pyxel.btnp(pyxel.KEY_UP):
            self.selected_option = (self.selected_option - 1) % len(self.menu_options)
        if pyxel.btnp(pyxel.KEY_RETURN):
            self.handle_menu_selection()

    def update_game(self):
        '''
        jeu en lui-même
        '''
        # Logique de jeu


    def handle_menu_selection(self):
        '''
        permet d'actionner une option sélectionnée dans le menu
        '''
        if self.selected_option == 0:  # "Jouer"
            self.state = "game"
        elif self.selected_option == 1: #"Quitter"
            pyxel.quit()

    def draw(self):
        '''
        gère les premières étapes de l'affichage
        '''
        pyxel.cls(0)  # Efface l'écran (couleur 0 = noir)
        if self.state == "menu":
            self.draw_menu()
        elif self.state == "game":
            self.draw_game()


    def draw_menu(self):
        '''
        gère l'affichage du menu
        '''
        pyxel.text(50, 30, "Menu Principal", 7)
        for i, option in enumerate(self.menu_options):
            color = 7 if i == self.selected_option else 8  # Blanc si sélectionné, gris sinon
            pyxel.text(50, 50 + i * 10, option, color)
            pyxel.text(10, 10, f"Souris : ({self.mouse_x}, {self.mouse_y})", 7)

    def draw_game(self):
        '''
        affiche le jeu en lui-même
        '''
        pyxel.cls(0)
        pyxel.bltm(0,0,0,45,15,255,255, 6)
        #pyxel.bltm(x, y, numéro tilemap, x(tilemap), y(tilemap), taille horizontale, taille verticale, [couleur de transparence)]
        pyxel.ellib(25, 25, 70, 40, 7)
        #pyxel.
        for i in range(1,16):
            try:
                y = int(round(code_courbe.fonction_courbe(self.souris_x, self.souris_y, 8, 13),0))
                pyxel.pset(i, y, 0)
            except Exception as e:
                print(f"Erreur ds la courbe : {e}")
        pyxel.text(10, 10, f"Souris : ({self.mouse_x}, {self.mouse_y})", 7)
        pyxel.tilemap(0).pget(tuile_x, tuile_y)
        #pyxel.tilemap(numéro de tilemap).pget(tuile_x, tuile_y)

App()
