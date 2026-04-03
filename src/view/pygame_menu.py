#---------------------------------------------------------------#
#               Universidad Central -Sede Coquimbo-             #
#                                                               #
#       Nombre del proyecto: Backtracking con heurística MRV    #
#               Nombre del archivo: pygame_menu.py              #
#               Programador: Sebastian Arredondo                #
#                   Fecha de inicio: 25-10-2025                 #
#---------------------------------------------------------------#
# Funciones:                                                    #
#   -                                                           #
#---------------------------------------------------------------#
# Notas:                                                        #
#   -                                                           #
#                                                               #
#---------------------------------------------------------------#

import pygame
import sys
import os
import random
import time

ventana = None
bg = None
font = None
ruta_insert = None
botones_actuales = None
scroll_offset = 0


def manejar_tablero(x_inicial, y_inicial, matriz, animation, delay=0.05):
    global ventana, bg, font, ruta_insert, botones_actuales

    def crear_botones(filas=9, columnas=9, ancho=40, alto=40, separacion=1.4):
        botones = []
        for fila in range(filas):
            fila_botones = []
            for columna in range(columnas):
                x = x_inicial + columna * (ancho + separacion)
                y = y_inicial + fila * (alto + separacion)
                boton_rect = pygame.Rect(x, y, ancho, alto)
                boton_info = {
                    'rect': boton_rect,
                    'numero': matriz[fila][columna],
                    'visible': False
                }
                fila_botones.append(boton_info)
            botones.append(fila_botones)
        return botones

    def dibujar_botones(botones, color_numero=(98, 95, 85)):
        for fila in botones:
            for boton in fila:
                if boton['visible'] and boton['numero'] != 0:
                    texto = font.render(str(boton['numero']), True, color_numero)
                    texto_rect = texto.get_rect(center=boton['rect'].center)
                    ventana.blit(texto, texto_rect)

    def animar(botones):
        posiciones = [(i, j) for i in range(9) for j in range(9) if botones[i][j]['numero'] != 0]
        random.shuffle(posiciones)

        for i, j in posiciones:
            botones[i][j]['visible'] = True
            pygame.mixer.Sound(ruta_insert).play()
            ventana.blit(bg, (0, 0))
            dibujar_botones(botones)
            mostrar_logs()
            pygame.display.flip()
            time.sleep(delay)

    botones = crear_botones()
    botones_actuales = botones

    if animation:
        animar(botones)
    else:
        for fila in botones:
            for boton in fila:
                boton['visible'] = True

    return botones




def mostrar_logs(eventos=None):
    global ventana, ruta_logs, scroll_offset, user_scrolled

    font_log = pygame.font.Font(None, 15)
    view_source = os.path.dirname(__file__)
    ruta_logs = os.path.join(view_source, "..", "..", "results", "logs.txt")

    if not ruta_logs or not os.path.exists(ruta_logs):
        return

    rect_logs = pygame.Rect(819.4, 192.8, 375.6, 370)
    pygame.draw.rect(ventana, (98, 95, 85), rect_logs)
    pygame.draw.rect(ventana, (180, 174, 154), rect_logs, 2)

    with open(ruta_logs, "r") as archivo:
        lineas = archivo.readlines()

    line_height = font_log.get_height()
    contenido_total = len(lineas) * line_height
    visible_altura = rect_logs.height - 20  # margen

    if 'scroll_offset' not in globals():
        scroll_offset = 0
    if 'user_scrolled' not in globals():
        user_scrolled = False

    if eventos:
        for event in eventos:
            if event.type == pygame.MOUSEWHEEL:
                mouse_pos = pygame.mouse.get_pos()
                if rect_logs.collidepoint(mouse_pos):
                    scroll_offset += event.y * 20
                    max_offset = max(0, contenido_total - visible_altura)
                    scroll_offset = max(-max_offset, min(0, scroll_offset))
                    user_scrolled = True

    if not user_scrolled and contenido_total > visible_altura:
        scroll_offset = -(contenido_total - visible_altura)

    y = rect_logs.y + 10 + scroll_offset
    for linea in lineas:
        texto = font_log.render(linea.strip(), True, (180, 174, 154))
        if rect_logs.y < y < rect_logs.bottom - 10:
            ventana.blit(texto, (rect_logs.x + 10, y))
        y += texto.get_height()


def ejecutar():
    global ventana, bg, font, ruta_insert, botones_actuales, ruta_logs

    view_source = os.path.dirname(__file__)
    ruta_bg = os.path.join(view_source, "..", "..", "gui", "bg.png")
    if not os.path.exists(ruta_bg):
        raise FileNotFoundError("No se encontró el archivo de fondo: bg.png")
    bg = pygame.image.load(ruta_bg)
    ruta_bgm = os.path.join(view_source, "..", "..", "gui", "bgm.ogg")
    ruta_click = os.path.join(view_source, "..", "..", "gui", "click.ogg")
    ruta_insert = os.path.join(view_source, "..", "..", "gui", "insert.ogg")
    ruta_logs = os.path.join(view_source, "..", "results", "logs.txt")

    pygame.init()
    pygame.mixer.init()
    font = pygame.font.Font(None, 28)

    ventana = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption('Backtracking con heurística MRV')
    pygame.mouse.set_visible(True)
    pygame.mixer.music.load(ruta_bgm)
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)

    boton_generar = pygame.Rect(120.2, 166.7, 192.4, 15.3)
    boton_insertar = pygame.Rect(119.7, 208.9, 192.4, 15.3)
    boton_resolver = pygame.Rect(115.8, 462.7, 191.7, 66.3)
    boton_cuadrante = pygame.Rect(115.4,532.4,95.2,35.3)
    boton_4 = pygame.Rect(212,532.4,95.2,35.3)

    while True:
        eventos = pygame.event.get()
        accion = None
        for event in eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if boton_generar.collidepoint(event.pos):
                    pygame.mixer.Sound(ruta_click).play()
                    accion = "generar"
                if boton_insertar.collidepoint(event.pos):
                    pygame.mixer.Sound(ruta_click).play()
                    accion = "insertar"
                if boton_resolver.collidepoint(event.pos):
                    pygame.mixer.Sound(ruta_click).play()
                    accion = "resolver"
                if boton_cuadrante.collidepoint(event.pos):
                    pygame.mixer.Sound(ruta_click).play()
                    accion = "cuadrante"
                if boton_4.collidepoint(event.pos):
                    pygame.mixer.Sound(ruta_click).play()
                    accion = "4"

        ventana.blit(bg, (0, 0))

        if botones_actuales:
            dibujar_botones(botones_actuales)
        mostrar_logs(eventos)

        pygame.display.flip()

        if accion:
            yield accion


def dibujar_botones(botones, color_numero=(98, 95, 85)):
    global ventana, font
    for fila in botones:
        for boton in fila:
            if boton['visible'] and boton['numero'] != 0:
                texto = font.render(str(boton['numero']), True, color_numero)
                texto_rect = texto.get_rect(center=boton['rect'].center)
                ventana.blit(texto, texto_rect)

def animar_resolucion(historial_matrices, x_inicial=385.1, y_inicial=197.1, delay=200):

    global botones_actuales, ventana, ruta_insert

    matriz_anterior = None

    for matriz in historial_matrices:
        if matriz is None:
            continue

        if matriz_anterior is None:
            botones_actuales = manejar_tablero(x_inicial, y_inicial, matriz, animation=False)
        else:
            botones_actuales = []
            for fila in range(9):
                fila_botones = []
                for columna in range(9):
                    x = x_inicial + columna * (40 + 1.4)
                    y = y_inicial + fila * (40 + 1.4)
                    boton_rect = pygame.Rect(x, y, 40, 40)
                    numero = matriz[fila][columna]
                    visible = numero != 0 and (matriz_anterior[fila][columna] == 0)
                    if visible:
                        pygame.mixer.Sound(ruta_insert).play()
                    fila_botones.append({'rect': boton_rect, 'numero': numero, 'visible': True})
                botones_actuales.append(fila_botones)

        ventana.blit(bg, (0, 0))
        dibujar_botones(botones_actuales)
        mostrar_logs()
        pygame.display.flip()
        pygame.time.delay(delay)

        matriz_anterior = [fila[:] for fila in matriz]
