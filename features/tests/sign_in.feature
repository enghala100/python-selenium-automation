Feature: sign in feature
  Scenario: User can see sign in form page
    Given Open target page
    When click on sign in button
    Then verify sign in form opened


  Scenario: User can open and close Terms and Conditions from sign in page
   Given Open sign in page
   And Store original window
   When Click on Target terms and conditions link
   And Switch to new window
   Then Verify Terms and Conditions page is opened
   And Return to original window