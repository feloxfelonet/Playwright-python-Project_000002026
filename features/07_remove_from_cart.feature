@regression @cart @remove_from_cart
Feature: Remove product from cart

  Scenario: Remove a backpack from the cart
    Given I log in as "standard_user" with password "secret_sauce"
    When I add "Sauce Labs Backpack" to the cart
    And I remove "Sauce Labs Backpack" from the cart
    Then the cart badge should show 0 items
