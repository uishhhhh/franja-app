# Franja — viaja a tu hora

Metabuscador exploratorio de viajes: fijas **solo el origen** y tu franja (días, horas de salida/llegada,
duración máxima) y Franja busca **avión, tren y barco** a cualquier lugar del mundo, ordenado por precio.

> **Modo demostración**: precios y horarios son simulados (deterministas). No vende nada ni procesa pagos:
> modelo de redirección a proveedores, como un metabuscador.

## Qué hay aquí

| Fichero | Para qué |
|---|---|
| `index.html` | Toda la app (HTML + JS vanilla, sin build, sin dependencias) |
| `manifest.webmanifest`, `sw.js`, `icon-*.png` | La hacen instalable (PWA) y utilizable sin conexión |
| `capacitor.config.json`, `package.json` | Envoltorio Android (Capacitor) |
| `tools/make-icons.py` | Genera los iconos de la app Android en el workflow |
| `.github/workflows/apk.yml` | Compila el APK en GitHub en cada cambio en `main` |

## Web (GitHub Pages)

`Settings → Pages → Source: Deploy from a branch → main / (root)`. En un minuto estará en
`https://uishhhhh.github.io/franja-app/`. Desde el móvil, «Añadir a pantalla de inicio» la instala como PWA.

## APK

Cada push a `main` ejecuta *Compilar APK* (pestaña **Actions**, ~5 min). El resultado queda en
`Releases → Franja (APK más reciente)` con enlace fijo:

`https://github.com/uishhhhh/franja-app/releases/download/apk-latest/franja.apk`

Para instalarlo: descárgalo en el móvil, ábrelo y permite «instalar apps de origen desconocido» para el navegador.
Es un APK **de depuración** (válido para uso personal). Para Play Store hace falta un APK/AAB firmado con tu clave
(el workflow se puede ampliar con `assembleRelease` y un keystore guardado en *Secrets*).

## De demostración a datos reales

En `index.html`, objeto `CONFIG`: `MODE` y `PROXY_URL`. Cada medio es un adaptador intercambiable (`ADAPT.*.generar`).
Las APIs reales bloquean CORS y exigen ocultar claves: pon un proxy mínimo (p. ej. Cloudflare Worker) y haz que
`generar` lo llame devolviendo segmentos con el mismo formato. Ojo: Amadeus Self-Service cerró en julio de 2026 y
Aviasales Flight Search exige 50 000 usuarios mensuales; Travelpayouts (afiliación) es el primer paso realista.
