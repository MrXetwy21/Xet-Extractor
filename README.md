# Xet-Extractor

Xet-Extractor es una librería de Python diseñada para extraer texto que se encuentra entre dos delimitadores específicos dentro de una cadena de texto. Es útil para tareas de procesamiento de texto y análisis de datos.

## Instalación

Puedes instalar la librería directamente desde PyPI utilizando pip:

```bash
pip install Xet-Extractor
```

También puedes instalarla desde el repositorio clonándolo y utilizando `setup.py`:

```bash
python setup.py install
```

## Uso

Importa la función `Ext` desde el módulo `Xetractor` y úsala para extraer texto entre delimitadores:

```python
from Xetractor import Ext

# Ejemplo de uso
data = "Hola [mundo]!"
resultado = Ext(data, "[", "]")
print(resultado)  # Salida: mundo
```

### Parámetros de la función `Ext`
- `data` (str): La cadena de texto de entrada.
- `first` (str): El delimitador inicial.
- `last` (str): El delimitador final.

### Retorno
- Devuelve el texto que se encuentra entre los delimitadores especificados.
- Si no se encuentran los delimitadores, devuelve `None`.

## Autor

Creado por [MrXetwy21](https://github.com/MrXetwy21).

## Licencia

Este proyecto está licenciado bajo los términos de la licencia MIT.