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


def preparar(caixa, largura_final, altura_final, saida, foco_y=0.2):
    """Recorte fechado no rosto/ombros -- fechado o bastante pra sobrar so uma
    tira fina do banner de patrocinador (sem precisar de mascara nem tingir
    de verde por cima dela)."""
    im = Image.open(ORIGEM).convert("RGB")
    recorte = im.crop(caixa)
    fator = largura_final / recorte.width
    recorte = recorte.resize((largura_final, int(recorte.height * fator)), Image.LANCZOS)
    if recorte.height != altura_final:
        excedente = recorte.height - altura_final
        topo = int(excedente * foco_y)
        recorte = recorte.crop((0, topo, largura_final, topo + altura_final))
    recorte = ImageEnhance.Color(recorte).enhance(0.94)
    recorte = ImageEnhance.Contrast(recorte).enhance(1.05)
    recorte = afiar(recorte, fator)
    recorte.save(os.path.join(SAIDA, f"{saida}.jpg"), "JPEG", quality=90, subsampling=0)
    recorte.save(os.path.join(SAIDA, f"{saida}.webp"), "WEBP", quality=88)
    print(f"{saida}: {recorte.size} ok")


if __name__ == "__main__":
    # Caixa (x0, y0, x1, y1) na foto original de 913x915 -- fechado no busto,
    # so sobra uma faixa fina de banner nas bordas.
    preparar((300, 60, 645, 460), 900, 1125, "hero-leticia", foco_y=0.05)
    preparar((300, 60, 645, 460), 1000, 1000, "sobre-leticia", foco_y=0.4)
    preparar((280, 50, 665, 480), 1200, 630, "og-leticia", foco_y=0.35)
    print("done")
