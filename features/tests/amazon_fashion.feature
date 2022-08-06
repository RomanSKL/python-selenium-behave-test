Feature: Test cases on Amazon Fashion

  Scenario: User is able to select New Arrivals
    Given Open Amazon Fashion page
    When Hover over New Arrivals
    Then Verify images

  Scenario: User is able to select and search in a department
    Given Open Amazon Fashion page
    When Select Video Games department
    And Search for doom
    Then Verify user is on Video Games department