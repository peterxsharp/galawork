import sys
from playwright.sync_api import sync_playwright
W,H=int(sys.argv[1]),int(sys.argv[2]);t=float(sys.argv[3]);out=sys.argv[4]
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox','--disable-gpu','--hide-scrollbars','--force-color-profile=srgb'])
    pg=b.new_page(viewport={'width':W,'height':H},device_scale_factor=1)
    pg.goto('file:///home/ubuntu/rbc/gala_full.html')
    pg.wait_for_function('window.assetsReady && window.assetsReady()',timeout=30000)
    pg.evaluate(f'window.renderAt({t})');pg.wait_for_timeout(80)
    pg.screenshot(path=out,clip={'x':0,'y':0,'width':W,'height':H});b.close()
print('ok',out)
