@smoke @products @products_display
Feature: Product listing

  Scenario: Products are displayed after login
    Given I log in as "standard_user" with password "secret_sauce"
    Then I should see at least one product
