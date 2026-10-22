# Operatori Caritas: versione installabile

App online: https://paolocri.github.io/formazione-operatori/

Questa cartella contiene l'app pronta per essere messa online come web app installabile (PWA).

- `index.html`: l'app
- `manifest.webmanifest`: nome, colori e icone per l'installazione
- `sw.js`: rende l'app disponibile anche senza connessione
- `icons/`: icone per Android, iPhone e browser

## Pubblicarla gratis con GitHub Pages
1. Crea un account su github.com e un nuovo repository pubblico (es. `formazione-operatori`).
2. Carica tutti i file di questa cartella (Add file → Upload files).
3. Vai in Settings → Pages, scegli "Deploy from a branch", branch `main`, cartella `/ (root)`.
4. Dopo un minuto l'app è su `https://<tuo-utente>.github.io/formazione-operatori/`.

## Installarla sul telefono
- **Android (Chrome)**: apri il link, menu ⋮ → "Installa app".
- **iPhone (Safari)**: apri il link, Condividi → "Aggiungi alla schermata Home".

## Aggiornarla
Sostituisci `index.html` e cambia `VERSIONE` in `sw.js` (es. `formazione-v2`).
L'avanzamento dei corsi resta salvato su ogni telefono.
