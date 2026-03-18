Smart Transaction Risk Detector

Problem Understanding

This program analyzes daily transaction amounts to check whether spending behavior is normal or suspicious.
Each transaction is categorized based on its value.
Finally, it determines an overall risk level such as Low Risk, Moderate Risk, or High Risk.

Logic / Approach Used

I used a loop to take inputs and classify each transaction using conditions.
A dictionary is used to store categorized transactions.
Then I calculated total value and checked patterns to decide the final risk.

Personalization Applied

I took inputs one by one using a loop instead of using split().
I ignored invalid transactions while calculating total value.
I also prioritized High Risk if multiple high-risk transactions are present.

Example

Name of the user = Ramcharan
Transactions entered = 200, 1500, 3000, -50, 700

The program classifies transactions and checks patterns to decide the final risk level.

Test Cases

Test Case 1:
Transactions: 100, 200, 300
Output: Low Risk

Test Case 2:
Transactions: 2500, 3000, 4000, 1500, 800, 900
Output: High Risk

Learning Outcome

I learned how to use loops, conditions, and lists to solve problems.
I understood how dictionaries and tuples help in organizing data.
I also learned how to detect patterns and make logical decisions.
