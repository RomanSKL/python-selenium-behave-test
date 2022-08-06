Feature: Tests for bestsellers functionality

  Scenario: User able to find all top links
    Given Open Best Sellers
    Then Confirm 5 best sellers links


  Scenario: Bestsellers links can be open
    Given Open Best Sellers
    Then User can click through top links and verify correct page opens