from behave import given, when, then, step


@given('Open Amazon page')
def open_amazon(context):
    context.app.main_page.open_main_page()


@when('Search for {any_word}')
def search_amazon(context, any_word):
    context.app.header.search_amazon(any_word)


@then('Verify search results for {search_result} are shown')
def verify_search_results(context, search_result):
    context.app.search_result_page.verify_search_results(search_result)


