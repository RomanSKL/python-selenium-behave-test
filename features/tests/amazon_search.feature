
Feature: Amazon search


  Scenario Outline: Verify that user can search for products
    Given Open Amazon page
    When Search for <any_word>
    Then Verify search results for <search_result> are shown
    Examples:
    |any_word     |search_result  |
    |table        |"table"        |
    |dress        |"dress"        |
    |spoons       |"spoons"       |


