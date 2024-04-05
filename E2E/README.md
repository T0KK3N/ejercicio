# DevSu - E2E Opción 2 - Daniel Mora

## Descripción Del Proyecto
Este proyecto provee una solución a la opción 2 de e2e. En este proyecto se usó Selenium para realizar una prueba automatizada (purchase_flow_test.py) a la página https://www.saucedemo.com  en el cual se realiza el siguiente flujo de compra:

1. Autenticarse con el usuario: standard_user y password: secret_sauce

2. Agregar dos productos al carrito

3. Visualizar el carrito

4. Completar el formulario de compra

5. Finalizar la compra hasta la confirmación: "THANK YOU FOR YOUR ORDER"

## Tecnologías Usadas
1. Python 3.12.2
2. Selenium 4.18.1
3. Chrome webdriver 122.0.6261.111
4. VsCode 1.87.0

## Pasos Para La Ejecucióm
1. Asegúrate de tener Python instalado en tu dispositivo. Para ello, puedes descargar Python desde aquí: https://www.python.org/. En mi caso, utilicé la versión 3.12.2. Una vez que hayas descargado el asistente de instalación, simplemente sigue los pasos del asistente. Te sugiero encarecidamente que marques la opción para agregar la ruta al entorno de variables de Windows. Para verificar si se instaló correctamente, simplemente abre una terminal y escribe: python --version o py --version. Mostrará la versión si la instalación se realizó correctamente.
2. Instalar Selenium escribiendo en la terminal: pip install selenium. En caso de que eso no funcione, prueba con: py -m pip install selenium.

3. Instalar el controlador de Chrome. En mi caso, utilicé la versión 122.0.6261.111 y lo descargué desde aquí: https://googlechromelabs.github.io/chrome-for-testing/. Asegúrate de que coincida la plataforma y la versión de tu controlador de Chrome; puedes verificarlo haciendo clic en los 3 puntos en la esquina superior derecha de tu navegador Chrome, luego en Ayuda - Acerca de Google Chrome. Te sugiero pegar el archivo dentro de C:\Program Files (x86).

4. En mi caso, utilicé VsCode como mi editor de texto para desarrollar mi script de Python. Si estás utilizando VsCode, te sugiero que agregues las extensiones Python(2024.2.1) y Code Runner(v0.12.1) en la pestaña de Extensiones (utilicé las últimas versiones para ambas).

5. Para correr el script, abre una terminal, ubícate en la ubicación del script y ejecuta el comando py purchase_flow_test.py o python purchase_flow_test.py. Con la ayuda de Code Runner también puedes dirigirte a la flecha de Play ubicada en la parte superior derecha, dar click en el drop down y darle a la opción "Run Python File".

## Información de Contacto
Si tienen alguna pregunta, no duden en contactarme a danielmora414@gmail.com