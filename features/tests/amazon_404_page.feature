Feature: Test for 404 page


  Scenario: User is able to navigate to new window and back
    Given Open Amazon product B07NF5WRTYI877665410 page
    And Store original window
    When Click on a dog image
    And Switch to new window
    Then Verify blog is opened
    And Close blog
    And Return to original window



