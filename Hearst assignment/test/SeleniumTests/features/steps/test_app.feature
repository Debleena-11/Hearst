# Author: Debleena Jana
# Rev: 1.0
# Creation date: 09/04/2023
# This feature file supports and provides step definations for testing the frontend UI 
Feature: Testing number operations on a web page

  Scenario Outline: Selecting numbers and getting results from endpoints
    Given I open the application
    When I select number "<number>"
    And I click the "Send to Endpoint 1" button
    Then I expect to see the result as "<result_endpoint_1>"

    When I click the "Send to Endpoint 2" button
    Then I expect to see <condition> result

    Examples:
      | number | result_endpoint_1 | condition  |
      | 2      | 4                | no         |
      | 4      | 16               | no         |
	  | 6      | 36               | no         |
	  | 8      | 64               | no         |
	  
  Scenario Outline: Selecting numbers and getting results from endpoints
    Given I open the application
    When I select number "<number>"
    And I click the "Send to Endpoint 1" button
    Then I expect to see the result as "<result_endpoint_1>"

    When I click the "Send to Endpoint 2" button
    Then I expect to see <condition> result as "<result_endpoint_2>"

    Examples:
      | number | result_endpoint_1 | condition  | result_endpoint_2 |
      | 1      | 1                | a          | 0.5               |
      | 3      | 9                | a          | 1.5               |
      | 5      | 25               | a          | 2.5               |
	  | 7      | 49               | a          | 3.5               |
	  | 9      | 81               | a          | 4.5              |
	 

	  