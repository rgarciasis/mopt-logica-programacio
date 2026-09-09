from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from pathlib import Path

OUT=Path(__file__).resolve().parents[1]/'dist'/'downloads'; OUT.mkdir(parents=True,exist_ok=True)
INK=colors.HexColor('#111318'); VIOLET=colors.HexColor('#6854ff'); LIME=colors.HexColor('#c8ff31'); PALE=colors.HexColor('#f1efff'); MIST=colors.HexColor('#f3f4f1'); GREEN=colors.HexColor('#f1ffd0'); GREY=colors.HexColor('#667085')
pdfmetrics.registerFont(TTFont('DV','/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('DVB','/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'))
st=getSampleStyleSheet()
st.add(ParagraphStyle(name='TX',fontName='DVB',fontSize=23,leading=27,textColor=INK,spaceAfter=9))
st.add(ParagraphStyle(name='H1X',fontName='DVB',fontSize=16,leading=20,textColor=INK,spaceBefore=5,spaceAfter=7))
st.add(ParagraphStyle(name='H2X',fontName='DVB',fontSize=11,leading=14,textColor=VIOLET,spaceBefore=4,spaceAfter=4))
st.add(ParagraphStyle(name='BX',fontName='DV',fontSize=9,leading=12.5,textColor=INK,spaceAfter=4))
st.add(ParagraphStyle(name='SX',fontName='DV',fontSize=7.5,leading=9.5,textColor=GREY))
st.add(ParagraphStyle(name='CX',fontName='DV',fontSize=8.3,leading=11,textColor=INK))
def P(t,s='BX'): return Paragraph(t,st[s])
def head(c,d):
 c.saveState(); c.setFillColor(INK); c.rect(0,A4[1]-11*mm,A4[0],11*mm,fill=1,stroke=0); c.setFillColor(colors.white); c.setFont('DVB',8); c.drawString(16*mm,A4[1]-7*mm,'LÒGICA I PROGRAMACIÓ · AEA1 · TARGETES'); c.setFillColor(LIME); c.drawRightString(A4[0]-16*mm,A4[1]-7*mm,str(d.page)); c.restoreState()
def box(t,b,bg=MIST):
 x=Table([[P(t,'H2X')],[P(b,'CX')]],colWidths=[174*mm]); x.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),bg),('BOX',(0,0),(-1,-1),.6,colors.HexColor('#d1d5dc')),('LEFTPADDING',(0,0),(-1,-1),8),('RIGHTPADDING',(0,0),(-1,-1),8),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),7)])); return x
def cover(audience,title,sub):
 return [Spacer(1,17*mm),P(audience.upper(),'H2X'),P(title,'TX'),P(sub),Spacer(1,7*mm),box('12 hores · 4 categories · 40 targetes','Una categoria per sessió. Dins de cada sessió: nivell A, després B i finalment C. La mecànica no canvia mai.'),Spacer(1,5*mm),box('Una única rutina','Llegeix → pensa → tria una resposta → justifica → corregeix → registra.',PALE)]

sessions={
 'S':dict(title='Seqüència i traça',subtitle='Segueix instruccions en ordre i registra com canvia l’estat.',A=['S1','S2','S3'],B=['S4','S5','S6','S7'],C=['S9'],check=['S8','S10'],ce='1.3, 1.4, 1.6 i 1.10'),
 'P':dict(title='Patrons i codificació',subtitle='Descobreix regularitats i representa informació amb regles.',A=['P1','P2','P3','P8'],B=['P4','P5','P7'],C=['P9'],check=['P6','P10'],ce='1.2, 1.5, 1.6 i 1.11'),
 'L':dict(title='Lògica i deducció',subtitle='Separa dades, condicions i conclusions abans de decidir.',A=['L2','L3','L8'],B=['L1','L4','L5'],C=['L7','L9'],check=['L6','L10'],ce='1.1, 1.2, 1.6 i 1.10'),
 'X':dict(title='Xarxes i optimització',subtitle='Compara camins i estratègies per trobar una solució millor.',A=['X2','X8'],B=['X1','X3','X4','X5','X6'],C=['X9'],check=['X7','X10'],ce='1.3, 1.4, 1.6 i 1.10')}

def response_table(codes):
 rows=[[P('Codi','SX'),P('Resposta','SX'),P('Com ho sé? Regla, dada o pas clau','SX')]]
 for code in codes: rows.append([P(code,'CX'),'', ''])
 t=Table(rows,colWidths=[18*mm,30*mm,126*mm],rowHeights=[8*mm]+[11*mm]*len(codes))
 t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),INK),('TEXTCOLOR',(0,0),(-1,0),colors.white),('GRID',(0,0),(-1,-1),.45,colors.HexColor('#c9ced6')),('VALIGN',(0,0),(-1,-1),'MIDDLE'),('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6)])); return t

def student():
 path=OUT/'AEA1_Guia_alumnat_targetes.pdf'; d=SimpleDocTemplate(str(path),pagesize=A4,leftMargin=18*mm,rightMargin=18*mm,topMargin=18*mm,bottomMargin=15*mm)
 story=cover('Alumnat','Guia única de reptes','No hi ha tallers paral·lels ni activitats amagades. Cada sessió treballa deu targetes de la mateixa categoria, ordenades per dificultat.')
 story += [Spacer(1,6*mm),box('Com treballarem cada targeta','1. Llegeix-la en silenci. 2. Marca una opció. 3. Escriu una raó curta. 4. Contrasta-la quan ho indiqui el docent. 5. Corregeix amb un altre color.'),Spacer(1,5*mm),box('Què entregaràs?','Aquest únic document amb les respostes i justificacions. Les targetes es retornen sense escriure-hi.',GREEN),PageBreak()]
 for i,(fam,x) in enumerate(sessions.items(),1):
  story += [P(f'Sessió {i} · {x["title"]}','TX'),P(x['subtitle'],'H2X'),box('Ordre de treball',f'<b>Nivell A:</b> {", ".join(x["A"])} &nbsp; → &nbsp; <b>Nivell B:</b> {", ".join(x["B"])} &nbsp; → &nbsp; <b>Nivell C:</b> {", ".join(x["C"])}<br/><b>Control individual:</b> {" i ".join(x["check"])}',PALE),Spacer(1,4*mm),P('Pràctica guiada','H1X'),response_table(x['A']+x['B']+x['C']),Spacer(1,5*mm),P('Control individual · sense ajuda','H1X'),response_table(x['check']),Spacer(1,4*mm),box('Tancament','La targeta que més m’ha costat és ______ perquè ________________________________.<br/>L’estratègia que tornaré a utilitzar és ________________________________________.',GREEN)]
  if i<4: story.append(PageBreak())
 d.build(story,onFirstPage=head,onLaterPages=head)

def teacher():
 path=OUT/'AEA1_Guia_docent_targetes.pdf'; d=SimpleDocTemplate(str(path),pagesize=A4,leftMargin=18*mm,rightMargin=18*mm,topMargin=18*mm,bottomMargin=15*mm)
 story=cover('Professorat','Guia docent · circuit de targetes','Una metodologia, quatre sessions i cap material paral·lel. Les mateixes instruccions serveixen durant tota l’AEA1.')
 story += [Spacer(1,6*mm),box('Abans de començar','Imprimeix el banc A3 a una cara i talla cada full per la meitat. Separa les targetes en quatre famílies i, dins de cada família, en nivells A, B i C. Imprimeix una guia per alumne.'),Spacer(1,5*mm),box('Norma de correcció','La resposta correcta no és suficient: durant la posada en comú demana «quina dada, regla o pas ho demostra?». Les targetes de pràctica es corregeixen en grup; les dues finals són individuals.',GREEN),PageBreak()]
 story += [P('Estructura fixa de cada sessió','TX')]
 timeline=[('0–10','Presentació de la categoria i recordatori del protocol.'),('10–35','Nivell A · resolució individual i contrast per parelles.'),('35–75','Nivell B · rotació de targetes en parelles.'),('75–105','Nivell C · resolució guiada en equips.'),('105–125','Correcció conjunta i explicació conceptual.'),('125–150','Dues targetes de control individual.'),('150–165','Correcció diferida, registre i bitllet de sortida.')]
 t=Table([[P(a,'CX'),P(b,'CX')] for a,b in timeline],colWidths=[25*mm,149*mm]);t.setStyle(TableStyle([('GRID',(0,0),(-1,-1),.45,colors.HexColor('#ccd1d8')),('BACKGROUND',(0,0),(0,-1),PALE),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),7),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7)]));story += [t,Spacer(1,6*mm),box('Pausa flexible','Si la sessió inclou esbarjo, situa’l entre el nivell B i el nivell C. L’ordre de les targetes no canvia.'),Spacer(1,5*mm),box('Si falta temps','No eliminis el control individual. Redueix la posada en comú del nivell B a dues targetes i deixa la resta corregida al solucionari docent.'),PageBreak()]
 for i,(fam,x) in enumerate(sessions.items(),1):
  story += [P(f'Sessió {i} · {fam} · {x["title"]}','TX'),P(x['subtitle']),box('Targetes de pràctica',f'<b>A:</b> {", ".join(x["A"])} &nbsp; <b>B:</b> {", ".join(x["B"])} &nbsp; <b>C:</b> {", ".join(x["C"])}',PALE),Spacer(1,4*mm),box('Control individual',f'{" i ".join(x["check"])}. No es projecten les solucions fins que s’han recollit o girat els fulls.'),Spacer(1,4*mm),box('Què explicar en 10–15 minuts',f'Parteix de dues respostes reals de l’alumnat i posa nom a la idea central: {x["subtitle"].lower()} Evita introduir contingut nou que no aparegui a les targetes.'),Spacer(1,4*mm),box('Què observar',f'CE principals: {x["ce"]}. Registra només: comprensió de l’enunciat, estratègia utilitzada, justificació i capacitat de corregir.'),Spacer(1,4*mm),box('Ajuda graduada','Pista 1: demana que reformuli la pregunta. Pista 2: assenyala la dada o condició decisiva. Pista 3: resol el primer pas, però deixa la decisió final a l’alumne.',GREEN)]
  if i<4: story.append(PageBreak())
 story += [PageBreak(),P('Avaluació sense saturació','TX'),box('Pràctica formativa','Les vuit primeres targetes de cada sessió no generen una nota separada. Serveixen per practicar, verbalitzar estratègies i corregir errors.'),Spacer(1,5*mm),box('Evidència individual','Les dues targetes finals de cada sessió aporten 8 controls breus en total. Valora sobre 4 punts cadascuna: 1 resposta, 1 procediment, 1 justificació i 1 correcció.'),Spacer(1,5*mm),box('Lectura curricular','Agrupa els resultats per habilitat i CE; no calculis un percentatge de targetes completades. L’AEA1 continua vinculada a l’RA1 i als CE oficials 1.1–1.11.',GREEN)]
 d.build(story,onFirstPage=head,onLaterPages=head)

answers={
'S':[('S1','A','c) D4'),('S2','A','c) 6'),('S3','A','b) 4 · 1 · 2 · 3'),('S4','B','c) 5'),('S5','B','b) 5'),('S6','B','a) A blava · B vermella · C buida'),('S7','B','c) Vermell'),('S8','B','a) La línia 1'),('S9','C','c) 8'),('S10','C','b) La 3')],
'P':[('P1','A','a) 1,2,1 / 0,4 / 1,2,1 / 1,2,1'),('P2','A','c) 38'),('P3','A','c) 32'),('P4','B','b) Ratllada'),('P5','B','b) 16, 4 i 2'),('P6','B','b) ABABABAB'),('P7','B','a) Igual que fila 1, columna 1'),('P8','A','c) MRC-9I'),('P9','C','b) Columna C, fila 4'),('P10','C','a) NO · ARA · NO')],
'L':[('L1','B',"a) L’Ana"),('L2','A','b) El producte b'),('L3','A','b) 90 €'),('L4','B','c) El Pau'),('L5','B','b) 7'),('L6','B','b) 7'),('L7','C','a) 2'),('L8','A','c) El cas c'),('L9','C','b) El Pau'),('L10','C','b) 1r encès i apagat; 2n encès; entrar')],
'X':[('X1','B','b) 3'),('X2','A','b) 3'),('X3','B','c) 14'),('X4','B','b) 6'),('X5','B','c) 13'),('X6','B','b) 9 h'),('X7','B','b) De curta a llarga'),('X8','A','b) 2'),('X9','C','a) 17 min'),('X10','C','c) Començar per Oest o Est')]}
def solutions():
 path=OUT/'AEA1_Solucionari_targetes.pdf';d=SimpleDocTemplate(str(path),pagesize=A4,leftMargin=18*mm,rightMargin=18*mm,topMargin=18*mm,bottomMargin=15*mm)
 story=cover('Professorat','Solucionari ràpid','Respostes de les quaranta targetes. Per a la correcció oral, demana sempre el procediment abans de revelar l’opció.')+[PageBreak()]
 for i,(fam,rows) in enumerate(answers.items(),1):
  x=sessions[fam];story += [P(f'{fam} · {x["title"]}','TX')]
  data=[[P('Codi','SX'),P('Nivell','SX'),P('Resposta','SX'),P('Ús','SX')]]
  check=set(x['check'])
  for c,l,a in rows:data.append([P(c,'CX'),P(l,'CX'),P(a,'CX'),P('Control individual' if c in check else 'Pràctica','CX')])
  t=Table(data,colWidths=[18*mm,20*mm,96*mm,40*mm],repeatRows=1);t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),INK),('TEXTCOLOR',(0,0),(-1,0),colors.white),('GRID',(0,0),(-1,-1),.4,colors.HexColor('#cbd0d8')),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,MIST]),('VALIGN',(0,0),(-1,-1),'MIDDLE'),('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7)]));story += [t,Spacer(1,5*mm),box('Pregunta de correcció','Quina dada o condició descarta cadascuna de les altres opcions?',GREEN)]
  if i<4:story.append(PageBreak())
 d.build(story,onFirstPage=head,onLaterPages=head)

student();teacher();solutions();print('AEA1 card-only PDFs created')
