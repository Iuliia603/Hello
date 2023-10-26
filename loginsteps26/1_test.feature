@negative @major
  Scenario: Login without entering a Email and Password

    Given user is not logged in
    When user clicks Login button
    Then warning shown about 'No match for E-Mail Address and/or Password'
