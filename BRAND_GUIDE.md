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

## Colores — v0.1 PROVISIONAL

> La identidad visual definitiva está **pendiente**. Estos valores salen del logo y sirven de arranque. Tokens consumibles en [`tokens/`](tokens/).

| Nombre | Hex | RGB | Token |
|---|---|---|---|
| Rojo WebCom | `#E30613` | rgb(227, 6, 19) | `--wccr-rojo` |
| Azul marino | `#20217A` | rgb(32, 33, 122) | `--wccr-azul` |
| Blanco | `#FFFFFF` | — | `--wccr-blanco` |
| Negro | `#111111` | — | `--wccr-negro` |

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

> **Pendiente (fase de identidad visual):** decisión final de paleta y mapeo semántico, tipografía, versiones SVG del logo, favicon/iconos de app, plantillas.
