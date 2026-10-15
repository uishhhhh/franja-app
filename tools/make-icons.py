"""Genera assets/icon-*.png (1024x1024) para @capacitor/assets. Se ejecuta en el workflow."""
import os
from PIL import Image, ImageDraw, ImageFont
INK=(14,24,32); HOT=(255,74,28); PAPER=(243,245,244)
S=1024
def base(fg_only=False):
    im=Image.new('RGBA',(S,S),(0,0,0,0) if fg_only else INK+(255,))
    return im
def stripes(im):
    st=Image.new('RGBA',(S,S),(0,0,0,0)); d=ImageDraw.Draw(st); step=S/9
    for k in range(-6,8):
        x=S*.5+k*step*2
        d.polygon([(x,S),(x+step,S),(x+step+S*.5,0),(x+S*.5,0)],fill=HOT+(255,))
    mask=Image.new('L',(S,S),0); ImageDraw.Draw(mask).rectangle([S*.52,0,S,S],fill=255)
    a=st.split()[3]; a=Image.composite(a,Image.new('L',(S,S),0),mask)
    im.paste(st,(0,0),a)
def letra(im,scale):
    d=ImageDraw.Draw(im)
    f=None
    for p in ('/usr/share/fonts/truetype/dejavu/DejaVuSansCondensed-Bold.ttf','/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'):
        if os.path.exists(p): f=ImageFont.truetype(p,int(S*scale)); break
    f=f or ImageFont.load_default()
    bb=d.textbbox((0,0),'F',font=f); w,h=bb[2]-bb[0],bb[3]-bb[1]
    d.text(((S-w)/2-bb[0]-S*.06,(S-h)/2-bb[1]),'F',font=f,fill=PAPER+(255,))
os.makedirs('assets',exist_ok=True)
a=base(); stripes(a); letra(a,.74); a.convert('RGB').save('assets/icon-only.png')
b=base(); stripes(b); b.convert('RGB').save('assets/icon-background.png')
c=base(True); letra(c,.55); c.save('assets/icon-foreground.png')
