const s4Tabs = {
  "mission": {
    "title": "Fes desaparèixer i recuperar una imatge",
    "tag": "MISSIÓ · 10 MIN",
    "intro": "Continua el lloc de tres pàgines de la S3. Avui hi integraràs una imatge, un àudio i un vídeo amb alternatives accessibles.",
    "steps": [
      "Descarrega i descomprimeix el laboratori. Obre model.html al navegador i a l’editor.",
      "Primers cinc minuts: canvia formes.png per absent.png dins de src. Prediu el resultat, desa i actualitza.",
      "Recupera formes.png i comprova la imatge.",
      "Crea una còpia completa del projecte de la S3 abans de modificar-lo."
    ],
    "deliver": "Predicció i resultat al registre.",
    "success": "Pots explicar que HTML referencia el recurs: no l’inclou dins del codi.",
    "visual": "<p><a href=\"downloads/AEA2_S4_Practica.zip\" download>Baixa el laboratori ZIP ↓</a> · <a href=\"downloads/s4/model.html\" target=\"_blank\">Obre el model</a></p>"
  },
  "theory": {
    "title": "Ruta, significat i control",
    "tag": "IDEA CLAU · 15 MIN",
    "intro": "src indica on és el recurs. alt comunica el significat d’una imatge quan no es pot veure. controls permet controlar la reproducció.",
    "steps": [
      "Relaciona src amb la carpeta del document HTML.",
      "Descriu la informació útil de la imatge, sense repetir innecessàriament el text proper.",
      "Una imatge purament decorativa porta alt=\"\"; una imatge informativa necessita una alternativa adequada.",
      "No activis la reproducció automàtica. L’àudio necessita alternativa textual i el vídeo, subtítols o alternatives segons el contingut."
    ],
    "deliver": "Explicació oral de src, alt i controls.",
    "success": "Distingeixes localització, alternativa textual i reproducció.",
    "visual": ""
  },
  "model": {
    "title": "Llegeix un exemple que funciona",
    "tag": "MODEL · 15 MIN",
    "intro": "El model inclou fitxers reals i alternatives textuals. El so és un to sintètic, no una locució.",
    "steps": [
      "Obre model.html i identifica la imatge, l’àudio i el vídeo.",
      "Localitza els quatre fitxers referenciats dins de media.",
      "Compara les etiquetes: img no té etiqueta de tancament; audio i video sí.",
      "Llegeix les alternatives textuals i relaciona-les amb el contingut."
    ],
    "deliver": "Relació entre cada etiqueta i el fitxer que utilitza.",
    "success": "Pots seguir cada ruta des de model.html.",
    "visual": "<p><a href=\"downloads/AEA2_S4_Practica.zip\" download>Baixa el laboratori ZIP ↓</a> · <a href=\"downloads/s4/model.html\" target=\"_blank\">Obre el model</a></p><pre><code>&lt;img src=&quot;media/formes.png&quot; alt=&quot;Un rectangle verd i un cercle taronja dins d’un marc verd sobre fons blau&quot; width=&quot;400&quot;&gt;\n&lt;audio controls src=&quot;media/to.wav&quot;&gt;&lt;/audio&gt;\n&lt;video controls width=&quot;400&quot; src=&quot;media/formes.mp4&quot;&gt;\n  &lt;track kind=&quot;captions&quot; src=&quot;media/subtitols.vtt&quot; srclang=&quot;ca&quot; label=&quot;Català&quot; default&gt;\n&lt;/video&gt;</code></pre>"
  },
  "lab": {
    "title": "Canvia una cosa cada vegada",
    "tag": "LABORATORI · 30 MIN",
    "intro": "Treballa a la còpia local del laboratori; desa i actualitza després de cada canvi.",
    "steps": [
      "Canvia width de la imatge a 250; comprova que el fitxer original no canvia.",
      "Escriu un alt propi que conservi la informació rellevant.",
      "Treu controls de l’àudio, observa el resultat i recupera’l.",
      "Reprodueix i pausa el vídeo. Comprova la durada i el so a volum baix.",
      "Per provar els subtítols, segueix LLEGEIX.html: obre un terminal a la carpeta del laboratori, executa python3 -m http.server 8000 --bind 127.0.0.1 i visita http://127.0.0.1:8000/model.html. Activa Català al reproductor i reprodueix des del començament. Atura el servidor amb Ctrl+C en acabar.",
      "Si python3 no està disponible o el port està ocupat, demana ajuda al docent. No canviïs la seguretat del navegador. La prova dels subtítols és per HTTP, no amb doble clic al fitxer."
    ],
    "deliver": "model.html modificat i registre de les proves.",
    "success": "Imatge visible, àudio i vídeo reproduïbles i controls disponibles.",
    "visual": "<p><a href=\"downloads/AEA2_S4_Practica.zip\" download>Baixa el laboratori ZIP ↓</a> · <a href=\"downloads/s4/model.html\" target=\"_blank\">Obre el model</a></p>"
  },
  "project": {
    "title": "El teu esdeveniment, amb imatge, àudio i vídeo",
    "tag": "PROJECTE · 45 MIN",
    "intro": "Recupera index.html, programa.html i contacte.html de la S3. No substitueixis el projecte pel model.",
    "steps": [
      "Conserva les tres pàgines de la S3. Crea media/ al costat de programa.html i copia-hi els recursos que utilitzaràs.",
      "Afegeix una imatge que tingui sentit al teu esdeveniment, amb ruta relativa i alt adequat. Anota autoria, origen i permís.",
      "A programa.html afegeix un àudio amb controls, un títol relacionat amb el teu esdeveniment i una transcripció. Pots reutilitzar el to del model com a senyal d’inici: no el descriguis com una locució.",
      "Afegeix un vídeo amb controls i una pista track en català. Pots reutilitzar el vídeo de formes com a prova de pantalla del teu esdeveniment: explica que és una prova. Conserva el VTT coherent amb el so real.",
      "No cal enregistrar recursos nous. Si tries recursos propis, adapta també la transcripció, els subtítols i l’origen al registre.",
      "Copia el laboratori a practica_s4/. Prova el projecte des d’un servidor local iniciat a la carpeta on hi ha index.html. Comprova navegació, àudio, vídeo i subtítols."
    ],
    "deliver": "Les tres pàgines del teu projecte amb imatge, àudio, vídeo, VTT i alternatives textuals; pràctica separada.",
    "success": "Els tres mitjans funcionen dins del projecte, tenen un context propi i no es perden la navegació ni les alternatives accessibles.",
    "visual": ""
  },
  "challenge": {
    "title": "Rescata la pàgina multimèdia",
    "tag": "REPTE · 30 MIN",
    "intro": "Hi ha quatre errors intencionats a repte.html. Repara’ls sense moure ni reanomenar els recursos.",
    "steps": [
      "Obre repte.html a través del servidor local. Observa què falta abans d’editar.",
      "Revisa quatre aspectes: càrrega de la imatge, informació del text alt, controls de l’àudio i ruta de la pista VTT.",
      "Desa una còpia com repte_reparat.html. Canvia una cosa cada vegada, desa i actualitza.",
      "Per a cada error, escriu símptoma → causa → canvi → prova al registre.",
      "Torna a reproduir el vídeo des del començament amb la pista Català activada. Comprova també el text alternatiu mirant el codi."
    ],
    "deliver": "repte_reparat.html i quatre reparacions justificades.",
    "success": "Imatge correcta, alt descriptiu, àudio controlable i subtítols carregats per HTTP.",
    "visual": "<details><summary>Pista 1 · Per on començo?</summary><p>Compara els noms reals de media/ amb els src i compara els atributs amb model.html.</p></details><details><summary>Pista 2 · No tot és visible</summary><p>Un alt genèric no explica la imatge. Un àudio sense controls pot existir sense que el puguis activar. El VTT és un fitxer diferent del vídeo.</p></details>"
  },
  "deliver": {
    "title": "Un ZIP que funciona en un altre lloc",
    "tag": "LLIURAMENT · 20 MIN",
    "intro": "Entrega una sola carpeta comprimida amb el projecte complet i la pràctica.",
    "steps": [
      "Inclou index.html, programa.html, contacte.html i tots els recursos del lloc. Mantén les carpetes i rutes que has comprovat.",
      "Dins de practica_s4/ conserva LLEGEIX.html, model.html, repte.html, repte_reparat.html, media/ i registre_s4.txt completat.",
      "Comprimeix com AEA2_S4_Cognom_Nom.zip.",
      "Descomprimeix el ZIP en una carpeta nova. Inicia-hi el servidor local i comprova navegació, imatge, àudio, vídeo, subtítols i les quatre reparacions.",
      "Desa el ZIP al Drive compartit, adjunta el mateix fitxer a Classroom i prem Entrega."
    ],
    "deliver": "AEA2_S4_Cognom_Nom.zip amb projecte, pràctica i registre.",
    "success": "Els tres mitjans són al projecte; registre amb autoria, alternatives i quatre proves. No es puntua CSS.",
    "visual": ""
  },
  "guide": {
    "title": "Consulta quan ho necessitis",
    "tag": "GUIA · SENSE TEMPS ADDICIONAL",
    "intro": "No cal memoritzar: identifica què necessites, adapta l’exemple i comprova.",
    "steps": [
      "src=\"imatges/foto.png\": baixa a la carpeta imatges des del document actual.",
      "src=\"../imatges/foto.png\": puja una carpeta i entra a imatges.",
      "alt=\"\": només per a imatges decoratives. No és una solució per a una imatge informativa que no carrega.",
      "controls: atribut booleà. controls=\"false\" també el manté present; treu l’atribut per desactivar-lo.",
      "track: pista de subtítols en format WebVTT; srclang indica la llengua.",
      "Si falla un recurs, revisa nom, extensió, majúscules i carpeta; després desa i actualitza.",
      "Subtítols en local: cal provar la pàgina per http://127.0.0.1:8000, no per file://. Vegeu LLEGEIX.html del laboratori."
    ],
    "deliver": "Consulta lliure.",
    "success": "Tries l’atribut per la seva funció.",
    "visual": "<pre><code>&lt;img src=&quot;media/formes.png&quot; alt=&quot;Un rectangle verd i un cercle taronja dins d’un marc verd sobre fons blau&quot; width=&quot;400&quot;&gt;\n&lt;audio controls src=&quot;media/to.wav&quot;&gt;&lt;/audio&gt;\n&lt;video controls width=&quot;400&quot; src=&quot;media/formes.mp4&quot;&gt;\n  &lt;track kind=&quot;captions&quot; src=&quot;media/subtitols.vtt&quot; srclang=&quot;ca&quot; label=&quot;Català&quot; default&gt;\n&lt;/video&gt;</code></pre>"
  }
};
function showS4(k){const d=s4Tabs[k];document.querySelector('#s4Content').innerHTML=`<p class="overline">${d.tag}</p><h3>${d.title}</h3><p class="instruction">${d.intro}</p>${d.visual}<ol class="step-list">${d.steps.map(s=>`<li>${s}</li>`).join('')}</ol><div class="lesson-boxes"><div class="lesson-box"><b>Què has de produir?</b><span>${d.deliver}</span></div><div class="lesson-box success"><b>Criteri d’èxit</b><span>${d.success}</span></div></div>`;document.querySelectorAll('[data-s4]').forEach(b=>b.classList.toggle('selected',b.dataset.s4===k));}document.querySelectorAll('[data-s4]').forEach(b=>b.addEventListener('click',()=>{showS4(b.dataset.s4);document.querySelector('#s4Content').focus()}));showS4('mission');
