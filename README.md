# Voluntariado Connect: análisis y diseño (Fases 1 y 2)

Código fuente de los artefactos de análisis y diseño de **Voluntariado Connect**, la plataforma web con la que la universidad conecta a estudiantes interesados en la labor social con fundaciones y ONG locales. La plataforma gestiona perfiles, publica actividades de voluntariado, registra horas de servicio y emite certificados.

Universidad Manuela Beltrán, Ingeniería de Software, 2026.
Autores: Leidy Yohanna Cardona Bayona y Gustavo Adolfo Cardona Bayona.

El repositorio cubre las **Fases 1 a 4** de análisis y diseño y las fases del taller (entrevista con IA, Event Storming y User Story Mapping). Todos los diagramas están escritos como código (Graphviz y PlantUML), y los wireframes, los mockups y el prototipo salen de un mismo archivo HTML.

## Prototipo navegable

https://gustavo8015.github.io/TALLER-Tecnicas-de-Elicitaci-n-con-IA-y-Casos-de-Uso/fase-2-arquitectura/prototipo/

Toque los botones o las tarjetas para recorrer el flujo de inscripción del estudiante: inicio de sesión, búsqueda, detalle, confirmación y horas.

## Entrevista simulada asistida por IA

Antes del análisis se hizo una entrevista con MS Copilot, que actuó como director de una ONG poco tecnológico y preocupado por la privacidad de los datos de sus beneficiarios. La carpeta [`entrevista-ia/`](entrevista-ia/README.md) contiene el prompt, la transcripción de las 8 preguntas con sus capturas de pantalla y el **Entregable 2**: los hallazgos clasificados en Requisitos de Usuario, Requisitos Funcionales y Restricciones (No Funcionales).

## Contenido

| # | Artefacto | Fase | Código fuente | Imagen |
|---|-----------|------|---------------|--------|
| 1 | Requerimientos funcionales y no funcionales | 1 | Este README | |
| 2 | Árbol de descomposición funcional | 1 | [`arbol.dot`](fase-1-descubrimiento/arbol-descomposicion/arbol.dot) | [PNG](fase-1-descubrimiento/arbol-descomposicion/arbol.png) |
| 3 | Épicas y casos de uso | 1 | [`casos-de-uso.puml`](fase-1-descubrimiento/casos-de-uso/casos-de-uso.puml) | [PNG](fase-1-descubrimiento/casos-de-uso/casos-de-uso.png) |
| 4 | Wireframes | 1 | [`index.html`](fase-2-arquitectura/prototipo/index.html) en modo `?wf=1` | [PNG](fase-1-descubrimiento/wireframes/wireframes.png) |
| 5 | Architecture Decision Records (ADR) | 2 | Este README | |
| 6 | Diagramas C4, niveles 1 y 2 | 2 | [`c4-contexto.dot`](fase-2-arquitectura/c4/c4-contexto.dot), [`c4-contenedores.dot`](fase-2-arquitectura/c4/c4-contenedores.dot) | [Contexto](fase-2-arquitectura/c4/c4-contexto.png), [Contenedores](fase-2-arquitectura/c4/c4-contenedores.png) |
| 7 | Diagrama de despliegue | 2 | [`despliegue.puml`](fase-2-arquitectura/despliegue/despliegue.puml) | [PNG](fase-2-arquitectura/despliegue/despliegue.png) |
| 8 | Mockups | 2 | [`index.html`](fase-2-arquitectura/prototipo/index.html) | [PNG](fase-2-arquitectura/mockups/mockups.png) |
| 9 | Prototipo funcional | 2 | [`index.html`](fase-2-arquitectura/prototipo/index.html), [`flujo-prototipo.puml`](fase-2-arquitectura/prototipo/flujo-prototipo.puml) | [Flujo](fase-2-arquitectura/prototipo/flujo-prototipo.png), [Pantallas](fase-2-arquitectura/prototipo/pantallas-prototipo.png) |
| 10 | Historias de usuario | 3 | [`historias.json`](fase-3-detalle-agil/historias.json) | [Lista](fase-3-detalle-agil/README.md) |
| 11 | Criterios de aceptación y DoR | 3 | Documento del taller | [Mockups DoR](fase-3-detalle-agil/mockups-dor.png) |
| 12 | Diagrama entidad relación | 4 | [`entidad-relacion.puml`](fase-4-diseno-detallado/entidad-relacion/entidad-relacion.puml) | [PNG](fase-4-diseno-detallado/entidad-relacion/entidad-relacion.png) |
| 13 | Diagramas de clases por módulo | 4 | [`clases_inscripciones.puml`](fase-4-diseno-detallado/clases/clases_inscripciones.puml), [`clases_horas.puml`](fase-4-diseno-detallado/clases/clases_horas.puml) | [Inscripciones](fase-4-diseno-detallado/clases/clases_inscripciones.png), [Horas](fase-4-diseno-detallado/clases/clases_horas.png) |
| 14 | Diagramas de secuencia | 4 | [`sec_inscripcion.puml`](fase-4-diseno-detallado/secuencia/sec_inscripcion.puml), [`sec_certificado.puml`](fase-4-diseno-detallado/secuencia/sec_certificado.puml) | [Inscripción](fase-4-diseno-detallado/secuencia/sec_inscripcion.png), [Certificado](fase-4-diseno-detallado/secuencia/sec_certificado.png) |
| 15 | Diagrama C4 nivel 3 (componentes) | 4 | [`c4-componentes.dot`](fase-4-diseno-detallado/c4-componentes/c4-componentes.dot) | [PNG](fase-4-diseno-detallado/c4-componentes/c4-componentes.png) |
| 16 | Definition of Done | 4 | Documento del taller | |

```
voluntariado-connect/
├── entrevista-ia/              prompt, transcripción, capturas y Entregable 2
├── fase-1-descubrimiento/
│   ├── arbol-descomposicion/   árbol funcional (Graphviz)
│   ├── casos-de-uso/           casos de uso por épica (PlantUML)
│   └── wireframes/             captura de baja fidelidad
├── fase-2-arquitectura/
│   ├── c4/                     contexto y contenedores (Graphviz)
│   ├── despliegue/             despliegue en Azure (PlantUML)
│   ├── mockups/                captura de alta fidelidad
│   └── prototipo/              prototipo HTML y su flujo (PlantUML)
└── scripts/
    ├── render-diagramas.sh     genera los PNG de los diagramas
    └── capturas_pantallas.py   genera wireframes, mockups y pantallas
```

## Fases del taller

- **Fase 3: Event Storming y modelado como código.** [`actividad.puml`](taller-fase-3-event-storming/actividad.puml), exportado en [PNG](taller-fase-3-event-storming/actividad.png) y [SVG](taller-fase-3-event-storming/actividad.svg) (Entregable 3), y la [lluvia de eventos](taller-fase-3-event-storming/lluvia-de-eventos.png).
- **Fase 4: User Story Mapping.** [Tablero](taller-fase-4-story-mapping/tablero.png) con Backlog del Producto, Sprint 1 (MVP) y Para el futuro, generado por [`tablero.py`](taller-fase-4-story-mapping/tablero.py). Tablero público en Trello: https://trello.com/b/vN7XsR7X ([captura](taller-fase-4-story-mapping/tablero-trello.png)).
- **Fase 1: mapas de empatía.** Tablero de FigJam: https://www.figma.com/board/vp4WPlftkDTHNNZqGt0Kot

## Fase 1: descubrimiento y abstracción del negocio

### 1. Requerimientos

**Funcionales**

- RF-01. Registro e inicio de sesión de estudiantes con su correo institucional.
- RF-02. Roles de estudiante, coordinador de ONG, personal autorizado de la fundación y administrador universitario, con permisos diferenciados.
- RF-03. Registro de fundaciones. No pueden publicar hasta que la universidad verifique su legitimidad y a sus responsables.
- RF-04. Registro de los datos mínimos de los beneficiarios, ocultos para los voluntarios.
- RF-05. Crear, editar y cancelar actividades con nombre, descripción, fecha, horario, lugar, cupos, requisitos y responsable.
- RF-06. Búsqueda de actividades por fecha, franja horaria, localidad y causa.
- RF-07. Control de cupos al inscribirse y aviso de actividad llena.
- RF-08. Notificaciones de inscripción, cambios, cancelaciones, recordatorios y horas pendientes de aprobación.
- RF-09. Registro de asistencia y horas, con aprobación de un responsable de la fundación.
- RF-10. Historial de actividades y total de horas del estudiante frente al requisito de grado.
- RF-11. Certificado PDF con código de verificación.
- RF-12. Reportes de horas y voluntarios por fundación y por periodo.

**No funcionales (con métrica)**

- RNF-01. Privacidad: datos mínimos de beneficiarios y tratamiento conforme a la Ley 1581 de 2012. El rol estudiante no ve ningún campo de beneficiarios.
- RNF-02. Seguridad: control de acceso por rol y TLS 1.2 o superior. El 100 % de las rutas protegidas rechaza tokens inválidos.
- RNF-03. Usabilidad y accesibilidad: diseño para móvil, WCAG 2.1 AA y áreas táctiles de 44 px o más. Publicar una actividad toma cinco pasos o menos.
- RNF-04. Rendimiento: el percentil 95 de búsqueda y verificación de cupos está por debajo de 2 s con 200 usuarios concurrentes.
- RNF-05. Integridad y trazabilidad: bitácora de cambios en horas y certificados. Cero inscripciones por encima del cupo.

### 3. Épicas

- E1. Cuentas y acceso (RF-01, RF-02)
- E2. Gestión de fundaciones (RF-03, RF-04)
- E3. Gestión de actividades (RF-05, RF-06)
- E4. Inscripciones y notificaciones (RF-07, RF-08)
- E5. Registro y validación de horas (RF-09, RF-10)
- E6. Certificación y reportes (RF-11, RF-12)

## Fase 2: diseño arquitectural macro

### 5. Architecture Decision Records

Todas las decisiones están en estado **aceptado**.

| ADR | Decisión | Alternativa descartada |
|-----|----------|------------------------|
| 001 | Monolito modular, un módulo por épica | Microservicios: demasiado costo de operación para el volumen esperado |
| 002 | PostgreSQL relacional con transacciones ACID | NoSQL documental: el control de cupos necesita restricciones y transacciones |
| 003 | SPA en React, primero para móvil, con API REST en ASP.NET Core | Apps nativas: duplican el desarrollo |
| 004 | Inicio de sesión con Microsoft Entra ID (OpenID Connect) y permisos por rol | Cuentas locales para todos |
| 005 | Azure Static Web Apps, App Service, Database for PostgreSQL, Blob Storage y Communication Services | Máquinas virtuales administradas por el equipo |

## Cómo regenerar las imágenes

Requisitos: [Graphviz](https://graphviz.org/), [PlantUML](https://plantuml.com/) con Java, y Python 3 con `playwright` y `pillow`.

```bash
# Diagramas (árbol, casos de uso, C4, despliegue y flujo del prototipo)
PLANTUML="java -jar plantuml.jar" ./scripts/render-diagramas.sh

# Wireframes, mockups y pantallas del prototipo
pip install playwright pillow
playwright install chromium
python scripts/capturas_pantallas.py
```

Para ver el prototipo en local, abra `fase-2-arquitectura/prototipo/index.html` en el navegador. Los parámetros `?s=s3` (pantalla inicial) y `?wf=1` (modo wireframe) son opcionales.

## Alcance

Este repositorio cubre las cuatro fases de análisis y diseño. La implementación del código de la plataforma corresponde al Sprint 1.

Los datos de fundaciones, personas y actividades que aparecen en el prototipo son ficticios.
