# Voluntariado Connect: análisis y diseño (Fases 1 y 2)

Código fuente de los artefactos de análisis y diseño de **Voluntariado Connect**, la plataforma web con la que la universidad conecta a estudiantes interesados en la labor social con fundaciones y ONG locales. La plataforma gestiona perfiles, publica actividades de voluntariado, registra horas de servicio y emite certificados.

Universidad Manuela Beltrán, Ingeniería de Software, 2026.
Autores: Leidy Yohanna Cardona Bayona y Gustavo Adolfo Cardona Bayona.

El repositorio llega **solo hasta la Fase 2**. Todos los diagramas están escritos como código (Graphviz y PlantUML), y los wireframes, los mockups y el prototipo salen de un mismo archivo HTML.

## Prototipo navegable

https://gustavo8015.github.io/TALLER-Tecnicas-de-Elicitaci-n-con-IA-y-Casos-de-Uso/fase-2-arquitectura/prototipo/

Toque los botones o las tarjetas para recorrer el flujo de inscripción del estudiante: inicio de sesión, búsqueda, detalle, confirmación y horas.

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

```
voluntariado-connect/
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

Este repositorio cubre la Fase 1 (descubrimiento) y la Fase 2 (diseño arquitectural macro). Las historias de usuario, los criterios de aceptación, el modelo entidad relación y los diagramas de clases, de secuencia y C4 nivel 3 corresponden a fases posteriores.

Los datos de fundaciones, personas y actividades que aparecen en el prototipo son ficticios.
