Feature: Búsqueda de películas en IMDb
  Scenario: Buscar una película y validar su calificación
    Given El usuario se encuentra en la página principal de IMDb
    When El usuario busca la película "Pulp fiction"
    And El usuario abre el primer resultado
    Then Se muestra la página de la película "Pulp Fiction"
    And Se muestra la calificación de la película
