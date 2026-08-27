# -*- coding: utf-8 -*-
"""
Pipeline de imagem para o site da Leticia Caires.
Fonte: retrato real dela (fundo de luzes desfocado, sem banner de evento) --
substituiu a foto do evento rosa usada na primeira versao do site.
"""
from PIL import Image, ImageFilter, ImageEnhance
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ORIGEM = os.path.join(RAIZ, "assets", "originais", "foto_retrato", "leticia-retrato.jpg")
SAIDA = os.path.join(RAIZ, "assets", "img")
os.makedirs(SAIDA, exist_ok=True)


def afiar(im, fator_upscale):
    if fator_upscale > 1.15:
        im = im.filter(ImageFilter.GaussianBlur(0.4))
    raio = max(1.0, 1.4 * fator_upscale)
    return im.filter(ImageFilter.UnsharpMask(radius=raio, percent=130, threshold=2))


def preparar(caixa, largura_final, altura_final, saida, foco_y=0.5):
    im = Image.open(ORIGEM).convert("RGB")
    recorte = im.crop(caixa)
    fator = largura_final / recorte.width
    recorte = recorte.resize((largura_final, round(recorte.height * fator)), Image.LANCZOS)
    if recorte.height != altura_final:
        excedente = recorte.height - altura_final
        topo = int(excedente * foco_y)
        recorte = recorte.crop((0, topo, largura_final, topo + altura_final))
    recorte = ImageEnhance.Color(recorte).enhance(1.05)
    recorte = ImageEnhance.Contrast(recorte).enhance(1.04)
    recorte = afiar(recorte, fator)
    recorte.save(os.path.join(SAIDA, f"{saida}.jpg"), "JPEG", quality=91, subsampling=0)
    recorte.save(os.path.join(SAIDA, f"{saida}.webp"), "WEBP", quality=89)
    print(f"{saida}: {recorte.size} ok")


if __name__ == "__main__":
    # Caixa (x0, y0, x1, y1) no retrato original de 597x595
    preparar((60, 0, 536, 595), 900, 1125, "hero-leticia", foco_y=0.15)
    preparar((1, 0, 596, 595), 1000, 1000, "sobre-leticia", foco_y=0.4)
    preparar((0, 90, 597, 403), 1200, 630, "og-leticia", foco_y=0.5)
    print("done")
