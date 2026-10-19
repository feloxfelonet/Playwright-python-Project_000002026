@regression @checkout @checkout_success
Feature: Successful checkout

  Scenario: Complete checkout with valid details
    Given I log in as "standard_user" with password "secret_sauce"
    When I add "Sauce Labs Backpack" to the cart
    And I open the shopping cart
    And I start checkout
    And I enter checkout details "Alex", "Tester", "M1 1AA"
    And I continue checkout
    Then the checkout overview should be displayed
    When I finish checkout
    Then the order confirmation should be displayed
