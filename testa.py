from geoplan import Ponto2D, SegmentoDeReta2D, tela, altura, largura, Poligono2D

def testa_segmento():
    tela.title('Teste de pontos')

    p1 = Ponto2D(-largura//4, 0, des_coords=True, pos_coords='esquerda')
    p2 = Ponto2D(largura//4, 0, des_coords=True, pos_coords='direita')

    s1 = SegmentoDeReta2D(p1, p2)

    tela.exitonclick()

def testa_poligono():

    pt_1 = Ponto2D(130, -130)
    pt_2 = Ponto2D(130, 130, pos_coords='acima')
    pt_3 = Ponto2D(-130, 130, pos_coords='acima')
    pt_4 = Ponto2D(-130, -130)

    pol_1 = Poligono2D(pt_1, pt_2, pt_3, pt_4)

    pt_5 = Ponto2D(0, 0)
    pt_6 = Ponto2D(100, 0, pos_coords='direita')
    pt_7 = Ponto2D(0, 100, pos_coords='acima')

    pol_2 = Poligono2D(pt_5, pt_6, pt_7)

    tela.exitonclick()
