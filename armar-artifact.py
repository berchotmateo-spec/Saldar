# Arma la vista previa para el Artifact de claude.ai a partir de index.html:
# sin doctype/html/head/body propios (los pone el Artifact), título corto, y
# solo lo del <head> que sirve en la vista previa (fuentes y estilos).
#
# Uso: python3 armar-artifact.py [index.html] [salida.html]
import re, sys
src = sys.argv[1] if len(sys.argv) > 1 else "index.html"
dst = sys.argv[2] if len(sys.argv) > 2 else "saldar-artifact.html"
s = open(src, encoding="utf-8").read()
head = re.search(r"<head>(.*?)</head>", s, re.S).group(1)
body = re.search(r"<body>(.*?)</body>", s, re.S).group(1)
links = re.findall(r'<link rel="preconnect"[^>]*>|<link href="https://fonts\.googleapis\.com[^>]*>', head)
style = re.search(r"<style>.*?</style>", head, re.S).group(0)
out = "<title>Saldar</title>\n" + "\n".join(links) + "\n" + style + "\n" + body.strip() + "\n"
open(dst, "w", encoding="utf-8").write(out)
print(len(links), "links,", len(out), "bytes")
