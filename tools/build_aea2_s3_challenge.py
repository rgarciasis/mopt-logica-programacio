from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

OUT = Path('/workspace/sites/logica-programacio-smx/dist/downloads/AEA2_S3_repte_rutes.zip')

FILES = {
    'campus-byte/index.html': '''<!doctype html>
<html lang="ca">
  <head>
    <meta charset="utf-8">
    <title>Campus Byte</title>
  </head>
  <body>
    <nav>
      <a href="index.html">Inici</a>
      <a href="programa.html">Programa</a>
      <a href="contacte/contacte.html">Contacte</a>
    </nav>
    <h1>Campus Byte</h1>
    <p>Una jornada per compartir projectes digitals.</p>
    <p><a href="#horaris">Consulta els horaris</a></p>
  </body>
</html>
''',
    'campus-byte/pagines/programa.html': '''<!doctype html>
<html lang="ca">
  <head>
    <meta charset="utf-8">
    <title>Programa | Campus Byte</title>
  </head>
  <body>
    <nav>
      <a href="index.html">Inici</a>
      <a href="programa.html">Programa</a>
      <a href="contacte.html">Contacte</a>
    </nav>
    <h1>Programa</h1>
    <h2 id="horaris">Horaris</h2>
    <p>10 h · Mostra de webs</p>
    <p>12 h · Reptes de lògica</p>
  </body>
</html>
''',
    'campus-byte/contacte/contacte.html': '''<!doctype html>
<html lang="ca">
  <head>
    <meta charset="utf-8">
    <title>Contacte | Campus Byte</title>
  </head>
  <body>
    <nav>
      <a href="../../index.html">Inici</a>
      <a href="../pagines/programa.html">Programa</a>
      <a href="contacte.html">Contacte</a>
    </nav>
    <h1>Contacte</h1>
    <p>Escriu a l’equip organitzador des del Classroom.</p>
  </body>
</html>
''',
    'campus-byte/README.txt': '''REPTE CAMPUS BYTE

No moguis cap fitxer ni canviïs l’estructura de carpetes.
Troba i repara cinc avaries:
- dues a index.html;
- dues a pagines/programa.html;
- una a contacte/contacte.html.

Comprova el recorregut:
inici -> programa -> contacte -> inici
i l’enllaç que porta directament a l’apartat Horaris.
''',
}

OUT.parent.mkdir(parents=True, exist_ok=True)
with ZipFile(OUT, 'w', ZIP_DEFLATED) as archive:
    for name, content in FILES.items():
        archive.writestr(name, content)
print(OUT)
