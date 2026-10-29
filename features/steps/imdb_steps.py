from behave import given, when, then
from selenium import webdriver
from pages.imdb_page import ImdbPage

@given('El usuario se encuentra en la página principal de IMDb')
def step_given_user_on_imdb_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.imdb.com/")
    context.imdb_page = ImdbPage(context.driver)

@when('El usuario busca la película "{movie_name}"')
def step_when_user_searches_movie(context, movie_name):
    context.imdb_page.search(movie_name)

@when('El usuario abre el primer resultado')
def step_when_user_opens_first_result(context):
    context.imdb_page.open_first_result()

@then('Se muestra la página de la película "{movie_title}"')
def step_then_movie_page(context, movie_title):
    assert context.imdb_page.get_movie_title().casefold() == movie_title.casefold()

@then('Se muestra la calificación de la película')
def step_then_rating(context):
    rating = context.imdb_page.get_rating()
    assert 0 < rating <= 10
