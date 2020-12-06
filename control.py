from pygame import K_w,K_s,K_a,K_d,K_q,K_e,K_LEFT,K_RIGHT,K_UP,K_DOWN,K_z,K_x
from pygame.key import get_pressed
from numpy import array

class Control:
    def __init__(self):
        self.key = array([-1.5, 0.0, -0.5, 0.0, 0.0, 1.0])
        '''key[0] - W S 
           key[1] - A D
           key[2] - W S 
           key[3] - LEFT RIGHT 
           key[4] - UP DOWN
           key[5] - Z X 
        '''

    def pressed_keys(self):
        keys = get_pressed()

        seisCentesimas=0.06
        tecla=self.key[0]
        if keys[K_w]: #no se usa elif por si se presionan varias teclas a la vez
            tecla -= seisCentesimas
        if keys[K_s]:
            tecla += seisCentesimas
            
        tecla=self.key[1]
        cuatroCentesimas=0.04
        if keys[K_a]:
            tecla -= cuatroCentesimas
        if keys[K_d]:
            tecla += cuatroCentesimas
            
        tecla=self.key[2]
        if keys[K_q]:
            tecla += cuatroCentesimas
        if keys[K_e]:
            tecla -= cuatroCentesimas
            
        tecla=self.key[3]
        dosCentesimas=0.02
        if keys[K_LEFT]:
            tecla += dosCentesimas
        if keys[K_RIGHT]:
            tecla -= dosCentesimas
            
        tecla=self.key[4]
        if keys[K_UP]:
            tecla += dosCentesimas
        if keys[K_DOWN]:
            tecla -= dosCentesimas
            
        tecla=self.key[5]
        unoFloat=1.0
        if keys[K_z]:
            tecla -= unoFloat
            tecla = max(1, tecla)
        if keys[K_x]:
            tecla += unoFloat
            tecla = min(6.0, tecla)