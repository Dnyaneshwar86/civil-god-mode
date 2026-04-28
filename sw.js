const CACHE_NAME = 'civil-god-v3-tiranga';
const ASSETS = [
  'index.html',
  'manifest.json',
  'master_style.css',
  'portfolio.css',
  'macro_micro_civil_engine.html',
  'ultimate_execution_tree.html',
  'civil_god_mode_app_icon_1777348617757.png',
  'https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;900&family=JetBrains+Mono:wght@400;700&display=swap'
];

// Install: Cache all assets
self.addEventListener('install', (e) => {
  e.waitUntil(
    caches.open(CACHE_NAME).then((cache) => cache.addAll(ASSETS))
  );
  self.skipWaiting();
});

// Activate: Cleanup old caches
self.addEventListener('activate', (e) => {
  e.waitUntil(
    caches.keys().then((keys) => {
      return Promise.all(keys.map((key) => {
        if (key !== CACHE_NAME) return caches.delete(key);
      }));
    })
  );
});

// Fetch Strategy: Stale-While-Revalidate
self.addEventListener('fetch', (event) => {
  if (event.request.method !== 'GET') return;
  
  event.respondWith(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.match(event.request).then((cachedResponse) => {
        const fetchedResponse = fetch(event.request).then((networkResponse) => {
          cache.put(event.request, networkResponse.clone());
          return networkResponse;
        }).catch(() => {
          // If network fails, return cached response if available
          return cachedResponse;
        });

        return cachedResponse || fetchedResponse;
      });
    })
  );
});
