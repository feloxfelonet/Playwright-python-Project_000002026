@regression @checkout @negative @checkout_validation
Feature: Checkout validation

  Scenario: Checkout requires customer information
    Given I log in as "standard_user" with password "secret_sauce"
    When I add "Sauce Labs Backpack" to the cart
    And I open the shopping cart
    And I start checkout
    When I continue checkout
    Then the checkout information error should be visible
