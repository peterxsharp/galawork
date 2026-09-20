import os
from playwright.sync_api import sync_playwright
W,H=3840,2160
FPS=30; T=12.0; N=int(FPS*T)   # 360 frames
os.makedirs('frames',exist_ok=True)
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome',
        args=['--no-sandbox','--disable-gpu','--hide-scrollbars','--force-color-profile=srgb'])
    pg=b.new_page(viewport={'width':W,'height':H},device_scale_factor=1)
    pg.goto('file:///home/ubuntu/rbc/anim_full.html')
    pg.wait_for_function('window.assetsReady && window.assetsReady()',timeout=60000)
    clip={'x':0,'y':0,'width':W,'height':H}
    for i in range(N):
        t=i*T/N
        pg.evaluate(f'window.renderAt({t})')
        pg.screenshot(path=f'frames/f{i:04d}.png',clip=clip)
        if i%30==0: print('frame',i,flush=True)
    b.close()
print('CAPTURED',N)
