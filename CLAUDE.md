# Saldar — sitio web (demo)

Memoria del proyecto para cualquier sesión de Claude que lo retome. Se trabaja
con la skill `metodo-web-negocio-local`. **Nada de montos del abono,
contraseñas ni datos privados del dueño en este archivo** (el repo puede ser
o volverse público).

## Qué es

Web de una página para **Saldar** (Instagram [@saldar223](https://www.instagram.com/saldar223/)),
empresa de **fletes** de Mar del Plata. Es una **demo de venta** de Mateo
Berchot: se le muestra al dueño funcionando y se le ofrece con abono mensual.
Primer cliente no gastronómico (el anterior fue Pizzería La Nieve).

- Repo: `berchotmateo-spec/Saldar` — rama de trabajo `claude/new-session-2zu43k` (todavía no hay `main`).
- Archivo único: `index.html` (HTML + CSS + JS, sin build; solo Google Fonts).
- Sitio publicado: todavía no. Dominio: todavía no.
- Vista previa (Artifact): https://claude.ai/artifact/BFzHpRD3RUbbA9wNtDmvHT
  (privado: el dueño la ve recién cuando Mateo la comparte desde el menú
  Compartir). Se publicó el 19/10/2026, después de que Mateo habló con el
  dueño y le dio el OK.
- Para actualizar la vista previa: `python3 armar-artifact.py` (genera
  `saldar-artifact.html`, que no se sube al repo) y publicar ese archivo con
  `url` = el link de arriba, así queda el mismo link.

## Estado (19/10/2026)

- Demo armada **sin la ficha del negocio**: Instagram no se pudo leer desde la
  sesión y Saldar no aparece en Google ni en directorios de logística de MDP.
- **Todas las tarifas son de ejemplo** → barra "VISTA PREVIA: tarifas de ejemplo"
  arriba y etiqueta "Tarifas de ejemplo" en el presupuesto.
- **Todos los pedidos van al WhatsApp de Mateo** (5492235337853) para pruebas.
- Tiene `<meta name="robots" content="noindex">` para que Google no indexe la
  demo (precios de ejemplo y WhatsApp de Mateo). **Sacarlo al publicar.**
- Probado en Chromium a 1366 y 390 px: 0 errores de JS, sin desborde
  horizontal, mensaje de WhatsApp del flete bien armado, aviso cuando falta
  un dato, ninguna mención a envíos ni mensajería en el texto visible.
- "Pedir por WhatsApp" es un link común (`#pedir`) cuyo `href` se rearma con
  cada cambio del formulario; si falta un dato, el clic se cancela y avisa.
  No usar `window.open`: dentro del Artifact no anda para gente de afuera.

## Datos del negocio

| Dato | Valor en la web | Fuente y fecha |
|---|---|---|
| Nombre comercial | "Saldar" | El dueño, vía Mateo, 19/10/2026 ✅ |
| Rubro | Fletes | El dueño, vía Mateo, 19/10/2026 ✅ |
| Ciudad | Mar del Plata ("223" = característica de MDP) | Inferido, casi seguro |
| Servicios | Solo "Fletes" | El dueño, vía Mateo, 19/10/2026 ✅: hace fletes y **no tiene mensajería** |
| Zonas | Centro, Macrocentro, Puerto, Norte, Sur, Batán y Sierra, Miramar (solo informativas, sin precio) | ⚠️ De ejemplo |
| Tarifas | De ejemplo | ⚠️ Inventadas para la demo |
| WhatsApp | El de Mateo (pruebas) | ⚠️ Falta el del negocio |
| Horario | "A confirmar" | — |
| Dirección / depósito | "A confirmar" | — |
| Medios de pago | "A confirmar" | — |
| Qué no llevan | "A confirmar" | — |
| Si no hay nadie para recibir | "A confirmar" | — |
| Instagram | @saldar223 | — |
| Logo | Logotipo tipográfico hecho para la demo (SVG en el HTML) | ⚠️ Falta el real |
| Fotos | Ninguna (la web se ve bien sin fotos) | ⚠️ Faltan las reales |

## Lo que NO va en la web (pedido del dueño)

Al sacar algo, buscarlo en **todo** el `index.html`: textos, `<title>`,
`description`, Open Graph y JSON-LD.

- **Mensajería / envíos chicos** (sobres, paquetes, envíos para tiendas
  online): el dueño dice que no la tiene — 19/10/2026. Se sacó el cotizador
  de envíos por zona y tamaño, los recargos (urgente, ida y vuelta, cobro
  contra entrega), los precios por zona y la sección "Para empresas y
  tiendas online". Si algún día la suma, está en el historial de git
  (commit anterior a "Sacar la mensajería").

## Cómo actualizar las tarifas (y los datos)

Todo lo que cambia está **al final del `<script>`** de `index.html`, debajo del
comentario **"DATOS DE SALDAR — ACÁ SE CAMBIAN LOS PRECIOS"**:

- `NEGOCIO`: nombre, `whatsapp`, `instagram`, `tarifasDeEjemplo`, horario,
  pagos, dirección, qué no llevan (`noLlevan`), qué pasa si no hay nadie,
  servicios (con `activo: true/false`) y preguntas frecuentes.
- `ZONAS`: una por zona, con `barrios` (texto de ayuda), `lejos` (punto
  negro) y `mapa` (puntos del esquema SVG). Son solo informativas: el precio
  del flete no depende de la zona.
- `TARIFAS`: `redondeo`, `minimoHoras`, `ayudantePorHora`,
  `porPisoEscalera` y `vehiculos` (cada uno con `nombre`, `detalle` y
  `porHora`).

Reglas: los precios van **enteros, sin puntos ni $** (`22000`). El formato
`$ 22.000` lo hace la función `pesos()`.

Cálculo de un flete (`calcular()`): `porHora del vehículo × horas` (nunca
menos que `minimoHoras`) `+ ayudantes × horas × ayudantePorHora + pisos ×
porPisoEscalera`, redondeado a `TARIFAS.redondeo`. Si Saldar cobra distinto
(por viaje, por km, recargo fuera de la ciudad), cambiar `calcular()`.

Interruptores:
- `NEGOCIO.tarifasDeEjemplo = false` → se va la barra VISTA PREVIA y la etiqueta del presupuesto.
- `NEGOCIO.whatsapp` → cambiarlo por el del negocio (formato `549` + característica sin 0 + número sin 15).

Al cambiar zonas, actualizar también `areaServed` del JSON-LD en el `<head>`
(es estático, para que Google lo lea sin JavaScript).

Segunda etapa posible (comentada en el script): precio por kilómetros reales.
Nada de Google Maps (pide tarjeta).

## Decisiones de diseño (respetarlas)

- **Fondo claro** (pedido de Mateo para todas las webs). Sin tema oscuro.
- **Colores de la marca: azul y blanco, con detalles en negro** (el dueño,
  vía Mateo, 19/10/2026). Reemplazan la paleta inventada del primer borrador.
  - Azul `--azul` `#1847D6` (botones, precios, cinta, franja "Cómo
    funciona", logo). **Tono provisorio**: ajustarlo cuando llegue el logo.
  - Blanco y casi blanco `#F5F7FC` de fondo; tarjetas blancas.
  - Negro `--tinta` `#0C1018` para los detalles: cabecera del presupuesto,
    números de paso, barra de VISTA PREVIA, tarjeta de contacto, código de
    barras, punto de destino y Miramar en el mapa.
  - Los tokens están en `:root`; no hay naranja ni verde en ningún lado.
- Idea: **etiqueta / hoja de ruta**. Hoja de ruta con código de barras en
  la portada, cinta de embalaje azul con el nombre, el presupuesto como
  ticket, numeración de secciones en tipografía mono.
- La cinta azul tiene las letras **corriendo hacia la izquierda** (pedido
  de Mateo, 19/10/2026): dos tiras iguales que se corren su propio ancho en
  60 s. Se frena al pasar el mouse y queda quieta si el celular tiene
  "reducir movimiento".
- **Botones con forma de etiqueta de envío** (pedido de Mateo, 19/10/2026:
  "nada de pastilla, muy genérico"): esquinas casi rectas (5 px), borde negro
  de 2 px y sombra dura negra corrida 4 px. Si llevan ícono adelante, el ícono
  va en un "talón" separado por una línea punteada, como el troquel de una
  etiqueta. Con el mouse se levantan; al apretar se hunden como un sello.
  Mismo estilo en el WhatsApp de la cabecera. Sobre la tarjeta negra de
  contacto la sombra va en azul. No queda ningún `999px`.
- Tipografías: Barlow Condensed (títulos, aire de cartel de ruta), Barlow
  (texto) e IBM Plex Mono (etiquetas, precios del detalle).
- Logo provisorio: cuadrado azul con una "S" que es un recorrido (punto de
  origen → punto de destino negro) + "SALDAR / LOGÍSTICA · MDP".
- Mapa de zonas: esquema SVG propio (costa, mar al este, rutas 2, 226, 88 y 11),
  sin API de mapas. Los puntos salen de `ZONAS[].mapa`.
- Nada inventado sobre el negocio: sin años, cantidad de fletes, clientes,
  reseñas, seguros ni garantías. Lo que falta dice "A confirmar".
- Crédito al pie: "Sitio hecho por Mateo".
- Si llegan fotos reales (vehículos, fletes), usarlas **sin recortar**.

## PENDIENTES — confirmar con el dueño

| Qué | Por qué hay duda |
|---|---|
| ¿Hace mudanzas? | Si las hace, se suma al texto de Fletes y se evalúa `MovingCompany` en el JSON-LD |
| Zonas que cubre y sus barrios (¿Zona Oeste? ¿Batán y Sierra? ¿Miramar u otras ciudades?) | Las zonas y barrios son de ejemplo |
| Tarifas reales y **cómo cobra el flete** (por hora, por viaje, por km, recargo fuera de la ciudad) | Todas las tarifas son de ejemplo (por hora) |
| Vehículos que tiene (tipo y tamaño), mínimo de horas, ayudantes y precio, pisos por escalera | Vehículos y precios de ejemplo |
| WhatsApp del negocio | Hoy todo va al de Mateo |
| Horario y días | "A confirmar" en contacto y preguntas |
| Medios de pago | "A confirmar" |
| ¿Tiene local o depósito con dirección? ¿Se publica? | "A confirmar" |
| Qué no llevan | "A confirmar" en preguntas |
| Qué pasa si no hay nadie para recibir | "A confirmar" en preguntas |
| Franjas horarias del formulario (mañana / mediodía / tarde) | Puestas sin horario exacto |
| Clientes o marcas que se puedan nombrar (con permiso) | No hay ninguno en la web |
| Algo que lo distinga (fletes en el día, horario extendido, años en la ciudad…) | No se puso nada |
| Logo real (captura de la foto de perfil) | Logo tipográfico provisorio; también sirve para sacar el tono exacto de azul |
| Fotos propias (vehículos, equipo, fletes hechos) | Ninguna |

## Para publicar (cuando cierre)

- [ ] Cargar datos y tarifas reales; `tarifasDeEjemplo: false`.
- [ ] Cambiar `NEGOCIO.whatsapp` por el del negocio.
- [ ] Sacar `<meta name="robots" content="noindex">`.
- [ ] Revisar el JSON-LD (`areaServed`, y sumar `telephone`, `address`,
      `openingHours`, `url` solo si el dueño los confirma y quiere publicarlos).
      Si hace mudanzas, evaluar `MovingCompany` en vez de `LocalBusiness`.
- [ ] Imagen `og.jpg` 1200×630 para cuando se comparte por WhatsApp, y `canonical` con el dominio.
- [ ] `publicar.py` de la skill → `docs/`, GitHub Pages, dominio, Search Console, Perfil de Empresa.

## Registro de cambios

- 19/10/2026 — Mateo: "no tiene mensajería la empresa" → se sacó todo lo de
  envíos (cotizador por zona y tamaño, recargos, precios por zona, sección
  para tiendas online). La web queda de **fletes**: título, portada, cinta,
  cotizador, cómo funciona, contacto, pie y ficha de Google. Las zonas
  quedan solo como cobertura. También se corrigió el ícono gigante del
  botón "Consultanos".
- 19/10/2026 — Mateo pidió cambiar los botones de pastilla por algo menos
  genérico → botones tipo etiqueta con talón troquelado y sombra dura negra.
- 19/10/2026 — Mateo pasó los colores de Saldar: azul y blanco, con detalles
  en negro → toda la página pasó a esa paleta (azul provisorio `#1847D6`).
- 19/10/2026 — Mateo confirmó con el dueño: el nombre es **Saldar** y **hacen
  fletes** (el resto lo pasa después) → pestaña "Flete" y servicio "Fletes"
  prendidos (sin hablar de mudanzas, que no está confirmado); título, bajada,
  cinta y pie dicen "envíos y fletes".
- 19/10/2026 — Mateo pidió (comentario en el Artifact) que las letras de la
  cinta naranja se muevan hacia la izquierda → animación continua.
- 19/10/2026 — Mateo habló con el dueño y pidió publicar → Artifact privado
  publicado. El botón de pedido pasó a ser un link común a WhatsApp.
- 19/10/2026 — Demo inicial: portada, servicios, cotizador por zonas (y flete
  apagado), cómo funciona, zonas con mapa esquemático, empresas (apagado),
  preguntas, contacto. Tarifas de ejemplo; pedidos al WhatsApp de Mateo.
