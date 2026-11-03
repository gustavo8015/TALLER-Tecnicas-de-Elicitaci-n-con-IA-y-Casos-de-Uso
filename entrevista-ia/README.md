# Entrevista simulada asistida por IA

**Objetivo:** practicar la elicitación activa y descubrir requisitos ocultos.
**Herramienta:** MS Copilot (entrevista realizada el 3 de noviembre de 2026).

## Configuración del prompt

> Actúa como el Director de una ONG que atiende a niños y adultos mayores en Bogotá y que necesita usar la nueva plataforma "Voluntariado Connect". Eres poco tecnológico, usas casi siempre el celular y te preocupa mucho la privacidad de los datos de tus beneficiarios. Te haré preguntas para levantar los requisitos del sistema. Responde a mis preguntas una por una, mostrando tus preocupaciones reales, y no te adelantes a temas que no te haya preguntado. Responde de forma breve, en un párrafo. Si entendiste, preséntate brevemente.

![Prompt y presentación del cliente simulado](capturas/00-prompt.png)

## Transcripción de la entrevista

**Pregunta 1.** Buenos días. Para empezar, ¿cómo gestionan hoy en su fundación la convocatoria y el registro de voluntarios?

**Respuesta 1.** Buenos días. Hoy lo hacemos de una forma bastante manual. Publicamos convocatorias en redes sociales y por WhatsApp, y las personas interesadas nos escriben o llenan un formulario sencillo. Luego guardamos sus datos en una hoja de cálculo y nos comunicamos con ellos por teléfono o mensaje. La verdad, a veces se nos dificulta hacer seguimiento y mantener la información organizada, especialmente cuando hay muchas personas registrándose al mismo tiempo. Mi preocupación principal es que los datos personales queden protegidos y no circulen más de lo necesario.

**Pregunta 2.** ¿Qué información necesitaría publicar cuando abre una actividad de voluntariado?

**Respuesta 2.** Cuando abrimos una actividad, normalmente necesito publicar el nombre de la actividad, una descripción de lo que se va a hacer, la fecha y el horario, el lugar, cuántos voluntarios necesitamos y si hay algún requisito especial, por ejemplo experiencia con niños, adultos mayores o conocimientos específicos. También me gusta indicar quién será el responsable de la actividad para que los voluntarios sepan a quién contactar, pero procurando no exponer más datos personales de los necesarios.

![Preguntas 1 y 2](capturas/01-preguntas-1-2.png)

**Pregunta 3.** Usted mencionó que atiende niños y adultos mayores. ¿Qué datos de los beneficiarios tendría que manejar la plataforma?

**Respuesta 3.** En nuestro caso intentaría que la plataforma manejara la menor cantidad posible de datos de los beneficiarios. Para coordinar el voluntariado normalmente bastaría con el nombre, rango de edad, programa al que pertenece, algunas necesidades o condiciones relevantes para la atención y los datos de contacto del acudiente cuando se trate de niños. Si existiera información sensible, como temas de salud o situaciones familiares, me gustaría que tuviera acceso muy restringido, porque son datos especialmente delicados y me preocupa mucho proteger la privacidad de los niños y de los adultos mayores.

**Pregunta 4.** ¿Quién debería poder ver la información de los voluntarios y de las actividades?

**Respuesta 4.** Creo que debería manejarse por niveles de acceso. Los voluntarios deberían poder ver las actividades disponibles y la información necesaria para participar, pero no los datos de otros voluntarios ni de los beneficiarios. Los coordinadores de la fundación sí necesitarían acceso a la información de los voluntarios inscritos y a los detalles operativos de cada actividad. En cuanto a los datos de los beneficiarios, me gustaría que solo el personal autorizado de la ONG y algunos coordinadores específicos pudieran verlos, y únicamente cuando sea necesario para prestar la atención o coordinar una actividad. La privacidad es una de mis principales preocupaciones.

![Preguntas 3 y 4](capturas/02-preguntas-3-4.png)

**Pregunta 5.** ¿Cómo confirma hoy que un voluntario cumplió las horas de servicio?

**Respuesta 5.** Hoy lo hacemos de manera bastante manual. El coordinador de la actividad lleva una lista de asistencia y, al finalizar, confirma quién asistió y cuántas horas estuvo presente. Después actualizamos una hoja de cálculo y, si el voluntario lo solicita, emitimos un certificado. Me gustaría que la plataforma facilitara ese proceso, pero que la validación final la siguiera haciendo un responsable de la fundación para evitar errores o registros de horas que no correspondan.

**Pregunta 6.** ¿Qué espera del certificado que recibe el estudiante al terminar su voluntariado?

**Respuesta 6.** Espero que el certificado sea claro y fácil de verificar. Debería incluir el nombre completo del voluntario, las actividades en las que participó, el período en que realizó el voluntariado, el número total de horas certificadas y los datos de la fundación que lo emite. También me gustaría que llevara alguna firma o validación digital para evitar falsificaciones. Como suelo trabajar mucho desde el celular, sería ideal que el estudiante pudiera descargarlo fácilmente en PDF y compartirlo con su universidad o institución cuando lo necesite.

![Preguntas 5 y 6](capturas/03-preguntas-5-6.png)

**Pregunta 7.** ¿Qué dificultades ha tenido con otras herramientas tecnológicas y qué necesitaría para usar esta plataforma sin problemas?

**Respuesta 7.** La principal dificultad que he tenido es que muchas herramientas son complejas y están pensadas para personas con más conocimientos tecnológicos. A veces requieren muchos pasos, funcionan mejor en computador que en celular o tienen demasiadas opciones que terminan confundiendo. Para usar esta plataforma sin problemas necesitaría una interfaz sencilla, que funcione muy bien desde el móvil, con procesos claros para crear actividades, aprobar voluntarios y emitir certificados. También me gustaría contar con ayuda rápida o tutoriales básicos y, sobre todo, tener la tranquilidad de que la información de nuestros voluntarios y beneficiarios está protegida con buenos controles de seguridad y privacidad.

**Pregunta 8.** Por último, si la plataforma le enviara avisos o notificaciones, ¿qué le gustaría recibir y qué debería revisar la universidad antes de que una fundación publique actividades?

**Respuesta 8.** Me gustaría recibir notificaciones cuando se inscriban nuevos voluntarios, cuando una actividad esté próxima a realizarse, cuando haya cambios o cancelaciones y cuando sea necesario aprobar horas o emitir certificados. Como trabajo mucho desde el celular, agradecería alertas simples y oportunas, sin exceso de mensajes. En cuanto a la universidad, creo que debería verificar que la fundación sea una organización legítima, que la actividad tenga un propósito social claro, que existan condiciones adecuadas de seguridad para los voluntarios y que se cumplan las normas de protección de datos, especialmente cuando se trabaja con niños y adultos mayores. También me daría tranquilidad que revisara quiénes son los responsables de la actividad antes de permitir su publicación.

![Preguntas 7 y 8](capturas/04-preguntas-7-8.png)

## Entregable 2: clasificación de los hallazgos

### Requisitos de Usuario

- RU-01. El coordinador de la ONG necesita publicar actividades con nombre, descripción, fecha, horario, lugar, número de voluntarios, requisitos especiales y responsable de contacto.
- RU-02. El estudiante quiere buscar actividades según su horario, la localidad y el tipo de causa.
- RU-03. El coordinador quiere registrar la asistencia y las horas desde el celular, y que un responsable de la fundación haga la validación final.
- RU-04. El estudiante quiere consultar en cualquier momento las horas de servicio que lleva acumuladas.
- RU-05. El estudiante quiere descargar su certificado sin esperar a que la fundación lo elabore a mano.
- RU-06. El coordinador quiere recibir avisos simples cuando se inscriban voluntarios, cuando se acerque una actividad, cuando haya cambios o cancelaciones y cuando deba aprobar horas o certificados.
- RU-07. La universidad quiere verificar la legitimidad de cada fundación, el propósito social de sus actividades, las condiciones de seguridad y los responsables antes de permitir la publicación.
- RU-08. El coordinador quiere contar con ayuda rápida o tutoriales básicos para aprender a usar la plataforma.

### Requisitos Funcionales

- RFE-01. El sistema debe permitir el registro y el inicio de sesión de los estudiantes con su correo institucional.
- RFE-02. El sistema debe permitir el registro de fundaciones y bloquear la publicación de eventos hasta que la universidad las valide.
- RFE-03. El sistema debe permitir al coordinador crear, editar y cancelar eventos con nombre, descripción, fecha, horario, lugar, cupos, requisitos especiales y responsable de la actividad.
- RFE-04. El sistema debe ofrecer búsqueda de eventos con filtros por fecha, franja horaria, localidad y causa.
- RFE-05. El sistema debe controlar los cupos al momento de la inscripción y mostrar el aviso de evento lleno cuando no haya disponibilidad.
- RFE-06. El sistema debe notificar al coordinador las nuevas inscripciones, los cambios y cancelaciones, las actividades próximas y las horas o certificados pendientes de aprobación.
- RFE-07. El sistema debe permitir registrar la asistencia y las horas de cada voluntario y exigir la aprobación de un responsable de la fundación antes de sumarlas al historial.
- RFE-08. El sistema debe mostrar al estudiante el historial de actividades y el total de horas acumuladas.
- RFE-09. El sistema debe generar certificados descargables en PDF con el nombre completo del voluntario, las actividades, el periodo, el total de horas, los datos de la fundación y una firma o validación digital verificable por la universidad.
- RFE-10. El sistema debe generar para cada fundación un reporte exportable de horas y voluntarios por periodo.
- RFE-11. El sistema debe gestionar los roles de estudiante, coordinador de ONG, personal autorizado de la fundación y administrador universitario con permisos diferenciados.
- RFE-12. El sistema debe permitir a la fundación registrar solo los datos mínimos de los beneficiarios (nombre, rango de edad, programa, necesidades relevantes para la atención y contacto del acudiente en el caso de niños) y ocultarlos a los voluntarios.
- RFE-13. El sistema debe ofrecer ayuda contextual y tutoriales breves para las tareas principales del coordinador.

### Restricciones (No Funcionales)

- RNFE-01. Privacidad: la plataforma debe aplicar la minimización de datos y almacenar de los beneficiarios solo lo necesario para coordinar la atención. La información de salud o de situación familiar se trata como dato sensible, con acceso restringido (Ley 1581 de 2012, arts. 5 y 6), y los datos de niños, niñas y adolescentes deben respetar su interés superior (art. 7). El tratamiento de los datos requiere autorización previa del titular (art. 9) y atiende los principios de seguridad y de acceso y circulación restringida (art. 4).
- RNFE-02. Seguridad: el acceso debe controlarse por niveles. Los voluntarios ven las actividades y sus propios datos, pero no los de otros voluntarios ni los de los beneficiarios; los coordinadores ven a los inscritos y los detalles operativos; los datos de beneficiarios solo los consulta el personal autorizado de la ONG. Las comunicaciones deben viajar cifradas.
- RNFE-03. Usabilidad: un coordinador sin capacitación previa debe poder publicar una actividad en no más de cinco pasos.
- RNFE-04. Accesibilidad y compatibilidad: la interfaz debe adaptarse a teléfonos móviles y cumplir el nivel AA de las pautas WCAG 2.1, con textos legibles y botones claros (World Wide Web Consortium [W3C], 2018).
- RNFE-05. Rendimiento: la búsqueda de eventos y la verificación de cupos deben responder en menos de dos segundos (Universidad Manuela Beltrán, 2026).
- RNFE-06. Integridad y trazabilidad: toda modificación de las horas registradas debe quedar en un historial con usuario, fecha y valor anterior, para respaldar la autenticidad de los certificados.

Estos hallazgos se formalizan como RF y RNF en el punto 1 de la Fase 1 (ver el README principal).
