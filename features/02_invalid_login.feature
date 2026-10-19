@regression @login @negative @invalid_login
Feature: Invalid login

  Scenario: Invalid credentials are rejected
    Given I open the SauceDemo website
    When I enter username "invalid_user" and password "wrong_password"
    And I click the login button
    Then I should see a login error containing "Username and password do not match"
