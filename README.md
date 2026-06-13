# Branding WebCom Costa Rica

Fuente de verdad de la marca **WebCom Costa Rica (WCCR)**. Todo producto, web o sistema se "impregna" de la marca apuntando a este repo. Se cambia acá → se actualiza en todos lados.

> **"Si no lo corremos nosotros, no te lo vendemos."**

## Empezá por acá

| Documento | Para qué |
|---|---|
| **[FUNDAMENTO-DE-MARCA.md](FUNDAMENTO-DE-MARCA.md)** | La estrategia: a quién, qué dolor, diferenciación, voz, historia. El **por qué**. |
| **[BRAND_GUIDE.md](BRAND_GUIDE.md)** | Referencia rápida para devs e IAs: cómo aplicar la marca (voz, logos, colores, snippets). El **cómo**. |
| [docs/playbook-de-activacion.md](docs/playbook-de-activacion.md) | Cómo se activa la marca para atraer clientes (tácticas priorizadas). |
| [docs/mensajeria.md](docs/mensajeria.md) | Textos del sitio web, listos para montar, en la voz de la marca. |
| [docs/test-exposicion.md](docs/test-exposicion.md) | El "Test de Exposición Real": la pieza estrella de conversión. |

## Estructura

```
.
├── FUNDAMENTO-DE-MARCA.md      Estrategia (fuente de verdad del concepto)
├── BRAND_GUIDE.md              Guía rápida aplicable (humanos + IAs)
├── assets/
│   └── logos/                  Logos con nombres estables (sin espacios)
├── tokens/
│   ├── colors.css              Variables CSS    (consumible)
│   ├── colors.json             Design tokens    (consumible)
│   └── tailwind.tokens.js      Tokens Tailwind  (consumible)
└── docs/                       Activación: playbook, mensajería, test
```

> Material de origen confidencial (FODA, datos internos) se mantiene **fuera** de este repo público a propósito.

## Estado

| Capa | Estado |
|---|---|
| Fundamento estratégico | ✅ Cerrado |
| Identidad visual (paleta final, tipografía, SVG, iconos) | ⏳ Pendiente |
| Plantillas y assets aplicados (web, membrete, presentaciones) | ⏳ Pendiente |

> Los colores en `tokens/` son **v0.1 provisional** (extraídos del logo). Sirven de arranque; se reemplazan cuando se cierre la identidad visual.

## Logos

| Variante | Archivo |
|---|---|
| Rojo (máster, alta res.) | `assets/logos/wccr-logo-master-rojo.png` |
| Rojo | `assets/logos/wccr-logo-rojo.png` |
| Blanco | `assets/logos/wccr-logo-blanco.png` |
| Negro | `assets/logos/wccr-logo-negro.png` |
| Naranja (en revisión) | `assets/logos/wccr-logo-naranja.png` |

---

Molde de referencia (no fuente de verdad): [github.com/cloorus/brandingCPIC](https://github.com/cloorus/brandingCPIC).
