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
```

En macOS o Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar las dependencias

Ejecutar:

```bash
pip install -r requirements.txt
```

## Ejecución

Para iniciar el programa ejecutar:

```bash
python main.py
```

El sistema solicitará dos rutas de imágenes:

1. La fotografía de la persona registrada.
2. La fotografía de la persona que intenta iniciar sesión.

Ejemplo:

```text
Escribe la ruta de la foto registrada: foto_registro.jpg
Escribe la ruta de la foto para iniciar sesión: foto_intento.jpg
```

Si los rostros coinciden, el sistema mostrará:

```text
✅ ACCESO PERMITIDO
El rostro coincide con la persona registrada.
```

Si los rostros pertenecen a personas diferentes, mostrará:

```text
❌ ACCESO DENEGADO
El rostro NO coincide con la persona registrada.
```

## Funcionamiento

El programa utiliza la función `DeepFace.verify()` para comparar las características faciales presentes en las dos fotografías.

Para detectar los rostros se utiliza MTCNN.

DeepFace emplea modelos de redes neuronales previamente entrenados para generar representaciones numéricas de los rostros y determinar si existe suficiente similitud entre ellos para considerarlos pertenecientes a la misma persona.

## Recomendaciones

Se recomienda utilizar fotografías:

- Con buena iluminación.
- Donde el rostro sea claramente visible.
- Preferentemente de frente.
- Sin objetos que cubran gran parte del rostro.

## Nota

La primera ejecución puede tardar algunos minutos debido a que DeepFace puede descargar los modelos de redes neuronales necesarios para realizar la verificación facial.

## Objetivo académico

El objetivo de este proyecto es aplicar técnicas de visión por computadora utilizando modelos de redes neuronales previamente entrenados para desarrollar una aplicación funcional de verificación facial.
