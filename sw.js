// Cambia la versione a ogni aggiornamento dell'app, così i telefoni scaricano i file nuovi
const VERSIONE = "formazione-v3";
const FILE = ["./", "index.html", "manifest.webmanifest", "icons/icon-192.png", "icons/icon-512.png", "icons/apple-touch-icon.png"];

self.addEventListener("install", e => {
  e.waitUntil(caches.open(VERSIONE).then(c => c.addAll(FILE)).then(() => self.skipWaiting()));
});

self.addEventListener("activate", e => {
  e.waitUntil(caches.keys().then(k => Promise.all(k.filter(n => n !== VERSIONE).map(n => caches.delete(n)))).then(() => self.clients.claim()));
});

self.addEventListener("fetch", e => {
  const url = new URL(e.request.url);
  if (e.request.method !== "GET") return;
  // Pagine dell'app: prima la rete (per avere gli aggiornamenti), poi la copia salvata se sei offline
  if (url.origin === location.origin) {
    e.respondWith(fetch(e.request).then(r => {
      const copia = r.clone(); caches.open(VERSIONE).then(c => c.put(e.request, copia)); return r;
    }).catch(() => caches.match(e.request).then(r => r || caches.match("index.html"))));
    return;
  }
  // Caratteri di Google Fonts: copia salvata, così l'app resta bella anche offline
  if (url.host.endsWith("fonts.googleapis.com") || url.host.endsWith("fonts.gstatic.com")) {
    e.respondWith(caches.match(e.request).then(r => r || fetch(e.request).then(res => {
      const copia = res.clone(); caches.open(VERSIONE).then(c => c.put(e.request, copia)); return res;
    })));
  }
});
