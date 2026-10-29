Feature: Ingreso a la lobby
  Scenario: Ingresar con un nombre único a la lobby
    Given El usuario se encuentra en la página de login
    When El usuario ingresa con el nombre "Daiza"
    Then El nombre del usuario "Daiza" aparece en el dashboard

  Scenario: Ingresar con un nombre de usuario que contiene espacios
    Given El usuario se encuentra en la página de login
    When El usuario ingresa con el nombre "Daiza Zambrano"
    Then Se muestra un mensaje de error en el nombre de usuario
