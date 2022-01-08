from behave import step


@step('I verify that the search results is accurate')
def verify_search_results(context):
    context.search_results_page.assert_results_list(context.brand, context.product)
