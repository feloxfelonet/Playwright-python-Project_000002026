@regression @login @negative @locked_user
Feature: Locked out user

  Scenario: Locked out user cannot log in
    Given I open the SauceDemo website
    When I enter username "locked_out_user" and password "secret_sauce"
    And I click the login button
    Then I should see a login error containing "locked out"
