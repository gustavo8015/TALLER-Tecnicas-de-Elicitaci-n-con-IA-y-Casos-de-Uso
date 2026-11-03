"""Genera las imágenes de wireframes, mockups y pantallas del prototipo.

Abre fase-2-arquitectura/prototipo/index.html con Playwright y captura cada
pantalla. El parámetro ?wf=1 activa el modo wireframe (baja fidelidad).

Uso: pip install playwright pillow && playwright install chromium
     python scripts/capturas_pantallas.py
"""
from pathlib import Path
from playwright.sync_api import sync_playwright
from PIL import Image

RAIZ = Path(__file__).resolve().parent.parent
HTML = (RAIZ / "fase-2-arquitectura/prototipo/index.html").as_uri()
TMP = RAIZ / "scripts/_capturas"
TMP.mkdir(exist_ok=True)


def capturar():
    with sync_playwright() as p:
        nav = p.chromium.launch()
        pag = nav.new_page(viewport={"width": 420, "height": 820}, device_scale_factor=2)
        for s in ["s1", "s2", "s3", "s4", "s5", "s6"]:
            for wf in ["", "1"]:
                pag.goto(f"{HTML}?s={s}&wf={wf}")
                pag.wait_for_timeout(400)
                pag.locator(".phone").screenshot(path=TMP / f"{'wf' if wf else 'mk'}_{s}.png")
        nav.close()


def unir(nombres, salida):
    imgs = [Image.open(TMP / n) for n in nombres]
    w, h = imgs[0].size
    sep = 40
    lienzo = Image.new("RGB", (w * len(imgs) + sep * (len(imgs) - 1), h), "white")
    for i, im in enumerate(imgs):
        lienzo.paste(im, (i * (w + sep), 0))
    lienzo.save(salida)
    print("Generado", salida.relative_to(RAIZ))


if __name__ == "__main__":
    capturar()
    unir(["wf_s2.png", "wf_s3.png", "wf_s5.png", "wf_s6.png"], RAIZ / "fase-1-descubrimiento/wireframes/wireframes.png")
    unir(["mk_s2.png", "mk_s3.png", "mk_s5.png", "mk_s6.png"], RAIZ / "fase-2-arquitectura/mockups/mockups.png")
    unir(["mk_s1.png", "mk_s2.png", "mk_s3.png", "mk_s4.png", "mk_s5.png"], RAIZ / "fase-2-arquitectura/prototipo/pantallas-prototipo.png")
