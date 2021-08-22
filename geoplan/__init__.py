"""
Geometria plana
"""

# %%
import turtle

class Ponto2D:
    """Ponto da geometria plana, com abscissa (x) e ordenada (y).
    """
    def __init__(self, x: float, y: float) -> None:
        """Ponto da geometria plana.

        Args:
            x (float): abscissa (x)
            y (float): ordenada (y)
        """
        self._x = x
        self._y = y
        self._pincel = turtle.Pen(shape='circle', visible=True)
        self._pincel.up()
        self._pincel.setpos(x, y-30)
        self._pincel.write(f'({x}, {y})', align='center')
        self._pincel.setpos(x, y)
        self._pincel.stamp()
        self._exibido = False

    @property
    def x(self) -> float:
        return self._x
    
    @property
    def y(self) -> float:
        return self._y

    def __repr__(self) -> str:
        return f'Ponto2D: (x={self._x}, y={self._y})'

    def exibir(self):
        """Exibe o ponto
        """
        self._exibido = True
        self._pincel.showturtle()

    @property
    def exibido(self) -> bool:
        return self._exibido

    def esconder(self):
        """Esconde o ponto
        """
        self._exibido = False
        self._pincel.hideturtle()

    @property
    def escondido(self) -> bool:
        return not self._exibido

    def desenhar_linha_para(self, outro_ponto):
        """Desenha uma linha entre este ponto e outro ponto.

        Args:
            outro_ponto (Ponto2D): O outro ponto.
        """
        self._pincel.down()
        self._pincel.hideturtle()
        self._pincel.goto(outro_ponto.x, outro_ponto.y)
        self._pincel.goto(self.x, self.y)
        self._pincel.showturtle()


class SegmentoDeReta2D:
    """Segmento de reta em duas dimensões.
    """
    def __init__(self, ponto1: Ponto2D, ponto2: Ponto2D) -> None:
        """Segmento de reta em duas dimensões.

        Args:
            ponto1 (Ponto2D): Primeiro ponto do segmento de reta.
            ponto2 (Ponto2D): Segundo ponto do segmento de reta.
        """
        self._ponto1 = ponto1
        self._ponto2 = ponto2
        self._ponto1.desenhar_linha_para(self._ponto2)

    @property
    def ponto1(self):
        return self._ponto1
    
    @property
    def ponto2(self):
        return self._ponto2

    def __repr__(self) -> str:
        return f'SegmentoDeReta2D: (ponto1={self._ponto1}; ponto2={self._ponto2})'


tela = turtle.Screen()
largura, altura = tela.screensize()