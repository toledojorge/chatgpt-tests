Para agregar una funcionalidad "Hello World" a tu extensión de Chrome, puedes seguir estos pasos:

Crea una carpeta para tu extensión y crea un archivo HTML dentro de la carpeta llamado "hello.html". Este archivo contiene el código HTML que se mostrará cuando se active la extensión.
Copy code
<html>
  <head>
    <title>Hello World Extension</title>
  </head>
  <body>
    <h1>Hello World!</h1>
    <p>This is my first Chrome extension.</p>
  </body>
</html>
Crea otro archivo en la carpeta llamado "manifest.json". Este archivo contiene la información sobre tu extensión, incluyendo el nombre, la descripción y el archivo HTML que se mostrará cuando se active la extensión.
Copy code
{
  "manifest_version": 2,
  "name": "Hello World Extension",
  "description": "This is my first Chrome extension.",
  "version": "1.0",
  "browser_action": {
    "default_popup": "hello.html"
  }
}
Abre Google Chrome y dirígete a la página de extensiones haciendo clic en el menú de Chrome en la esquina superior derecha y seleccionando "Más herramientas" > "Extensiones".
En la página de extensiones, activa el modo de desarrollador haciendo clic en el botón "Modo de desarrollador" en la esquina superior derecha.
Haz clic en el botón "Cargar sin empaquetar" y selecciona la carpeta que contiene tu extensión.
Una vez cargada, tu extensión aparecerá en la lista de extensiones de Chrome y estará disponible para usarse. Cuando hagas clic en el ícono de la extensión en la barra de herramientas de Chrome, se mostrará el mensaje "Hello World!" en una ventana emergente.
Espero que esto te ayude. Si tienes alguna pregunta adicional, no dudes en hacérmelo saber. ¡Buena suerte con tu extensión!