
# PROYECTO PREENTREGA TALENTO TECH: Automatización de Pruebas en SauceDemo

Este proyecto tiene como objetivo demostrar la aplicación de **automatización y testing** de casos de prueba para la plataforma de demostración **SauceDemo**. Se utiliza un conjunto de tecnologías de testing automation líderes en la industria para validar las funcionalidades clave del sitio.

-----

## 🛠️ Tecnologías Aplicadas

Las siguientes herramientas y *frameworks* han sido empleados en el desarrollo de este proyecto:

  * **Python:** Lenguaje de programación principal para la lógica de los tests.
  * **Selenium WebDriver:** Herramienta para la interacción directa con el navegador y la automatización de acciones web.
  * **Pytest:** *Framework* de testing que facilita la escritura, organización y ejecución de los tests.
  * **`pytest-html`:** *Plugin* que permite generar informes de resultados detallados en formato HTML.

-----

## 📋 Casos de Prueba Automatizados

Los tests se centran en verificar los flujos de usuario más críticos dentro de la aplicación SauceDemo:

| Caso de Prueba | Descripción | Estado Esperado |
| :--- | :--- | :--- | 
| **Login Exitoso** | Verifica que un usuario con credenciales válidas pueda acceder correctamente al *dashboard*. | Acceso a la página de productos. 
| **Navegacion** | Verifica que todos los elementos de la pagina se encuentren presentes en la seccion de productos. | Los elementos como menu, boton de filtro, y productos deben mostrarse correctamente en la pagina. |
| **Agregar un producto al carrito** | Valida el proceso de agregar un artículo desde la lista de productos al carrito de compras. | El carrito debe mostrar el ítem agregado. Luego debe validar que el producto se encuentra en el carrito de compras | 


-----

## 📂 Estructura del Proyecto

La organización del proyecto sigue una estructura modular para facilitar la gestión y el mantenimiento de los tests:

```markdown
pre-entrega-automation-testing-brian-buera/
├── report/
│     └── reporte.html      # Informe de resultados generado por pytest-html
├── tests/
│     └── __init__.py
│     └── test_pagina.py    # Contiene los casos de prueba automatizados
├── utils/
│     └── __init__.py
│     └── funciones.py      # Funciones de ayuda
├── requirements.txt        # Lista de dependencias del proyecto
└── README.md
```

-----

## ⚙️ Instalación

1.  **Clonar el Repositorio:**
    Clona este repositorio usando `git` y navega hasta el directorio del proyecto:

    ```bash
    git clone https://github.com/usuario/proyecto.git
    cd proyecto
    ```

2.  **Instalar Dependencias:**
    Se recomienda usar un entorno virtual. Instala todas las librerías necesarias especificadas en el archivo `requirements.txt`:

    ```bash
    # (Opcional) Crear y activar un entorno virtual
    # python -m venv venv
    # source venv/bin/activate   # En Linux/macOS
    # .\venv\Scripts\activate    # En Windows

    pip install -r requirements.txt
    ```

-----

## 🚀 Uso (Ejecución de Tests)

Para ejecutar los tests automatizados y generar el informe de resultados, utiliza el siguiente comando con **Pytest**:

### 1\. Ejecutar todos los tests

Ejecuta todos los tests:

```bash
pytest -m test
```

Ejecuta prueba de login:

```bash
pytest -v -m login
```

Ejecuta prueba de navegacion:

```bash
pytest -v -m navegacion
```

Ejecuta prueba de compra:

```bash
pytest -v -m compra
```

### 2\. Ejecutar y generar informe HTML

Para ejecutar los tests y, además, generar el informe de resultados en la ruta especificada (`report/reporte.html`), utiliza el *flag* `--html`:

```bash
pytest --html=report/reporte.html
```


