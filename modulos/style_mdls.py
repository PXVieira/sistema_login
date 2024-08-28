from rich import print


# cores
def verde(self):
    cor = f"[green]{self}[/]"
    return cor


def azul(self):
    cor = f"[blue]{self}[/]"
    return cor


def vermelho(self):
    cor = f"[red]{self}[/]"
    return cor


def preto(self):
    cor = f"[black]{self}[/]"
    return cor


# formatação de textos
def sublinhado(self):
    texto = f"[u]{self}[/]"
    return texto


def negrito(self):
    texto = f"[b]{self}[/]"
    return texto


def tachado(self):
    texto = f"[s]{self}[/]"
    return texto


def italico(self):
    texto = f"[i]{self}[/]"
    return texto


def linha():
    t = print(f'{"-":-^100}')
    return t


def titulo(txt):
    linha()
    print(f"{txt:^100}")
    linha()
