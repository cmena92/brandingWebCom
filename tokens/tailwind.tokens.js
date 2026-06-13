// WebCom Costa Rica — tokens para Tailwind. v1.0 "Sala de Control" (dark-first).
// Uso: theme.extend = require('.../tokens/tailwind.tokens.js')
module.exports = {
  colors: {
    wccr: {
      azul: '#20217A',
      rojo: '#E30613',
      'azul-bright': '#4D5BFF',
      'azul-soft': '#2A2D5C',
      bg: '#0B0D1A',
      surface: '#14172E',
      'surface-2': '#1E2240',
      text: '#EAECF5',
      muted: '#9AA0BE',
      faint: '#5B6080',
      danger: '#E30613',
      warning: '#FFB020',
      ok: '#2BD9A8',
      blanco: '#FFFFFF',
      gris: { DEFAULT: '#6B6F76', light: '#C9CBCF', dark: '#2B2B33' },
    },
  },
  fontFamily: {
    display: ['Space Grotesk', 'system-ui', 'sans-serif'],
    body: ['Inter', 'system-ui', 'sans-serif'],
    mono: ['JetBrains Mono', 'ui-monospace', 'monospace'],
  },
};
