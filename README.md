# Edible Bouquets
[View the live project here](https://final-ms4-app.herokuapp.com/)

## Application for people, who is looking for special and outstanding gifts.

# Project description
“Edible Bouquets” is an e-commerce application that allows selling all kinds hand made edible bouquets. Fruit/veggies bouquets, chocolate bouquets, meat/cheese bouquets are novel and delicious gifts for any occasion, such as:
|  |  |
| ------ | ------ |
| Valentine’s Day | Valentine’s Day |
| Mother's Day | Baby showers |
| Wedding anniversaries |Corporate gifts  |
| Thank you gifts | Get well soon |
| Engagements | Communions |
| Christenings | Christmas gifts and more |

“Edible Bouquets” offers a healthy, exciting, and delicious alternative to sending flowers. 
The purpose of the application is to allow users to easily and quickly find the product, select the necessary quantity and buy it online with an option of delivery. As well as contact the owner directly via the contact form if necessary.

There are the following categories of Users:  
1.	General Users
3.	Admin (the Application Owner)  

Thus, the Application will help to:
-	Register/Sign in to the User Account
-	Sign out from the User Account
-	Easily view the list of all products.
-	Easily view the list of categories.
-	Sort products by category/price/name and more.
-	Search products with the search option
-	Choose products and add them to the shopping bag
-	Choose/edit the number of products
-	Choose/edit the size of products
-	Delete products from the shopping bag
-	Purchase the needed quantity of products
-	Track the history of purchased products

# User Stories  
[User Stories](/media/userstories.png)

# Wireframe
Initial wireframes for the project are shown below, representing the desktop, tablet, and mobile views.
[Wireframe](/wireframe/)

# Database Model
[Database](/media/database.pdf)

# UX
The purpose of the project is to design a responsive website for all kinds of devices (mostly for desktops and smartphones) for making navigation fast and efficient. User can easily define their actions and navigate easily.  
Thus, users can:  

1. All products page / Pop up a modal window with carousel:
    -	Clearly understand that the project’s purpose is to help find a novel and delicious gift for any occasion.  

2. Navigation bar:
    -	Clearly understand that there is a search option to find a specific product by a keyword (search icon on a mobile screen).
    -	Clearly understand that it is always possible to be redirected to the all products page by the Logo (left side) and 'SHOP ALL' button.
    -	Clearly understand that it is always possible to find all products due to the “SHOP ALL” button.
    -	Clearly understand that it is always possible to find products related to different categories 'Chocolate Bouquets', 'Meat & Cheese', 'Veggies & Fruits'.
    -	Clearly understand that it is always possible to contact the owner via the 'Contact Us' page.
    -	Clearly understand that it is always possible to Login or Register an account.
    -	Clearly understand that it is always possible to sort products by 8 different variants. 
    -	It is always possible to view the User’s profile with previously created orders (if a user signed in).
    -   It is always possible to view the bag total in euros.
    -	In case if the Admin User is Signed In, it is always possible to view the User’s profile with previously created orders.
    -	In case if the Admin User is Signed In, it is always possible to add/edit/delete products.

3.  Within All pages except 'Contact Us:
    -	Easily find all presented products.
    -	Product title.
    -	Product Price
    -	Product category
    -	Product rating
    -	Edit/Delete options for Admin  
    -	If product card has hovered: User can see 
    -	-   Product available sizes
    -   -   Product base ingredients

4. Contact Us page, User can:
    -   Easily fill out the form and submit
    -   Get confirmation when the form was sent
    -   User will get an email with confirmation and a copy of his query

5. After hitting the product photo, the User can:
    -   See product larger image.
    -	See product full description. 
    -	Easily find how to increase/decrease product quantity.
    -	Easily find how to select product size.
    -	Easily find how to add the product to the Shopping Bag by hitting the respective button.
    -	Easily find how to get back to products by hitting the respective button.
    -	Easily find a short description of all available sizes.
    -	Can see up to five random products from the same category (small images on the left side)
    -	-   If a small image hovered: the small image will be shown instead of the main products image
    -	-    If a small image is clicked: the user will be redirected to that product full description page
    -	Edit/Delete options for Admin.  

6. After adding the product to the Shopping Bag, the User can:
    -	See the Success/Error toast message with the additional info. 
    -	In case of Success, the User will see the Order information in the toast message: product title/quantity/total price/threshold for free delivery/Button to Secure Checkout.  
    -	Easily go to the Secure Checkout due to the respective button.  

7. After hitting the Secure Checkout button, the User can:
    -	See the Shopping Bag with product image/title/quantity/price/total price/delivery price and threshold for free delivery/Button to Secure Checkout/ Button to Shopping.  
    -	See the buttons to Update/Remove product quantity.  

8. After hitting the Secure Checkout button, the User can:
    -	See the Order details with product photo/title/quantity/order price/total price
    -	See the Order Info Form
    -	See the field for entering the Card number for making a purchase
    -	See the Adjust Bag/Complete Order buttons
    -	See how much the User is charged.  

9. After hitting the Secure Checkout button, the User can:
    -	See the full Order details 
    -	See the toast (success/error) message
    -	In case of success user can see the toast message with the Order Confirmation (user will get full order details with confirmation email)
    -	See the link to Return to the Shopping.  

10. All forms are validated what makes it easier for the User to apply corrective actions.  

11. According to the specific actions User gets the Success/Error messages in case of successful or wrong actions.  

12. User can save previous order info.  

13. User can reset the password in case if it is forgotten.  

# Features  

## Existing features  

-	The website is responsive on all device sizes according to the initial goal.

-	Collapsible, fixed-top left-side Navigation bar with a toggle button (Mobile Collapse) allows making navigation bar responsive and comfortable to use on all devices.

-	Internal links on the navigation bar:
    1.	Logo on the top-left side allows any time to revert to the “Shop All” page when clicked.
    2.	“Shop All” - also allows return to the “Shop All” page when clicked.
    3.	Search bar allows users to search for desired products by keywords in the product description.
    4.	“SHOP ALL” select all products.
    5.	“CHOCOLATE BOUQUETS” select desired product Category.
    6.	“MEET & CHEESE” select desired product Category.
    7.	“VEGGIES & FRUITS” with dropdown menu allows to select desired products by defined keyword.
    8.	“CONTACT US” allows contacting the website owner.
    9.	“My Account” allows users to reach the Profile, check the Order information or Log Out for Registered/Logged-in Users.
    10.	“My Account” allows to Register/Login for non-registered/non-logged Users.
    11.	“Shopping bag” icon with link leads to the Shopping Bag.  

-	Toast-messages 

    1. Allow users to receive interactive messages.  
  
-	 Validated forms
        1.	Sign In
        2.	Sign Up
        3.	Sign Out
        4.	Checkout
        5.	Search  
        6.	Contact Us

-	All pages with products
    1. Provides Users with clickable product Cards with additional information on them.
    2. Admin can see/use - delete/edit product buttons.
    3. Back to top button (right bottom corner).  

-   Product details Page  

    1. Increase/Decrease product quantity buttons are provided.
    2. “Add to bag” button is provided.
    3. “Keep Shopping” button is provided.

-   Shopping Bag Page  

    1. Update/Remove product quantity buttons.
    2. “Keep Shopping” button is provided.
    3. “Secure Checkout” button is provided.  

-   Checkout Page  
    1. Validation form with Name/Email/Delivery details. (User can choose delivery address).
    2. A Stripe payment field below the delivery form.
    3. “Adjust Bag” (redirects back to the “Shopping Bag” page)/
    4. ”Complete Order” button to make a payment.
    5. By ticking the check box below the Delivery form, the user can save his info for future orders prefill.
    5. loading overlay pop-up when payment is processing.
 
-	Contact Us page  
    1. Contact Us form with js validation form and relevant error messages.

- Sign UP  
    1. Non-registered Users can Sign Up from My Account on the Navbar.
    2. A validated Form with the Email/Username/Password input fields is displayed.
    3. Once the form is filled in and sent, users can see the displayed message with the notification that a Confirmation email was sent. 

## Features to Add  

-	Admin possibility to Add/Edit/Delete product category on the frontend side.
-	User possibility to leave comments and score a product.

# Technologies Used

## Languages Used  

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/CSS)
-   [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
-   [jQuery](https://en.wikipedia.org/wiki/JQuery)
-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))  

## Frameworks, Libraries & Programs Used

-   [Bootstrap 4.4.1](https://getbootstrap.com/docs/4.4/getting-started/introduction/)
    To provide the responsiveness and styling of the website.
-   [jQuery](https://jquery.com/) 
    To implement some fornt end features.  
-   [Jinja](https://jinja.palletsprojects.com/en/2.11.x/) Is used for the Python template.  
-   [Heroku](https://dashboard.heroku.com/) The cloud platform for deploying the app.  
-   [Django](https://www.djangoproject.com/) High-level Python Web framework.
-   [PostgreSQL](https://www.postgresql.org/) Database management system.
-   [AWS](https://aws.amazon.com/) Used for storing static files.
-   [Stripe](https://stripe.com/en-se) Used to handle the payments at checkout.
-   [Randomkeygen](https://randomkeygen.com/) Used to generate random key.
-   [Git](https://git-scm.com/) 
    Git for version control.
-   [GitHub](https://github.com/)
    GitHub to store the projects code.
-   [wireframe.cc](https://wireframe.cc/) 
    For the project design.
-   [AmIResponsive]( http://ami.responsivedesign.is/)  
    I used this service for making my project screenshots
-   [W3C Markup Validation Service](https://validator.w3.org/) 
    For HTML code testing.
-   [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) 
    For CSS code testing
-   [Autoprefixer CSS online](https://autoprefixer.github.io/) 
    For CSS auto prefixer
-   [JSHint](https://jshint.com/)
    For JS code testing
-   [Realfavicongenerator](https://realfavicongenerator.net/)
    I used this service for generating favicon for the website
-   [PEP8 online](http://pep8online.com/)
    For Python code testing
-   Chrome Developer Tools 
    I used this service to test code changes and the responsivity of the website.  

# Testing  

[View testing information here](/*.md)  

# Deployment  

## Needed Installation Prerequisites  

The following technologies needed to be installed in the IDE environment to run the project.

- Python3
- Git
- pip3  

It is important to be registered on the following platforms:

- Heroku
- AWS
- Stripe  

## Cloning on GitHub  

- Login to GitHub.
- Open Dialog/life-maker.
- Click "Code" then under "Clone" copy the link with the HTTPS URL.
- Go to the terminal in your IDE environment.
- Change the working directory to where you want the clone to be saved by typing cd and the name of the directory.
- Type git clone and paste the copied HTTPS URL.
- After pressing enter the clone will be saved to your chosen directory.  

## Local Deployment On Gitpod  

- After cloning the repository on GitHub go to the chosen IDE environment and open the clone directory.
- Install the libraries from the requirements.txt, in the terminal type - pip3 install -r requirements.txt.
- Set your environment variables in your Gitpod settings or create an env.py file.
- If setting variables within an env.py file add this file to the created .gitignore file in order not to expose your variables when pushing to GitHub.
- Your environment variables will need to be set as follows:
#
    os.environ["DEVELOPMENT"] = "True"
    os.environ["SECRET_KEY"] = "Your Secret key"
    os.environ["STRIPE_PUBLIC_KEY"] = "Your Stripe Public key"
    os.environ["STRIPE_SECRET_KEY"] = "Your Stripe Secret key"
    os.environ["STRIPE_WH_SECRET"] = "Your Stripe WH_Secret key"
- Create the database from the models by typing in the terminal python3 manage.py 'makemigrations'. 
- Followed by python3 manage.py migrate
- Load the data fixtures by typing in the terminal: python3 manage.py 'loaddata' products
- Create a superuser so you can log in to the Django admin by typing in the terminal: python3 manage.py 'createsuperuser' (providing email and password)
- The site can now be run locally by typing in the terminal python3 manage.py 'runserver'.  


## Heroku Deployment
- After logging in to Heroku, select "Create New App" Choose the region closest to you and select "Create app".
- On the resources tab, to provision the database in the add-on field search for and select "Heroku Postgres".
- A pop-up should appear and under "Plan name" use "Hobby Dev-Free" and select "Provision".
- Go to your IDE and type pip3 install dj_database_url and pip3 install psycopg2-binary as these need to be installed to use Postgres. Also pip install gunicorn for the webserver.
- To make sure Heroku installs all of the apps when deployed save the requirements by typing in the terminal pip3 freeze > requirements.txt
- Back on Heroku under settings, select "Reveal config vars" and copy the key from DATABASE_URL.
- In the project folder on settings.py in the database setting, comment out the current database setting.
- This should be replaced with:  
#
    DATABASES = {
        'default': dj_database_url.parse('<Enter the copied DATABASE_URL key here>')
    }  

- Add the data to the postgres database by typing in the terminal python3 manage.py makemigrations. Followed by python3 manage.py migrate
- Load the data fixtures by typing in the terminal: python3 manage.py loaddata products
- Create a superuser so you can log in to the Django admin by typing in the terminal: python3 manage.py createsuperuser
- Return to database setting in settings.py and remove code 
#
    DATABASES = {
        'default': dj_database_url.parse('<Enter the copied DATABASE_URL key here>')
    }  
  and uncomment the previous database setting.
- Create a Procfile and add web: gunicorn life_maker.wsgi:application
- Login to Heroku through the cli heroku login -i
- Temporarily disable collect static by typing heroku config:set DISABLE_COLLECTSTATIC=1
- Add `final-ms4-app.herokuapp.com, localhost' to ALLOWED_HOSTS in settings.py.
- The app can now be deployed by typing in the terminal heroku git:remote -a vision-furniture and git push heroku master
- On Heroku dashboard under "Deploy" set "Deployment method" to connect to Gitub.  
- Under "Automatic Deploy" set "Enable automatic deploy" so the code is automatically deployed to Heroku and GitHub.  

## Adding Static Files to AWS  

- Go to AWS website, select S3 under services, create a new bucket (it is important to select the close to you region), choose to allow all public access.
- Go to the new bucket and under properties, tab turn on static website hosting.
- Under the permissions tab the CORS configuration tab and enter the following:  
#
    [
      {
          "AllowedHeaders": [
              "Authorization"
          ],
          "AllowedMethods": [
              "GET"
          ],
          "AllowedOrigins": [
              "*"
          ],
          "ExposeHeaders": []
      }
    ]  

- Go to the bucket policy tab, select "policy generator" to create a security policy for this bucket.
- It is required to add:  

1. Policy type: S3 bucket policy
2. Effect: Allow
3. Principal: *
4. Action: GetObject
5. Copy the ARN from the bucket policy tab. And paste it into the ARN box at the bottom.
6. Click Add statement. Then generate policy.  

- Copy the policy into the bucket policy editor.
- Add /* onto the end of the resource key. Click Save.
- Go to the access control list tab and set the list objects permission for everyone under the Public Access section.
- Create a user to access the bucket by selecting IAM from the services menu.
- Select "Groups" and select "Create new group". Add in a new group name and click next, next again then "create new group"
- Create a policy to access the bucket, by selecting "policies" then "create policy".  
- Select JSON tab and import managed policy. Search for s3 and import "AmazonS3FullAccess".
- Copy the bucket policy ARN from the bucket policy in s3 > permissions. Paste it into the JSON resource key on create policy twice giving the second paste a /* at the end. Select "review policy". Give the policy a name and description and create the policy.
- Go to "groups", select the new group, select "attach policy", search for the newly created policy, and attach it to the policy.
- Go to "users", add user, create a user name, give them programmatic access and select next.
- Add the new user to the group and select next to create user then download the .csv file.
- Go to your IDE terminal type: pip3 intsall boto3 and pip3 intall django-storages to install the packages to connect to django. Type: pip3 freeze > requirements.txt so they get installed on Heroku when it's deployed.
- Add 'storages' to installed apps on the settings.py file. Add the following code to tell Django which bucket to communicate with:  


    if 'USE_AWS' in os.environ:
        # Cache control
        AWS_S3_OBJECT_PARAMETERS = {
            'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
            'CacheControl': 'max-age=94608000',
        }

        # Bucket Config
        AWS_STORAGE_BUCKET_NAME = 'final-ms4-app'
        AWS_S3_REGION_NAME = 'eu-west-1'
        AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
        AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    
        # Static and media files
        STATICFILES_STORAGE = 'custom_storages.StaticStorage'
        STATICFILES_LOCATION = 'static'
        DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
        MEDIAFILES_LOCATION = 'media'
    
        # Override static and media URLs in production
        STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
        MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'  

- Add the AWS keys on Heroku from the .csv file to the config vars. 
- Add USE_AWS: True, so that the setting file knows to use the AWS configuration when deploying to Heroku
- Remove the COLLECTSTATIC variable.
- Push all the changes to Github to provide automatic deployment to Heroku.  


# Credits  

## Tutorials  

- The application is mostly based on the Boutique Ado from the Code Insitute tutorial project.  

## Media  

- Images and product names, descriptions were taken from [Lunch Bunch](https://lunchbunch.com.au/)  


# Acknowledgements
- To my mentor Marcel Mulders for patience and helping me through the process.
- To the Slack community, for support and prompt reactions during the process.