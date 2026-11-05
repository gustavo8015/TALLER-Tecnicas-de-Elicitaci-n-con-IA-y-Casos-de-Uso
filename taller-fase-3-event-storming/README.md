# Taller, Fase 3: Event Storming y modelado como código

Proceso modelado: "Un estudiante se inscribe a una actividad y recibe su certificado".

- `lluvia-de-eventos.html` / `lluvia-de-eventos.png`: eventos de dominio en orden cronológico, con comandos, actores, políticas y puntos críticos.
- `actividad.puml`: diagrama de actividades en PlantUML con carriles, cuatro decisiones y un `fork` para las notificaciones paralelas.
- `actividad.png` y `actividad.svg`: diagrama renderizado (Entregable 3).

Secuencia de eventos: Cuenta Creada → Fundación Registrada → ONG Validada → Evento Publicado → Estudiante Inscrito → Recordatorio Enviado → Horas Registradas → Horas Aprobadas → Certificado Emitido → Certificado Verificado.

Para volver a renderizar: `java -jar plantuml.jar -tpng -tsvg actividad.puml`, o pegar el código en el servidor web de PlantUML.
