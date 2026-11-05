#!/usr/bin/env bash
# Genera los PNG de todos los diagramas a partir de su código fuente.
# Requisitos: Graphviz (dot) y PlantUML (plantuml.jar o comando plantuml) con Java.
set -euo pipefail
cd "$(dirname "$0")/.."
PLANTUML="${PLANTUML:-plantuml}"

for f in fase-1-descubrimiento/arbol-descomposicion/arbol.dot \
         fase-2-arquitectura/c4/c4-contexto.dot \
         fase-2-arquitectura/c4/c4-contenedores.dot \
         fase-4-diseno-detallado/c4-componentes/c4-componentes.dot; do
  dot -Tpng -Gdpi=200 "$f" -o "${f%.dot}.png"
  echo "Generado ${f%.dot}.png"
done

for f in fase-1-descubrimiento/casos-de-uso/casos-de-uso.puml \
         fase-2-arquitectura/despliegue/despliegue.puml \
         fase-2-arquitectura/prototipo/flujo-prototipo.puml \
         fase-4-diseno-detallado/entidad-relacion/entidad-relacion.puml \
         fase-4-diseno-detallado/clases/clases_inscripciones.puml \
         fase-4-diseno-detallado/clases/clases_horas.puml \
         fase-4-diseno-detallado/secuencia/sec_inscripcion.puml \
         fase-4-diseno-detallado/secuencia/sec_certificado.puml \
         taller-fase-3-event-storming/actividad.puml; do
  $PLANTUML -tpng "$f"
  echo "Generado ${f%.puml}.png"
done
