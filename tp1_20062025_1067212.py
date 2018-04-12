######################
# Tic Tac Toe Extreme - TP 1 (10%)
# Par Alexandre Chartrand - 20062025
# et Jad Yammine - 1067212
# Remis en date du 22 Mars 2017
#

import sys
import random

# PS: Les lignes n'ont pas tous 72 caracteres, car dans certains cas,
#     la lisibilite du code etait comprimise
#     Les lignes de code ont ete raccourcies le plus possible


# Classe qui gere le lancement d'une partie, l'affichage
# et qui affiche l'arbre selon les entrees donnees
class MetaGame:
    def __init__(self, entier, paramA, paramP, profondeur):

        # Creation d'un jeu
        jeu = list(entier,0)

        # Activation du mode arbre
        if paramA:
            jeu.afficherArbre(int(profondeur))


        # Activation du mode print
        elif paramP:
            printGame(entier)

        # Trouve le plus optimal et le retourne
        else:
            jeu.nPredictionMoves(1000)


# Classe list (represente une configuration d'un petit TTT)
class list:

    def __init__(self, t, d):

        # self.entier contient l'entier representant un petit TTT
        self.entier = t

        #self.depth est la profondeur d'un membre de la liste
        self.depth = d

        # self.next represente un tableau qui contient les enfants
        # d'une node
        self.next = []

        # self.plm (player move) contient un tableau avec tous les
        # mouvements possibles que peut faire un joueur
        self.plm = []

        # Contient le joueur qui doit prochainement joueur
        self.nextPlayer = None


    # Fonction qui renvoir les mouvements possibles d'un joueur
    # La fonction renvoie un tableau contenant tous les indices du
    # grand TTT ou qu'un joueur peut legalement se deplacer

    def plmove(self, i):
        q = []
        partieNulle = True

        for j in range(0 + 9 * i, 9 + 9 * i):
            if trouverValeurCase(self.entier, j) != 0:
                partieNulle = False

        if self.__fw__(i) == None and partieNulle == False:

            for j in range(0+9*i, 9+9*i):
                if trouverValeurCase(self.entier, j) == 0:
                    q.append(j)

        else:
            for j in range(0,9):
                if self.__fw__(j) == None:
                    for k in range(0 + 9 * j, 9 + 9 * j):
                        if trouverValeurCase(self.entier, k) == 0:
                            q.append(k)
        self.plm = q

        return self.plm



    # Fonction qui genere le prochain les enfants d'un noeud.
    # La fonction ajoute a self.next les prochains noeud de la
    # partie apres un coup

    def nextgrids(self,i):
        self.nextPlayer = self.getNextPlayer()
        entierBinaire = str(strToByte(self.entier))

        self.plmove(i)


        for j in range(0, len(self.plmove(i))):

            nouvelIndiceDernierCoupJoue = format(self.plm[j], '07b')
            new = nouvelIndiceDernierCoupJoue \
                  + entierBinaire[7:2*self.plm[j]+7] \
                  + self.nextPlayer \
                  + entierBinaire[2*self.plm[j]+9:]

            newInt = int(new, 2)
            self.next.append(list(newInt, (self.depth + 1)))


    # Fonction qui trouve le vanqueur d'une partie d'un petit TTT
    # La fonction renvoie le vainqueur ou None s'il n'y en a aucune
    # fw pour find winner

    def __fw__(self, i):

        if (trouverValeurCase(self.entier, 9*i) == trouverValeurCase(self.entier, 9*i+3)) \
                and (trouverValeurCase(self.entier, 9*i+3) == trouverValeurCase(self.entier, 9*i+6)) \
                and not (trouverValeurCase(self.entier, 9*i+6) == 0):
                    return trouverValeurCase(self.entier, 9*i+6)

        elif (trouverValeurCase(self.entier, 9*i+1) == trouverValeurCase(self.entier, 9*i+4)) \
                and (trouverValeurCase(self.entier, 9*i+4) == trouverValeurCase(self.entier, 9*i+7)) \
                and not (trouverValeurCase(self.entier, 9*i+7) == 0):
                    return trouverValeurCase(self.entier, 9*i+7)

        elif (trouverValeurCase(self.entier, 9*i+2) == trouverValeurCase(self.entier, 9*i+5)) \
                and (trouverValeurCase(self.entier, 9*i+5) == trouverValeurCase(self.entier, 9*i+8)) \
                and not (trouverValeurCase(self.entier, 9*i+8) == 0):
            return trouverValeurCase(self.entier, 9*i+8)

        elif (trouverValeurCase(self.entier, 9*i) == trouverValeurCase(self.entier, 9*i+1)) \
                and (trouverValeurCase(self.entier, 9*i+1) == trouverValeurCase(self.entier, 9*i+2)) \
                and not (trouverValeurCase(self.entier, 9*i+2) == 0):
            return trouverValeurCase(self.entier, 9*i+2)

        elif (trouverValeurCase(self.entier, 9*i+3) == trouverValeurCase(self.entier, 9*i+4)) \
                and (trouverValeurCase(self.entier, 9*i+4) == trouverValeurCase(self.entier, 9*i+5)) \
                and not (trouverValeurCase(self.entier, 9*i+5) == 0):
            return trouverValeurCase(self.entier, 9*i+5)

        elif (trouverValeurCase(self.entier, 9*i+6) == trouverValeurCase(self.entier, 9*i+7)) \
                and (trouverValeurCase(self.entier, 9*i+7) == trouverValeurCase(self.entier, 9*i+8)) \
                and not (trouverValeurCase(self.entier, 9*i+8) == 0):
            return trouverValeurCase(self.entier, 9*i+8)

        elif (trouverValeurCase(self.entier, 9*i+0) == trouverValeurCase(self.entier, 9*i+4)) \
                and (trouverValeurCase(self.entier, 9*i+4) == trouverValeurCase(self.entier, 9*i+8)) \
                and not (trouverValeurCase(self.entier, 9*i+8) == 0):
            return trouverValeurCase(self.entier, 9*i+8)

        elif (trouverValeurCase(self.entier, 9*i+2) == trouverValeurCase(self.entier, 9*i+4)) \
                and (trouverValeurCase(self.entier, 9*i+4) == trouverValeurCase(self.entier, 9*i+6)) \
                and not (trouverValeurCase(self.entier, 9*i+6) == 0):
            return trouverValeurCase(self.entier, 9*i+6)
        else:
            return None


    # Fonction qui choisit un chemin aleatoire dans une partie et
    # ajoute dans un tableau (winner) le gagnant de la partie

    def predictmove(self):

        # On trouve l'indice du dernier joueur
        indiceDernierJoueur = trouverIndiceDernierCoup(self.entier)

        # On cree une nouvelle generation d'enfants
        self.nextgrids(indiceDernierJoueur % 9)

        # On choisit aleatoirement parmi les coups possibles un coup
        choix = int(random.random()*len(self.plmove(indiceDernierJoueur % 9)))

        # On recall la fonction predict move jusqua ce qu'il n'y aille
        # plus d'enfants possibles. Ainsi, nous nous rendons jusqu'a
        # la fin de la partie avec un chemin completement aleatoire

        if len(self.next) !=0:
            self.next[choix].predictmove()


        else:
            # Des qu'il n'y a plus d'enfants possibles (atteinte de la
            # fin d'une partie), on ajoute le gagnants des 9 petites
            # parties de TTT dans un tableau

            les9GagnantsDuTTTLocal = []

            for i in range(0,9):
                les9GagnantsDuTTTLocal.append(self.__fw__(i))


            # On verifie si la partie est gagnee en verifant s' il y a
            # un gros TTT avec les 9 petits TTT. S'il y a un vainqueur,
            # on ajoute au tableau global winner une valeur, sinon,
            # on lui ajoute None.

            if les9GagnantsDuTTTLocal[0] == les9GagnantsDuTTTLocal[3] \
                    and les9GagnantsDuTTTLocal[3] == les9GagnantsDuTTTLocal[6] \
                    and not les9GagnantsDuTTTLocal[6] == 0:
                winner.append(les9GagnantsDuTTTLocal[6])

            elif les9GagnantsDuTTTLocal[1] == les9GagnantsDuTTTLocal[4] \
                    and les9GagnantsDuTTTLocal[4] == les9GagnantsDuTTTLocal[7] \
                    and not les9GagnantsDuTTTLocal[7] == 0:
                winner.append(les9GagnantsDuTTTLocal[7])

            elif les9GagnantsDuTTTLocal[2] == les9GagnantsDuTTTLocal[5] \
                    and les9GagnantsDuTTTLocal[5] == les9GagnantsDuTTTLocal[8] \
                    and not les9GagnantsDuTTTLocal[8] == 0:
                winner.append(les9GagnantsDuTTTLocal[8])

            elif les9GagnantsDuTTTLocal[0] == les9GagnantsDuTTTLocal[1] \
                    and les9GagnantsDuTTTLocal[1] == les9GagnantsDuTTTLocal[2] \
                    and not les9GagnantsDuTTTLocal[2] == 0:
                winner.append(les9GagnantsDuTTTLocal[2])

            elif les9GagnantsDuTTTLocal[3] == les9GagnantsDuTTTLocal[4] \
                    and les9GagnantsDuTTTLocal[4] == les9GagnantsDuTTTLocal[5] \
                    and not les9GagnantsDuTTTLocal[5] == 0:
                winner.append(les9GagnantsDuTTTLocal[5])

            elif les9GagnantsDuTTTLocal[6] == les9GagnantsDuTTTLocal[7] \
                    and les9GagnantsDuTTTLocal[7] == les9GagnantsDuTTTLocal[8] \
                    and not les9GagnantsDuTTTLocal[8] == 0:
                winner.append(les9GagnantsDuTTTLocal[8])

            elif les9GagnantsDuTTTLocal[0] == les9GagnantsDuTTTLocal[4] \
                    and les9GagnantsDuTTTLocal[4] == les9GagnantsDuTTTLocal[8] \
                    and not les9GagnantsDuTTTLocal[8] == 0:
                winner.append(les9GagnantsDuTTTLocal[8])

            elif les9GagnantsDuTTTLocal[2] == les9GagnantsDuTTTLocal[4] \
                    and les9GagnantsDuTTTLocal[4] == les9GagnantsDuTTTLocal[6] \
                    and not les9GagnantsDuTTTLocal[6] == 0:
                winner.append(les9GagnantsDuTTTLocal[6])

            else:
                winner.append(None)


    # Fonction qui cree un stack contenant les vainqueurs de N parties
    # avec des chemins aleatoires (pour chacun des enfants)
    # La fonction renvoie l'enfant qui a le plus de victoire parmis
    # les N parties generees. C'est donc cet enfant qui serait le choix
    # le plus optimise

    # nombreVictoireSelonEnfantI est un tableau contenant le nb de
    # victoires pour chaque branche
    # [300, 200, 3] par exemple. On choisirait dans ce cas la premiere
    # branche (celle avec 300 victoire sur 1000)

    def nPredictionMoves(self, n):

        nombreVictoireSelonEnfantI = []
        joueur = self.getNextPlayer()

        # On genere les enfants de la node
        indiceDernierJoueur = trouverIndiceDernierCoup(self.entier)
        self.nextgrids(indiceDernierJoueur % 9)

        # Pour chacun des enfants d'une node :
        for i in range(0, len(self.next)):
            nombreVictoireSelonEnfantI.append(0)

            # Pour tous les enfants x, on cree n chemins aleatoires
            # (La fonction prediction ajoute les n chemins dans le
            # tableau winner)

            for j in range(0, n):
                self.predictmove()

            # On dequeue une prediction du tableau
            for k in range(0, n):
                a = winner.pop(0)

                # Si le resultat de cette partie est egale au joueur,
                # on ajoute 1 au nombre de victoires

                if a == int(joueur,2):
                    nombreVictoireSelonEnfantI[i] = nombreVictoireSelonEnfantI[i] +1


        # On recherche ensuite le tableau qui a le plus de victoire
        if len(nombreVictoireSelonEnfantI) != 0:

            # L'index du tableau ayant le plus de victoire est la
            # branche a choisir
            indexMax = nombreVictoireSelonEnfantI.index(max(nombreVictoireSelonEnfantI))

            # Decommenter la ligne suivante pour voir le nombre de
            # victoires dans chacun des enfants (sur 1000)
            # print(nombreVictoireSelonEnfantI)

            # On imprime le noeud associe a la branche qui a eu le plus
            # de victoire
            print(self.next[indexMax].entier)


    # Fonction qui, a l'aide d'un stack, ajoute dans un tableau
    # les valeurs des entiers dans l'ordre BREADTH-FIRST (
    # traverse en largeur) et ajoute la profondeur a cote de
    # chaque node

    # ex : [12214124... 0 121313... 1 124512... 1 12421... 2]

    # PS: Le code est un peu inspire de l'algorythme de
    # BREADTH-FIRST-Search vu en cours

    def arbre(self, n):

        stack = []

        # On ajoute la root
        stack.append(self)

        # Affichage sera constitue des nodes, bien placees
        affichage = []
        profondeur = 0

        while not len(stack) == 0 and not profondeur > n:

            p = stack[0]

            # On dequeue une node
            stack = stack[1:]

            # On l'ajoute au tableau
            affichage.append(str(p.entier))

            # On ajoute le profondeur apres chaque node (pour
            # aider dans l'affichage
            affichage.append(p.depth)

            # On genere les enfants qu'on ajoute a la stack
            indiceDernierJoueur = trouverIndiceDernierCoup(p.entier)
            p.nextgrids(indiceDernierJoueur % 9)

            for c in p.next:
                stack.append(c)

            profondeur = p.depth

        # On retourne le tableau bien place, avec la profondeur a
        # code de chaque node
        return affichage



    # Fonction qui affiche l'arbre
    # Utilise la fonction arbre et affiche le tableau retourne par
    # celle-ci a l'ecran

    def afficherArbre(self, n):

        arbre = self.arbre(n)
        affichage = ""

        # On lit le tableau d'arbre
        for i in range(0, len(arbre) - 2, 2):

            # Si la profondeur de 2 nodes consecutives est identique,
            # on affiche un espace entre chaque valeurs des nodes
            if arbre[i + 1] == arbre[i + 3]:
                affichage = affichage + str(arbre[i]) + " "

            # Si la profondeur de 2 nodes consecutives est identique,
            # on saute une ligne. Ainsi, on a la forme voulu de l'arbre
            else:
                affichage = affichage + str(arbre[i]) + "\n"

        print(affichage)


    # Fonction qui echange le joueur

    def getNextPlayer(self):

        # On trouve le dernier joueur qui a joue, et on echange ce joueur avec
        # le joueur suivant
        dernierJoueur = trouverValeurCase(self.entier, trouverIndiceDernierCoup(self.entier))
        if dernierJoueur == 1:
            return "10"
        else:
            return "01"



# Voici les fonction statiques utilisees dans ce tp:

# Fonction qui trouve l'indice dans le tableau du dernier

def trouverIndiceDernierCoup(entier):
        last = int(entier) >> 162 & 127
        return last


# Fonction qui retourne la valeur a une certaine case:

def trouverValeurCase(entier, i):
        valeur = int(entier) >> ((80 - i) << 1) & 3
        return valeur


# Fonction qui transforme un string en serie de bits
# La fonction fill aussi les "0" manquant au debut de la sequence
# de bits

def strToByte(x):
        return "{0:0169b}".format(int(x))


# Fonction qui print un jeu depuis un entier donnee

def printGame(byte):
    grid = ""
    dernierCoup = trouverIndiceDernierCoup(byte)

    for i in range(0,81):

        # Si une des 81 est "01", on ajoute x
        if trouverValeurCase(byte, i) == 0:
            grid = grid + chr(46)

        # Si une des 81 est "10", on ajoute o
        elif trouverValeurCase(byte, i) == 1:
            grid = grid + chr(120)

        # Sinon, on ajoute .
        else:
            grid = grid + chr(111)

    #On indique le dernier coup en remplacant le symbole dans la suite
    # par sa majuscule respective. On capitalise donc le symbole du dernier coup
    grid = grid[:dernierCoup] + grid[dernierCoup:dernierCoup+1].upper() + grid[dernierCoup+1:]


    # On imprime le board
    imprimer3RangeesDuJeu(0, 6, grid)
    print(chr(45) * 29)
    imprimer3RangeesDuJeu(27, 33, grid)
    print(chr(45) * 29)
    imprimer3RangeesDuJeu(54, 60, grid)


# Fonction qui imprime les x et les o dans l'ordre et qui ajoute
# Les rangees ------....   et les |

def imprimer3RangeesDuJeu(firstRow, lastRow, board):

    space = chr(32)
    horizontalBar = chr(124)

    # Pour 3 rangees de donnees, on affiche successivement:
    # La premiere rangee, ensuite la deuxieme, ensuite la troisieme
    # ex : voici l'impression de la premiere rangee
    #           x o x | o x o | x o x

    for i in range(firstRow,lastRow+1,3):
        print(board[i] + space + board[i+1] + space + board[i+2] + space
              + horizontalBar + space + board[i+9] + space + board[i + 10]
              + space + board[i + 11] + space + horizontalBar + space
              + board[i + 18] + space + board[i + 19] + space + board[i + 20])


# Fonction qui determine si une entree s est un nombre

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


# Une variable globale utilisee dans le travail:
# winner contient les gagnants d'un jeu aleatoire
winner = []


# Fonction main

def main():
    user_command = []
    for arg in sys.argv:
        user_command.append(arg)

    paramP = False
    paramA = False
    profondeur = 0
    entier = "0"

    # S'il y a trop ou pas assez de parametres, on
    # ferme le programme
    if len(user_command) <= 1 or len(user_command) > 4:
        print("Parametres invalides")
        return

    # Cas 1 :Seul l'entier
    if len(user_command) == 2:
        if is_number(user_command[1]):
            entier = user_command[1]
        else:
            print("Parametres invalides")
            return

    # Cas 2 : p et entier
    if len(user_command) == 3:

        # Cas 1 : fichier.py p entier
        if user_command[1] == "p":
            if is_number(user_command[2]):
                paramP = True
                entier = user_command[2]

            else:
                print("Parametres invalides")
                return
        else:
            print("Parametres invalides")
            return

    # Cas 3 : a, profondeur et entier
    if len(user_command) == 4:

        if user_command[1] == "a":
            if is_number(user_command[2]):
                if is_number(user_command[3]):

                    profondeur = user_command[2]
                    entier = user_command[3]
                    paramA = True

                else:
                    print("Parametres invalides")
                    return
            else:
                print("Parametres invalides")
                return
        else:
            print("Parametres invalides")
            return


    # On lance le jeu
    MetaGame(entier, paramA, paramP, profondeur)


# Lancement du main
if __name__ == "__main__":
    main()
