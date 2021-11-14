### Test Navbar and sorting
- Outline of Testing Nav Bar
    -  Goal is to check all links are working, search field validation, and functionality
-  Test planning
    -  On the deployed site in desktop and mobile screen, check if the logo link is working and renders All Bouquets page
    -  On the deployed site in desktop and mobile screen, click through all buttons and make sure each relevant page renders correctly
    -  On the deployed site in desktop and mobile screen, make sure search field validation and functionality works

| Nav Bar |  Page Rendered | Error | 
| ------ | ------ |  ------ |
| Main logo link (All Bouquets page) | x | |
| Shop All button (All Bouquets page) | x | |
| Chocolate button (All Chocolate Bouquets page) | x | |
| Meat & Cheese button (All Meat & Cheese page) | x | |
| Veggies button (All Veggies page) | x | |
| Fruits button (All Fruits page) | x | |
| Contact Us button (Contact Us page) | x | |
| My Account / Register button (Register page) | x | |
| My Account / Login button (Login page) | x | |
| My Account / Logout button (Logout page) | x | |
| My Account / Product Managment button (Product Managment page) | x | |
| My Account / My Profile button ( My Profile page) | x | 
| Bag icon (Bag page) | x | |

- Search field data (product title/description)

| Search field |  OK | Error | 
| ------ | ------ |  ------ |
| Empty request (Error notification) | x | |
| Exisiting word in title request | x | |
| Exisiting word in descripti request | x | |
| Word none from title/description (return none) | x | |

- Sorting products - sort by

| Sorting |  OK | Error | 
| ------ | ------ |  ------ |
| Price (low to high)| x | |
| Price (high to low)| x | |
| Rating (low to high)| x | |
| Rating (high to low)| x | |
| Name (A-Z)| x | |
| Name (Z-A)| x | |
| Category (A-Z)| x | |
| Category (Z-A)| x | |

- Product cards - link to the product details page

| Product card |  Product Details page | Error | 
| ------ | ------ |  ------ |
| 'BABY GIRL' CHOCOLATE STRAWBERRY BOUQUET| x | |
| ALLURE CHOCOLATE STRAWBERRY BOUQUET - MILK| x | |
| MEAT & CHEESE BEER BOUQUET| x | |
| 'FRESH STRAWBERRY' FRUIT - ROSES GIFT BASKET| x | |
| RUSTIC BARN VEGGIES BOUQUET| x | |

- Outcomes
  - All button and card links are working.
  - Search field validation and functionality are working.
  - Sorting works

### Product details page
- Outline of Testing Nav Bar
    -  Goal is to check all links, buttons and front end functionality is working
-  Test planning
    -  On the deployed site in desktop and mobile screen, if sidebar (Similar:) with products displayed, hovered product image becomes large and link to selected product is working.
    -  On the deployed site in desktop and mobile screen, check if size selection affects product price (front end).
    -  On the deployed site in desktop and mobile screen, check if the quantity can be adjusted

-   Buttons

| Button |  Ok | Error | 
| ------ | ------ |  ------ |
| Keep Shopping (All Bouquets) | x | |
| Add to Bag (add to bag) | x | | 
| Add to Bag (user notification) | x | | 


-   Left side column (Similar) display:

| Left side column |  Ok | Error | 
| ------ | ------ |  ------ |
| Displayed on LG screen | x | |
| Hidden on MD screen |  | x [Fixed]| 
| Hidden on SM screen | x | |

- Left side column (Similar) links and hover effect:

| Left side column |  Ok | Error | 
| ------ | ------ |  ------ |
| Hover effect | x | |
| Links to product detail working | x | | 

-   Change size functionality

| Size |  Ok | Error | 
| ------ | ------ |  ------ |
| SMALL (add 0 EU to price)| x | |
| MEDIUM (add 12 EU to price)| x | |
| LARGE (add 20 EU to price)| x | |

-   Adjust quantity

| Quantity |  Ok | Error | 
| ------ | ------ |  ------ |
| Plus| x | |
| Minus| x | |
| Zerro (can't sellect)| x | |
| More than 99 (can't sellect)| x | |

- Fix
    -  Side column is not hidden on MD screens.
- Outcomes
    - Error fixed. The side column now is displayed only on LG screen.

### Test Shopping Bag page
- Outline of Testing Sign Un Form
    -  Goal is to check that all links are working, adjust the quantity and remove buttons are working
-  Test planning
    - On the deployed site navigate to the Shopping Bag page
    - Try to add/decrease quantity of the product 
    - Try to add/decrease quantity of the product 
    - Check if Shopping / Checkout buttons work correctly
    - Check if Bag Total, Delivery, Grand Total, Free delivery data is correct

| Product Qty manipulation|  Ok | Error |User Notification|
| ------ | ------ |  ------ | ------ |
| Change qty from 1 to 9| x |  |Success|
| Change qty from 9 to 5| x |  |Success|
| Change qty from 5 to 35| x |  |Success|
| Change qty from 35 to 7| x |  |Success|
| Remove product from bag| x |  |Success|

| Product Qty| Price| Subtotal| Bag Total | Delivery |Grand Total|Free Delivery Delta |Result|
| ------ | ------ |  ------ | ------ |------ |------ |------ |------ |
| 1 | 55.00 | 55.00 |55.00| 0.00 | 55.00 | 0.00 | Correct |
| 6 | 55.00 |330.00 |330.00  | 0.00 | 330.00 | 0.00 | Correct |
| 1 | 37.30 | 37.30 | 37.30 | 5.00 | 42.30 | 12.70 |Correct |
| 1 | 48.30 | 48.30 | 48.30 | 5.00 | 53.30 | 1.70 |Success|

-   Outcomes
    - Product quantity manipulation functionality works.
    - Shopping bag data calculation works correctly.
    - Shopping, Checkout buttons redirect user to relevant pages




### Test Contact Us Form
- Outline of Testing Contact Us Form
    -  Goal is to check Contact Us form validation, user notifications, confirmation emails
 -  Test planning
    - On the deployed site navigate to the Contact Us page
    - Send a message using the Contact Us form
    - Check if invalid entries give the user feedback 
    - Check if the user redirected to the success page
    - Check if a confirmation email received 

| Form field validation|  Ok | Error | Message|
| ------ | ------ |  ------ | ------ |
| Your name (empty)|  | x |Name cannot be empty|
| Your name (TestName)| x |  |
| Your email (empty)|  | x |Email cannot be empty|
| Your email (testgmail.com)|  | x |Email format invalid|
| Your email (email) | x |  | |
|  Subject (empty) |  | x | Subject cannot be empty |
| Subject (subject)| x | ||
| Your message (empty)|  |x |Message cannot be empty|
| Your message (message)| x | ||

- Implementation
  - Form filed out and Send button pressed:
  - Message sent page not renders
  - User message sent/received by the owner
  - Confirmation email with a copy of user original message - sent and received by user

-   Fix
    - Message Sent page not renders.
-   Outcomes
    - Contact Us Validation and user notification works.

### Test Sign Up Form
- Outline of Testing Sign Un Form
    -  Goal is to check the registration form, user notification messages, and confirmation emails
 -  Test planning
    - On the deployed site navigate to the Register page
    - Register using the registration form
    - Check the registration form if invalid entries give the user feedback 
    - Check successful registration reveals toast message and sends an automatic email to new user
    - Confirm that automatic email link allows user to complete registration and Sign In 

| Sign Up Form |  OK |Error| 
| ------ | ------ |  ------ |
| Navigate to the Register page | x | |
| All fields are required | x | |
| Incorrect email input (example: testgmail.com) |  | x |
| Incorrect email confirmation input (example: test@gmail.com, test1@gmail.com)|  | x |
| Correct email input (example: test@gmail.com) | x  |  |
| Incorrect pasword input |  | x |
| Correct pasword input | x |  |
| Verification email sent (nitification) | x |  |
| Verification email received | x |  |
| Verification email link works | x |  |
| Email confirmation works | x |  |
| Sign In works as new user | x |  |

- Fix
    -  Form header and button text from Sign Up to Register for consistent user experience.
    -  Confirmation email - change domain name/display name in admin panel

- Outcomes
    - Sign Up form: validation, user notifications, and email confirmation functionality work as expected.


### Test Sign in Form
- Outline of Testing Sign In Form
    -  Goal is to check Sign In form and user notification messages
- Test planning
    - On the deployed site navigate to the login page
    - Check login form if invalid entries give the user feedback 
    - Login with existing user

| Sign In Form |  OK |Error| 
| ------ | ------ |  ------ |
| Navigate to the Login page | x | |
| All fields are required | x | |
| Incorrect username and password input |  | x |
| Incorrect username input |  | x |
| Incorrect password input |  | x |
| Correct username and password input | x |  |

- Outcomes
  - Sign In form: validation and user notifications functionality works as expected.


### Test Sign out functionality
- Outline of Test
    -  Make sure users and super users can log out
- Test planning
    - On the deployed site login under existing user/superuser, navigate to the Logout page and logout.

| Sign Out Form |  OK |Error| 
| ------ | ------ |  ------ |
| Navigate to the Logout page | x | |
| Logout as user | x | |
| Logout as superuser | x | |

- Fix
    -  Changed Sign Out text Logout
- Outcomes
    - Sign out functionality works


### Test Update Profile
- Outline of Test
  -  Check that our form submits to Django admin and retains updated user profile information
- Test planning
  - Set up a user and input information
  - Change some user information
  - submit the form
  - check Django admin updates on the back end
  - check profile updates on the front end
- Implementation
  - Login
  - Navigated to the profile page
  - Input information into the profile form
  - Press the Update Information button
  - Checked response received success toast
  - Checked information appeared correctly in Django admin
  - Checked information was visible to the user on profile after update button submitted information
  - Checked information automatically appear in the secure checkout form

- Results
  - Update Profile function worked on front and back end
- Outcomes
  - Update Profile function fit for purpose of the site



### Test Stripe
- Test
   - Check if the order was passed from checkout app to stripe 
- Implementation
   - Selected product from Temple Lean site
   - Go through check out process fill out form
   - Enter the following card details
      - Card Number 4242 4242 4242 4242 
      - CVC 424
      - Postal code 42424
    - Complete Order
    - Login to stripe account 
    - Review API requests in stripe account on the developer page
    - Select webhooks enter deployed site links
    - Click send testwebhook 

- Outcomes
  - Stripe was integrated and the test payment functionality is active and working
  - Webhook functionality is active and working

### Testing Web Browser Screens
-   Web Browser: Chrome, Firefox, Opera, Edge
    - There were no obvious bugs on desktop or mobile views within this browser

### Testing Device screens
- Chrome developer tools: Websites appearance and functionality was available across multiple devices listed below;
  - Moto G4
  - Galaxy S5
  - Pixel 2
  - Pixel 2 XL
  - iPhone 5/SE
  - iPhone 6/7/8
  - iPhone 6/7/8 Plus
  - iPhone X
  - iPad
  - iPad Pro
  - Surface Duo


### Testing Markdown
I check the README.MD file spelling using [Grammarly: Free Online Writing Assistant](https://app.grammarly.com/)


### Code Validators
I used the following code validators to help me debug my code 
 - HTML - [link to HTML validator](https://validator.w3.org/)
   - All HTML pages were placed in validator to check best practice
 - CSS Validator - [link to CSS validator](https://jigsaw.w3.org/css-validator/#validate_by_input)
    - No obvious errors were seen
 - Python Validator [link to PEP8 Validator](http://pep8online.com/)
    - Some lines too long 
    - Didn't fix as it threw a whitespace error which effects the functionality of the site 
-   JS validation [JSHint](https://jshint.com/)
    - Missing semicolon.