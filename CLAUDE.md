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
sucursal en Buenos Aires. Está **desde 2015**. También hace **mudanzas** y lleva **congelados**. **En la web se dice "logística y distribución", nunca "fletes"**
(pedido de Mateo, 20 y 27/10/2026). Es una **demo de venta** de Mateo
Berchot: se le muestra al dueño funcionando y se le ofrece con abono mensual.
Primer cliente no gastronómico (el anterior fue Pizzería La Nieve).

- Repo: `berchotmateo-spec/Saldar` — rama de trabajo `claude/new-session-2zu43k` (todavía no hay `main`).
- Archivo único: `index.html` (HTML + CSS + JS, sin build; solo Google Fonts).
- **Dominio: `saldarlogistica.com.ar`** (lo compró Mateo en NIC.ar el
  27/10/2026; `saldar.com.ar` estaba tomado). Vence en un año: renovarlo
  antes del 27/10/2027 (la fecha exacta está en nic.ar → Mis dominios). El
  dueño quiere la web en internet antes del fin de semana del 31/10 para
  poner QR en carteles.
- **Publicación (hecha el 28/10/2026):** GitHub Pages desde la rama
  `claude/new-session-2zu43k` (es la rama por defecto del repo; no hay
  `main`), carpeta **`/docs`**. Después de cada cambio:
  `python3 publicar.py saldarlogistica.com.ar` (arma `docs/` con `CNAME`,
  `robots.txt`, `sitemap.xml`, `.nojekyll`, `img/` y `og.jpg`) y commitear
  `docs/`. **El repo es privado**: GitHub Pages gratis solo anda con repos
  públicos, así que Mateo tiene que hacerlo público (se revisó el
  historial el 27/10/2026: no hay nada privado). Cadena del dominio: NIC.ar
  (delegación a los 2 nameservers de Cloudflare) → Cloudflare (4 A del `@`
  a `185.199.108.153`, `.109.153`, `.110.153`, `.111.153` y CNAME `www` →
  `berchotmateo-spec.github.io`, todo en gris, "DNS only") → GitHub Pages
  (Custom domain `saldarlogistica.com.ar`, después Enforce HTTPS).
  Estado 27/10/2026: repo público ✅, Pages desde la rama `/docs` con el
  Custom domain ✅ (el github.io ya redirige al dominio), cuenta de
  Cloudflare con el sitio agregado ✅; nameservers de Cloudflare:
  **`nina.ns.cloudflare.com`** y **`sergi.ns.cloudflare.com`**. Los 5
  registros en Cloudflare cargados y en gris ✅ (captura de Mateo).
  Delegación en NIC.ar publicada ✅ (se vio el 27/10/2026 a las 21:16 de
  Argentina: NS de Cloudflare, los 4 A de GitHub y el `www`). Falta que
  GitHub emita el certificado del dominio ("Check again" en Pages; puede
  tardar hasta 24 h) y tildar **Enforce HTTPS**. Desde la sesión: el proxy
  no deja pedir `http://` (405); con `curl -vI https://saldarlogistica.com.ar/
  2>&1 | grep subject` se ve el certificado: `CN=*.github.io` = todavía no
  está el del dominio. El 28/10/2026 a las 0:05 de Argentina (casi 3 h después
  de la delegación) seguía sin certificado; el DNS estaba bien (4 A, `www`,
  sin AAAA ni CAA que lo trabe). Si no aparece, el remedio es sacar el
  dominio en Pages (*Remove*) y volver a ponerlo (*Save*). Ojo: eso puede
  hacer que GitHub commitee en la rama (borra y vuelve a crear
  `docs/CNAME`): hacer `git pull` antes del próximo push.
  **28/10/2026, 12:49 de Argentina: certificado emitido ✅** (Let's Encrypt,
  `CN=saldarlogistica.com.ar`, vence el 26/01/2027 y GitHub lo renueva
  solo), **Enforce HTTPS tildado ✅** (captura de Mateo),
  `https://saldarlogistica.com.ar/` responde 200 y `www` redirige al
  dominio sin `www`. En Pages puede seguir diciendo "DNS Check in Progress"
  en amarillo: no afecta.
- **El DNS se puede revisar desde la sesión** con DNS por HTTPS (el `dig`
  no anda): `curl -sS -H 'accept: application/dns-json'
  'https://cloudflare-dns.com/dns-query?name=saldarlogistica.com.ar&type=NS'`.
  `"Status":3` = todavía no está delegado (así estaba el 27/10/2026 a la
  noche, recién comprado).
- QR: `qr/qr-saldarlogistica.png` (2460 px, para WhatsApp o Canva) y
  `qr/qr-saldarlogistica.svg` (imprenta). Abre `https://saldarlogistica.com.ar`
  (leído de vuelta con zxing-cpp). Hecho con `qr.py` de la skill.
- Imagen para compartir: `og.jpg` (1200 × 630), hecha en Chromium desde
  `og-fuente.html` (logo, "Desde 2015 · cargas en camión", el titular y una
  cinta con el dominio). El `<head>` tiene `canonical`, `og:url`,
  `og:image` y el JSON-LD `url`, `logo` e `image`, todo con el dominio.
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
| Trayectoria | **Desde 2015**: bajada de la portada, hoja de ruta ("Saldar · desde 2015"), pregunta "¿Desde cuándo están?", pie, description, Open Graph y JSON-LD (`foundingDate`) | El dueño, vía Mateo, 27/10/2026 ✅ |
| Depósito | Victoriano Montes 1963, Mar del Plata (link a Google Maps). La carga sale desde acá | El dueño, vía Mateo, 20/10/2026 ✅. Mateo escribió "victoriano monte"; la calle es Dr. Victoriano E. Montes |
| Servicios | Buenos Aires → Mar del Plata y Mar del Plata → Buenos Aires, y mudanzas (dentro de Mar del Plata y entre Buenos Aires y Mar del Plata, de ida y de vuelta) | El dueño, vía Mateo, 19, 20, 22 y 23/10/2026 ✅. **No tiene mensajería** |
| Congelados | Se permiten | El dueño, vía Mateo, 22/10/2026 ✅ |
| Factura | Hace Factura A | El dueño, vía Mateo, 22/10/2026 ✅ |
| Vehículos | Camiones | El dueño, vía Mateo, 20/10/2026 ✅ |
| Cómo cobra | Por bulto según sus kilos, de a 10 kg. **Cada bulto puede pesar hasta 4.000 kg** (audio del dueño, 27/10: "por bulto se puede hasta 4.000 kilos… se puede un montón"; antes "unos 400 kg por bulto"): el campo de kilos llega a 4.000 y la pregunta dice "si tenés algo más pesado, escribinos". **De 1 a 10 kg se cobra el mínimo: $ 9.181,97.** **Opción palet** (aparte, para el que embala toda la carga en un palet; con muchos bultos le conviene): **$ 86.260,40 el palet completo.** De Mar del Plata a Buenos Aires, recargo del 20 % sobre todo (bultos y palets) | El dueño, vía Mateo, 20 y 23/10/2026 ✅ (falta cuánto suma cada 10 kg). Audios del 23/10: "primero es por peso y por bulto, y después los que lo quieran mandar en palet, por palet" |
| Valor declarado | El cliente pone cuánto vale **toda** la mercadería, bultos y palets (**obligatorio**, "sí o sí"), en **pesos, dólares o euros** (Saldar lo pasa a pesos); va en el mensaje de WhatsApp ("$ 250.000", "US$ 1.500", "€ 1.200"). **Con él se calcula el seguro: valor × 6 ÷ 1.000 (0,6 %)**. **El cotizador lo calcula solo en pesos** (se suma al total como una línea más). En dólares o euros no lo calcula: debajo del total dice que lo pasan a pesos y calculan el seguro por WhatsApp, y el mensaje dice "+ seguro" y "a calcular (pasar US$ 1.500 a pesos)" | Pedido del dueño, vía Mateo, 23/10/2026 ✅. Monedas y "para todo": audio del dueño, 27/10/2026 ✅. Seguro: el dueño, vía Mateo, 27/10/2026 ✅ ("valor declarado x 6 dividido 1000"). Dólares y euros: audio del dueño, 27/10/2026 ✅ ("que solo se cotice en pesos y si es en euros o en dólares, que escriban al WhatsApp, que hacemos la conversión") |
| Entrega | **Buenos Aires → Mar del Plata: a domicilio.** **Mar del Plata → Buenos Aires: se retira por la sucursal de Buenos Aires** (el formulario esconde la dirección de entrega, el aviso y el mensaje dicen "Retira en: Sucursal de Buenos Aires…") | El dueño, vía Mateo, 20/10/2026 ✅. Retiro: 27/10/2026 ✅ ("cuando sale de mdp a bs as se retira por el depósito" = la sucursal de Villa Soldati; Mateo lo confirmó el mismo día) |
| Sucursal Buenos Aires | **John William Cooke 3155, Villa Soldati (CABA)**, C1437 (link a Google Maps). La carga de Buenos Aires → Mar del Plata sale de acá, y acá se retira la que viene de Mar del Plata. Recibe de 8 a 17 | Dirección: el dueño, vía Mateo, 23/10/2026 ✅ (escribió "Cooke John William 3155"). Barrio: buscado por Claude el 23/10/2026 (Waze, directorios de transporte y un aviso de galpón en Cooke 3200 dicen CABA, C1437, Villa Soldati). En esa altura hay un predio con varios expresos (Tres Lomas, Veninga, TransRE…), uno con horario de lunes a viernes de 8 a 17 |
| Tarifas | 1–10 kg $ 9.181,97 (real). Cada 10 kg más: + $ 1.800 | ⚠️ El mínimo es real; el "+ $ 1.800" es de ejemplo (`kilos.ejemplo: true`, se ve "(ejemplo)") |
| Palet | $ 86.260,40 el palet completo | El dueño, vía Mateo, 23/10/2026 ✅ |
| WhatsApp | El de Mateo (pruebas) | ⚠️ Falta el del negocio |
| Horario | Trabaja de lunes a sábados. Recepción de carga: **sucursal de Buenos Aires de 8 a 17**, **depósito de Mar del Plata de 8 a 13** (el depósito está abierto de 8 a 15), de lunes a viernes. **De Buenos Aires la carga sale el sábado.** Sábados el depósito de Mar del Plata está cerrado | El dueño, vía Mateo, 22, 23 y 27/10/2026 ✅ ("de lunes a viernes se recibe mercadería, porque ya sale el sábado"; 27/10: "en mdp de 8 a 15, pero para recibir mercadería de 8 a 13", `horarioMdp` y `recepcion`). El 23/10 reemplaza el "8 a 16:30" y aclara el "6 a 15": el galpón de Mar del Plata abre a las 5, pero la mercadería se recibe desde las 8 aprox. (en la web va solo la recepción, para que nadie llegue a las 5). El 22/10 había dicho "los sábados no sale la mercadería" (se entendió del depósito de Mar del Plata); la web ya no lo dice. En el JSON-LD (depósito): lunes a viernes 8 a 15 |
| Medios de pago | Efectivo y transferencia | El dueño, vía Mateo, 22/10/2026 ✅ (reemplaza "todos los medios"). Tarjeta: el dueño prefiere esperar (23/10/2026); en la web no se menciona |
| Zonas de entrega | Mar del Plata y Buenos Aires; en Mar del Plata también Batán y Sierra de los Padres con costo extra | El dueño, vía Mateo, 22/10/2026 ✅ (el monto del extra falta) |
| Qué no llevan | Cristalería no, salvo que esté bien embalada; en ese caso viaja sin seguro (solo en preguntas; el cotizador no lo controla) | El dueño, vía Mateo, 27/10/2026 ✅ |
| Cada cuánto viajan | De Buenos Aires sale el sábado (lo recibido de lunes a viernes) | El dueño, vía Mateo, 23/10/2026 ✅ (falta Mar del Plata → Buenos Aires) |

| Instagram | @saldar223 | — |
| Logo | El real: `img/saldar-logo.webp` (708 × 140, sacado del PDF "SALDAR.pdf", que trae una imagen de 1201 × 281). Ícono de la pestaña: `img/favicon.png`, la "S" del logo en blanco sobre azul | El dueño, vía Mateo, 27/10/2026 ✅. Si pasan el logo en vector (SVG, AI, PDF sin imagen adentro), cambiarlo |
| CUDS | Saldar es **sponsor** de CUDS, club de rugby de Mar del Plata; los socios de CUDS tienen un descuento en el servicio (se consulta por WhatsApp, sin monto en la web). Escudo: `img/cuds-logo.webp` (del PDF "cuds_logo.pdf", vectorial) | El dueño, vía Mateo, 27/10/2026 ✅ ("son sponsors del club"). En la web: "¡Somos sponsors de CUDS!" + carnet de socio (opción 2 elegida por Mateo) |
| Trabajá con nosotros | Recuadro en el pie con botón "Mandar mi CV" y link en el menú (no es sección) que abre el mail de la persona a logisticasaldar1963@gmail.com, asunto "CV - Trabajá con nosotros" y un modelo (nombre, teléfono, en qué le gustaría trabajar); el CV lo adjunta ella | Pedido del dueño, vía Mateo, 27/10/2026 ✅. Mail: **logisticasaldar1963@gmail.com** (`NEGOCIO.mailCV`, el dueño vía Mateo, 27/10/2026) |
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
  `horarioMdp` (cuándo está abierto el depósito de Mar del Plata),
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
  lo que suma cada 10 kg más, `maximo` = 4000 kg, `ejemplo`: sacarlo
  cuando `porTramoExtra` sea real), **`zonasMdp`** (Mar del
  Plata sin extra, Batán y Sierra de los Padres con `extra`; solo aparece
  cuando la entrega es en Mar del Plata) **`seguro`** (`porMil`: 6 = valor declarado × 6 ÷ 1.000) y `sentidos` (de dónde
  sale la carga en cada sentido: depósito de Mar del Plata o sucursal de
  Buenos Aires; `direccionSalida` y `recepcionSalida` dicen qué dato de
  `NEGOCIO` tiene la dirección y el horario de ese lugar, para el aviso del
  cotizador; `recargo` en %: 20 para Mar del Plata → Buenos Aires, 0 para
  la vuelta; `retiro: true` = en destino se retira por la sucursal, sin
  dirección de entrega).

Reglas: los precios van **sin puntos de miles ni $; los centavos con punto**
(`9181.97`, `15000`). El formato (`$ 9.181,97`, `$ 15.000`) lo hace la
función `pesos()`: muestra centavos solo si el monto los tiene.

Cálculo (`calcular()`): cada fila de bultos tiene kilos y cantidad; el
precio de un bulto (`precioBulto()`) es `minimo + (tramos − 1) × porTramoExtra`,
con `tramos = ⌈kg / 10⌉` (10 kg = mínimo, 25 kg = 3 tramos, 4.000 kg = 400);
`total = suma de (cantidad × precio de cada fila) + palets × porPalet +
recargo del sentido (20 % sobre bultos y palets, de Mar del Plata a Buenos
Aires) + extra de la zona + seguro`
(zona: solo Batán / Sierra de los Padres; seguro: valor × porMil ÷ 1.000, solo si el valor está en pesos — en dólares o euros no se calcula y un aviso debajo del total dice que se calcula por WhatsApp), redondeado a `TARIFAS.redondeo`. Si
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
  queda entre 1 y 4.000 al salir del campo) + **"Opción palet"** cerrada
  ("¿Embalás todo en un palet?"; al abrirla suma 1 palet y muestra el
  contador, al cerrarla lo saca; si los bultos ya suman lo que vale un palet,
  se pinta de azul y dice "te puede convenir") + "Valor declarado de la
  mercadería" (`#moneda` $ Pesos / US$ Dólares / € Euros + `#valor`, acepta
  250000 o 250.000; obligatorio; `MONEDAS` y `valorDeclarado()` arman el
  texto del mensaje). El seguro (0,6 %) sale en el presupuesto como una
  línea más si es en pesos; si es en otra moneda, debajo del total
  (`#ticket-seguro`, `MONEDAS_NOMBRE`): "+ Seguro (0,6 % del valor
  declarado): como el valor está en dólares, lo pasamos a pesos y te lo
  calculamos por WhatsApp."; sin valor dice "completá el valor declarado". De Mar
  del Plata a Buenos Aires se esconde la dirección de entrega (`#campo-dir`)
  y el aviso dice que se retira por la sucursal (`retiroFrase()`). Nunca
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
- **Se dice "de CUDS", nunca "del CUDS"** (pedido de Mateo, 27/10/2026): en
  títulos, carnet, pasos, casilla del cotizador, mensaje de WhatsApp y
  preguntas.
- **Club CUDS** (sección 05, después de Recorrido) = **opción 2 "Carnet de
  socio"** de los prototipos, elegida por Mateo (27/10/2026): arriba
  "¡Somos sponsors de CUDS!" con los logos "CUDS × SALDAR" al lado
  (`.cuds-cabeza`, `.cuds-dupla`, × en SVG); después el **carnet** negro
  (`.carnet`): escudo en un recuadro blanco, "Beneficio para socios del
  CUDS" y "Tenés **descuento** en el servicio" (la palabra en azul), y un
  **talón** troquelado (línea punteada con muescas del color del fondo) con
  "¿Cómo lo pedís?" y el botón de WhatsApp "Pedir mi descuento" ("Soy socio
  de CUDS y quiero consultar por el descuento"); abajo **3 pasos**: Sos
  socio de CUDS · Nos escribís por WhatsApp · Te confirmamos el descuento.
  En el celular el talón va debajo. En el cotizador, casilla "Soy socio de CUDS" que suma una
  línea al pedido. Pregunta frecuente del descuento. Nada de montos.
- **Trabajá con nosotros** **no es una sección** (pedido de Mateo,
  27/10/2026): es un recuadro en el pie, arriba del logo (`.pie-trabajo`,
  `[data-mail-cv-bloque]`: tarjeta blanca con borde negro y sombra azul,
  ícono de sobre, título "Trabajá con nosotros", "Mandanos tu CV a …" y
  botón "Mandar mi CV"; más a la vista por pedido del dueño, 27/10/2026), y
  el "08" del menú, los dos `[data-mail-cv]`: `mailto:` a
  `NEGOCIO.mailCV` con asunto "CV - Trabajá con nosotros" y un modelo en el
  cuerpo. Abren en pestaña nueva (como WhatsApp, para que anden en la vista
  previa). Si `mailCV` quedara vacío, los links y el recuadro se esconden.
- **Menú de las tres rayitas** (`#menu-boton` + `#menu-panel`, en todos los
  tamaños; pedido de Mateo, 27/10/2026): botón cuadrado con el mismo estilo
  que el WhatsApp de la cabecera (se pone negro con una × al abrir). El
  panel baja debajo de la cabecera con las 7 secciones numeradas, **"08
  Trabajá con nosotros"** (mismo estilo, abre el mail; no es sección), y
  abajo WhatsApp e Instagram (pedido de Mateo, 28/10/2026: se sacó el
  recuadro de "Trabajá con nosotros" que estaba debajo de Instagram). Se cierra al tocar un link o con Esc.
  En la compu sigue también el menú corto (Servicios, Recorrido, Preguntas,
  Contacto). En el celular (< 600 px) el WhatsApp de la cabecera se esconde
  (está en el menú) y el logo baja a 34 px (30 px en < 380 px).
- Orden de secciones: 01 Servicios, 02 Cotizador, 03 Cómo funciona, 04
  Recorrido, 05 Club CUDS, 06 Preguntas, 07 Contacto (CUDS en
  `seccion-blanca`).
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
| Cuánto suma cada 10 kg más (o la tabla de precios de 10 a 4.000 kg) | Solo está el mínimo de 1 a 10 kg ($ 9.181,97); hoy + $ 1.800 de ejemplo por cada 10 kg |
| (Opcional, más adelante) Que el cotizador pase solo los dólares o euros a pesos: ¿qué cotización usan (oficial, blue, MEP…)? | Hoy se calcula por WhatsApp (pedido del dueño, 27/10/2026). Se podría con la cotización del día de un servicio público (p. ej. DolarApi), pero depende de que ese servicio ande |
| Cristalería sin seguro: ¿el cotizador tiene que preguntar si va cristalería? | Hoy solo está en preguntas frecuentes |
| Que en Buenos Aires la carga también sale de la sucursal | Inferido de "sale desde el depósito" + "hay sucursal en Buenos Aires" |
| ¿Retiran a domicilio además de entregar? | Se entendió que no: la carga sale del depósito; el formulario no pide dirección de retiro |
| WhatsApp del negocio | Hoy todo va al de Mateo |
| Franjas horarias del formulario (mañana / mediodía / cualquier horario) | Puestas sin horario exacto; se sacó "tarde". ¿En qué horario entregan? |
| Clientes o marcas que se puedan nombrar (con permiso) | No hay ninguno en la web |
| Algo más que lo distinga (frecuencia, seguimiento…) | Ya está "desde 2015" (27/10/2026) |
| Dominio: ¿cuál de las opciones? ¿A nombre de quién (CUIT del dueño)? | `saldar.com.ar` está tomado; lista de opciones arriba ("Qué es"). Lo compra Mateo en NIC.ar |
| Fotos propias (los camiones, el depósito, cargas) | Ninguna |

## Para publicar (cuando cierre)

- [ ] Cargar datos y tarifas reales; `tarifasDeEjemplo: false`.
- [ ] Cambiar `NEGOCIO.whatsapp` por el del negocio.
- [ ] Sacar `<meta name="robots" content="noindex">`.
- [x] JSON-LD: sucursal como `department` (Villa Soldati, CABA, C1437),
      `url`, `logo` e `image` con el dominio (27/10/2026). `telephone`
      cuando esté el WhatsApp del negocio.
- [x] `og.jpg` 1200×630 y `canonical` con el dominio (27/10/2026).
- [x] `publicar.py` en la raíz → `docs/` con `CNAME` (27/10/2026).
- [x] QR en `qr/` (27/10/2026).
- [x] Mateo: repo público, GitHub Pages (rama `claude/new-session-2zu43k`,
      `/docs`, Custom domain), Cloudflare, delegación en NIC.ar y Enforce
      HTTPS (27 y 28/10/2026).
- [ ] Search Console (propiedad de dominio) y Perfil de Empresa de Google.
- [ ] Recordatorio en el calendario de Mateo para renovar el dominio.

## Registro de cambios

- 28/10/2026 — Mateo (captura del menú en el celular): "agregá el 08
  trabajar con nosotros y quitalo de abajo" → "08 Trabajá con nosotros" en
  la lista numerada del menú (abre el mail) y fuera el recuadro que estaba
  debajo de Instagram. El recuadro del pie queda (lo pidió el dueño más a la
  vista).
- 28/10/2026 — La página quedó en internet en
  **https://saldarlogistica.com.ar** con candado (certificado de Let's
  Encrypt emitido por GitHub, Enforce HTTPS tildado por Mateo). Sigue con
  `noindex`, el WhatsApp de Mateo y precios de ejemplo hasta que el dueño
  pase los datos.
- 27/10/2026 — Mateo compró el dominio **saldarlogistica.com.ar** → en la
  página `canonical`, `og:url`, `og:image` y JSON-LD con `url`, `logo` e
  `image`; imagen `og.jpg` (y su fuente `og-fuente.html`); `publicar.py`
  copiado de la skill y `docs/` armada con el `CNAME`; QR en `qr/`. El repo
  es privado y no hay `main`: Pages va desde la rama de trabajo, `/docs`,
  y Mateo tiene que hacer público el repo. El dominio todavía no estaba
  delegado (DNS por HTTPS: NXDOMAIN). Se deja el `noindex` hasta tener el
  WhatsApp del negocio y los precios reales.
- 27/10/2026 — Mateo confirmó el retiro por la sucursal de Buenos Aires
  ("la 1 está correcto") y pasó dos audios del dueño: los 4.000 kg son por
  bulto; el seguro de valores en dólares o euros lo calculan ellos por
  WhatsApp ("que solo se cotice en pesos") → preguntas "¿Hasta cuántos kilos
  puede pesar un bulto?" y del precio, ayuda de los bultos "Cada bulto puede
  pesar hasta 4.000 kg"; el cotizador ya no calcula el seguro en dólares o
  euros (aviso debajo del total, mensaje "+ seguro" y "a calcular (pasar
  US$ 1.500 a pesos)"), ayuda del valor y pregunta del valor declarado.
- 27/10/2026 — Mateo pasó datos del dueño: de Mar del Plata a Buenos Aires
  "se retira por el depósito"; está desde 2015; no llevan cristalería salvo
  bien embalada y sin seguro; cargas de hasta 4.000 kg e incluso más; el
  depósito de Mar del Plata abre de 8 a 15 pero recibe de 8 a 13; el CV más
  a la vista; el seguro es valor declarado × 6 ÷ 1.000 → retiro por la
  sucursal de Buenos Aires en ese sentido (sin dirección de entrega, aviso,
  "Llega a: Buenos Aires (retiro en sucursal)", mensaje "Retira en:",
  servicio con etiqueta "Retiro en sucursal", paso 3, recorrido, preguntas
  de domicilio y zonas); "desde 2015" en portada, hoja de ruta, pregunta
  nueva, pie, description, Open Graph y JSON-LD (`foundingDate`); pregunta
  "¿Qué cosas no llevan?" con la cristalería; kilos hasta 4.000 (pregunta
  "¿Hasta cuántos kilos llevan?", miles con punto: "de 3.990 a 4.000 kg");
  `horarioMdp` 8 a 15 y `recepcion` 8 a 13 (tarjeta del depósito, contacto,
  preguntas, aviso del cotizador); recuadro "Trabajá con nosotros" con
  botón "Mandar mi CV" en el pie; seguro del 0,6 % en el presupuesto, el
  mensaje y las preguntas (`TARIFAS.seguro`).
- 27/10/2026 — Mateo (captura del celular): más espacio entre "TENÉS" y el
  recuadro azul de "DESCUENTO", y que diga "socio de CUDS", no "del" →
  interlineado del título del carnet de .95 a 1.14; "del CUDS" → "de CUDS"
  en toda la web (8 lugares).
- 27/10/2026 — Audio de Mateo (el dueño): el valor declarado puede ser en
  euros o dólares (ellos lo pasan a pesos) y es para toda la mercadería,
  bultos y palets, sí o sí → selector de moneda al lado del valor ($ Pesos,
  US$ Dólares, € Euros), el mensaje dice la moneda, ayuda nueva y pregunta
  "¿Qué es el valor declarado?".
- 27/10/2026 — Mateo eligió la opción 2 de los prototipos del CUDS (carnet
  de socio) → la sección 05 pasó a título + logos, carnet con talón y
  botón "Pedir mi descuento", y 3 pasos. Prototipos:
  https://claude.ai/artifact/3RK6JhcF3Jyu78mrMxh1od
- 27/10/2026 — Mateo: "Trabajá con nosotros" que no sea una sección, que
  esté en el pie y lleve al mail; y un menú de tres rayitas con todo, eso
  incluido → se sacó la sección 07 (Contacto pasó a 07); link en el pie que
  abre el mail con un modelo; menú en la cabecera con las secciones,
  WhatsApp, Instagram y "Trabajá con nosotros".
- 27/10/2026 — Mateo pasó el mail para los CV: logisticasaldar1963@gmail.com
  → `NEGOCIO.mailCV`; "Trabajá con nosotros" ya abre el mail con los datos;
  la barra de VISTA PREVIA ya no menciona el mail.
- 27/10/2026 — 3 prototipos del sector CUDS (compu y celular) en un lienzo
  de diseño aparte: https://claude.ai/artifact/3RK6JhcF3Jyu78mrMxh1od. Todos
  con "¡Somos sponsors del CUDS!", los dos logos y el descuento para socios
  por WhatsApp, sin montos.
- 27/10/2026 — Mateo: "la x entre ambos logos hacela más grande" → la ×
  pasó de letra a una cruz dibujada (SVG, negra, 24 a 38 px). Pidió también
  3 prototipos del sector CUDS antes de tocar la web (página aparte).
- 27/10/2026 — Mateo (comentario en la vista previa): sacar "Sponsors del
  CUDS", que se repite; la tarjeta del socio está bien; "¡Somos sponsors!"
  arriba de los logos → se sacaron el título y la frase "Saldar es sponsor
  del CUDS, club de rugby de Mar del Plata"; el título nuevo va arriba del
  recuadro de logos.
- 27/10/2026 — Mateo: "agregá el logo del CUDS, una X y el logo de Saldar;
  abajo, lo de socio está excelente" → en la sección del CUDS el escudo solo
  pasó a un recuadro "CUDS × SALDAR"; la tarjeta "¿Sos socio del CUDS?"
  quedó igual.
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
