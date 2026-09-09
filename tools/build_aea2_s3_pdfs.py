from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate, Frame, KeepTogether, PageBreak, PageTemplate,
    Paragraph, Preformatted, Spacer, Table, TableStyle,
)

OUT = Path('/workspace/sites/logica-programacio-smx/dist/downloads')
OUT.mkdir(parents=True, exist_ok=True)

INK = colors.HexColor('#10151d')
PAPER = colors.HexColor('#f3f5f2')
WHITE = colors.white
MUTED = colors.HexColor('#69717d')
LINE = colors.HexColor('#d8ddd8')
ACID = colors.HexColor('#ccff3d')
VIOLET = colors.HexColor('#6e5cff')
CYAN = colors.HexColor('#25d7d0')
PALE_VIOLET = colors.HexColor('#eeeaff')
PALE_CYAN = colors.HexColor('#e9fffb')
PALE_ACID = colors.HexColor('#edffd1')
PALE_ORANGE = colors.HexColor('#fff0df')

FONT_DIR = Path('/usr/share/fonts/truetype/dejavu')
pdfmetrics.registerFont(TTFont('DV', str(FONT_DIR / 'DejaVuSans.ttf')))
pdfmetrics.registerFont(TTFont('DV-Bold', str(FONT_DIR / 'DejaVuSans-Bold.ttf')))
pdfmetrics.registerFont(TTFont('Mono', str(FONT_DIR / 'DejaVuSansMono.ttf')))

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='TitleX', fontName='DV-Bold', fontSize=26, leading=29, textColor=INK, spaceAfter=8))
styles.add(ParagraphStyle(name='SubX', fontName='DV', fontSize=11.5, leading=16, textColor=MUTED, spaceAfter=12))
styles.add(ParagraphStyle(name='H1X', fontName='DV-Bold', fontSize=18, leading=22, textColor=INK, spaceBefore=6, spaceAfter=8))
styles.add(ParagraphStyle(name='H2X', fontName='DV-Bold', fontSize=12.5, leading=16, textColor=VIOLET, spaceBefore=5, spaceAfter=5))
styles.add(ParagraphStyle(name='BodyX', fontName='DV', fontSize=9.5, leading=14, textColor=INK, spaceAfter=6))
styles.add(ParagraphStyle(name='SmallX', fontName='DV', fontSize=8.2, leading=11.5, textColor=MUTED))
styles.add(ParagraphStyle(name='TinyX', fontName='DV', fontSize=7.2, leading=9.2, textColor=MUTED))
styles.add(ParagraphStyle(name='CodeX', fontName='Mono', fontSize=7.7, leading=11, textColor=WHITE))
styles.add(ParagraphStyle(name='CallX', fontName='DV-Bold', fontSize=10.2, leading=14, textColor=INK))
styles.add(ParagraphStyle(name='CenterX', fontName='DV-Bold', fontSize=10.5, leading=13, alignment=1, textColor=INK))


def P(text, style='BodyX'):
    return Paragraph(text, styles[style])


def code(text, width=170*mm):
    return Table([[Preformatted(text, styles['CodeX'])]], colWidths=[width], style=TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), INK),
        ('LEFTPADDING', (0, 0), (-1, -1), 9), ('RIGHTPADDING', (0, 0), (-1, -1), 9),
        ('TOPPADDING', (0, 0), (-1, -1), 8), ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    ]))


def box(title, body, fill=PALE_VIOLET, accent=VIOLET):
    return Table([[P(title, 'CallX')], [P(body, 'BodyX')]], colWidths=[170*mm], style=TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), fill), ('LINEBEFORE', (0, 0), (0, -1), 4, accent),
        ('LEFTPADDING', (0, 0), (-1, -1), 10), ('RIGHTPADDING', (0, 0), (-1, -1), 10),
        ('TOPPADDING', (0, 0), (-1, 0), 8), ('TOPPADDING', (0, 1), (-1, 1), 1),
        ('BOTTOMPADDING', (0, -1), (-1, -1), 8),
    ]))


def grid(items, cols=2, fill=WHITE):
    cells = [[P(title, 'CallX'), P(body, 'SmallX')] for title, body in items]
    rows = []
    for i in range(0, len(cells), cols):
        row = cells[i:i + cols]
        while len(row) < cols:
            row.append([])
        rows.append(row)
    t = Table(rows, colWidths=[170*mm/cols]*cols, hAlign='LEFT')
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), fill), ('BOX', (0, 0), (-1, -1), .6, LINE),
        ('INNERGRID', (0, 0), (-1, -1), .6, LINE), ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 8), ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 8), ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    ]))
    return t


def steps(items):
    rows = [[P(str(i), 'CenterX'), P(item, 'BodyX')] for i, item in enumerate(items, 1)]
    t = Table(rows, colWidths=[13*mm, 157*mm])
    t.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'), ('LINEBELOW', (0, 0), (-1, -1), .5, LINE),
        ('BACKGROUND', (0, 0), (0, -1), INK), ('TEXTCOLOR', (0, 0), (0, -1), WHITE),
        ('LEFTPADDING', (0, 0), (-1, -1), 7), ('RIGHTPADDING', (0, 0), (-1, -1), 7),
        ('TOPPADDING', (0, 0), (-1, -1), 7), ('BOTTOMPADDING', (0, 0), (-1, -1), 7),
    ]))
    return t


def checklist(items):
    return Table([[P('□', 'CenterX'), P(item, 'BodyX')] for item in items], colWidths=[11*mm, 159*mm], style=TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'), ('LINEBELOW', (0, 0), (-1, -1), .45, LINE),
        ('LEFTPADDING', (0, 0), (-1, -1), 5), ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('TOPPADDING', (0, 0), (-1, -1), 6), ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))


class NumberedDoc(BaseDocTemplate):
    def __init__(self, filename, label, **kwargs):
        self.label = label
        super().__init__(filename, pagesize=A4, leftMargin=20*mm, rightMargin=20*mm, topMargin=18*mm, bottomMargin=16*mm, **kwargs)
        self.addPageTemplates(PageTemplate(id='main', frames=Frame(self.leftMargin, self.bottomMargin, self.width, self.height, id='body'), onPage=self._page))

    def _page(self, canvas, doc):
        canvas.saveState()
        canvas.setStrokeColor(LINE); canvas.setLineWidth(.5); canvas.line(20*mm, 13*mm, 190*mm, 13*mm)
        canvas.setFont('DV-Bold', 7.5); canvas.setFillColor(VIOLET); canvas.drawString(20*mm, 9*mm, self.label)
        canvas.setFont('DV', 7.5); canvas.setFillColor(MUTED); canvas.drawRightString(190*mm, 9*mm, str(doc.page))
        canvas.restoreState()


def cover(story, label, title, subtitle, chips):
    story += [P(label, 'H2X'), P(title, 'TitleX'), P(subtitle, 'SubX')]
    story.append(Table([[P(c, 'CenterX') for c in chips]], colWidths=[170*mm/len(chips)]*len(chips), style=TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), ACID), ('BOX', (0, 0), (-1, -1), .6, INK),
        ('INNERGRID', (0, 0), (-1, -1), .6, INK), ('TOPPADDING', (0, 0), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 9),
    ])))
    story.append(Spacer(1, 9*mm))


def build_student():
    path = OUT / 'AEA2_S3_Guia_alumnat.pdf'
    story = []
    cover(story, 'AEA2 · SESSIÓ 3 · ALUMNAT', 'Connecta les pàgines', 'Converteix tres documents HTML en un lloc web navegable i aprèn a reparar rutes sense provar a l’atzar.', ['165 MIN', 'INDIVIDUAL + PARELLES', '3 PÀGINES', 'UN ZIP'])
    story.append(box('Missió de la sessió', 'Continuaràs el projecte de les sessions 1 i 2. Crearàs programa.html i contacte.html, afegiràs una navegació comuna i comprovaràs que totes les rutes funcionen des de totes les pàgines.', PALE_ACID, ACID))
    story += [Spacer(1, 5*mm), P('Què lliuraràs?', 'H1X')]
    story.append(code('''AEA2_S3_Cognom_Nom.zip
├── index_s2.html
├── index.html
├── programa.html
├── contacte.html
├── repte_rutes_reparat/
└── registre_s3.txt'''))
    story += [Spacer(1, 5*mm), P('Recorregut', 'H1X')]
    story.append(grid([
        ('1 · Conserva', 'Crea index_s2.html abans de modificar el projecte.'),
        ('2 · Entén', 'Identifica element, atribut, destinació i text clicable.'),
        ('3 · Entrena', 'Resol quatre rutes amb origen i destinació.'),
        ('4 · Construeix', 'Crea tres pàgines amb una navegació comuna.'),
        ('5 · Repara', 'Corregeix les cinc avaries de Campus Byte.'),
        ('6 · Prova', 'Descomprimeix el ZIP i verifica que segueix funcionant.'),
    ], fill=PAPER))
    story += [PageBreak()]

    story += [P('1. Anatomia d’un enllaç', 'H1X')]
    story.append(code('<a href="programa.html">Consulta el programa</a>'))
    story.append(grid([
        ('<code>a</code>', 'Element que crea l’enllaç.'),
        ('<code>href</code>', 'Atribut que indica la destinació.'),
        ('<code>programa.html</code>', 'Valor de l’atribut i ruta del fitxer.'),
        ('Text clicable', 'Ha d’explicar on porta; evita «clica aquí».'),
    ], fill=PALE_VIOLET))
    story += [Spacer(1, 5*mm), P('2. Quatre tipus de destinació', 'H1X')]
    story.append(grid([
        ('Mateixa carpeta', '<code>href="programa.html"</code>'),
        ('Dins d’una carpeta', '<code>href="pagines/programa.html"</code>'),
        ('Pujar una carpeta', '<code>href="../index.html"</code>'),
        ('Web externa', '<code>href="https://developer.mozilla.org/"</code>'),
        ('Part del document', '<code>href="#horaris"</code>'),
        ('Identificador de destí', '<code>&lt;h2 id="horaris"&gt;</code>'),
    ]))
    story += [Spacer(1, 5*mm), box('Regla d’or', 'La ruta relativa sempre es calcula des del fitxer que conté href. ../ significa «puja una carpeta».', PALE_CYAN, CYAN)]
    story += [PageBreak()]

    story += [P('3. Model: tres fitxers germans', 'H1X')]
    story.append(code('''projecte/
├── index.html
├── programa.html
└── contacte.html'''))
    story.append(P('Com que els tres documents comparteixen carpeta, poden utilitzar exactament la mateixa navegació:', 'BodyX'))
    story.append(code('''<nav>
  <a href="index.html">Inici</a>
  <a href="programa.html">Programa</a>
  <a href="contacte.html">Contacte</a>
</nav>'''))
    story += [Spacer(1, 4*mm), P('Laboratori de rutes', 'H1X')]
    story.append(grid([
        ('A · index.html → programa.html', 'Ruta: ______________________________'),
        ('B · pagines/programa.html → index.html', 'Ruta: ______________________________'),
        ('C · pagines/programa.html → contacte/contacte.html', 'Ruta: ______________________________'),
        ('D · qualsevol pàgina → MDN', 'Ruta: ______________________________'),
    ], fill=PAPER))
    story += [Spacer(1, 4*mm), box('Abans de respondre', 'Subratlla l’origen, encercla la destinació i compta quantes carpetes has de pujar o baixar.', PALE_ACID, ACID)]
    story += [PageBreak()]

    story += [P('4. Projecte: construeix el teu petit lloc web', 'H1X')]
    story.append(steps([
        'Obre el projecte de la sessió 2 i comprova index.html.',
        'Duplica index.html i anomena la còpia <b>index_s2.html</b>. No l’editis.',
        'Crea <b>programa.html</b> i <b>contacte.html</b>. Pots utilitzar les bases descarregables.',
        'Canvia title, h1 i contingut perquè cada pàgina tingui una funció diferent.',
        'Afegeix una nav amb Inici, Programa i Contacte als tres documents.',
        'A programa.html crea <code>id="horaris"</code> i un enllaç a <code>#horaris</code>.',
        'Afegeix un enllaç extern adequat amb una URL completa que comenci per https://.',
        'Prova els tres enllaços des de cadascuna de les tres pàgines.',
    ]))
    story += [Spacer(1, 5*mm), P('Checklist del projecte', 'H1X')]
    story.append(checklist([
        'Hi ha tres fitxers HTML i cada pàgina té title i h1 propis.',
        'La nav és present i coherent a totes les pàgines.',
        'Des de qualsevol pàgina puc arribar a les altres dues.',
        'El fragment #horaris arriba a l’apartat correcte.',
        'L’enllaç extern utilitza una URL completa.',
        'Els noms de fitxer no contenen espais, accents ni majúscules inesperades.',
    ]))
    story += [PageBreak()]

    story += [P('5. Repte Campus Byte', 'H1X')]
    story.append(box('Condició del repte', 'No moguis ni reanomenis cap fitxer. Has de reparar les rutes respectant l’estructura de carpetes facilitada.', PALE_ORANGE, colors.HexColor('#ff9f43')))
    story += [Spacer(1, 4*mm)]
    story.append(code('''campus-byte/
├── index.html
├── pagines/
│   └── programa.html
└── contacte/
    └── contacte.html'''))
    story += [Spacer(1, 4*mm), P('Procediment', 'H1X')]
    story.append(steps([
        'Descomprimeix AEA2_S3_repte_rutes.zip i obre index.html.',
        'Diagnostica sense editar: anota cada enllaç que no arriba al lloc correcte.',
        'Escriu origen → destinació → ruta avariada → ruta correcta.',
        'Corregeix les cinc avaries, una cada vegada.',
        'Prova inici → programa → contacte → inici i l’accés directe als horaris.',
        'Anomena la carpeta final <b>repte_rutes_reparat</b>.',
    ]))
    story += [Spacer(1, 4*mm), box('Pista graduada', 'Nivell 1: llegeix l’arbre de carpetes. Nivell 2: des de programa cal pujar una carpeta. Nivell 3: des de l’inici, Programa és dins de pagines/.', PALE_VIOLET, VIOLET)]
    story += [PageBreak()]

    story += [P('6. Lliurament i prova final', 'H1X')]
    story.append(checklist([
        'index_s2.html conserva la versió anterior.',
        'index.html, programa.html i contacte.html s’obren correctament.',
        'repte_rutes_reparat conté els tres documents del repte.',
        'registre_s3.txt explica cinc reparacions i tres decisions.',
        'La carpeta completa està comprimida com AEA2_S3_Cognom_Nom.zip.',
        'He descomprimit una còpia del ZIP i he tornat a provar els enllaços.',
    ]))
    story += [Spacer(1, 6*mm), box('Prova de transport', 'Si el lloc continua funcionant després de descomprimir-lo en una altra carpeta, les rutes relatives s’han conservat correctament.', PALE_ACID, ACID)]
    story += [Spacer(1, 7*mm), P('Tancament individual', 'H1X')]
    story.append(grid([
        ('Ara entenc que ../ significa...', '_________________________________________________<br/>_________________________________________________'),
        ('La comprovació més útil ha estat...', '_________________________________________________<br/>_________________________________________________'),
    ], fill=PAPER))
    story += [Spacer(1, 7*mm), P('Criteri d’èxit final', 'H2X'), P('El professorat pot descomprimir el ZIP, obrir index.html i recórrer tot el lloc sense corregir cap ruta ni preguntar on és cada fitxer.', 'BodyX')]

    NumberedDoc(str(path), 'AEA2 · S3 · Guia de l’alumnat').build(story)
    return path


def build_teacher():
    path = OUT / 'AEA2_S3_Guia_docent.pdf'
    story = []
    cover(story, 'AEA2 · SESSIÓ 3 · DOCENT', 'Connecta les pàgines', 'Guió operatiu, respostes, pistes, avaluació i alternatives per impartir una sessió de rutes sense improvisar.', ['165 MIN', 'CE 2.5-2.8', 'PROJECTE + REPTE', 'SOLUCIONS'])
    story.append(box('Finalitat didàctica', 'Passar d’un document HTML a un lloc de tres pàgines. L’alumnat ha de deduir rutes relatives a partir de l’origen i la destinació, provar-les i documentar les reparacions.', PALE_ACID, ACID))
    story += [Spacer(1, 5*mm), P('Evidències principals', 'H1X')]
    story.append(grid([
        ('Projecte propi', 'index.html, programa.html i contacte.html amb navegació comuna.'),
        ('Còpia de seguretat', 'index_s2.html conserva el punt de partida.'),
        ('Repte reparat', 'Campus Byte amb cinc avaries corregides.'),
        ('Registre', 'Decisions, rutes i comprovacions explicades.'),
    ]))
    story += [Spacer(1, 5*mm), P('Traçabilitat', 'H1X')]
    story.append(grid([
        ('CE 2.5 i 2.6', 'Atribut href i valors adequats.'),
        ('CE 2.7', 'Organització coherent de fitxers.'),
        ('CE 2.8', 'Enllaços interns, externs i fragments.'),
        ('CE 2.10-2.12', 'Mètode de treball, registre i consulta.'),
        ('CE 2.14-2.17', 'Relacions, treball compartit, iniciativa i autonomia.'),
        ('CE 2.3', 'Codi indentat i llegible.'),
    ], fill=PAPER))
    story += [PageBreak()]

    story += [P('Preparació prèvia', 'H1X')]
    story.append(checklist([
        'Obre la presentació i la sessió 3 del web.',
        'Descarrega i descomprimeix el repte Campus Byte.',
        'Comprova les cinc avaries i conserva una còpia sense reparar.',
        'Verifica que l’alumnat pot veure les extensions dels fitxers.',
        'Prepara les bases programa.html i contacte.html per a qui no tingui la sessió 2.',
        'Publica al Classroom una única tasca amb el nom del ZIP esperat.',
    ]))
    story += [Spacer(1, 5*mm), P('Temporització global', 'H1X')]
    story.append(grid([
        ('0-10 · Missió', 'Mapa de tres pàgines i còpia index_s2.html.'),
        ('10-30 · Idea clau', 'a, href, origen, destinació i tipus de ruta.'),
        ('30-50 · Model', 'Tres fitxers germans i navegació comuna.'),
        ('50-75 · Laboratori', 'Quatre rutes amb resposta immediata.'),
        ('75-120 · Projecte', 'Construcció i prova del lloc propi.'),
        ('120-145 · Repte', 'Diagnòstic i reparació de Campus Byte.'),
        ('145-165 · Lliurament', 'ZIP, prova de transport i registre.'),
        ('Pausa', 'Després del laboratori o durant el projecte.'),
    ], fill=PALE_CYAN))
    story += [Spacer(1, 5*mm), box('Frase guia', '«La ruta surt d’on soc i arriba on vull anar». Repeteix-la abans de cada exemple.', PALE_VIOLET, VIOLET)]
    story += [PageBreak()]

    story += [P('Conducció · minuts 0-75', 'H1X')]
    story.append(steps([
        '<b>0-10 · Missió.</b> Projecta les tres pàgines. Demana què hauria d’explicar cadascuna. Comprova la còpia index_s2.html.',
        '<b>10-20 · Anatomia.</b> Separa a, href, valor i text clicable. Contrasta «Programa» amb «Clica aquí».',
        '<b>20-30 · Tipus.</b> Modela mateixa carpeta, ../, URL completa i fragment. Assenyala sempre origen i destinació.',
        '<b>30-40 · Model.</b> Mostra tres fitxers germans. Llegeix href com una instrucció: «obre aquest fitxer».',
        '<b>40-50 · Predicció.</b> Canvia una majúscula o un nom i pregunta què fallarà abans de provar.',
        '<b>50-65 · Laboratori.</b> Resolució individual de quatre casos. No permetis avançar sense justificació oral o escrita.',
        '<b>65-75 · Contrast.</b> Parelles comparen recorreguts. Recupera només els casos amb discrepància.',
    ]))
    story += [Spacer(1, 6*mm), box('Preguntes útils', '«En quin fitxer ets?» · «On és la destinació?» · «Has de pujar una carpeta?» · «Coincideixen majúscules i extensió?»', PALE_ACID, ACID)]
    story += [Spacer(1, 6*mm), box('Intervenció que cal evitar', 'No escriguis tu la ruta correcta ni permetis afegir ../ a l’atzar. Fes tornar a l’arbre de carpetes.', PALE_ORANGE, colors.HexColor('#ff9f43'))]
    story += [PageBreak()]

    story += [P('Guió · minuts 75-165', 'H1X')]
    story.append(steps([
        '<b>75-85 · Crea.</b> L’alumnat genera programa.html i contacte.html o utilitza les bases.',
        '<b>85-100 · Navega.</b> Afegeix nav als tres documents. Comprova que no s’ha editat index_s2.html.',
        '<b>100-110 · Fragment i externa.</b> Crea id="horaris", #horaris i una URL https completa.',
        '<b>110-120 · Revisió creuada.</b> La parella prova els enllaços començant per una pàgina diferent d’index.html.',
        '<b>120-125 · Diagnòstic.</b> Descomprimeixen Campus Byte i anoten els errors sense editar.',
        '<b>125-140 · Reparació.</b> Una ruta cada vegada, amb prova immediata i registre.',
        '<b>140-145 · Recorregut complet.</b> Inici → programa → contacte → inici i accés als horaris.',
        '<b>145-155 · Empaqueta.</b> Completen registre_s3.txt i creen el ZIP.',
        '<b>155-165 · Transporta.</b> Descomprimeixen una còpia i tornen a provar-la abans de lliurar.',
    ]))
    story += [Spacer(1, 5*mm), box('Si falta temps', 'Mantén obligatòries les tres pàgines, la nav comuna i tres reparacions del repte. Completa les dues reparacions restants a l’inici de la sessió 4.', PALE_CYAN, CYAN)]
    story += [PageBreak()]

    story += [P('Solucions del laboratori i del projecte', 'H1X')]
    story.append(grid([
        ('A · index → programa', '<code>programa.html</code>'),
        ('B · pagines/programa → index', '<code>../index.html</code>'),
        ('C · pagines/programa → contacte/contacte', '<code>../contacte/contacte.html</code>'),
        ('D · qualsevol pàgina → MDN', '<code>https://developer.mozilla.org/</code>'),
    ], fill=PALE_VIOLET))
    story += [Spacer(1, 5*mm), P('Condicions mínimes del projecte', 'H1X')]
    story.append(checklist([
        'index.html, programa.html i contacte.html comparteixen carpeta.',
        'Cada document té title i h1 propis.',
        'La navegació apareix als tres documents i utilitza textos descriptius.',
        'Tots els enllaços interns funcionen des de qualsevol pàgina.',
        'programa.html conté id="horaris" i un enllaç a #horaris.',
        'Hi ha una URL externa completa i adequada.',
        'index_s2.html no s’ha modificat.',
    ]))
    story += [Spacer(1, 5*mm), code('''<nav>
  <a href="index.html">Inici</a>
  <a href="programa.html">Programa</a>
  <a href="contacte.html">Contacte</a>
</nav>''')]
    story += [PageBreak()]

    story += [P('Campus Byte · solucions', 'H1X')]
    story.append(grid([
        ('1 · index.html → programa', '<code>programa.html</code> → <code>pagines/programa.html</code>'),
        ('2 · index.html → horaris', '<code>#horaris</code> → <code>pagines/programa.html#horaris</code>'),
        ('3 · programa.html → inici', '<code>index.html</code> → <code>../index.html</code>'),
        ('4 · programa.html → contacte', '<code>contacte.html</code> → <code>../contacte/contacte.html</code>'),
        ('5 · contacte.html → inici', '<code>../../index.html</code> → <code>../index.html</code>'),
        ('Fragment', 'Conservar <code>id="horaris"</code> a programa.html.'),
    ], fill=PALE_CYAN))
    story += [Spacer(1, 6*mm), P('Com donar pistes sense resoldre', 'H1X')]
    story.append(grid([
        ('Pista 1', 'Demana el camí complet del fitxer d’origen.'),
        ('Pista 2', 'Fes dibuixar només les carpetes implicades.'),
        ('Pista 3', 'Recorda que ../ puja exactament un nivell.'),
        ('Pista 4', 'Mostra l’inici de la ruta i deixa que l’acabin.'),
    ]))
    story += [Spacer(1, 6*mm), box('Variant vàlida', 'Accepta ./programa.html en lloc de programa.html quan tots dos fitxers són germans, si l’alumne pot explicar que ./ representa la carpeta actual.', PALE_ACID, ACID)]
    story += [PageBreak()]

    story += [P('Avaluació formativa sobre 10 punts', 'H1X')]
    story.append(grid([
        ('2 · Navegació', 'Nav present i coherent a les tres pàgines.'),
        ('2 · Rutes internes', 'Funcionen des de tots els documents.'),
        ('2 · Altres destinacions', 'Fragment i URL externa correctes.'),
        ('2 · Reparació', 'Cinc avaries diagnosticades i corregides.'),
        ('1 · Organització', 'Noms i estructura de carpeta coherents.'),
        ('1 · Registre', 'Decisions i proves comprensibles.'),
    ], fill=PAPER))
    story += [Spacer(1, 5*mm), P('Errors previsibles i resposta docent', 'H1X')]
    story.append(grid([
        ('Obre una pàgina en blanc', 'Comprova primer quin fitxer ha obert i on l’ha desat.'),
        ('Només funciona des d’index', 'Obliga a començar la prova des de programa o contacte.'),
        ('Majúscules diferents', 'Compara caràcter a caràcter el nom i el valor de href.'),
        ('Massa ../', 'Torna a dibuixar l’origen i compta nivells.'),
        ('Fragment no es mou', 'Comprova que href="#horaris" coincideix amb id="horaris".'),
        ('ZIP trencat', 'Descomprimeix-lo en una altra carpeta i detecta quina relació s’ha perdut.'),
    ]))
    story += [Spacer(1, 5*mm), box('Adaptació', 'Proporciona les dues bases a qui necessiti menys càrrega de còpia. Per ampliar, situa programa.html dins d’una carpeta pagines/ i demana que recalculin tota la navegació.', PALE_VIOLET, VIOLET)]
    story += [Spacer(1, 5*mm), P('Fonts de consulta', 'H2X'), P('MDN Web Docs, “Creating links” i “Dealing with files” · developer.mozilla.org<br/>WHATWG, HTML Living Standard, element a · html.spec.whatwg.org', 'TinyX')]

    NumberedDoc(str(path), 'AEA2 · S3 · Guia docent').build(story)
    return path


for result in (build_student(), build_teacher()):
    print(result)
