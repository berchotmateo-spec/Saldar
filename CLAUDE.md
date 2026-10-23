# Saldar — sitio web (demo)

Memoria del proyecto para cualquier sesión de Claude que lo retome. Se trabaja
con la skill `metodo-web-negocio-local`. **Nada de montos del abono,
contraseñas ni datos privados del dueño en este archivo** (el repo puede ser
o volverse público).

## Qué es

Web de una página para **Saldar** (Instagram [@saldar223](https://www.instagram.com/saldar223/)),
empresa de **logística en camión entre Mar del Plata y Buenos Aires** (en los
dos sentidos), con depósito en Victoriano Montes 1963, Mar del Plata, y
sucursal en Buenos Aires. También hace **mudanzas** y lleva **congelados**. **En la web se dice "logística", nunca "fletes"**
(pedido de Mateo, 20/10/2026). Es una **demo de venta** de Mateo
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
  horizontal, mensaje de WhatsApp bien armado en los dos sentidos, aviso
  cuando falta un dato, links a Google Maps, ninguna mención a "fletes" ni a
  mensajería en el texto visible.
- "Pedir por WhatsApp" es un link común (`#pedir`) cuyo `href` se rearma con
  cada cambio del formulario; si falta un dato, el clic se cancela y avisa.
  No usar `window.open`: dentro del Artifact no anda para gente de afuera.

## Datos del negocio

| Dato | Valor en la web | Fuente y fecha |
|---|---|---|
| Nombre comercial | "Saldar" | El dueño, vía Mateo, 19/10/2026 ✅ |
| Rubro | Logística en camión Mar del Plata ⇄ Buenos Aires | El dueño, vía Mateo, 20/10/2026 ✅ ("logística", no "fletes") |
| Depósito | Victoriano Montes 1963, Mar del Plata (link a Google Maps). La carga sale desde acá | El dueño, vía Mateo, 20/10/2026 ✅. Mateo escribió "victoriano monte"; la calle es Dr. Victoriano E. Montes |
| Servicios | Mar del Plata → Buenos Aires y Buenos Aires → Mar del Plata, y mudanzas | El dueño, vía Mateo, 19, 20 y 22/10/2026 ✅. **No tiene mensajería** |
| Congelados | Se permiten | El dueño, vía Mateo, 22/10/2026 ✅ |
| Factura | Hace Factura A | El dueño, vía Mateo, 22/10/2026 ✅ |
| Vehículos | Camiones | El dueño, vía Mateo, 20/10/2026 ✅ |
| Cómo cobra | Según el peso (y la cantidad de bultos). **De Mar del Plata a Buenos Aires, recargo del 20 %** | El dueño, vía Mateo, 20 y 23/10/2026 ✅ (los montos y los rangos faltan; el 20 % es real) |
| Entrega | A domicilio | El dueño, vía Mateo, 20/10/2026 ✅ |
| Sucursal Buenos Aires | Existe; dirección "A confirmar" | El dueño, vía Mateo, 20/10/2026 ✅ (los datos los pasa después) |
| Tarifas | Por bulto según rango de peso: hasta 5 kg $ 6.000, 5–15 kg $ 9.000, 15–30 kg $ 14.000, 30–50 kg $ 20.000 | ⚠️ Inventadas para la demo |
| WhatsApp | El de Mateo (pruebas) | ⚠️ Falta el del negocio |
| Horario | Trabaja de lunes a sábados. Recepción de carga en el depósito: lunes a viernes de 8 a 16:30. Sábados el depósito está cerrado y no sale mercadería | El dueño, vía Mateo, 22/10/2026 ✅. Reemplaza el "de 6 a 15" del 20/10. En el JSON-LD: lunes a viernes 8 a 16:30 |
| Medios de pago | Efectivo y transferencia | El dueño, vía Mateo, 22/10/2026 ✅ (reemplaza "todos los medios"). Tarjeta: "se puede habilitar" en la web y posnet en el depósito |
| Zonas de entrega | Mar del Plata y Buenos Aires; en Mar del Plata también Batán y Sierra de los Padres con costo extra | El dueño, vía Mateo, 22/10/2026 ✅ (el monto del extra falta) |
| Qué no llevan | "A confirmar" | — |
| Cada cuánto viajan | "A confirmar" | — |

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
- **La palabra "fletes"**: Mateo prefiere "logística" (20/10/2026). Buscar
  "flete" en todo el archivo antes de publicar.
- **Fletes dentro de la ciudad por hora** (vehículo, horas, ayudantes, pisos)
  y las zonas de Mar del Plata: se sacaron el 20/10/2026 cuando el dueño
  explicó que hace Mar del Plata ⇄ Buenos Aires en camión y cobra por bultos.

## Cómo actualizar las tarifas (y los datos)

Todo lo que cambia está **al final del `<script>`** de `index.html`, debajo del
comentario **"DATOS DE SALDAR — ACÁ SE CAMBIAN LOS PRECIOS"**:

- `NEGOCIO`: nombre, `whatsapp`, `instagram`, `tarifasDeEjemplo`, `horario`,
  `recepcion` y `sabados` (horario de recepción del depósito), `direccion` +
  `ciudad` (depósito; arman el link a Google Maps), **`sucursalBA`** (cuando
  Mateo pase la dirección de la sucursal, va acá y aparece sola en recorrido,
  contacto, preguntas, cotizador y mensaje), `pagos`, `factura`,
  `congelados`, `domicilio`, `zonas`, `noLlevan`, `frecuencia`, servicios
  (la tarjeta de Mudanzas tiene su propio botón de WhatsApp con `boton`) y
  preguntas frecuentes.
- `TARIFAS`: `redondeo`, `maxBultos`, `pesoMaximo`, **`pesos`** (rangos de
  peso, cada uno con `nombre`, `frase` y `porBulto`), **`zonasMdp`** (Mar del
  Plata sin extra, Batán y Sierra de los Padres con `extra`; solo aparece
  cuando la entrega es en Mar del Plata) y `sentidos` (de dónde
  sale la carga en cada sentido: depósito de Mar del Plata o sucursal de
  Buenos Aires; `recargo` en %: 20 para Mar del Plata → Buenos Aires, 0 para
  la vuelta).

Reglas: los precios van **enteros, sin puntos ni $** (`9000`). El formato
`$ 9.000` lo hace la función `pesos()`.

Cálculo (`calcular()`): cada bulto se cobra según su rango de peso;
`total = suma de (bultos de cada rango × porBulto) + recargo del sentido
(20 % sobre los bultos de Mar del Plata a Buenos Aires) + extra de la zona`
(solo Batán / Sierra de los Padres), redondeado a `TARIFAS.redondeo`. Si Saldar cobra por kilo, con
mínimo por viaje, o distinto según el sentido, cambiar `calcular()` y
`TARIFAS`.

El link a Google Maps es un link común (`https://www.google.com/maps/search/?api=1&query=…`):
no usa la API ni pide clave. Está en la tarjeta del recorrido, en contacto y
en el JSON-LD (`hasMap`).

Interruptores:
- `NEGOCIO.tarifasDeEjemplo = false` → se va la barra VISTA PREVIA y la etiqueta del presupuesto.
- `NEGOCIO.whatsapp` → cambiarlo por el del negocio (formato `549` + característica sin 0 + número sin 15).

El JSON-LD del `<head>` es estático (para que Google lo lea sin JavaScript):
si cambian la dirección, las ciudades o el horario, actualizarlo a mano.

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
- Idea: **etiqueta / hoja de ruta**. Hoja de ruta MDP → BA con código de
  barras en la portada, cinta de embalaje azul con el nombre, el presupuesto
  como ticket, numeración de secciones en tipografía mono.
- Titular: "Mar del Plata – Buenos Aires, ida y vuelta." (lo resaltado es
  "ida y vuelta", porque los camiones van y vienen). Arriba dice "Logística ·
  Mar del Plata – Buenos Aires".
- Cotizador: sentido (dos tarjetas) + una fila por rango de peso con su
  contador; las filas con bultos se marcan en azul; si llega a Mar del Plata,
  se elige la zona (Batán y Sierra con costo extra). Debajo del día dice "La
  carga sale de lunes a viernes".
- Servicios: los dos sentidos (con etiquetas En camión, Según el peso, A
  domicilio, Congelados), Mudanzas (botón "Pedir presupuesto" que abre
  WhatsApp con un mensaje de mudanza) y "¿Necesitás otra cosa?". En "Tus datos" un aviso
  dice desde dónde sale la carga según el sentido; solo se pide la dirección
  de entrega (entregan a domicilio, la carga sale del depósito).
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
- Recorrido: esquema SVG propio (Río de la Plata, costa atlántica, Buenos
  Aires, Mar del Plata, "≈ 400 km · ida y vuelta"), con la línea del camino
  animada (se queda quieta con "reducir movimiento"). Sin API de mapas.
- Nada inventado sobre el negocio: sin años, cantidad de envíos, clientes,
  reseñas, seguros ni garantías. Lo que falta dice "A confirmar".
- Crédito al pie: "Desarrollado por ConnectHUB" (pedido de Mateo, 19/10/2026).
- Si llegan fotos reales (camiones, depósito, cargas), usarlas **sin recortar**.

## PENDIENTES — confirmar con el dueño

| Qué | Por qué hay duda |
|---|---|
| Datos de la sucursal de Buenos Aires (dirección, horario) | Mateo los pasa después; hoy "A confirmar" |
| ¿El "de 6 a 15" sigue valiendo para algo (entregas, oficina)? | Se sacó porque choca con la recepción hasta las 16:30 |
| Costo extra de Batán y Sierra de los Padres: ¿cuánto? ¿por envío o por bulto? | Hoy $ 5.000 de ejemplo por envío |
| Mudanzas: ¿dentro de Mar del Plata, a Buenos Aires o las dos? ¿cómo se cotizan? | Hoy solo "pedí presupuesto por WhatsApp" |
| Pago con tarjeta: "se puede habilitar" en la web y posnet en el depósito | Para la web hace falta la cuenta de Mercado Pago (u otra) del negocio: link o botón de pago. Cuando haya posnet, sumar "tarjeta en el depósito" a `pagos` |
| Precios reales según el peso: ¿por kilo o por rangos? ¿qué rangos y cuánto? ¿hay mínimo? ¿igual en los dos sentidos? | Hoy 4 rangos de ejemplo por bulto, iguales en los dos sentidos |
| Más de 50 kg: ¿lo llevan? ¿cómo se cobra? | Hoy dice "escribinos y lo cotizamos" |
| Que en Buenos Aires la carga también sale de la sucursal | Inferido de "sale desde el depósito" + "hay sucursal en Buenos Aires" |
| ¿Retiran a domicilio además de entregar? | Se entendió que no: la carga sale del depósito; el formulario no pide dirección de retiro |
| Cada cuánto viajan (días de salida a Buenos Aires y de vuelta) | "A confirmar" en preguntas |
| A qué partes de Buenos Aires entregan (CABA, GBA…) | La web dice "Buenos Aires" |
| WhatsApp del negocio | Hoy todo va al de Mateo |
| Qué no llevan | "A confirmar" en preguntas |
| Franjas horarias del formulario (mañana / mediodía / cualquier horario) | Puestas sin horario exacto; se sacó "tarde" porque cierran a las 15 |
| Clientes o marcas que se puedan nombrar (con permiso) | No hay ninguno en la web |
| Algo que lo distinga (frecuencia, años haciendo el recorrido, seguimiento…) | No se puso nada |
| Logo real (captura de la foto de perfil) | Logo tipográfico provisorio; también sirve para sacar el tono exacto de azul |
| Fotos propias (los camiones, el depósito, cargas) | Ninguna |

## Para publicar (cuando cierre)

- [ ] Cargar datos y tarifas reales; `tarifasDeEjemplo: false`.
- [ ] Cambiar `NEGOCIO.whatsapp` por el del negocio.
- [ ] Sacar `<meta name="robots" content="noindex">`.
- [ ] Revisar el JSON-LD: sumar la sucursal de Buenos Aires (como segundo
      `LocalBusiness` o `department`) cuando estén sus datos, y `telephone` y
      `url` solo si el dueño los confirma.
- [ ] Imagen `og.jpg` 1200×630 para cuando se comparte por WhatsApp, y `canonical` con el dominio.
- [ ] `publicar.py` de la skill → `docs/`, GitHub Pages, dominio, Search Console, Perfil de Empresa.

## Registro de cambios

- 23/10/2026 — Mateo: "de Mar del Plata a Buenos Aires tiene un recargo del
  20 %" → `recargo: 20` en ese sentido; el cotizador suma la línea del
  recargo, la tarjeta del sentido dice "Recargo del 20 %" (la otra "Sin
  recargo") y la pregunta del precio lo explica. Con esto quedan confirmados
  los dos sentidos.
- 22/10/2026 — Mateo pasó: congelados sí; zonas MDP, Buenos Aires y Batán /
  Sierras con costo extra; pagos en efectivo o transferencia (tarjeta se puede
  habilitar); Factura A; lunes a sábados, recepción lunes a viernes de 8 a
  16:30, sábados no sale mercadería ni hay nadie en el depósito; envíos MDP →
  BA; mudanzas → zona de entrega con extra en el cotizador, aviso de días,
  tarjeta y pregunta de Mudanzas, etiqueta Congelados, preguntas de
  congelados, factura, zonas y recepción, horario y pagos nuevos en contacto y
  JSON-LD (`MovingCompany`, `paymentAccepted`, horario lunes a viernes).
- 20/10/2026 — Mateo: "logística" en vez de "fletes"; todos los medios de
  pago; hay sucursal en Buenos Aires (datos después); lunes a sábados;
  entregan a domicilio; sale desde el depósito; el precio es según el peso →
  todos los textos pasaron a logística, el cotizador cobra por bulto según
  rango de peso, el formulario pide solo la dirección de entrega, aviso de
  desde dónde sale la carga, tarjeta y dato de la sucursal "A confirmar",
  preguntas nuevas y horario en el JSON-LD.
- 20/10/2026 — Mateo pasó datos del dueño: horario de 6 a 15, dirección
  Victoriano Montes 1963 (con link a Maps), los camiones llevan de Mar del
  Plata a Buenos Aires y traen de Buenos Aires a Mar del Plata, cobra por
  viaje según la cantidad de bultos → cotizador nuevo (sentido + bultos),
  servicios por sentido, sección "Recorrido" con esquema MDP – BA en vez de
  las zonas de la ciudad, preguntas nuevas, titular "ida y vuelta", JSON-LD
  con dirección y mapa. Se sacó el cotizador por hora (vehículo, ayudantes,
  pisos) y las zonas de Mar del Plata.
- 19/10/2026 — Mateo pidió cambiar el crédito del pie → "Desarrollado por
  ConnectHUB" en vez de "Sitio hecho por Mateo".
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
