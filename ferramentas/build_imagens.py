# -*- coding: utf-8 -*-
"""
Pipeline de imagem para o site da Leticia Caires.
So existe UMA foto real (evento "Amigas de Peito", fundo rosa) -- o pipeline
recorta e trata essa mesma foto para hero + sobre, sem fabricar fotos novas.
"""
from PIL import Image, ImageFilter, ImageEnhance, ImageOps, ImageDraw
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ORIGEM = os.path.join(RAIZ, "assets", "originais", "fotos_leticia_caires", "foto_evento_01.png")
SAIDA = os.path.join(RAIZ, "assets", "img")
os.makedirs(SAIDA, exist_ok=True)

VERDE_ESCURO = (30, 58, 44)  # #1E3A2C -- usado pra "tingir" a leitura da foto


def afiar(im, fator_upscale):
    if fator_upscale > 1.15:
        im = im.filter(ImageFilter.GaussianBlur(0.4))
    raio = max(1.0, 1.6 * fator_upscale)
    return im.filter(ImageFilter.UnsharpMask(radius=raio, percent=140, threshold=2))


def tingir_suave(im, cor, forca=0.16):
    """Sobrepoe uma camada de cor da marca em opacidade baixa (nao remove a
    identidade da pessoa, so tira o choque do rosa do banner de fundo)."""
    camada = Image.new("RGB", im.size, cor)
    return Image.blend(im.convert("RGB"), camada, forca)


def desfocar_fundo(im, centro_rel, raio_rel, cor_fundo, blur_fundo=48, pluma=30, forca_cor_fundo=0.85):
    """Falso efeito de profundidade de campo: o fundo (banner de patrocinador,
    cheio de logo) fica desfocado E tingido bem forte na cor da marca -- vira
    uma mancha verde abstrata, ilegivel de proposito. A pessoa fica nitida e
    com a cor natural dela, numa elipse ao redor do corpo."""
    largura, altura = im.size
    fundo = im.filter(ImageFilter.GaussianBlur(blur_fundo))
    fundo = ImageEnhance.Color(fundo).enhance(0.12)
    fundo = ImageEnhance.Brightness(fundo).enhance(0.8)
    fundo = tingir_suave(fundo, cor_fundo, forca_cor_fundo)

    mascara = Image.new("L", im.size, 0)
    desenho = ImageDraw.Draw(mascara)
    cx, cy = centro_rel[0] * largura, centro_rel[1] * altura
    rx, ry = raio_rel[0] * largura, raio_rel[1] * altura
    desenho.ellipse((cx - rx, cy - ry, cx + rx, cy + ry), fill=255)
    mascara = mascara.filter(ImageFilter.GaussianBlur(pluma))

    return Image.composite(im, fundo, mascara)


def preparar(caixa, largura_final, altura_final, saida, foco_y=0.2,
             centro_rel=(0.48, 0.36), raio_rel=(0.16, 0.45)):
    im = Image.open(ORIGEM).convert("RGB")
    recorte = im.crop(caixa)
    fator = largura_final / recorte.width
    recorte = recorte.resize((largura_final, int(recorte.height * fator)), Image.LANCZOS)
    if recorte.height != altura_final:
        excedente = recorte.height - altura_final
        topo = int(excedente * foco_y)
        recorte = recorte.crop((0, topo, largura_final, topo + altura_final))
    recorte = desfocar_fundo(recorte, centro_rel, raio_rel, VERDE_ESCURO)
    recorte = ImageEnhance.Contrast(recorte).enhance(1.05)
    recorte = afiar(recorte, fator)
    recorte.save(os.path.join(SAIDA, f"{saida}.jpg"), "JPEG", quality=90, subsampling=0)
    recorte.save(os.path.join(SAIDA, f"{saida}.webp"), "WEBP", quality=88)
    print(f"{saida}: {recorte.size} ok")


if __name__ == "__main__":
    # Caixa (x0, y0, x1, y1) na foto original de 913x915
    preparar((215, 15, 715, 640), 900, 1125, "hero-leticia", foco_y=0.2,
              centro_rel=(0.48, 0.36), raio_rel=(0.16, 0.45))
    preparar((120, 40, 850, 915), 1000, 1000, "sobre-leticia", foco_y=0.15,
              centro_rel=(0.44, 0.27), raio_rel=(0.15, 0.42))
    preparar((250, 60, 690, 500), 1200, 630, "og-leticia", foco_y=0.3,
              centro_rel=(0.5, 0.4), raio_rel=(0.16, 0.52))
    print("done")
