
Feature: Amazon Sign In tests

  @smoke
  Scenario: Sign In page can be opened from SignIn popup
    Given Open Amazon page
    When Click on button from SignIn popup
    Then Verify Sign In page is opened


  Scenario: SignIn popup is visible for a few seconds in the main page
    Given Open Amazon page
    Then SignIn popup is present
    When Wait for 4 seconds
    Then SignIn popup is present
    Then SignIn popup disappears


  @smoke
  Scenario: Logged out user sees Sign in page when clicking Orders
    Given Open Amazon page
    When Click Amazon Orders link
    Then Verify Sign In page is opened