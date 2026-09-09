from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "dist" / "downloads"
OUT.mkdir(parents=True, exist_ok=True)
INK = colors.HexColor("#111318")
VIOLET = colors.HexColor("#6854ff")
LIME = colors.HexColor("#c8ff31")
MIST = colors.HexColor("#f3f4f1")
GREY = colors.HexColor("#667085")
pdfmetrics.registerFont(TTFont("DejaVu", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DejaVu-Bold", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="TitleX", parent=styles["Title"], fontName="DejaVu-Bold", fontSize=23, leading=27, textColor=INK, spaceAfter=10))
styles.add(ParagraphStyle(name="H1X", parent=styles["Heading1"], fontName="DejaVu-Bold", fontSize=16, leading=20, textColor=INK, spaceBefore=5, spaceAfter=8))
styles.add(ParagraphStyle(name="H2X", parent=styles["Heading2"], fontName="DejaVu-Bold", fontSize=11.5, leading=15, textColor=VIOLET, spaceBefore=6, spaceAfter=5))
styles.add(ParagraphStyle(name="BodyX", parent=styles["BodyText"], fontName="DejaVu", fontSize=9.2, leading=13, textColor=INK, spaceAfter=5))
styles.add(ParagraphStyle(name="SmallX", parent=styles["BodyText"], fontName="DejaVu", fontSize=7.6, leading=10, textColor=GREY))
styles.add(ParagraphStyle(name="CardX", parent=styles["BodyText"], fontName="DejaVu", fontSize=8.6, leading=12, textColor=INK))
styles.add(ParagraphStyle(name="BossX", parent=styles["Title"], fontName="DejaVu-Bold", fontSize=32, leading=35, alignment=TA_CENTER, textColor=colors.white))

def P(text, style="BodyX"):
    return Paragraph(text, styles[style])

def header(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(INK)
    canvas.rect(0, A4[1]-11*mm, A4[0], 11*mm, fill=1, stroke=0)
    canvas.setFont("DejaVu-Bold", 8)
    canvas.setFillColor(colors.white)
    canvas.drawString(16*mm, A4[1]-7*mm, "LÒGICA I PROGRAMACIÓ · AEA1")
    canvas.setFillColor(LIME)
    canvas.drawRightString(A4[0]-16*mm, A4[1]-7*mm, f"{doc.page}")
    canvas.restoreState()

def box(title, body, color=MIST):
    t = Table([[P(title, "H2X")], [P(body, "CardX")]], colWidths=[174*mm])
    t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),color),("BOX",(0,0),(-1,-1),0.7,colors.HexColor('#d8dbe0')),("LEFTPADDING",(0,0),(-1,-1),8),("RIGHTPADDING",(0,0),(-1,-1),8),("TOPPADDING",(0,0),(-1,-1),6),("BOTTOMPADDING",(0,0),(-1,-1),7)]))
    return t

def lines(n=4):
    data = [[""] for _ in range(n)]
    t = Table(data, colWidths=[174*mm], rowHeights=[8*mm]*n)
    t.setStyle(TableStyle([("LINEBELOW",(0,0),(-1,-1),0.45,colors.HexColor('#b9bec7'))]))
    return t

def cover(title, subtitle, audience):
    return [Spacer(1,18*mm), P(audience.upper(), "H2X"), P(title,"TitleX"), P(subtitle,"BodyX"), Spacer(1,8*mm), box("12 hores · 4 sessions · 24 reptes", "Cada sessió combina sis targetes amb una experiència manipulativa central. Totes les activitats es fan sense pantalles i el ritme es pot adaptar a cada equip."), Spacer(1,6*mm), box("Rutina que sempre es repeteix", "1. Briefing. &nbsp; 2. Circuit A. &nbsp; 3. Taller manipulatiu. &nbsp; 4. Microlliçó. &nbsp; 5. Circuit B. &nbsp; 6. Passaport individual.", colors.HexColor('#efedff'))]

def student_pdf():
    path=OUT/"AEA1_Quadern_alumnat_12h.pdf"
    doc=SimpleDocTemplate(str(path),pagesize=A4,rightMargin=18*mm,leftMargin=18*mm,topMargin=18*mm,bottomMargin=16*mm)
    s=cover("Passaport de reptes · AEA1","Les targetes són el recorregut principal. A cada sessió faràs dues targetes comunes i en triaràs quatre més. No cal copiar els enunciats: registra el codi, la idea clau i com l’has comprovat.","Alumnat")
    s += [Spacer(1,8*mm), P("Què entregaràs?","H1X"), P("Aquest únic passaport, en paper o escanejat en PDF. Contindrà 24 reptes registrats, quatre tallers i quatre reflexions individuals. Les targetes originals es reutilitzen i no s’hi escriu."), PageBreak()]
    sessions=[
      ("S1 · Pensar abans d’actuar", "Targetes S · perspectives, dades i descomposició", "Comunes: S1 i S2. Tria quatre targetes entre S3 i S10. Taller: la màquina que no pensa.", ["Repte 1: codi ___ · idea o regla ______________________________", "Repte 2: codi ___ · idea o regla ______________________________", "Reptes escollits: ___  ___  ___  ___ · Quin t’ha fet canviar d’estratègia i per què?"], "Abans d’actuar convé…"),
      ("S2 · Donar ordres que funcionen", "Targetes L · lògica, seqüències i depuració", "Comunes: L1 i L2. Tria quatre targetes entre L3 i L10. Taller: l’autòmat al laberint.", ["Repte 1: codi ___ · comprovació ______________________________", "Repte 2: codi ___ · comprovació ______________________________", "Reptes escollits: ___  ___  ___  ___ · On has detectat la primera divergència?"], "El canvi que ha fet el nostre programa més clar és…"),
      ("S3 · Codificar sense perdre informació", "Targetes P · patrons, representació i abstracció", "Comunes: P1 i P2. Tria quatre targetes entre P3 i P10. Taller: transmissió de sprite.", ["Repte 1: codi ___ · patró detectat ____________________________", "Repte 2: codi ___ · patró detectat ____________________________", "Reptes escollits: ___  ___  ___  ___ · Quina representació ha estat més clara?"], "La informació que no podia perdre era…"),
      ("S4 · Estratègia i repte final", "Targetes X · integració, eficiència i autonomia", "Comunes: X1 i X2. Tria quatre targetes entre X3 i X10. Taller: torneig d’ordenació i Boss individual.", ["Repte 1: codi ___ · estratègia _______________________________", "Repte 2: codi ___ · estratègia _______________________________", "Reptes escollits: ___  ___  ___  ___ · Quina solució era correcta però millorable?"], "Ara sé comprovar una solució quan…")]
    for idx,(title,concept,mission,qs,exitq) in enumerate(sessions):
        s += [P(title,"TitleX"), P(concept,"H2X"), box("MISSIÓ",mission,colors.HexColor('#efedff')), Spacer(1,4*mm), P("Registre imprescindible","H1X")]
        for q in qs:
            s += [P("• "+q,"BodyX"), lines(1), Spacer(1,2*mm)]
        s += [box("TANCAMENT INDIVIDUAL",exitq+" _________________________________<br/><br/>La meva aportació observable ha estat: _________________________________",colors.HexColor('#f3ffd5'))]
        if idx<3: s += [PageBreak()]
    doc.build(s,onFirstPage=header,onLaterPages=header)

def teacher_pdf():
    path=OUT/"AEA1_Guia_docent_12h.pdf"
    doc=SimpleDocTemplate(str(path),pagesize=A4,rightMargin=18*mm,leftMargin=18*mm,topMargin=18*mm,bottomMargin=16*mm)
    s=cover("AEA1 · Circuit de reptes desconnectats","Guia operativa de quatre sessions. Les targetes són el fil conductor i els tallers manipulatius converteixen cada família de reptes en una experiència.","Professorat")
    s += [Spacer(1,7*mm), box("DECISIÓ DIDÀCTICA", "Les targetes ocupen uns 80 minuts de cada sessió i són obligatòries. Cada alumne resol dues targetes comunes i quatre d’elecció: 24 reptes en total. Les altres 16 permeten diferenciar, recuperar o ampliar sense convertir-se en deures pendents.",colors.HexColor('#f3ffd5')), PageBreak()]
    data=[
      ("S1 · Pensar abans d’actuar","S1–S2 comunes + 4 de S3–S10","Màquina humana: ambigüitat, perspectives i descomposició.","1.1, 1.2, 1.3, 1.6, 1.8, 1.9"),
      ("S2 · Ordres que funcionen","L1–L2 comunes + 4 de L3–L10","Autòmat al tauler: seqüència, traça, depuració i bloc.","1.4, 1.5, 1.6, 1.7, 1.10"),
      ("S3 · Codificar informació","P1–P2 comunes + 4 de P3–P10","Transmissió de sprite: patró, representació i compressió.","1.2, 1.5, 1.6, 1.8, 1.9"),
      ("S4 · Estratègia i Boss","X1–X2 comunes + 4 de X3–X10","Torneig d’ordenació i Boss individual amb segona vida.","1.3, 1.4, 1.6, 1.10, 1.11")]
    s += [P("Mapa de les 12 hores","TitleX")]
    tab=Table([[P("Sessió","SmallX"),P("Targetes","SmallX"),P("Taller","SmallX"),P("CE principals","SmallX")]]+[[P(a,"CardX"),P(b,"CardX"),P(c,"CardX"),P(d,"CardX")] for a,b,c,d in data],colWidths=[39*mm,32*mm,68*mm,35*mm],repeatRows=1)
    tab.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,0),INK),("TEXTCOLOR",(0,0),(-1,0),colors.white),("GRID",(0,0),(-1,-1),0.4,colors.HexColor('#ccd0d7')),("VALIGN",(0,0),(-1,-1),'TOP'),("ROWBACKGROUNDS",(0,1),(-1,-1),[colors.white,MIST]),("LEFTPADDING",(0,0),(-1,-1),5),("RIGHTPADDING",(0,0),(-1,-1),5),("TOPPADDING",(0,0),(-1,-1),6),("BOTTOMPADDING",(0,0),(-1,-1),6)]))
    s += [tab, PageBreak()]
    timings=[
      ("S1 · Pensar abans d’actuar",[("0–10","Briefing i model de resolució."),("10–65","Circuit A: S1, S2 i una targeta escollida."),("65–115","Taller de màquina humana."),("115–130","Microlliçó a partir dels errors observats."),("130–155","Circuit B: tres targetes escollides."),("155–165","Passaport individual.")],"No corregeixis l’executor: ha d’actuar literalment. Valida una targeta amb una pregunta, no donant la resposta."),
      ("S2 · Ordres que funcionen",[("0–10","Briefing i predicció."),("10–65","Circuit A: L1, L2 i una targeta escollida."),("65–115","Taller de l’autòmat al laberint."),("115–130","Microlliçó: traça, depuració i blocs."),("130–155","Circuit B: tres targetes escollides."),("155–165","Passaport individual.")],"Tauler damunt la taula. Primer comprova que la ruta funciona; només després compara longitud o eficiència."),
      ("S3 · Codificar informació",[("0–10","Briefing i exemple de patró."),("10–65","Circuit A: P1, P2 i una targeta escollida."),("65–115","Taller de transmissió de sprite."),("115–130","Microlliçó: representació i compressió."),("130–155","Circuit B: tres targetes escollides."),("155–165","Passaport individual.")],"No imposis un codi al principi. Demana sempre dues dades: errors de reconstrucció i nombre de símbols."),
      ("S4 · Estratègia i Boss",[("0–10","Briefing i criteris del Boss."),("10–55","Circuit A: X1, X2 i dues targetes escollides."),("55–90","Torneig d’ordenació."),("90–105","Microlliçó: correcció, eficiència i traça."),("105–125","Circuit B: dues targetes escollides."),("125–150","Boss individual."),("150–165","Segona vida i passaport.")],"La segona vida conserva l’error, afegeix una correcció i n’explica la causa. No és repetir la prova.")]
    for i,(title,rows,note) in enumerate(timings):
        s += [P(title,"TitleX"), box("ABANS", "Prepara tres targetes recomanades per equip, el material del taller i un quadern per alumne. Projecta només la fase actual."), Spacer(1,4*mm)]
        tt=Table([[P(a,"CardX"),P(b,"CardX")] for a,b in rows],colWidths=[25*mm,149*mm])
        tt.setStyle(TableStyle([("GRID",(0,0),(-1,-1),0.45,colors.HexColor('#d8dbe0')),("BACKGROUND",(0,0),(0,-1),colors.HexColor('#efedff')),("VALIGN",(0,0),(-1,-1),'TOP'),("LEFTPADDING",(0,0),(-1,-1),7),("RIGHTPADDING",(0,0),(-1,-1),7),("TOPPADDING",(0,0),(-1,-1),7),("BOTTOMPADDING",(0,0),(-1,-1),7)]))
        s += [tt, Spacer(1,5*mm), box("INTERVENCIÓ CLAU",note,colors.HexColor('#f3ffd5')), Spacer(1,5*mm), box("EVIDÈNCIA", "Recull només el registre del taller i el tancament individual. Observa una fortalesa i una prioritat de millora; no cal puntuar cada targeta.")]
        if i<3:s += [PageBreak()]
    s += [PageBreak(),P("Avaluació i Boss","TitleX"),P("L’RA1 manté l’estructura acordada: Ex1 individual 40% + Pj1.1 60%. Les activitats de les sessions generen evidències formatives; no són quatre notes independents."),box("BOSS · 10 PUNTS", "2 p · descomposició i ordre &nbsp; · &nbsp; 2 p · regla o patró &nbsp; · &nbsp; 2 p · traça i comprovació &nbsp; · &nbsp; 2 p · detecció/correcció de l’error &nbsp; · &nbsp; 2 p · justificació individual."),Spacer(1,5*mm),box("SEGONA VIDA", "Després del primer lliurament, dona 10–15 minuts. L’alumne corregeix amb un altre color i completa: «El meu error era…; ho he detectat perquè…; la correcció funciona perquè…». Pot recuperar fins a 2 punts si la justificació és coherent."),Spacer(1,5*mm),box("TRAÇABILITAT", "Només s’utilitzen els CE oficials 1.1–1.11. Qualsevol referència antiga a CE 1.12 o a una durada de 14 hores queda descartada.",colors.HexColor('#ffecec'))]
    doc.build(s,onFirstPage=header,onLaterPages=header)

def boss_pdf():
    path=OUT/"AEA1_Boss_individual.pdf"
    doc=SimpleDocTemplate(str(path),pagesize=A4,rightMargin=18*mm,leftMargin=18*mm,topMargin=18*mm,bottomMargin=16*mm)
    s=[Spacer(1,8*mm),P("BOSS FINAL","TitleX"),P("Nom i cognoms: ____________________________________    Data: ______________"),box("NORMES", "Treball individual. Pots consultar la guia breu. No pots demanar una solució. A la segona vida, no esborres: corregeixes amb un altre color i expliques el canvi."),Spacer(1,5*mm),P("1 · Ordena la missió","H1X"),P("Has de preparar i comprovar 6 equips. Escriu entre 5 i 8 passos. Marca quins poden passar alhora i quins depenen d’un pas anterior."),lines(6),P("2 · Escriu una regla","H1X"),P("Crea una regla inequívoca per separar els equips en: llestos, revisió de xarxa i revisió de programari. Indica què passa si un cas compleix dues condicions."),lines(5),PageBreak(),P("3 · Fes la traça","H1X"),P("Estat inicial: A=2, B=5. Executa: A←A+1; B←B−A; si B&lt;2, B←B+4. Registra el valor després de cada pas."),lines(5),P("4 · Caça el bug","H1X"),P("Algú afirma que la seqüència sempre acaba amb B=4. Decideix si és cert, localitza la primera afirmació incorrecta i justifica-ho amb la traça."),lines(5),Spacer(1,4*mm),box("SEGONA VIDA", "La meva primera resposta fallava perquè…<br/><br/>La correcció és…<br/><br/>Ara sé que funciona perquè…",colors.HexColor('#f3ffd5'))]
    doc.build(s,onFirstPage=header,onLaterPages=header)

student_pdf(); teacher_pdf(); boss_pdf()
print("created", *(p.name for p in OUT.glob("AEA1_*12h.pdf")), "AEA1_Boss_individual.pdf")
