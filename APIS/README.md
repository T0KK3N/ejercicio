# DevSu - APIS Opción 3 - Daniel Mora

## Descripción Del Proyecto
Este proyecto provee una solución a la opción 3 de APIS. En este proyecto se usó Cypress.io para realizar pruebas de servicios REST a la página https://petstore.swagger.io/ en el cual se identifica las entradas y captura las salidas para cada uno de los siguientes casos:

1. Crear un usuario (APIS/cypress/e2e/createUserTest.cy.js)

2. Buscar el usuario creado (APIS/cypress/e2e/findUserTest.cy.js)

3. Actualizar el nombre y el correo del usuario (APIS/cypress/e2e/updateUserTest.cy.js)

4. Buscar el usuario actualizado (APIS/cypress/e2e/findUserTest.cy.js)

5. Eliminar el usuario (APIS/cypress/e2e/deleteUserTest.cy.js)

## Tecnologías Usadas
1. Node v20.12.1
2. Cypress 13.7.2
3. VsCode 1.87.0

## Pasos Para La Ejecucióm
1. Instalar Node.js a través de esta página: https://nodejs.org/en. En ella encontrarás la opción de download Node.js(LTS). Seguir los pasos que recomienda el instalador. Para comprobar si se instaló de manera correcta puedes correr el comando node -v dentro de un cmd.
2. En mi caso estoy usando VsCode como mi editor de texto. Abrir la carpeta del proyecto, abrir una terminal y correr el comando npm install.
3. Una vez instaladas las dependencias, en la terminal correr npx cypress open para abrir Cypress, elegir E2E Testing y elegir su browser de preferencia  (en mi caso elegí Chrome). 
4. Dentro de Cypress, en la tab de Specs, abrir cypress\e2e y ahí se encontraran los 5 archivos (createUserTest.cy.js, findUserTest.cy.js, updateUserTest.cy.js, findUserTest.cy.js, deleteUserTest.cy.js). Para probarlos, dar doble click sobre el nombre del archivo, es importante hacerlo en el orden mostrado.

## Información de Contacto
Si tienen alguna pregunta, no duden en contactarme a danielmora414@gmail.com


