# Proyecto-Optimizacion-INF-292

Ambiente de desarollo:
  - Sistema operativo: Windows 11 Pro
  - Editor de texto: Vscode
  - Version Python = 3.12.0

Consideraciones antes de ejecutar:
  - Tener instalado python
  - Tener instalado el modulo numpy
  - El programa no debería pedir ninguna instalación de paquetes adicionales.
  - El programa hace uso de la libreria threading en la opción 4, ejecutando 3 hilos. Por esta razón al ejecutar la opción 4 es posible que los resultados de consola no se muestren en el mismo orden. 
  - Se fijo una seed para numpy y random, así se obtienen los mismos datos siempre al ejecutar, manteniendo la aleatoriedad del proyecto, solo hay que cambiar la seed y todo cambiará.

Comandos de Ejecución:
  - python main.py

Consideraciones del desarrollo del código:
  - Los valores son mostrados por consola, inicialmente consideré guardalos en un txt pero aún no definimos que formato usaremos para que luego el LPSolve pueda leerlo, así que por ahora solo se muestra por consola los valores generados.

Como usar el programa:
  - Por ahora el programa da a elegir 4 opciones, la opcion 1 permite crear 5 instancias pequeñas, ya definidas en instancias_p.txt, y así con las siguientes 2 opciones, con mediana y grande respectivamente. La ultima opcion crea las 15 instancias solicitadas en el pdf del proyecto.
