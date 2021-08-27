"""
Geometria plana
"""

import turtle
from typing import List


class Ponto2D:
    """Ponto da geometria plana, com abscissa (x) e ordenada (y)."""

    def __init__(
        self, 
        x: float, 
        y: float, 
        des_coords: bool = True, 
        pos_coords: str = "abaixo"
    ) -> None:
        """Ponto da geometria plana.

        Args:
            x (float): abscissa (x)
            y (float): ordenada (y)
            des_coords (bool): define se as coordenadas serão desenhadas
            pos_coords (str): posição de desenho das coordenadas ('acima', 'abaixo', 'esquerda' ou 'direita')
        """
        self._x = x
        self._y = y
        pincel = turtle.Pen(shape="circle", visible=False)
        self._pincel = pincel

        pincel.speed("fastest")
        pincel.hideturtle()
        pincel.up()

        if des_coords:
            if pos_coords == "abaixo":
                pincel.setpos(x, y - 20)
            elif pos_coords == "acima":
                pincel.setpos(x, y + 5)
            elif pos_coords == "direita":
                pincel.setpos(x + 25, y - 6)
            elif pos_coords == "esquerda":
                pincel.setpos(x - 25, y - 6)

            pincel.write(f"({x}, {y})", align="center")

        # Desenha um pequeno círculo para representar o ponto
        pincel.setpos(x, y - 2)
        pincel.down()
        pincel.begin_fill()
        pincel.circle(2)
        pincel.end_fill()
        pincel.setpos(x, y)

    @property
    def x(self) -> float:
        return self._x

    @property
    def y(self) -> float:
        return self._y

    def __repr__(self) -> str:
        return f"Ponto2D: (x={self._x}, y={self._y})"

    def desenhar_linha_para(self, outro_ponto):
        """Desenha uma linha entre este ponto e outro ponto.

        Args:
            outro_ponto (Ponto2D): O outro ponto.
        """

        self._pincel.down()
        self._pincel.goto(outro_ponto.x, outro_ponto.y)
        self._pincel.goto(self.x, self.y)


class SegmentoDeReta2D:
    """Segmento de reta em duas dimensões."""

    def __init__(
        self, 
        ponto1: Ponto2D, 
        ponto2: Ponto2D
    ) -> None:
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
        return f"SegmentoDeReta2D: (ponto1={self._ponto1}; ponto2={self._ponto2})"


class Poligono2D:
    """Polígono em duas dimensões"""

    def __init__(self, *pontos: List[Ponto2D]) -> None:
        """Polígono em duas dimensões.

        Args:
            pontos (typing.List[Pontos2D]): Lista de pontos
        """
        assert len(pontos) >= 3
        # assert all(nao_colineares(pontos))
        self._vertices = tuple(pontos)
        self._arestas = self._gerar_arestas()

    def _gerar_arestas(self):
        vertices = self._vertices
        qt_vertices = len(vertices)
        arestas = []
        for i, vt in enumerate(vertices):
            arestas.append(SegmentoDeReta2D(vt, vertices[(i + 1) % qt_vertices]))


tela = turtle.Screen()
largura, altura = tela.screensize()
