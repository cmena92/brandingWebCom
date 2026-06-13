# Guía de Marca WebCom — Referencia Rápida

> Documento estructurado para que **humanos e IAs** apliquen correctamente la marca WebCom en cualquier producto: web, apps, sistemas, propuestas, correos.
> El **por qué** detrás de todo esto está en [FUNDAMENTO-DE-MARCA.md](FUNDAMENTO-DE-MARCA.md). Leélo una vez.

## Identidad

- **Nombre:** WebCom Costa Rica
- **Siglas:** WCCR
- **Sello:** *"Si no lo corremos nosotros, no te lo vendemos."*
- **Promesa madre:** Se acabaron las cajas negras. Claridad y control de tu propia casa.
- **A quién le habla:** directores de TI (foco de arranque: colegios profesionales).
- **País:** Costa Rica

## Declaración de unicidad

> Para los directores de TI, WebCom es el único socio que te muestra —medido y en claro— qué tan expuesto estás de verdad; porque no te vendemos nada que no corramos, midamos y suframos primero en nuestra propia casa.

## Voz — cómo escribe y habla la marca

Una marca que vende **claridad** no puede hablar enredado. El texto de cualquier producto debe sonar así:

- **Directo y sin humo** — las cosas como son. Frases cortas. Cero relleno corporativo.
- **De colega a colega** — le hablás a un par que estuvo en la trinchera, no a un "usuario".
- **Honesto con cicatrices** — mostrar lo que se rompió y se arregló genera confianza.
- **Claro por obsesión** — traducir lo técnico, matar el jerga. El villano es el humo.

### Verbal — HACER / NO HACER

| HACER | NO HACER |
|---|---|
| "Te mostramos, medido, qué tan expuesto estás." | "Soluciones sinérgicas de ciberseguridad de clase mundial." |
| "Esto lo rompimos nosotros primero. Por eso lo conocemos." | Vender miedo o urgencia falsa. |
| Hablar en segunda persona, claro y corto. | Siglas sin explicar. Párrafos de relleno. |
| Mostrar el número, la métrica, la prueba. | Prometer lo que no corremos nosotros mismos. |

## Logos

| Variante | Archivo | Uso |
|---|---|---|
| Rojo (máster) | `assets/logos/wccr-logo-master-rojo.png` | Archivo madre (alta resolución) |
| Rojo | `assets/logos/wccr-logo-rojo.png` | Fondos claros |
| Blanco | `assets/logos/wccr-logo-blanco.png` | Fondos oscuros o con color |
| Negro | `assets/logos/wccr-logo-negro.png` | Monocromático, documentos B/N |
| Naranja | `assets/logos/wccr-logo-naranja.png` | Variante (en revisión) |

## Sistema visual — v1.0 · "Sala de Control"

> Dirección: **instrumento / panel de seguridad**. Dark-first, alto contraste, el rojo como **alerta de exposición** (no como decoración). Vista en vivo: [`preview.html`](preview.html). Tokens consumibles en [`tokens/`](tokens/).

**Cada color es un ROL, no un gusto:**

| Rol | Hex | Token | Uso |
|---|---|---|---|
| Azul · autoridad | `#20217A` | `--wccr-azul` | Base de marca, confianza |
| Azul · acción | `#4D5BFF` | `--wccr-primary` | Botones, links (interactivo) |
| Rojo · exposición | `#E30613` | `--wccr-danger` | Alerta, riesgo, "estás expuesto" |
| Ámbar · atención | `#FFB020` | `--wccr-warning` | Puntos ciegos, advertencias |
| Verde · en control | `#2BD9A8` | `--wccr-ok` | Éxito, seguro |
| Lienzo | `#0B0D1A` | `--wccr-bg` | Fondo base (oscuro) |
| Panel | `#14172E` | `--wccr-surface` | Tarjetas, paneles |
| Texto | `#EAECF5` | `--wccr-text` | Texto principal sobre oscuro |

> Los tres semánticos (rojo / ámbar / verde) mapean exactamente a los niveles del [Test de Exposición](docs/test-exposicion.md): *A ciegas / Con puntos ciegos / En control*.

## Tipografía

| Rol | Fuente | Token | Por qué |
|---|---|---|---|
| Títulos | **Space Grotesk** | `--wccr-font-display` | Técnica, con carácter, precisa |
| Cuerpo / UI | **Inter** | `--wccr-font-body` | Legibilidad workhorse |
| Datos / métricas | **JetBrains Mono** | `--wccr-font-mono` | La "lectura del instrumento" |

Todas libres (Google Fonts). El **mono en los datos** es lo que hace que se sienta un tablero de verdad — usalo para puntajes, métricas y estados.

**Consumir desde un producto:**

```css
@import url('../wccr_branding/tokens/colors.css');
.btn { background: var(--wccr-azul); color: var(--wccr-blanco); }
```

```js
// tailwind.config.js
const wccr = require('../wccr_branding/tokens/tailwind.tokens.js');
module.exports = { theme: { extend: { colors: wccr.colors } } };
```

## Reglas de logo

### HACER
- Mantener las proporciones originales.
- Respetar el área de protección (espacio libre alrededor).
- Logo sobre fondo que garantice lectura clara.

### NO HACER
- No deformar, rotar ni estirar.
- No cambiar los colores del logo.
- No colocarlo sobre fondos que dificulten su lectura.

---

> **Hecho:** dirección visual, paleta con roles, mapeo semántico, tipografía.
> **Pendiente:** versiones SVG del logo, favicon/iconos de app, plantillas, y aplicar el sistema al sitio web.
