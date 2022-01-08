from behave import step

from ui.page_objects.home import HomePage
from ui.page_objects.search_results import SearchResultsPage


@step('I go to the fravega home page')
def go_to_home(context):
    context.home_page = HomePage(context.driver)
    context.home_page.go()


@step('I search for "{product}"')
def search_product(context, product):
    context.home_page.search_product(product)
    context.search_results_page = SearchResultsPage(context.driver)
    context.product = product


@step('I filter by the first brand')
def filter_by_brand(context):
    context.brand = context.search_results_page.filter_by_brand()
