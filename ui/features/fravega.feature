Feature: Fravega

  Scenario: Heladeras test
      Given I go to the fravega home page
      When I search for "heladeras"
      And I filter by the first brand
      Then I verify that the search results is accurate