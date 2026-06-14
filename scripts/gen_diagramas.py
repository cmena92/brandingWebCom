#!/usr/bin/env python3
"""Genera los diagramas del libro de marca WebCom (PNG, renderizan bien en GitHub).
Uso: python scripts/gen_diagramas.py   (desde la raiz del repo)
Requiere: Pillow.  Fuentes: usa Arial de Windows; cae a default si no esta.
"""
from PIL import Image, ImageDraw, ImageFont
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets", "diagramas")
APP = os.path.join(ROOT, "assets", "aplicaciones")
os.makedirs(OUT, exist_ok=True)
os.makedirs(APP, exist_ok=True)

# Paleta
BG="#0B0D1A"; SURFACE="#14172E"; SURF2="#1E2240"; TEXT="#EAECF5"; MUTED="#9AA0BE"
AZUL="#20217A"; AZULB="#4D5BFF"; ROJO="#E30613"; AMBAR="#FFB020"; VERDE="#2BD9A8"; WHITE="#FFFFFF"

FONTS = ["C:/Windows/Fonts/arial.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"]
BOLD  = ["C:/Windows/Fonts/arialbd.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"]

def font(sz, bold=False):
    for p in (BOLD if bold else FONTS):
        if os.path.exists(p):
            return ImageFont.truetype(p, sz)
    return ImageFont.load_default()

def logo(name):
    return Image.open(os.path.join(ROOT, "assets", "logos", name)).convert("RGBA")

def fit(img, w=None, h=None):
    iw, ih = img.size
    if w: h2 = int(ih * w / iw); return img.resize((w, h2), Image.LANCZOS)
    if h: w2 = int(iw * h / ih); return img.resize((w2, h), Image.LANCZOS)
    return img

def dashed_rect(d, box, color, dash=14, gap=10, width=2):
    x0,y0,x1,y1 = box
    def line(a,b,horiz):
        x,y = a
        while (x < b[0]) if horiz else (y < b[1]):
            if horiz: d.line([(x,y),(min(x+dash,b[0]),y)], fill=color, width=width); x+=dash+gap
            else:     d.line([(x,y),(x,min(y+dash,b[1]))], fill=color, width=width); y+=dash+gap
    line((x0,y0),(x1,y0),True); line((x0,y1),(x1,y1),True)
    line((x0,y0),(x0,y1),False); line((x1,y0),(x1,y1),False)

def ctext(d, xy, t, f, fill, anchor="la"):
    d.text(xy, t, font=f, fill=fill, anchor=anchor)

# ---------- 1. PALETA ----------
def paleta():
    W,H=1280,640; im=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(im)
    ctext(d,(48,40),"Paleta WebCom",font(40,True),TEXT)
    ctext(d,(48,92),"Cada color es un ROL, no un gusto.",font(20),MUTED)
    rows=[("Azul · autoridad",AZUL),("Azul · acción",AZULB),("Rojo · exposición",ROJO),
          ("Ámbar · atención",AMBAR),("Verde · en control",VERDE),
          ("Lienzo",BG),("Panel",SURFACE),("Texto",TEXT)]
    cols=4; cw=(W-96-30*(cols-1))//cols; ch=210; x0=48; y0=150
    for i,(name,hexc) in enumerate(rows):
        r,c=divmod(i,cols); x=x0+c*(cw+30); y=y0+r*(ch+24)
        d.rounded_rectangle([x,y,x+cw,y+ch],12,fill=SURF2)
        d.rounded_rectangle([x+14,y+14,x+cw-14,y+120],8,fill=hexc,
                            outline="#FFFFFF" if hexc==BG else None)
        ctext(d,(x+18,y+136),name,font(18,True),TEXT)
        ctext(d,(x+18,y+166),hexc.upper(),font(17),MUTED)
    im.save(os.path.join(OUT,"color-paleta.png")); print("ok color-paleta.png")

# ---------- 2. AREA DE PROTECCION ----------
def proteccion():
    W,H=1100,640; im=Image.new("RGB",(W,H),WHITE); d=ImageDraw.Draw(im)
    ctext(d,(48,36),"Área de protección",font(30,True),"#111111")
    ctext(d,(48,82),"Margen mínimo libre alrededor del logo = X (½ de la altura del logo).",font(18),"#444444")
    lg=fit(logo("wccr-logo-rojo.png"),w=420)
    bbox=lg.getbbox(); lg=lg.crop(bbox); lw,lh=lg.size
    cx,cy=W//2,360; lx,ly=cx-lw//2,cy-lh//2
    unit=lh//2  # area de proteccion = 1/2 de la altura del logo
    im.paste(lg,(lx,ly),lg)
    dashed_rect(d,(lx-unit,ly-unit,lx+lw+unit,ly+lh+unit),ROJO,width=2)
    # indicador de la unidad X dentro del margen superior
    my=(ly-unit+ly)//2
    d.rectangle([cx-unit//2,my-5,cx+unit//2,my+5],fill=AZULB)
    ctext(d,(cx+unit//2+12,my),"X = ½ de la altura",font(17,True),AZUL,anchor="lm")
    ctext(d,(48,H-46),"Nada de texto, otros logos ni bordes dentro de la zona punteada.",font(16),ROJO)
    im.save(os.path.join(OUT,"logo-area-proteccion.png")); print("ok logo-area-proteccion.png")

# ---------- 3. USOS INCORRECTOS ----------
def incorrectos():
    W,H=1180,460; im=Image.new("RGB",(W,H),WHITE); d=ImageDraw.Draw(im)
    ctext(d,(48,30),"Usos incorrectos",font(30,True),"#111111")
    base=fit(logo("wccr-logo-rojo.png"),w=210)
    bb=base.getbbox(); base=base.crop(bb)
    cells=[]
    # estirar
    s=base.resize((base.width,int(base.height*1.9)),Image.LANCZOS); cells.append(("No deformar",s))
    # rotar
    r=base.rotate(18,expand=True,resample=Image.BICUBIC); cells.append(("No rotar",r))
    # recolorar (grayscale)
    g=base.convert("LA").convert("RGBA"); cells.append(("No cambiar el color",g))
    # fondo de bajo contraste
    cells.append(("No sobre fondos sin contraste",base))
    cols=4; cw=(W-96-24*(cols-1))//cols; ch=300; x0=48; y0=96
    for i,(cap,img) in enumerate(cells):
        x=x0+i*(cw+24); y=y0
        bg = "#E9C9CB" if i==3 else "#F4F4F6"
        d.rounded_rectangle([x,y,x+cw,y+ch-60],12,fill=bg)
        im_w=min(cw-40,img.width); ph=fit(img,w=im_w)
        px=x+(cw-ph.width)//2; py=y+(ch-60-ph.height)//2
        im.paste(ph,(px,py),ph if ph.mode=="RGBA" else None)
        # X roja
        m=18; d.line([(x+m,y+m),(x+cw-m,y+ch-60-m)],fill=ROJO,width=6)
        d.line([(x+cw-m,y+m),(x+m,y+ch-60-m)],fill=ROJO,width=6)
        ctext(d,(x+cw//2,y+ch-44),cap,font(16,True),"#111111",anchor="ma")
    im.save(os.path.join(OUT,"logo-usos-incorrectos.png")); print("ok logo-usos-incorrectos.png")

# ---------- 4. TARJETA ----------
def tarjeta():
    W,H=1050,600; im=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(im)
    d.rounded_rectangle([40,40,W-40,H-40],20,fill=SURFACE,outline=AZUL,width=2)
    lg=fit(logo("wccr-logo-blanco.png"),w=300); im.paste(lg,(80,90),lg)
    d.line([(80,250),(80+300,250)],fill=ROJO,width=4)
    ctext(d,(80,290),"Crisman Mena",font(34,True),TEXT)
    ctext(d,(80,336),"Dirección de TI",font(20),MUTED)
    ctext(d,(80,470),"webcom.cr",font(20,True),AZULB)
    ctext(d,(80,502),"crisman@webcom.cr",font(18),MUTED)
    ctext(d,(W-300,H-150),'"Si no lo corremos\nnosotros, no te\nlo vendemos."',font(20,True),MUTED)
    im.save(os.path.join(APP,"tarjeta.png")); print("ok tarjeta.png")

# ---------- 5. FIRMA DE CORREO ----------
def firma():
    W,H=900,260; im=Image.new("RGB",(W,H),WHITE); d=ImageDraw.Draw(im)
    lg=fit(logo("wccr-logo-rojo.png"),w=210); im.paste(lg,(40,70),lg)
    d.line([(290,50),(290,210)],fill="#DDDDDD",width=2)
    ctext(d,(320,60),"Crisman Mena",font(26,True),"#111111")
    ctext(d,(320,96),"Dirección de TI · WebCom Costa Rica",font(18),"#555555")
    ctext(d,(320,140),"webcom.cr  ·  crisman@webcom.cr",font(17),AZUL)
    ctext(d,(320,176),"Si no lo corremos nosotros, no te lo vendemos.",font(15,True),ROJO)
    im.save(os.path.join(APP,"firma-correo.png")); print("ok firma-correo.png")

if __name__=="__main__":
    paleta(); proteccion(); incorrectos(); tarjeta(); firma()
    print("Diagramas generados en assets/diagramas y assets/aplicaciones")
