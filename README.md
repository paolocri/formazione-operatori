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

## Privacy
- Il sito contiene solo informazioni pubbliche e non usa cookie, statistiche o servizi esterni: i caratteri sono ospitati qui (cartella `fonts/`), non su Google.
- L'area operatore "Passaggi" salva i dati **solo sul telefono** di chi la usa, cifrati (AES-GCM 256) con una chiave ricavata dal PIN (PBKDF2, 310.000 iterazioni). Nessun dato viene inviato a server.
- Dopo 5 PIN sbagliati i passaggi vengono cancellati; quelli già inseriti in Matrioska si cancellano dopo 7 giorni.
- Non vanno inseriti nomi, cognomi né dati sulla salute: solo codice Matrioska o iniziali.
