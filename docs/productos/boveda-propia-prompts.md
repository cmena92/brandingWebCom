# Prompts de imágenes — Bóveda Propia

> Para generar las imágenes de la landing ([`boveda-propia.html`](../../boveda-propia.html)) en una IA de imágenes (Midjourney, Flux, DALL·E, Ideogram).
> Cada slot de la landing (`IMG-1`, `IMG-2`, `IMG-3`) tiene su prompt acá.

## ⚠️ Lo primero: la regla de oro

Las IAs de imágenes **escriben texto basura** (letras inventadas). Por eso:
- **IMG-1 (hero)** → imagen pura, sin texto. La IA la hace perfecta.
- **IMG-2 (infografía)** y **IMG-3 (diagrama)** → generá el FONDO/estilo con la IA, y **el texto y las etiquetas los ponés vos en Canva o Figma** encima. Si una IA mete texto, va a salir mal.
- Para diagramas técnicos exactos, lo mejor es un editor de diagramas (Excalidraw, draw.io, Figma) usando los colores de marca. Abajo te dejo el contenido exacto del diagrama.

---

## Estilo de marca (pegá esto en CADA prompt)

```
dark security operations center aesthetic, near-black deep navy background (#0B0D1A),
dark UI panels (#14172E), accents in electric blue (#4D5BFF) and brand navy (#20217A),
alert red (#E30613) used sparingly, mint green (#2BD9A8) and amber (#FFB020) as status lights,
subtle dotted grid texture, high contrast, crisp, precise, enterprise-grade, clean geometric,
cinematic lighting, sharp focus, NOT cartoonish, NOT generic stock photo, technical authority, clarity
```

---

## IMG-1 · HERO (imagen pura, sin texto)

> Ratio 4:3. Va en el hero, al lado del titular.

```
A sleek digital vault and secure server glowing in a dark security operations center,
a single brushed-metal key or padlock as the hero object, faint zero-trust network lines
radiating outward, blurred holographic security dashboard panels in the background,
dramatic hero shot with depth of field,
[PEGAR ESTILO DE MARCA AQUÍ]
--ar 4:3 --style raw
```

Variante (más abstracta): cambiá "key or padlock" por "a glowing locked vault door made of light".

---

## IMG-2 · INFOGRAFÍA DEL DOLOR (fondo IA + texto en Canva)

> Ratio 16:9 o cuadrado. Concepto: el caos de las contraseñas hoy.

Generá el visual del caos con la IA:
```
Conceptual scene of password chaos in a company: glowing keys scattered everywhere,
floating sticky notes, fragments of spreadsheet cells and chat bubbles drifting in disorder,
a few keys cracked and glowing red (compromised), tangled connections, sense of disorder and risk,
[PEGAR ESTILO DE MARCA AQUÍ]
--ar 16:9
```

Después, en Canva/Figma, montá encima la estructura de la infografía:
- **Lado izquierdo "ANTES (hoy)":** Excel · chats · post-its · navegador → etiqueta roja `EXPUESTO`. Frase: *"Si cae una, caen todas."*
- **Flecha al centro:** `→ Bóveda Propia →`
- **Lado derecho "DESPUÉS":** una bóveda ordenada → etiqueta verde `BAJO CONTROL`.
- Usá la tipografía de marca (Space Grotesk títulos, JetBrains Mono para las etiquetas de estado).

---

## IMG-3 · DIAGRAMA DE ARQUITECTURA (la prueba de seriedad)

> Lo MÁS importante para el "peso de empresa seria". Hacelo en un editor de diagramas con los colores de marca (queda exacto y profesional). Contenido exacto:

```
[ Usuario / Equipo ]
        │  (extensión navegador · app móvil · escritorio)
        ▼
[ Red ZERO-TRUST ]  ──  verificación continua, nada confiable por defecto
        │
        ▼
[ Doble autenticación (MFA) ]
        │
        ▼
[ TU servidor propio · Vaultwarden endurecido ]
        │
        ├─ Respaldos automáticos
        └─ Monitoreo + métricas de adopción

Etiqueta grande: "Enterprise por dentro. Simple por fuera."
```

Si querés además un visual de impacto (no el diagrama exacto, sino una ilustración isométrica):
```
Isometric illustration of a secure self-hosted server protected by layered shields and
a zero-trust network perimeter, clean lines connecting a laptop and phone to a central vault,
[PEGAR ESTILO DE MARCA AQUÍ]
--ar 16:9
```

---

## Bonus · Iconos para "Qué incluye" (5 tarjetas)

```
a set of 5 minimal line icons, uniform 2px stroke, sharp geometric corners,
electric blue (#4D5BFF) on transparent, enterprise UI style, consistent:
1) a server, 2) a network shield (zero-trust), 3) a fingerprint/2FA, 4) a browser window,
5) a graduation cap (training)
--ar 1:1
```

---

## Bonus · La cara humana (NO uses IA acá)

Para el "peso de empresa con años", lo que más golpea es una **foto real** tuya o del equipo, sobria, bien iluminada, fondo oscuro. Una IA generando "personas falsas" haría justo lo contrario de lo que querés (volvería a oler a IA). **Foto real > render.**

---

### Dónde van en la landing
| Slot | Archivo sugerido | Reemplaza en |
|---|---|---|
| IMG-1 | `assets/productos/boveda/hero.png` | placeholder `[ IMG-1 · HERO ]` |
| IMG-2 | `assets/productos/boveda/infografia-dolor.png` | `[ IMG-2 · INFOGRAFÍA DEL DOLOR ]` |
| IMG-3 | `assets/productos/boveda/arquitectura.png` | `[ IMG-3 · DIAGRAMA DE ARQUITECTURA ]` |
