from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, KeepTogether, Preformatted
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

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

FONT_DIR = Path('/usr/share/fonts/truetype/dejavu')
pdfmetrics.registerFont(TTFont('DV', str(FONT_DIR / 'DejaVuSans.ttf')))
pdfmetrics.registerFont(TTFont('DV-Bold', str(FONT_DIR / 'DejaVuSans-Bold.ttf')))
pdfmetrics.registerFont(TTFont('Mono', str(FONT_DIR / 'DejaVuSansMono.ttf')))
pdfmetrics.registerFont(TTFont('Mono-Bold', str(FONT_DIR / 'DejaVuSansMono-Bold.ttf')))

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='TitleX', fontName='DV-Bold', fontSize=26, leading=29, textColor=INK, spaceAfter=8))
styles.add(ParagraphStyle(name='SubX', fontName='DV', fontSize=11.5, leading=16, textColor=MUTED, spaceAfter=12))
styles.add(ParagraphStyle(name='H1X', fontName='DV-Bold', fontSize=18, leading=22, textColor=INK, spaceBefore=6, spaceAfter=8))
styles.add(ParagraphStyle(name='H2X', fontName='DV-Bold', fontSize=12.5, leading=16, textColor=VIOLET, spaceBefore=5, spaceAfter=5))
styles.add(ParagraphStyle(name='BodyX', fontName='DV', fontSize=9.5, leading=14, textColor=INK, spaceAfter=6))
styles.add(ParagraphStyle(name='SmallX', fontName='DV', fontSize=8.2, leading=11.5, textColor=MUTED))
styles.add(ParagraphStyle(name='TinyX', fontName='DV', fontSize=7.3, leading=9.5, textColor=MUTED))
styles.add(ParagraphStyle(name='CodeX', fontName='Mono', fontSize=7.7, leading=11, textColor=WHITE, leftIndent=0, rightIndent=0, spaceAfter=7))
styles.add(ParagraphStyle(name='CallX', fontName='DV-Bold', fontSize=10.2, leading=14, textColor=INK))
styles.add(ParagraphStyle(name='CenterX', fontName='DV-Bold', fontSize=11, leading=14, alignment=TA_CENTER, textColor=INK))


def P(text, style='BodyX'):
    return Paragraph(text, styles[style])


def code(text):
    return Table([[Preformatted(text, styles['CodeX'])]], colWidths=[170*mm], style=TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), INK), ('BOX',(0,0),(-1,-1),0.6,INK),
        ('LEFTPADDING',(0,0),(-1,-1),8), ('RIGHTPADDING',(0,0),(-1,-1),8),
        ('TOPPADDING',(0,0),(-1,-1),8), ('BOTTOMPADDING',(0,0),(-1,-1),8),
    ]))


def box(title, body, fill=PALE_VIOLET, accent=VIOLET):
    data=[[P(title,'CallX')],[P(body,'BodyX')]]
    return Table(data, colWidths=[170*mm], style=TableStyle([
        ('BACKGROUND',(0,0),(-1,-1),fill), ('LINEBEFORE',(0,0),(0,-1),4,accent),
        ('LEFTPADDING',(0,0),(-1,-1),10), ('RIGHTPADDING',(0,0),(-1,-1),10),
        ('TOPPADDING',(0,0),(-1,0),8), ('BOTTOMPADDING',(0,-1),(-1,-1),8),
        ('TOPPADDING',(0,1),(-1,1),1),
    ]))


def grid(items, cols=2, widths=None, fill=colors.white):
    cells=[]
    for title, body in items:
        cells.append([P(title,'CallX'), P(body,'SmallX')])
    rows=[]
    for i in range(0,len(cells),cols):
        row=[]
        for cell in cells[i:i+cols]:
            row.append(cell)
        while len(row)<cols: row.append([])
        rows.append(row)
    if widths is None: widths=[170*mm/cols]*cols
    t=Table(rows,colWidths=widths,hAlign='LEFT')
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,-1),fill), ('BOX',(0,0),(-1,-1),0.6,LINE),
        ('INNERGRID',(0,0),(-1,-1),0.6,LINE), ('VALIGN',(0,0),(-1,-1),'TOP'),
        ('LEFTPADDING',(0,0),(-1,-1),8), ('RIGHTPADDING',(0,0),(-1,-1),8),
        ('TOPPADDING',(0,0),(-1,-1),8), ('BOTTOMPADDING',(0,0),(-1,-1),8),
    ]))
    return t


def steps(items):
    rows=[]
    for i,item in enumerate(items,1):
        rows.append([P(str(i),'CenterX'),P(item,'BodyX')])
    t=Table(rows,colWidths=[13*mm,157*mm])
    t.setStyle(TableStyle([
        ('VALIGN',(0,0),(-1,-1),'TOP'), ('LINEBELOW',(0,0),(-1,-1),0.5,LINE),
        ('BACKGROUND',(0,0),(0,-1),INK), ('TEXTCOLOR',(0,0),(0,-1),WHITE),
        ('LEFTPADDING',(0,0),(-1,-1),7), ('RIGHTPADDING',(0,0),(-1,-1),7),
        ('TOPPADDING',(0,0),(-1,-1),7), ('BOTTOMPADDING',(0,0),(-1,-1),7),
    ]))
    return t


class NumberedDoc(BaseDocTemplate):
    def __init__(self, filename, doc_label, **kw):
        self.doc_label=doc_label
        super().__init__(filename, pagesize=A4, leftMargin=20*mm, rightMargin=20*mm, topMargin=18*mm, bottomMargin=16*mm, **kw)
        frame=Frame(self.leftMargin,self.bottomMargin,self.width,self.height,id='body')
        self.addPageTemplates(PageTemplate(id='main',frames=frame,onPage=self._page))
    def _page(self,canvas,doc):
        canvas.saveState()
        canvas.setFont('DV-Bold',7.5); canvas.setFillColor(VIOLET)
        canvas.drawString(20*mm, 9*mm, self.doc_label)
        canvas.setFont('DV',7.5); canvas.setFillColor(MUTED)
        canvas.drawRightString(190*mm,9*mm,f'{doc.page}')
        canvas.setStrokeColor(LINE); canvas.setLineWidth(.5); canvas.line(20*mm,13*mm,190*mm,13*mm)
        canvas.restoreState()


def cover(story, label, title, subtitle, chips):
    story += [P(label,'H2X'),P(title,'TitleX'),P(subtitle,'SubX')]
    story.append(Table([[P(c,'CenterX') for c in chips]],colWidths=[170*mm/len(chips)]*len(chips),style=TableStyle([
        ('BACKGROUND',(0,0),(-1,-1),ACID),('BOX',(0,0),(-1,-1),0.6,INK),('INNERGRID',(0,0),(-1,-1),0.6,INK),
        ('TOPPADDING',(0,0),(-1,-1),9),('BOTTOMPADDING',(0,0),(-1,-1),9)
    ])))
    story.append(Spacer(1,10*mm))


def build_concepts():
    path=OUT/'AEA2_Conceptes_web_resum.pdf'; story=[]
    cover(story,'AEA2 · CONSULTA PERMANENT','Conceptes web essencials','Una guia breu per entendre què passa abans, durant i després d’obrir una pàgina web.',['HISTÒRIA','CLIENT / SERVIDOR','FITXERS','TIPUS DE WEB'])
    story += [P('1. Internet i la Web no són el mateix','H1X')]
    story.append(grid([
        ('Internet','La infraestructura que connecta xarxes i dispositius. També permet correu, missatgeria, jocs en línia i molts altres serveis.'),
        ('World Wide Web','Un servei que utilitza Internet per consultar documents i recursos enllaçats mitjançant URLs i navegadors.'),
    ]))
    story += [Spacer(1,5*mm),P('Una història en tres moments','H2X')]
    story.append(grid([
        ('1989 · La proposta','Tim Berners-Lee presenta al CERN una proposta per compartir informació mitjançant documents connectats.'),
        ('1990 · Les primeres peces','Es creen el primer servidor web, el primer navegador/editor i el primer lloc web.'),
        ('1991 · El web s’obre','El projecte es dona a conèixer fora del CERN i comença a créixer.'),
        ('Avui · La base continua','URL, petició, resposta, fitxers i un navegador que interpreta el document.'),
    ],fill=PAPER))
    story += [Spacer(1,5*mm),P('2. Què passa quan escrius una URL?','H1X')]
    story.append(steps([
        '<b>El client</b>, normalment el navegador, demana un recurs.',
        'La petició viatja fins al <b>servidor</b> que allotja el lloc.',
        'El servidor localitza i envia fitxers: HTML, imatges, CSS o altres recursos.',
        'El navegador interpreta la resposta i construeix la pàgina visible.',
    ]))
    story += [Spacer(1,4*mm),box('Idea clau','El servidor no envia una fotografia de la pàgina. Envia dades i fitxers que el navegador interpreta.',PALE_ACID,ACID),PageBreak()]

    story += [P('3. On són els fitxers?','H1X')]
    story.append(grid([
        ('Treball local','Els fitxers són dins d’una carpeta del teu ordinador. Pots obrir index.html, però altres persones no hi poden accedir per Internet.'),
        ('Web publicada','Una còpia dels fitxers és en un servidor connectat. Les persones hi arriben mitjançant una URL.'),
        ('index.html','És el nom habitual del document d’entrada d’una carpeta web. El servidor el pot servir automàticament.'),
        ('Carpetes del projecte','Ordenen documents, imatges i altres recursos. Una ruta incorrecta impedeix que el navegador trobi el fitxer.'),
    ]))
    story += [Spacer(1,5*mm),P('4. Què interpreta el navegador?','H1X')]
    story.append(code('''<!doctype html>\n<html lang="ca">\n  <head>\n    <meta charset="utf-8">\n    <title>Títol de la pestanya</title>\n  </head>\n  <body>\n    <h1>Contingut principal</h1>\n    <p>Un paràgraf visible.</p>\n  </body>\n</html>'''))
    story.append(box('HTML descriu estructura i significat','El navegador analitza les etiquetes i construeix el document. HTML no es compila ni s’executa com un programa Python. JavaScript, que arribarà més endavant, sí que pot afegir comportament.',PALE_CYAN,CYAN))
    story += [Spacer(1,5*mm),P('5. Una URL és una adreça completa','H1X')]
    story.append(code('https://exemple.cat/activitats/cartell.html'))
    story.append(grid([
        ('https','Protocol: indica com es fa la comunicació.'),('exemple.cat','Domini: identifica el lloc.'),
        ('activitats/','Ruta: indica la carpeta.'),('cartell.html','Recurs: el fitxer demanat.'),
    ],fill=PAPER))
    story += [PageBreak()]

    story += [P('6. No totes les webs funcionen igual','H1X')]
    story.append(grid([
        ('Web estàtica','El servidor envia documents preparats. És ideal per començar a entendre HTML.'),
        ('Web dinàmica','El contingut es genera o canvia segons dades, persones o accions.'),
        ('Gestor de continguts','Eines com WordPress permeten publicar mitjançant un panell.'),
        ('Botiga electrònica','Combina catàleg, comptes, pagaments i gestió de comandes.'),
        ('Aplicació web','Permet treballar, editar, comunicar-se o crear directament al navegador.'),
        ('Frontend i backend','El frontend és la part amb què interactues; el backend processa dades i serveis al servidor.'),
    ]))
    story += [Spacer(1,5*mm),P('7. Com reconec una web ben construïda?','H1X')]
    story.append(steps([
        'Les etiquetes representen correctament la funció del contingut.',
        'La jerarquia de títols permet entendre l’organització.',
        'Els atributs i les rutes tenen valors clars.',
        'Les carpetes i els noms de fitxer segueixen un criteri estable.',
        'El contingut es pot consultar amb diferents dispositius i necessitats.',
        'El codi es pot llegir, validar, mantenir i explicar.',
    ]))
    story += [Spacer(1,5*mm),box('Tres capes que aprendrem a separar','HTML = estructura i significat · CSS = presentació · JavaScript = comportament.',PALE_ACID,ACID)]
    story += [Spacer(1,5*mm),P('Fonts de consulta','H2X'),P('CERN, “A short history of the Web” · home.cern/science/computing/birth-web/short-history-web<br/>W3C, “HTML and CSS” · w3.org/standards/webdesign/htmlcss<br/>MDN Web Docs, “How the web works” · developer.mozilla.org/docs/Learn_web_development/Getting_started/Web_standards/How_the_web_works','TinyX')]
    NumberedDoc(str(path),'AEA2 · Conceptes web essencials').build(story)
    return path


def build_student():
    path=OUT/'AEA2_S2_Guia_alumnat.pdf'; story=[]
    cover(story,'AEA2 · SESSIÓ 2 · ALUMNAT','Contingut amb sentit','Continua el mateix projecte i transforma informació solta en una pàgina que es pugui entendre.',['165 MIN','INDIVIDUAL + PARELLES','4 FITXERS','UN ZIP'])
    story.append(box('Missió de la sessió','Milloraràs index.html amb una jerarquia clara. No busquem una pàgina bonica: busquem una pàgina ben organitzada i un codi que puguis explicar.',PALE_ACID,ACID))
    story += [Spacer(1,5*mm),P('Què lliuraràs?','H1X')]
    story.append(code('''AEA2_S2_Cognom_Nom.zip\n├── index_s1.html\n├── index.html\n├── repte_jerarquia_reparat.html\n└── registre_s2.txt'''))
    story += [Spacer(1,5*mm),P('Recorregut','H1X')]
    story.append(grid([
        ('1 · Conserva','Crea index_s1.html abans de modificar el projecte.'),('2 · Entén','Aprèn a distingir h1, h2, h3 i p.'),
        ('3 · Prova','Experimenta al laboratori sense risc.'),('4 · Aplica','Millora el teu index.html.'),
        ('5 · Repara','Corregeix la jerarquia de PixelFest.'),('6 · Entrega','Comprova, documenta i comprimeix.'),
    ],fill=PAPER))
    story += [PageBreak()]

    story += [P('Idea clau: una etiqueta explica la funció','H1X')]
    story.append(grid([
        ('<code>&lt;h1&gt;</code>','Títol principal del document. En aquesta activitat n’utilitzarem un.'),
        ('<code>&lt;h2&gt;</code>','Obre un apartat que depèn del tema principal.'),
        ('<code>&lt;h3&gt;</code>','Obre un subapartat dins d’un h2.'),
        ('<code>&lt;p&gt;</code>','Conté explicacions escrites amb frases.'),
        ('<code>&lt;strong&gt;</code>','Marca informació especialment important.'),
        ('<code>&lt;em&gt;</code>','Dona èmfasi i pot canviar la manera de llegir.'),
        ('<code>&lt;!-- --&gt;</code>','Comentari per explicar el codi. No es mostra a la pàgina.'),
        ('Tabulació','Fa visibles les capses i dependències del document.'),
    ]))
    story += [Spacer(1,5*mm),P('Anatomia d’un element','H2X'),code('<strong>inscripció obligatòria</strong>')]
    story.append(P('<b>Etiqueta d’obertura</b> + contingut + <b>etiqueta de tancament</b>. L’etiqueta es tria pel significat, no per l’aspecte que mostra el navegador.','BodyX'))
    story.append(box('Pregunta de decisió','Si dubtes entre h2 i p, pregunta: «Aquest text obre un apartat o explica una idea?»',PALE_CYAN,CYAN))
    story += [PageBreak()]

    story += [P('1. Missió i còpia de seguretat','H1X')]
    story.append(steps([
        'Obre la carpeta del projecte de la sessió 1.',
        'Localitza index.html i comprova que s’obre al navegador.',
        'Duplica’l i anomena la còpia <b>index_s1.html</b>.',
        'Escriu al registre què ha d’entendre primer la persona que visita la pàgina.',
    ]))
    story += [Spacer(1,4*mm),box('Si vas faltar o no tens el fitxer','Baixa AEA2_S2_base.html, canvia el nom a index.html i substitueix el contingut de mostra pel teu.',PALE_VIOLET,VIOLET)]
    story += [Spacer(1,5*mm),P('2. Model guiat','H1X')]
    story.append(code('''<!-- Presentació principal -->\n<h1>ByteFest</h1>\n<p>Una trobada de tecnologia creativa.</p>\n\n<!-- Informació del programa -->\n<h2>Què hi trobaràs</h2>\n<p>Podràs provar <strong>arcade i robòtica</strong>.</p>\n<h3>Taller destacat</h3>\n<p>Construirem un joc <em>pas a pas</em>.</p>'''))
    story.append(steps([
        'Localitza l’únic h1.',
        'Explica de quin h2 depèn «Taller destacat».',
        'Justifica per què «Una trobada...» és p i no h2.',
        'Indica què aporta cada comentari.',
    ]))
    story += [PageBreak()]

    story += [P('3. Laboratori: una prova cada vegada','H1X')]
    story.append(steps([
        'Canvia el contingut del h1 sense crear-ne un altre.',
        'Afegeix un segon h2 amb un paràgraf propi.',
        'Afegeix un h3 que depengui d’un h2.',
        'Marca una informació important amb strong i una expressió amb em.',
        'Afegeix un comentari que expliqui la funció d’un bloc.',
        'Després de cada canvi: prediu, executa i comprova.',
    ]))
    story += [Spacer(1,5*mm),P('4. Projecte: millora index.html','H1X')]
    story.append(grid([
        ('Obligatori','1 h1 · 2 h2 · 3 p o més · strong · em · 2 comentaris.'),
        ('Només si té sentit','1 h3 per a un subapartat real.'),
        ('Codi','Estructura completa, etiquetes tancades i tabulació consistent.'),
        ('Comprovació','Una parella ha d’identificar tema i apartats sense editar.'),
    ],fill=PAPER))
    story += [Spacer(1,4*mm),box('Criteri d’èxit','Una altra persona entén el tema principal i els apartats, i tu pots justificar les etiquetes.',PALE_ACID,ACID),PageBreak()]

    story += [P('5. Repte: repara PixelFest','H1X'),P('Observa el codi durant dos minuts sense editar. Enumera almenys cinc problemes abans de tocar-lo.','BodyX')]
    story.append(code('''<!doctype html>\n<html lang="ca">\n  <head>\n    <meta charset="utf-8">\n    <title>PixelFest</title>\n  </head>\n  <body>\n    <h2>Una jornada digital</h2>\n    <h1>PixelFest 2027</h1>\n    <h1>Programa</h1>\n    <p>Arcade, píxel art i música\n    <h3>Inscripció</h3>\n    <p>Reserva <b>avui</b> la teva plaça.</p>\n    <!-- text -->\n  </body>\n</html>'''))
    story.append(steps([
        'Deixa un únic h1 i ordena la resta de títols.',
        'Tanca totes les etiquetes.',
        'Substitueix b per strong.',
        'Escriu comentaris que expliquin blocs reals.',
        'Desa el resultat com repte_jerarquia_reparat.html.',
    ]))
    story += [PageBreak()]

    story += [P('6. Comprova i entrega','H1X')]
    story.append(grid([
        ('index_s1.html','S’obre i conserva la versió anterior.'),('index.html','Té jerarquia clara i tots els requisits.'),
        ('repte reparat','Conserva la informació i corregeix l’estructura.'),('registre_s2.txt','Conté cinc reparacions i dues decisions explicades.'),
    ]))
    story += [Spacer(1,5*mm),P('Checklist final','H2X')]
    story.append(steps([
        'He obert els tres HTML al navegador.',
        'He comprovat els noms i les extensions dels fitxers.',
        'El projecte té un únic h1 i no salta nivells sense motiu.',
        'Els comentaris expliquen blocs i no són paraules genèriques.',
        'He comprimit els quatre fitxers en un únic ZIP.',
        'El ZIP es diu AEA2_S2_Cognom_Nom.zip i s’obre correctament.',
    ]))
    story += [Spacer(1,6*mm),box('Tancament individual','Completa al registre: «Ara entenc que un h2 no és només text gran, sinó que...»',PALE_CYAN,CYAN)]
    NumberedDoc(str(path),'AEA2 · S2 · Guia de l’alumnat').build(story)
    return path


def build_teacher():
    path=OUT/'AEA2_S2_Guia_docent.pdf'; story=[]
    cover(story,'AEA2 · SESSIÓ 2 · PROFESSORAT','Guia docent operativa','Contingut amb sentit: jerarquia, text, èmfasi, comentaris i documentació del procés.',['165 MIN','RA2','INDIVIDUAL + PARELLES','VERSIÓ OPERATIVA'])
    story.append(grid([
        ('Objectiu','Triar etiquetes segons la funció del contingut i justificar la jerarquia.'),
        ('Producte','Evolució d’index.html + reparació d’un document amb jerarquia incorrecta.'),
        ('Lliurable','ZIP amb index_s1.html, index.html, repte reparat i registre.'),
        ('CE prioritaris','2.1-2.6, 2.10-2.12, 2.16 i 2.17.'),
    ]))
    story += [Spacer(1,5*mm),box('Decisió didàctica','No presentem les etiquetes com una llista per memoritzar. Cada concepte apareix perquè l’alumnat ha de prendre una decisió visible en el seu projecte.',PALE_ACID,ACID)]
    story += [Spacer(1,5*mm),P('Preparació prèvia','H1X')]
    story.append(steps([
        'Obre la sessió 2 a la web i comprova el laboratori.',
        'Descarrega la presentació, la base, el repte i la plantilla de registre.',
        'Comprova que els equips mostren les extensions de fitxer.',
        'Prepara un ZIP de mostra amb l’estructura esperada.',
        'Decideix el canal de lliurament del Classroom.',
    ]))
    story += [PageBreak()]

    story += [P('Guió minut a minut','H1X')]
    timeline=[
        ('0-10 · Missió','Obren index.html, creen index_s1.html i formulen què ha d’entendre primer el visitant.','No permetis editar abans de crear la còpia.'),
        ('10-30 · Idea clau','Explica h1, h2, h3, p, strong, em i comentaris amb la presentació.','Pregunta sempre per la funció, no per la mida.'),
        ('30-45 · Model','Transforma textos solts en estructura. L’alumnat decideix abans de veure l’etiqueta.','«Obre un apartat o explica una idea?»'),
        ('45-75 · Laboratori','Canvis d’un en un, predicció i execució.','Si fallen, recuperen l’exemple i repeteixen un sol canvi.'),
        ('75-120 · Projecte','Millora individual d’index.html i revisió creuada al minut 100.','La pausa es pot inserir al minut 110.'),
        ('120-145 · Repte','Cinc problemes per escrit abans d’editar; reparació per parelles.','Demana començar pel tema principal i les dependències.'),
        ('145-165 · Entrega','Comparació de versions, registre, ZIP i comprovació.','Obre almenys un ZIP abans de tancar.'),
    ]
    rows=[]
    for a,b,c in timeline: rows.append([P(a,'CallX'),P(b,'BodyX'),P(c,'SmallX')])
    t=Table(rows,colWidths=[35*mm,85*mm,50*mm],repeatRows=0)
    t.setStyle(TableStyle([
        ('VALIGN',(0,0),(-1,-1),'TOP'),('GRID',(0,0),(-1,-1),0.5,LINE),
        ('BACKGROUND',(0,0),(0,-1),PAPER),('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),
        ('TOPPADDING',(0,0),(-1,-1),8),('BOTTOMPADDING',(0,0),(-1,-1),8)
    ])); story.append(t)
    story += [Spacer(1,5*mm),box('Si falta temps','Mantén la comparació entre versions i trasllada la reparació al principi de la sessió 3. No eliminis la documentació del canvi.',PALE_VIOLET,VIOLET),PageBreak()]

    story += [P('Microteoria: què has d’explicar','H1X')]
    story.append(grid([
        ('h1','Tema principal del document. En aquesta activitat en fem servir un.'),('h2','Apartat que depèn del tema principal.'),
        ('h3','Subapartat que depèn d’un h2.'),('p','Text explicatiu escrit en frases.'),
        ('strong','Importància semàntica.'),('em','Èmfasi que afecta la lectura.'),
        ('comentari','Documenta el codi; no es mostra al navegador.'),('tabulació','Fa visible la relació entre blocs.'),
    ]))
    story += [Spacer(1,5*mm),box('Frase suggerida','«Una etiqueta HTML no diu com de gran ha de ser un text. Diu quin paper té dins del document.»',PALE_CYAN,CYAN)]
    story += [Spacer(1,5*mm),P('Preguntes que fan pensar','H2X')]
    story.append(steps([
        'Quin és el tema de tota la pàgina?',
        'Aquest text obre un apartat o explica una idea?',
        'De quin h2 depèn aquest h3?',
        'Aquesta paraula és important o només la vols veure en negreta?',
        'El comentari ajuda una altra persona a entendre el bloc?',
    ]))
    story += [PageBreak()]

    story += [P('Model de projecte correcte','H1X')]
    story.append(code('''<!doctype html>\n<html lang="ca">\n  <head>\n    <meta charset="utf-8">\n    <title>ByteFest</title>\n  </head>\n  <body>\n    <!-- Presentació principal -->\n    <h1>ByteFest</h1>\n    <p>Una trobada de tecnologia creativa.</p>\n\n    <!-- Informació del programa -->\n    <h2>Què hi trobaràs</h2>\n    <p>Podràs provar <strong>arcade i robòtica</strong>.</p>\n    <h3>Taller destacat</h3>\n    <p>Construirem un joc <em>pas a pas</em>.</p>\n\n    <h2>Horaris</h2>\n    <p>Dissabte de 10 a 13 h.</p>\n  </body>\n</html>'''))
    story += [Spacer(1,4*mm),P('Accepta variacions quan...','H2X')]
    story.append(steps([
        'El contingut és adequat i coherent amb la missió.',
        'L’alumne pot explicar la funció de cada nivell.',
        'Un h3 depèn realment del h2 anterior.',
        'Strong i em aporten significat, no només decoració.',
        'Els comentaris identifiquen blocs o decisions útils.',
    ]))
    story += [PageBreak()]

    story += [P('Solució del repte PixelFest','H1X')]
    story.append(code('''<!doctype html>\n<html lang="ca">\n  <head>\n    <meta charset="utf-8">\n    <title>PixelFest</title>\n  </head>\n  <body>\n    <!-- Presentació de l’esdeveniment -->\n    <h1>PixelFest 2027</h1>\n    <p>Una jornada digital.</p>\n\n    <!-- Informació del programa -->\n    <h2>Programa</h2>\n    <p>Arcade, píxel art i música.</p>\n    <h3>Inscripció</h3>\n    <p>Reserva <strong>avui</strong> la teva plaça.</p>\n  </body>\n</html>'''))
    story += [Spacer(1,4*mm),P('Problemes que s’han de detectar','H2X')]
    story.append(grid([
        ('Ordre global','El descriptor apareixia abans del h1.'),('Dos h1','«Programa» havia de ser un apartat.'),
        ('Paràgraf obert','Faltava el tancament del primer p.'),('Dependència','Cal justificar si Inscripció és h3 o h2.'),
        ('b en lloc de strong','Es demana marcar importància semàntica.'),('Comentari genèric','«text» no ajuda a entendre el codi.'),
    ],fill=PAPER))
    story += [Spacer(1,4*mm),box('Variant vàlida','«Inscripció» pot ser h2 si es tracta com un apartat germà de «Programa». La decisió ha de ser consistent i explicable.',PALE_ACID,ACID),PageBreak()]

    story += [P('Avaluació formativa sobre 10','H1X')]
    rows=[
        [P('Indicador','CallX'),P('Punts','CallX'),P('Evidència observable','CallX')],
        [P('Jerarquia','BodyX'),P('3','CenterX'),P('Un h1; h2 i h3 amb dependència coherent.','BodyX')],
        [P('Text i èmfasi','BodyX'),P('2','CenterX'),P('Paràgrafs complets; strong i em amb significat.','BodyX')],
        [P('Codi llegible','BodyX'),P('2','CenterX'),P('Tancaments, comentaris útils i tabulació.','BodyX')],
        [P('Reparació','BodyX'),P('2','CenterX'),P('Detecta errors i relaciona problema, canvi i comprovació.','BodyX')],
        [P('Lliurament','BodyX'),P('1','CenterX'),P('Versions conservades, noms correctes i ZIP accessible.','BodyX')],
    ]
    t=Table(rows,colWidths=[36*mm,18*mm,116*mm],repeatRows=1)
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,0),INK),('TEXTCOLOR',(0,0),(-1,0),WHITE),
        ('GRID',(0,0),(-1,-1),0.5,LINE),('VALIGN',(0,0),(-1,-1),'MIDDLE'),
        ('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),
        ('TOPPADDING',(0,0),(-1,-1),8),('BOTTOMPADDING',(0,0),(-1,-1),8)
    ])); story.append(t)
    story += [Spacer(1,6*mm),P('Criteris d’avaluació treballats','H2X')]
    story.append(grid([
        ('2.1-2.4','Estructura, comentaris, tabulació i ús adequat d’etiquetes.'),
        ('2.5-2.6','Atributs i valors adequats; es reforcen lang, charset i title.'),
        ('2.10-2.12','Temps, metodologia, documentació i consulta de recursos.'),
        ('2.16-2.17','Iniciativa, presa de decisions i aprenentatge autònom.'),
    ]))
    story += [Spacer(1,5*mm),box('Feedback recomanat','Una decisió de jerarquia encertada + el primer error estructural + una acció concreta per corregir-lo.',PALE_CYAN,CYAN),PageBreak()]

    story += [P('Ajuda graduada i incidències habituals','H1X')]
    story.append(grid([
        ('Pista 1 · Pregunta','«Quin és el tema de tota la pàgina?»'),('Pista 2 · Dependència','«De quin apartat forma part aquest text?»'),
        ('Pista 3 · Esquema','Escriu només h1, h2 i h3 en un paper abans de tornar al codi.'),('Pista 4 · Model','Compara amb el model i localitza la primera diferència.'),
        ('No veu els canvis','Comprova fitxer obert, Ctrl+S, Ctrl+R i extensió .html.'),('Tot sembla negreta','Recorda que aspecte i significat no són el mateix.'),
        ('Crea molts h1','Demana que resumeixi tota la pàgina en un únic tema.'),('Comentaris inútils','Pregunta si ajudarien una persona que no ha escrit el codi.'),
    ],fill=PAPER))
    story += [Spacer(1,5*mm),P('Adaptacions sense canviar l’objectiu','H2X')]
    story.append(steps([
        '<b>Més suport:</b> parteix d’AEA2_S2_base.html i limita el projecte a dos h2 sense h3.',
        '<b>Més autonomia:</b> demana un tercer apartat i una justificació escrita de la jerarquia.',
        '<b>Absència:</b> guia PDF + base HTML + laboratori web; lliura els mateixos quatre fitxers.',
        '<b>Sense connexió:</b> utilitza la guia impresa i els fitxers descarregats; el navegador local és suficient.',
    ]))
    story += [Spacer(1,5*mm),P('Materials','H2X'),P('Presentació AEA2_S2_Presentacio.pptx · Guia de l’alumnat · AEA2_S2_base.html · AEA2_S2_repte_jerarquia.html · AEA2_S2_registre.txt · Resum de conceptes web.','BodyX')]
    NumberedDoc(str(path),'AEA2 · S2 · Guia docent operativa').build(story)
    return path


if __name__=='__main__':
    for result in (build_concepts(),build_student(),build_teacher()):
        print(result)
