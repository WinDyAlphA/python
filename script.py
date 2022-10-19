class Arbre:
    def __init__(self, racine=None):
        self.racine = racine  # type : Noeud


class Noeud:
    def __init__(self, v, g=None, d=None):
        self.g = g  # type Noeud
        self.d = d  # type Noeud
        self.v = v


def parcours_prefixe(arbre):
    if arbre.racine is None:
        return
    pile = [arbre.racine]
    while pile:
        noeud = pile.pop()
        print(noeud.v)
        if noeud.d is not None:
            pile.append(noeud.d)
        if noeud.g is not None:
            pile.append(noeud.g)


def parcours_infixe(arbre):
    if arbre.racine is None:
        return
    pile = [arbre.racine]
    while pile:
        noeud = pile.pop()
        if noeud.d is not None:
            pile.append(noeud.d)
        print(noeud.v)
        if noeud.g is not None:
            pile.append(noeud.g)


def parcours_postfixe(arbre):
    if arbre.racine is None:
        return
    pile = [arbre.racine]
    while pile:

        noeud = pile.pop()
        if noeud.g is not None:
            pile.append(noeud.g)
        if noeud.d is not None:
            pile.append(noeud.d)
        print(noeud.v)


def parcours_iteratif_préfixe(arbre):
    pile = [arbre.racine]
    while pile:
        noeud = pile.pop()
        print(noeud.v)
        if noeud.d is not None:
            pile.append(noeud.d)
        if noeud.g is not None:
            pile.append(noeud.g)


def parcours_iteratif_infixe(arbre):
    pile = [arbre.racine]
    while pile:
        noeud = pile.pop()
        if noeud.d is not None:
            pile.append(noeud.d)
        print(noeud.v)
        if noeud.g is not None:
            pile.append(noeud.g)


def parcours_iteratif_sufixe(arbre):
    pile = [arbre.racine]
    while pile:
        noeud = pile.pop()
        if noeud.d is not None:
            pile.append(noeud.d)
        if noeud.g is not None:
            pile.append(noeud.g)
        print(noeud.v)

# parcours iteratif avec file


def parcours_iteratif_prefixe_largeur(arbre):
    pile = [arbre.racine]
    while pile:
        noeud = pile.pop(0)
        print(noeud.v)
        if noeud.g is not None:
            pile.append(noeud.g)
        if noeud.d is not None:
            pile.append(noeud.d)


def taille(arbre):
    pile = [arbre.racine]
    count = 0
    while pile:
        noeud = pile.pop()
        if noeud.d is not None:
            pile.append(noeud.d)
        if noeud.g is not None:
            pile.append(noeud.g)
        count += 1
    print(count)


def feuille(arbre):
    pile = [arbre.racine]
    count = 0
    while pile:
        noeud = pile.pop()
        if noeud.d is not None:
            pile.append(noeud.d)
        if noeud.g is not None:
            pile.append(noeud.g)
        if noeud.g is None:
            if noeud.d is None:

                count += 1
    print(count)


if __name__ == '__main__':
    arbre = Arbre()
    arbre.racine = Noeud(1)
    arbre.racine.g = Noeud(2)
    arbre.racine.d = Noeud(3)
    arbre.racine.g.g = Noeud(4)
    arbre.racine.g.d = Noeud(5)
    arbre.racine.d.g = Noeud(6)

    parcours_iteratif_préfixe(arbre)
    print("\n-------\n")
    parcours_iteratif_prefixe_largeur(arbre)
    print("\n-------\n")
    taille(arbre)
    print("\n-------\n")
    feuille(arbre)
    print("\n-------\n")
    feuille(arbre)
    print("\n-------\n")
