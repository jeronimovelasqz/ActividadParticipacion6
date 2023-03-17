class Casa:
    def __init__(self):
        self.mano = self.mano

class Mano:
    def __init__(self):
        pass

    def es_blackjack(self) -> bool:
        pass

    def valor_mano(self, carta):
        pass

    def destapar_oculta(self, carta):
        pass

    def comparar_manos(self, cartas):
        pass

class Carta:
    def __init__(self, pinta: str, valor: str, tapado: bool):
        self.pinta = pinta
        self.valor = valor
        self.tapado = tapado


class Baraja:
    def __init__(self):
        pass

    def revolver(self) -> Carta:
        pass

    def repartir_cartas(self, tapada) -> Carta:
        pass

class BlackJack:
    def __init__(self, apuesta: int):
        self.apuesta = apuesta

    def registrar_jugador(self, nombre):
        pass

    def iniciar_juego(self, apuesta):
        pass

    def quitar_fichas_o_agregar(self, fichas):
        pass

    def reiniciar(self):
        pass


class Jugador:
    def __init__(self, fichas:int , nombre: str):
        self.fichas = fichas
        self.nombre = nombre

    def inicializar_mano(self, cartas):
        pass


