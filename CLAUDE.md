# Saldar — sitio web (demo)

Memoria del proyecto para cualquier sesión de Claude que lo retome. Se trabaja
con la skill `metodo-web-negocio-local`. **Nada de montos del abono,
contraseñas ni datos privados del dueño en este archivo** (el repo puede ser
o volverse público).

## Qué es

Web de una página para **Saldar** (Instagram [@saldar223](https://www.instagram.com/saldar223/)),
empresa de **logística y distribución en camión entre Buenos Aires y Mar del Plata** (en los
dos sentidos; **predomina Buenos Aires → Mar del Plata**, por eso va primero en
toda la web), con depósito en Victoriano Montes 1963, Mar del Plata, y
sucursal en Buenos Aires. También hace **mudanzas** y lleva **congelados**. **En la web se dice "logística y distribución", nunca "fletes"**
(pedido de Mateo, 20 y 27/10/2026). Es una **demo de venta** de Mateo
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
- **Los precios son reales salvo uno**: lo que suma cada 10 kg más (y el
  extra de Batán y Sierras) es de ejemplo → barra "VISTA PREVIA: Falta un
  precio…" arriba, etiqueta "Vista previa" en el presupuesto y "(ejemplo)"
  en la ayuda de los bultos.
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
| Rubro | Logística y distribución en camión Buenos Aires ⇄ Mar del Plata, en los dos sentidos | El dueño, vía Mateo, 20, 23 y 27/10/2026 ✅ ("logística y distribución", no "fletes"; "ambos" sentidos) |
| Depósito | Victoriano Montes 1963, Mar del Plata (link a Google Maps). La carga sale desde acá | El dueño, vía Mateo, 20/10/2026 ✅. Mateo escribió "victoriano monte"; la calle es Dr. Victoriano E. Montes |
| Servicios | Buenos Aires → Mar del Plata y Mar del Plata → Buenos Aires, y mudanzas (dentro de Mar del Plata y entre Buenos Aires y Mar del Plata, de ida y de vuelta) | El dueño, vía Mateo, 19, 20, 22 y 23/10/2026 ✅. **No tiene mensajería** |
| Congelados | Se permiten | El dueño, vía Mateo, 22/10/2026 ✅ |
| Factura | Hace Factura A | El dueño, vía Mateo, 22/10/2026 ✅ |
| Vehículos | Camiones | El dueño, vía Mateo, 20/10/2026 ✅ |
| Cómo cobra | Por bulto según sus kilos, de a 10 kg, **hasta unos 400 kg por bulto**. **De 1 a 10 kg se cobra el mínimo: $ 9.181,97.** **Opción palet** (aparte, para el que embala toda la carga en un palet; con muchos bultos le conviene): **$ 86.260,40 el palet completo.** De Mar del Plata a Buenos Aires, recargo del 20 % sobre todo (bultos y palets) | El dueño, vía Mateo, 20 y 23/10/2026 ✅ (falta cuánto suma cada 10 kg). Audios del 23/10: "primero es por peso y por bulto, y después los que lo quieran mandar en palet, por palet" |
| Valor declarado | El cliente pone cuánto vale la mercadería (obligatorio para mandar el pedido); va en el mensaje de WhatsApp, no cambia el precio | Pedido del dueño, vía Mateo, 23/10/2026 ✅ |
| Entrega | A domicilio | El dueño, vía Mateo, 20/10/2026 ✅ |
| Sucursal Buenos Aires | **John William Cooke 3155, Villa Soldati (CABA)**, C1437 (link a Google Maps). La carga de Buenos Aires → Mar del Plata sale de acá. Recibe de 8 a 17 | Dirección: el dueño, vía Mateo, 23/10/2026 ✅ (escribió "Cooke John William 3155"). Barrio: buscado por Claude el 23/10/2026 (Waze, directorios de transporte y un aviso de galpón en Cooke 3200 dicen CABA, C1437, Villa Soldati). En esa altura hay un predio con varios expresos (Tres Lomas, Veninga, TransRE…), uno con horario de lunes a viernes de 8 a 17 |
| Tarifas | 1–10 kg $ 9.181,97 (real). Cada 10 kg más: + $ 1.800 | ⚠️ El mínimo es real; el "+ $ 1.800" es de ejemplo (`kilos.ejemplo: true`, se ve "(ejemplo)") |
| Palet | $ 86.260,40 el palet completo | El dueño, vía Mateo, 23/10/2026 ✅ |
| WhatsApp | El de Mateo (pruebas) | ⚠️ Falta el del negocio |
| Horario | Trabaja de lunes a sábados. Recepción de carga: **sucursal de Buenos Aires de 8 a 17**, **depósito de Mar del Plata de 8 a 15**, de lunes a viernes. **De Buenos Aires la carga sale el sábado.** Sábados el depósito de Mar del Plata está cerrado | El dueño, vía Mateo, 22 y 23/10/2026 ✅ ("de lunes a viernes se recibe mercadería, porque ya sale el sábado"). El 23/10 reemplaza el "8 a 16:30" y aclara el "6 a 15": el galpón de Mar del Plata abre a las 5, pero la mercadería se recibe desde las 8 aprox. (en la web va solo la recepción, para que nadie llegue a las 5). El 22/10 había dicho "los sábados no sale la mercadería" (se entendió del depósito de Mar del Plata); la web ya no lo dice. En el JSON-LD (depósito): lunes a viernes 8 a 15 |
| Medios de pago | Efectivo y transferencia | El dueño, vía Mateo, 22/10/2026 ✅ (reemplaza "todos los medios"). Tarjeta: el dueño prefiere esperar (23/10/2026); en la web no se menciona |
| Zonas de entrega | Mar del Plata y Buenos Aires; en Mar del Plata también Batán y Sierra de los Padres con costo extra | El dueño, vía Mateo, 22/10/2026 ✅ (el monto del extra falta) |
| Qué no llevan | "A confirmar" | — |
| Cada cuánto viajan | De Buenos Aires sale el sábado (lo recibido de lunes a viernes) | El dueño, vía Mateo, 23/10/2026 ✅ (falta Mar del Plata → Buenos Aires) |

| Instagram | @saldar223 | — |
| Logo | El real: `img/saldar-logo.webp` (708 × 140, sacado del PDF "SALDAR.pdf", que trae una imagen de 1201 × 281). Ícono de la pestaña: `img/favicon.png`, la "S" del logo en blanco sobre azul | El dueño, vía Mateo, 27/10/2026 ✅. Si pasan el logo en vector (SVG, AI, PDF sin imagen adentro), cambiarlo |
| CUDS | Saldar es **sponsor** del CUDS, club de rugby de Mar del Plata; los socios del CUDS tienen un descuento en el servicio (se consulta por WhatsApp, sin monto en la web). Escudo: `img/cuds-logo.webp` (del PDF "cuds_logo.pdf", vectorial) | El dueño, vía Mateo, 27/10/2026 ✅ ("son sponsors del club"). En la web: "Sponsors del CUDS" |
| Trabajá con nosotros | Formulario (nombre, teléfono, puesto, mensaje) que abre el mail de la persona con todo escrito; el CV lo adjunta ella | Pedido del dueño, vía Mateo, 27/10/2026 ✅. ⚠️ Falta el mail (`NEGOCIO.mailCV`) |
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
  `recepcion` (recepción en el depósito de Mar del Plata), `recepcionBA`
  (recepción en la sucursal de Buenos Aires) y `sabados`, `direccion` +
  `ciudad` (depósito; arman el link a Google Maps), **`sucursalBA`** (calle
  y número) + `barrioBA` + `ciudadBA` (sucursal; aparecen solas en recorrido, contacto, preguntas,
  cotizador, mensaje y link a Google Maps; en el JSON-LD van a mano, en
  `department`), `pagos`, `factura`,
  `congelados`, `domicilio`, `zonas`, `noLlevan`, `frecuencia`,
  **`mailCV`** (mail donde llegan los CV; vacío = "A confirmar"), servicios
  (la tarjeta de Mudanzas tiene su propio botón de WhatsApp con `boton`) y
  preguntas frecuentes.
- `TARIFAS`: `redondeo` (0 = no redondea y muestra centavos), `maxBultos`
  (de un mismo peso), **`palet`** (`porPalet`, `max`), **`kilos`**
  (`minimo` = precio de 1 a `tramo` kg, `tramo` = 10, **`porTramoExtra`** =
  lo que suma cada 10 kg más, `maximo` = 400 kg por bulto, `ejemplo`: sacarlo
  cuando `porTramoExtra` sea real), **`zonasMdp`** (Mar del
  Plata sin extra, Batán y Sierra de los Padres con `extra`; solo aparece
  cuando la entrega es en Mar del Plata) y `sentidos` (de dónde
  sale la carga en cada sentido: depósito de Mar del Plata o sucursal de
  Buenos Aires; `direccionSalida` y `recepcionSalida` dicen qué dato de
  `NEGOCIO` tiene la dirección y el horario de ese lugar, para el aviso del
  cotizador; `recargo` en %: 20 para Mar del Plata → Buenos Aires, 0 para
  la vuelta).

Reglas: los precios van **sin puntos de miles ni $; los centavos con punto**
(`9181.97`, `15000`). El formato (`$ 9.181,97`, `$ 15.000`) lo hace la
función `pesos()`: muestra centavos solo si el monto los tiene.

Cálculo (`calcular()`): cada fila de bultos tiene kilos y cantidad; el
precio de un bulto (`precioBulto()`) es `minimo + (tramos − 1) × porTramoExtra`,
con `tramos = ⌈kg / 10⌉` (10 kg = mínimo, 25 kg = 3 tramos, 400 kg = 40);
`total = suma de (cantidad × precio de cada fila) + palets × porPalet +
recargo del sentido (20 % sobre bultos y palets, de Mar del Plata a Buenos
Aires) + extra de la zona`
(solo Batán / Sierra de los Padres), redondeado a `TARIFAS.redondeo`. Si
Saldar pasa una tabla con precios que no suben parejo cada 10 kg, o cobra
por kilo exacto, cambiar `precioBulto()` (y `rangoBulto()`, que arma el
texto "de 20 a 30 kg").

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
  - Azul `--azul` `#0756DB` (botones, precios, cinta, franja "Cómo
    funciona"). Sale del logo real (`#0864FF`, 27/10/2026), un punto más
    oscuro: con `#0864FF` el texto azul sobre los fondos celestes no llega
    al contraste mínimo (4,3 a 1). `--azul-osc #0544B0`, `--azul-claro
    #E7F0FF`, `--azul-suave #DFE9FF`.
  - Blanco y casi blanco `#F5F7FC` de fondo; tarjetas blancas.
  - Negro `--tinta` `#0C1018` para los detalles: cabecera del presupuesto,
    números de paso, barra de VISTA PREVIA, tarjeta de contacto, código de
    barras, punto de destino y Miramar en el mapa.
  - Los tokens están en `:root`; no hay naranja ni verde en ningún lado.
- Idea: **etiqueta / hoja de ruta**. Hoja de ruta MDP → BA con código de
  barras en la portada, cinta de embalaje azul con el nombre, el presupuesto
  como ticket, numeración de secciones en tipografía mono.
- **Orden: Buenos Aires → Mar del Plata primero** (el que más hacen; pedido de
  Mateo, 23/10/2026): título, portada, hoja de ruta (BA → MDP), cinta,
  servicios, cotizador (viene elegido), recorrido (primero la sucursal de
  Buenos Aires), ficha de Google y pie.
- Titular: "Buenos Aires – Mar del Plata, ida y vuelta." (lo resaltado es
  "ida y vuelta", porque los camiones van y vienen). Arriba dice "Logística y
  distribución · Buenos Aires – Mar del Plata".
- Cotizador: sentido (dos tarjetas) + filas de bultos (peso en kg +
  cantidad + ×, cada una muestra su precio "c/u · de 20 a 30 kg"; botón "+
  Agregar un bulto de otro peso"; arranca con 1 bulto de 10 kg; el peso
  queda entre 1 y 400 al salir del campo) + **"Opción palet"** cerrada
  ("¿Embalás todo en un palet?"; al abrirla suma 1 palet y muestra el
  contador, al cerrarla lo saca; si los bultos ya suman lo que vale un palet,
  se pinta de azul y dice "te puede convenir") + "Valor declarado de la
  mercadería" (`#valor`, acepta 250000 o 250.000; obligatorio). Nunca
  presentar el palet como alternativa al mismo nivel ("por peso o por
  palet"): el precio es **por peso y por bulto**, el palet es una opción
  (pedido del dueño, 23/10/2026); se puede cotizar solo
  bultos, solo palets o las dos cosas; las filas con bultos se marcan en azul; si llega a Mar del Plata,
  se elige la zona (Batán y Sierra con costo extra). Debajo del día dice
  `cuandoSale` del sentido: "Recibimos la carga de lunes a viernes y sale
  el sábado" (Buenos Aires → Mar del Plata) o "Recibimos la carga de lunes
  a viernes" (Mar del Plata → Buenos Aires).
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
- **Logo real** (imagen `img/saldar-logo.webp`): 44 px de alto en la cabecera
  desde 900 px, 38 px en el celular y en el pie. No deformarlo ni recortarlo.
- **Club CUDS** (sección 05, después de Recorrido): escudo a la izquierda,
  "Sponsors del CUDS" ("Saldar es sponsor del CUDS, club de rugby de Mar
  del Plata") y una tarjeta negra "¿Sos socio del CUDS?" con
  botón de WhatsApp ("Soy socio del CUDS y quiero consultar por el
  descuento"). En el cotizador, casilla "Soy socio del CUDS" que suma una
  línea al pedido. Pregunta frecuente del descuento. Nada de montos.
- **Trabajá con nosotros** (sección 07, antes de Contacto; link en el pie):
  pide nombre y teléfono (obligatorios), puesto y mensaje; el botón "Mandar
  mi CV por mail" es un `mailto:` a `NEGOCIO.mailCV` con asunto "CV -
  nombre" y los datos en el cuerpo. Sin servidor: el archivo lo adjunta la
  persona en su mail. Mientras `mailCV` esté vacío, avisa "Falta cargar el
  mail" y la barra de VISTA PREVIA lo menciona.
- Orden de secciones: 01 Servicios, 02 Cotizador, 03 Cómo funciona, 04
  Recorrido, 05 Club CUDS, 06 Preguntas, 07 Trabajo, 08 Contacto (fondos
  blancos alternados: CUDS y Trabajo en `seccion-blanca`).
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
| ¿De Mar del Plata a Buenos Aires qué días sale la carga? ¿También el sábado? | El 22/10 dijo "los sábados no sale la mercadería" y el 23/10 "ya sale el sábado" (pregunta sobre Buenos Aires). La web dice el sábado solo para Buenos Aires → Mar del Plata |
| Costo extra de Batán y Sierra de los Padres: ¿cuánto? ¿por envío o por bulto? | Hoy $ 5.000 de ejemplo por envío |
| Mudanzas: ¿cómo se cotizan? | Confirmado: dentro de Mar del Plata y entre Buenos Aires y Mar del Plata, de ida y de vuelta. Hoy "pedí presupuesto por WhatsApp" |
| Pago con tarjeta (más adelante) | El dueño prefiere esperar (23/10/2026). Cuando quiera: cuenta de Mercado Pago (u otra) para el link o botón de pago en la web; con posnet, sumar "tarjeta en el depósito" a `pagos` |
| Cuánto suma cada 10 kg más (o la tabla de precios de 10 a 400 kg) | Solo está el mínimo de 1 a 10 kg ($ 9.181,97); hoy + $ 1.800 de ejemplo por cada 10 kg |
| Valor declarado: ¿cambia el precio (seguro, un %)? ¿Es obligatorio? | Hoy solo va en el mensaje y es obligatorio para mandar el pedido |
| Más de 400 kg en un bulto | Hoy "escribinos"; el campo no deja pasar de 400 |
| Que en Buenos Aires la carga también sale de la sucursal | Inferido de "sale desde el depósito" + "hay sucursal en Buenos Aires" |
| ¿Retiran a domicilio además de entregar? | Se entendió que no: la carga sale del depósito; el formulario no pide dirección de retiro |
| A qué partes de Buenos Aires entregan (CABA, GBA…) | La web dice "Buenos Aires" |
| WhatsApp del negocio | Hoy todo va al de Mateo |
| Qué no llevan | "A confirmar" en preguntas |
| Franjas horarias del formulario (mañana / mediodía / cualquier horario) | Puestas sin horario exacto; se sacó "tarde". ¿En qué horario entregan? |
| Clientes o marcas que se puedan nombrar (con permiso) | No hay ninguno en la web |
| Algo que lo distinga (frecuencia, años haciendo el recorrido, seguimiento…) | No se puso nada |
| Mail para los CV de "Trabajá con nosotros" | Mateo se lo pidió al dueño (27/10/2026). Va en `NEGOCIO.mailCV` |
| Fotos propias (los camiones, el depósito, cargas) | Ninguna |

## Para publicar (cuando cierre)

- [ ] Cargar datos y tarifas reales; `tarifasDeEjemplo: false`.
- [ ] Cambiar `NEGOCIO.whatsapp` por el del negocio.
- [ ] Sacar `<meta name="robots" content="noindex">`.
- [ ] Revisar el JSON-LD: la sucursal ya está como `department` (Villa
      Soldati, CABA, C1437), y `telephone` y `url` solo si el dueño los
      confirma.
- [ ] Imagen `og.jpg` 1200×630 para cuando se comparte por WhatsApp, y `canonical` con el dominio.
- [ ] `publicar.py` de la skill → `docs/`, GitHub Pages, dominio, Search Console, Perfil de Empresa.

## Registro de cambios

- 27/10/2026 — Mateo: "sí, son sponsors del club" → sección del CUDS: título
  "Sponsors del CUDS" y "Saldar es sponsor del CUDS, club de rugby de Mar
  del Plata" (antes decía "acompaña").
- 27/10/2026 — Mateo pasó el logo de Saldar y el del CUDS (PDF) y pidió:
  "Trabajá con nosotros" para dejar el CV (el mail lo pasa el dueño), y un
  sector del CUDS con descuento para socios por WhatsApp → logo real en
  cabecera y pie (`img/saldar-logo.webp`), ícono de la pestaña con la "S",
  se sacó el logo provisorio (símbolo `#marca`); azul de toda la web
  ajustado al del logo (`#0756DB`); sección 05 Club CUDS con escudo y botón
  de WhatsApp; casilla "Soy socio del CUDS" en el cotizador; pregunta del
  descuento; sección 07 "Trabajá con nosotros" con `mailto:` (`mailCV`
  vacío por ahora); link en el pie; barra de VISTA PREVIA con el mail que
  falta; secciones renumeradas.
- 27/10/2026 — Mateo: "que diga logística y distribución" → `<title>`,
  description, Open Graph, JSON-LD, bajada de la portada, cinta, pie y
  comentario del código; el logo dice "LOGÍSTICA Y DISTRIBUCIÓN" (más
  ancho, "SALDAR" espaciado para emparejar, un poco más grande en la compu).
- 23/10/2026 — Mateo: "de lunes a viernes se recibe mercadería, porque ya
  sale el sábado"; "las mudanzas son para ambas también" → tarjeta de la
  sucursal "El sábado sale para Mar del Plata"; debajo del día, texto según
  el sentido (`cuandoSale`); "¿Cada cuánto viajan?" con la salida del
  sábado desde Buenos Aires; `sabados` = "el depósito de Mar del Plata está
  cerrado" (se sacó "no sale mercadería", que chocaba); mudanzas "dentro de
  Mar del Plata y entre Buenos Aires y Mar del Plata, de ida y de vuelta".
- 23/10/2026 — Mateo: "es la dirección de la sucursal de Buenos Aires, buscá
  dónde está" → buscado: John W. Cooke 3155 queda en Villa Soldati, CABA
  (C1437). `barrioBA: "Villa Soldati"`, `ciudadBA: "Ciudad de Buenos
  Aires"`; tarjeta "Sucursal · Villa Soldati, CABA" con la calle como
  título; el barrio va en contacto, aviso del cotizador, mensaje, preguntas,
  link a Maps y JSON-LD (`addressLocality`, `addressRegion`, `postalCode`).
- 23/10/2026 — Mateo pasó la dirección de la sucursal: "Cooke John William
  3155" → `sucursalBA: "John William Cooke 3155"` y `ciudadBA`; la tarjeta
  de la sucursal en Recorrido lleva la dirección como título y botón "Ver en
  Google Maps" (igual que el depósito); contacto con link al mapa; el aviso
  del cotizador y el mensaje dicen desde dónde sale; preguntas "¿Desde dónde
  sale la carga?" (las dos direcciones) y "¿Tienen sucursal…?" (dirección y
  horario); JSON-LD con la sucursal como `department`.
- 23/10/2026 — Audios de Mateo (el dueño): el precio es por peso y por
  bulto; el palet es un tipo de bulto, una opción aparte para el que embala
  todo junto y le conviene por la cantidad de bultos; agregar valor
  declarado → "Opción palet" cerrada debajo de los bultos (aviso "te puede
  convenir"), campo "Valor declarado" obligatorio que va en el mensaje, y
  "por peso o por palet" pasó a "por peso y por bulto" en portada, hoja de
  ruta, cotizador, etiquetas ("Por peso y bulto", "Opción palet"),
  preguntas, Open Graph y JSON-LD.
- 23/10/2026 — Mateo: el galpón de Mar del Plata abre a las 5, pero se
  empieza a recibir mercadería a las 8 aprox. → la web queda igual (muestra
  la recepción, de 8 a 15); anotado en Datos del negocio.
- 23/10/2026 — Mateo pasó respuestas del dueño: los envíos son en los dos
  sentidos; mudanzas dentro de Mar del Plata y también a Buenos Aires;
  recepción de mercadería de 8 a 17 en Buenos Aires y de 8 a 15 en Mar del
  Plata; la tarjeta se deja para más adelante → `recepcion` 8 a 15,
  `recepcionBA` nuevo (tarjeta de la sucursal en Recorrido, contacto,
  pregunta del horario y aviso del cotizador en los dos sentidos), JSON-LD
  cierra 15:00, textos de Mudanzas (tarjeta y pregunta). El extra de Batán y
  Sierras, los precios por peso, la sucursal y el WhatsApp los pasa después.
- 23/10/2026 — Mateo: el recargo del 20 % (Mar del Plata → Buenos Aires) es
  para todo → confirmado sobre bultos y palets (ya se calculaba así); la
  pregunta "¿Cómo se calcula el precio?" lo aclara.
- 23/10/2026 — Mateo: el palet completo vale $ 86.260,40 y el cotizador
  tiene que aceptar un bulto con sus kilos puntuales, de cualquier peso hasta
  unos 400 kg → las filas fijas por rango de peso pasaron a filas de bultos
  con peso en kg y cantidad (se agregan y se quitan), el precio sube cada
  10 kg desde el mínimo (ese paso es de ejemplo), palet real, pregunta
  "¿Hasta cuántos kilos por bulto?" y barra de VISTA PREVIA "Falta un precio".

- 23/10/2026 — Mateo: "también hay valor por palet" → fila de palets en el
  cotizador (precio de ejemplo), línea en el presupuesto y en el mensaje,
  pregunta "¿Llevan palets?", y "por peso o por palet" en portada, hoja de
  ruta, etiquetas y ficha de Google.
- 23/10/2026 — Mateo: de 1 a 10 kg se cobra el mínimo ($ 9.181,97), después
  de a 10 kg; predominan los viajes de Buenos Aires a Mar del Plata → rangos
  nuevos de a 10 kg (el primero real, el resto marcado "ejemplo"), precios
  con centavos sin redondear, y Buenos Aires → Mar del Plata primero en toda
  la web (viene elegido en el cotizador).
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
