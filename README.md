# Lògica i Programació · 1r SMX

Paquet de treball del mòdul optatiu **Lògica i Programació** (99 hores, curs 2026-2027).

Aquest repositori conté la versió 19 del site, els materials descarregables disponibles fins ara, fitxes, activitats, guies d'alumnat i professorat, presentacions, solucionaris, fitxers HTML de pràctica i els generadors utilitzats per crear una part dels PDF.

## Avís de privacitat

El paquet inclou **solucionaris i guies exclusives del professorat**. Creeu inicialment el repositori de GitHub com a **privat**.

No activeu GitHub Pages amb aquest paquet complet si no voleu que els fitxers de `dist/downloads/` siguin públics. Ocultar un botó o una secció amb JavaScript no protegeix els documents. Per publicar una web d'alumnat caldrà generar una versió separada sense els solucionaris.

## Estructura

- `dist/`: web estàtica completa preparada per publicar.
- `dist/downloads/`: documents i fitxers descarregables enllaçats des del site.
- `editable/`: editables Word que encara són útils com a base de treball.
- `references/`: programació, matriu de RA i presentació original del mòdul.
- `tools/`: scripts generadors de materials de l'AEA1 i l'AEA2.
- `.openai/hosting.json`: identificador de la publicació actual a ChatGPT Sites.

## Estat dels materials

### AEA0 · Missió zero

Material complet disponible: guia d'alumnat, guia docent, presentació, passaport, taulers A3, kit d'equip i solucionari.

### AEA1 · Laboratori de pensament computacional

La versió vigent és la reorganització centrada en targetes desconnectades: banc de reptes, guia d'alumnat, guia docent, solucionari i Boss individual.

Alguns documents de les primeres sessions es conserven perquè formen part de l'estat actual del site, però poden correspondre a una estructura anterior. Cal contrastar-los amb la guia docent de targetes abans d'utilitzar-los.

### AEA2 · Arquitectes de la informació

Hi ha continguts i materials de les sessions 1, 2 i 3: conceptes web, presentacions, guies, fitxers HTML inicials, registres i reptes. L'AEA2 encara està en desenvolupament.

### AEA3-AEA6

La navegació i informació mínima poden aparèixer al site, però els materials complets encara no s'han desenvolupat.

## Pujar el paquet a GitHub

1. Creeu un repositori nou i marqueu-lo com a **Private**.
2. Descomprimiu aquest ZIP.
3. Pugeu el contingut de la carpeta `logica-programacio-smx` a l'arrel del repositori.
4. Manteniu la branca principal amb el nom `main`.

## Publicació opcional amb GitHub Pages

La web està preparada dins la carpeta `dist/`. El repositori incorpora un flux de publicació automàtica a GitHub Pages:

1. Aneu a `Settings > Pages`.
2. A `Build and deployment`, seleccioneu `GitHub Actions`.
3. Feu una actualització a la branca `main` o executeu manualment el flux `Publica el site a GitHub Pages`.

**Important:** aquesta operació exposarà també els solucionaris que hi ha a `dist/downloads/`. Abans de fer-la, cal separar la web pública de l'alumnat de la zona docent protegida.

## Fitxer d'entrada

La pàgina principal és `dist/index.html`. El projecte és una web estàtica i no necessita instal·lar paquets ni executar cap procés de compilació per consultar-la localment.

## Recordatori de projecte

Quan el site i totes les AEA estiguin acabats, caldrà actualitzar la programació oficial del mòdul perquè reflecteixi l'organització, la metodologia, les activitats i els instruments d'avaluació definitius.
