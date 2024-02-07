from app.engine.jeton import Rond, Croix
from app.engine.grille import Grille
from app.engine.ai.ai import min_max


class Joueur:
    def __init__(self, pseudo: str, jeton: Rond | Croix, est_humain: bool = True):
        self.pseudo = pseudo
        self.jeton = jeton
        self.est_humain = est_humain

    def get_pseudo(self):
        return self.pseudo

    def get_jeton(self):
        return self.jeton

    def get_est_humain(self):
        return self.est_humain

    def choisir_colonne(self, grille: Grille)->int:
        """
        Demande au joueur de choisir une colonne pour placer son pion
        Si le joueur n'est pas humain, la colonne est choisie grâce à la méthode min-max
        :param grille:
        :return:
        """
        if self.est_humain:
            colonne = input(f"Joueur {self.pseudo} choisissez une colonne : ")
            while not colonne.isdigit():
                print("Erreur : Veillez saisir un entier")
                colonne = input(f"Joueur {self.pseudo} choisissez une colonne : ")
            colonne = int(colonne)
        else:
            colonne = min_max(grille, 4, self.jeton, Rond() if self.jeton == Croix() else Croix(), self.jeton)[0]
        return colonne

    def __str__(self):
        return f"{self.pseudo} avec le jeton {self.jeton}"