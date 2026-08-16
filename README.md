
# Sistema de inicio de sesión con verificación facial

## Descripción

Este proyecto implementa un sistema sencillo de inicio de sesión mediante verificación facial utilizando Python y la librería DeepFace.

El sistema compara la fotografía de una persona registrada con una segunda fotografía correspondiente a un intento de inicio de sesión.

Si DeepFace determina que ambos rostros pertenecen a la misma persona, el sistema permite el acceso. En caso contrario, el acceso es denegado.

## Funcionalidades

- Verificación facial mediante DeepFace.
- Detección de rostros utilizando MTCNN.
- Comparación de dos fotografías.
- Acceso permitido cuando los rostros coinciden.
- Acceso denegado cuando los rostros son diferentes.
- Manejo básico de errores.

## Tecnologías utilizadas

- Python
- DeepFace
- MTCNN
- Redes neuronales preentrenadas

## Instalación

### 1. Clonar o descargar el repositorio

Descargar los archivos del proyecto desde GitHub.

### 2. Crear un entorno virtual

En Windows:

```bash
python -m venv venv
venv\Scripts\activate
