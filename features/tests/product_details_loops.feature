# Created by skliarovrn at 5/17/22

Feature: Tests for product page

  Scenario: User can select colors
    Given Open Amazon product B07MNHBRCJ page
    Then Verify user can click through colors


  Scenario: Able to select different color of jeans
    Given Open Jeans B07BJKRR25 page
    Then Verify ability to select colors


  Scenario: Able to select sweaters
    Given Open sweater page
    Then Verify user able to select colors