import pygame as py
from funciones import rotar_imagen
personaje_quieto_derecha = [py.image.load("Recursos/SHAGY EAT/1.png"),
                            py.image.load("Recursos/SHAGY EAT/2.png"),
                            py.image.load("Recursos/SHAGY EAT/3.png"),
                            py.image.load("Recursos/SHAGY EAT/4.png"),
                            py.image.load("Recursos/SHAGY EAT/5.png"),
                            py.image.load("Recursos/SHAGY EAT/6.png"),
                            py.image.load("Recursos/SHAGY EAT/7.png"),
                            py.image.load("Recursos/SHAGY EAT/8.png"),
                            py.image.load("Recursos/SHAGY EAT/9.png"),
                            py.image.load("Recursos/SHAGY EAT/10.png"),
                            py.image.load("Recursos/SHAGY EAT/11.png"),
                            py.image.load("Recursos/SHAGY EAT/12.png"),
                            py.image.load("Recursos/SHAGY EAT/13.png"),
                            py.image.load("Recursos/SHAGY EAT/14.png"),
                            py.image.load("Recursos/SHAGY EAT/15.png"),
                            py.image.load("Recursos/SHAGY EAT/16.png"),
                            py.image.load("Recursos/SHAGY EAT/17.png"),
                            py.image.load("Recursos/SHAGY EAT/18.png")]
personaje_quieto_izquierda = rotar_imagen(personaje_quieto_derecha)

personaje_camina_derecha = [py.image.load("Recursos/SHAGY WALK/0.png"),
                            py.image.load("Recursos/SHAGY WALK/1.png"),
                            py.image.load("Recursos/SHAGY WALK/2.png"),
                            py.image.load("Recursos/SHAGY WALK/3.png"),
                            py.image.load("Recursos/SHAGY WALK/4.png"),
                            py.image.load("Recursos/SHAGY WALK/5.png"),
                            py.image.load("Recursos/SHAGY WALK/6.png"),
                            py.image.load("Recursos/SHAGY WALK/7.png"),
                            py.image.load("Recursos/SHAGY WALK/8.png"),
                            py.image.load("Recursos/SHAGY WALK/9.png")]
personaje_camina_izquierda = rotar_imagen(personaje_camina_derecha)

personaje_salta_derecha = [py.image.load("Recursos/SHAGY JUMP/1.png"),
                           py.image.load("Recursos/SHAGY JUMP/2.png"),
                           py.image.load("Recursos/SHAGY JUMP/3.png"),
                           py.image.load("Recursos/SHAGY JUMP/4.png"),
                           py.image.load("Recursos/SHAGY JUMP/5.png"),
                           py.image.load("Recursos/SHAGY JUMP/6.png"),
                           py.image.load("Recursos/SHAGY JUMP/7.png"),
                           py.image.load("Recursos/SHAGY JUMP/8.png"),
                           py.image.load("Recursos/SHAGY JUMP/9.png")]
personaje_salta_izquierda = rotar_imagen(personaje_salta_derecha)

enemigo_quieto_izquierda = [py.image.load("Recursos/Soldado/1.png"),
                            py.image.load("Recursos/Soldado/1.png"),
                            py.image.load("Recursos/Soldado/1.png"),
                            py.image.load("Recursos/Soldado/2.png"),
                            py.image.load("Recursos/Soldado/2.png"),
                            py.image.load("Recursos/Soldado/2.png"),
                            py.image.load("Recursos/Soldado/3.png"),
                            py.image.load("Recursos/Soldado/3.png"),
                            py.image.load("Recursos/Soldado/3.png"),
                            py.image.load("Recursos/Soldado/4.png"),
                            py.image.load("Recursos/Soldado/4.png"),
                            py.image.load("Recursos/Soldado/4.png"),
                            py.image.load("Recursos/Soldado/3.png"),
                            py.image.load("Recursos/Soldado/3.png"),
                            py.image.load("Recursos/Soldado/3.png"),
                            py.image.load("Recursos/Soldado/2.png"),
                            py.image.load("Recursos/Soldado/2.png"),
                            py.image.load("Recursos/Soldado/2.png"),]

enemigo_dispara = [py.image.load("Recursos/soldado_shoot/1.png"),
                   py.image.load("Recursos/soldado_shoot/1.png"),
                   py.image.load("Recursos/soldado_shoot/1.png"),
                   py.image.load("Recursos/soldado_shoot/2.png"),
                   py.image.load("Recursos/soldado_shoot/2.png"),
                   py.image.load("Recursos/soldado_shoot/2.png"),
                   py.image.load("Recursos/soldado_shoot/3.png"),
                   py.image.load("Recursos/soldado_shoot/3.png"),
                   py.image.load("Recursos/soldado_shoot/3.png"),
                   py.image.load("Recursos/soldado_shoot/4.png"),
                   py.image.load("Recursos/soldado_shoot/4.png"),
                   py.image.load("Recursos/soldado_shoot/4.png"),
                   py.image.load("Recursos/soldado_shoot/5.png"),
                   py.image.load("Recursos/soldado_shoot/5.png"),
                   py.image.load("Recursos/soldado_shoot/5.png"),
                   py.image.load("Recursos/soldado_shoot/6.png"),
                   py.image.load("Recursos/soldado_shoot/6.png"),
                   py.image.load("Recursos/soldado_shoot/6.png"),
                   py.image.load("Recursos/soldado_shoot/7.png"),
                   py.image.load("Recursos/soldado_shoot/7.png"),
                   py.image.load("Recursos/soldado_shoot/7.png"),
                   py.image.load("Recursos/soldado_shoot/4.png"),
                   py.image.load("Recursos/soldado_shoot/4.png"),
                   py.image.load("Recursos/soldado_shoot/4.png"),
                   py.image.load("Recursos/soldado_shoot/3.png"),
                   py.image.load("Recursos/soldado_shoot/3.png"),
                   py.image.load("Recursos/soldado_shoot/3.png"),
                   py.image.load("Recursos/soldado_shoot/2.png"),
                   py.image.load("Recursos/soldado_shoot/2.png"),
                   py.image.load("Recursos/soldado_shoot/2.png"),]

enemigo_muere = [py.image.load("Recursos/soldado_muere/1.png"),
                 py.image.load("Recursos/soldado_muere/2.png"),
                 py.image.load("Recursos/soldado_muere/3.png"),
                 py.image.load("Recursos/soldado_muere/4.png"),
                 py.image.load("Recursos/soldado_muere/5.png"),
                 py.image.load("Recursos/soldado_muere/6.png"),
                 py.image.load("Recursos/soldado_muere/7.png"),
                 py.image.load("Recursos/soldado_muere/8.png"),
                 py.image.load("Recursos/soldado_muere/9.png"),
                 py.image.load("Recursos/soldado_muere/10.png"),
                 py.image.load("Recursos/soldado_muere/11.png"),
                 py.image.load("Recursos/soldado_muere/12.png"),]

explosion = [py.image.load("Recursos/Explosion/1.png"),
             py.image.load("Recursos/Explosion/2.png"),
             py.image.load("Recursos/Explosion/3.png"),
             py.image.load("Recursos/Explosion/4.png"),
             py.image.load("Recursos/Explosion/5.png"),
             py.image.load("Recursos/Explosion/6.png"),
             py.image.load("Recursos/Explosion/7.png"),
             py.image.load("Recursos/Explosion/8.png"),
             py.image.load("Recursos/Explosion/9.png"),
             py.image.load("Recursos/Explosion/10.png"),
             py.image.load("Recursos/Explosion/11.png"),
             py.image.load("Recursos/Explosion/12.png"),
             py.image.load("Recursos/Explosion/13.png"),
             py.image.load("Recursos/Explosion/14.png"),
             py.image.load("Recursos/Explosion/15.png"),
             py.image.load("Recursos/Explosion/16.png"),
             py.image.load("Recursos/Explosion/17.png"),
             py.image.load("Recursos/Explosion/18.png"),
             py.image.load("Recursos/Explosion/19.png"),
             py.image.load("Recursos/Explosion/20.png"),
             py.image.load("Recursos/Explosion/21.png"),
             py.image.load("Recursos/Explosion/22.png"),
             py.image.load("Recursos/Explosion/23.png"),
             py.image.load("Recursos/Explosion/24.png"),]

corazones = [py.image.load("Recursos/Items/corazones/1.png"),
            py.image.load("Recursos/Items/corazones/2.png"),
            py.image.load("Recursos/Items/corazones/3.png"),
            py.image.load("Recursos/Items/corazones/4.png"),
            py.image.load("Recursos/Items/corazones/5.png"),
            py.image.load("Recursos/Items/corazones/6.png"),
            py.image.load("Recursos/Items/corazones/7.png"),
            py.image.load("Recursos/Items/corazones/8.png"),
            py.image.load("Recursos/Items/corazones/9.png"),
            py.image.load("Recursos/Items/corazones/10.png"),
            py.image.load("Recursos/Items/corazones/11.png"),
            py.image.load("Recursos/Items/corazones/12.png"),
            py.image.load("Recursos/Items/corazones/13.png"),
            py.image.load("Recursos/Items/corazones/14.png"),
            py.image.load("Recursos/Items/corazones/15.png"),
            py.image.load("Recursos/Items/corazones/16.png"),
            py.image.load("Recursos/Items/corazones/17.png"),
            py.image.load("Recursos/Items/corazones/18.png")]

lista_corazones = []
for list in corazones:
    list = py.transform.scale(list, (55,55))
    lista_corazones.append(list)