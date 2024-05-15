# bank_management_oop

## Code characteristics

- Object Oriented Approach
- Code Modularity
- Readability
- Exception handling
- Graphical User Interface

## Functionalities

## User Functionalities:

### Create an Account:

- Users can register with their name, email, address, and account type (Savings or Current).
  Initial balance starts at 0.
- Account numbers are automatically generated for security and uniqueness.

### Deposit and Withdraw Funds :

- Users can deposit any amount.
- Withdrawals are permitted only if sufficient funds exist.
- A clear error message is displayed for insufficient balance ("Withdrawal amount exceeded").

### Check Account Balance:

- Users can view their current account balance at any time.

### Transaction History:

- Users can access a record of their deposit and withdrawal transactions.

### Loan Management:

- Users can apply for loans up to two times.
- Loan features and limitations might be further defined based on your project requirements.

### Transfer Funds:

- Users can transfer money to other accounts within the system.
- Error handling ensures an informative message ("Account does not exist") if the recipient's account is not found.
- Security measures (password verification) could be implemented for transfers.

## Admin Functionalities:

### Create Accounts:

- Admins can create user account (useful for initial setup).

### Delete User Accounts:

- Admins can delete user accounts (consider security measures and confirmation prompts for future implementation).

### View All Accounts:

- Admins can access a comprehensive list of all user accounts and their details.

### Check Bank Balance:

- Admins can view the total available balance of the bank, providing oversight into overall finances.

### Check Loan Totals :

- Admins can track the total loan amount issued by the bank, assisting in risk analysis and loan management.

### Loan Feature Control:

- Admins can temporarily disable or enable the loan feature to maintain financial stability or adhere to regulatory requirements.
