
Feature: Test for Amazon search



  @smoke
  Scenario: Verify that user can search for coffee
    Given Open Amazon page
    When Search for coffee
    Then Verify search results for coffee are shown


  Scenario: Verify that your Amazon Cart is empty
    Given Open Amazon page
    When Click cart icon
    Then Verify that1 Your Amazon Cart is empty


  Scenario: User can add a product to the card
    Given Open Amazon page
    When Search for Tritan Farm to Table Pitcher
    And Click on the first product
    And Click on Add to cart button
    And Open cart page
    Then Verify cart has 1 item(s)



  Scenario Outline: Verify that user can search for products
    Given Open Amazon page
    When Search for <any_word>
    Then Verify search results for <search_result> are shown
    Examples:
    |any_word     |search_result  |
    |table        |"table"        |
    |dress        |"dress"        |
    |spoons       |"spoons"       |


  Scenario: User sees ham menu btn on the main page
    Given Open Amazon page
    Then Verify hamburger menu btn present


  Scenario: User sees correct amount of footer links
    Given Open Amazon page
    Then Verify there are 38 footer links

# HW4!


  Scenario: User is able to add a product to the card
    Given Open Amazon page
    When Search for Table tennis rubbers
    And Click on the first product
    # And Store product name
    And Click on Add to cart button
    And Open cart page
    Then Verify cart has 1 item(s)
    # And Verify cart has correct product


  Scenario: Find some things you can do here links
    Given Open Customer Service page
    Then Confirm 9 Some things you can do here links
    

  Scenario: Verify that user can see product names and images
    Given Open Amazon page
    When Search for coffee
    Then Verify that every product has a name and an image


  Scenario: User can see language options
    Given Open Amazon page
    When Hover over language options
    Then Verify Spanish option present


  Scenario: User can select and search in a department
    Given Open Amazon page
    When Select department by audible
    And Search for Faust
    Then Verify audible department is selected

    # ^^^^
  Scenario Outline: User can select and search in a department
    Given Open Amazon page
    When Select department by <alias>
    And Search for <search_query>
    Then Verify <selected_dept> department is selected
    Examples:
    |alias        |search_query    |selected_dept      |
    |stripbooks   |Faust           |books              |
    |audible      |Alice in        |audible            |

