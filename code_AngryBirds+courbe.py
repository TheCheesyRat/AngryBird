import pyxel
from math import *
import courbe_vecteur_test  # Assurez-vous que ce fichier existe et contient la fonction fonction_courbe

class App:
    def __init__(self):
        pyxel.init(160, 120)
        self.state = "menu"
        self.menu_options = ["Jouer", "Quitter", "test"]
        self.selected_option = 0
        pyxel.mouse(True)
        self.souris_x = 0
        self.souris_y = 0
        pyxel.load("assets.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        if self.state == "menu":
            self.update_menu()
        elif self.state == "game":
            self.update_game()
        self.souris_x = pyxel.mouse_x
        self.souris_y = pyxel.mouse_y

    def update_menu(self):
        if pyxel.btnp(pyxel.KEY_DOWN):
            self.selected_option = (self.selected_option + 1) % len(self.menu_options)
        if pyxel.btnp(pyxel.KEY_UP):
            self.selected_option = (self.selected_option - 1) % len(self.menu_options)
        if pyxel.btnp(pyxel.KEY_RETURN):
            self.handle_menu_selection()

    def update_game(self):
        pass  # Logique de jeu (à ajouter)

    def handle_menu_selection(self):
        if self.selected_option == 0:
            self.state = "game"
        elif self.selected_option == 1:
            pyxel.quit() # Utilisez pyxel.quit() pour quitter proprement

    def draw(self):
        pyxel.cls(0)
        if self.state == "menu":
            self.draw_menu()
        elif self.state == "game":
            self.draw_game()

    def draw_menu(self):
        pyxel.text(50, 30, "Menu Principal", 7)
        for i, option in enumerate(self.menu_options):
            if i == self.selected_option:
                color = 7
            else:
                color = 8
            pyxel.text(50, 50 + i * 10, option, color)
        pyxel.text(10, 10, f"Souris : ({self.souris_x}, {self.souris_y})", 7)

    def draw_game(self):
        pyxel.cls(6)
        pyxel.bltm(0, 0, 0, 64, 8, 255, 255, 6)
        for x in range(1, 50):
            try:
                z = tuple(courbe_vecteur_test.vecteur(self.souris_x, self.souris_y, 23, 93, x))
                #y = int(courbe_vecteur_test.vecteur(self.souris_x, self.souris_y, 23, 93, x)) # pour ancienne fonction: 8, 13)) et 10= arondie 9.81
                pyxel.pset(z[0] +23, z[1] +93, 1)
            except Exception as e:
                print(f"Erreur dans fonction_courbe : {e}")

        pyxel.text(10, 10, f"Souris : ({self.souris_x}, {self.souris_y})", 7)

App()
