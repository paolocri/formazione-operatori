# Rigenera index.html della PWA a partire dalla pagina dell'artifact (../app-formazione/index.html)
import os, re
here = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(here, '../app-formazione/index.html')).read()
title_end = src.index('</title>') + len('</title>')
body_start = src.index('<header class="topbar">')
headpart = src[title_end:body_start].replace('<meta name="claude:viewport-fit-sides" content="cover">', '')
# Caratteri dal nostro sito invece che da Google Fonts (privacy: niente IP inviato a Google)
headpart = re.sub(r'<link rel="preconnect"[^>]*>\n?', '', headpart)
headpart = re.sub(r'<link rel="stylesheet" href="https://fonts.googleapis.com[^>]*>', '<link rel="stylesheet" href="fonts/fonts.css">', headpart)
assert 'googleapis' not in headpart and 'gstatic' not in headpart
body = src[body_start:].replace('render();\n</script>', '''render();
if ("serviceWorker" in navigator) addEventListener("load", () => navigator.serviceWorker.register("sw.js").catch(()=>{}));
</script>''')
assert 'serviceWorker' in body
out = f'''<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Operatori Caritas</title>
<meta name="description" content="Servizi della Caritas diocesana di Vercelli, notizie e materiali di Caritas Italiana per gli operatori.">
<meta name="theme-color" content="#9e0b23">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" href="icons/favicon-32.png" sizes="32x32">
<link rel="apple-touch-icon" href="icons/apple-touch-icon.png">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="Operatori">
<style>
:root{{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px);color-scheme:light}}
body{{margin:0;font:14px system-ui,sans-serif}}
img{{max-width:100%}}
[hidden]{{display:none!important}}
</style>{headpart}
</head>
<body>
{body}
</body>
</html>
'''
open(os.path.join(here, 'index.html'), 'w').write(out)
sw = os.path.join(here, 'sw.js'); t = open(sw).read()
n = int(re.search(r'formazione-v(\d+)', t).group(1)) + 1
open(sw, 'w').write(re.sub(r'formazione-v\d+', f'formazione-v{n}', t))
print('ok, versione', n)
