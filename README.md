# Sustainable Living

This project is a Django based website for an e-commerce shop called Sustainable Living that sells eco-friendly household products. Users can search through items online and purchase them. Users can also sign up and sign in to view their previous orders.

![Homepage on Different Devices](/media/readme-images/homepage_different_devices.png)

[Deployed Website](https://sustainable-living-47990b315e83.herokuapp.com/)

## Table of Contents

- [Goals](#goals)
- [Key Features](#key-features)
- [Potential Users](#potential-users)
- [UX Design & Development](#ux-design--development)
  - [5 Layers of UX](#5-layers-of-ux)
  - [Agile Development](#agile-development)
  - [Wireframes](#wireframes)
  - [Images](#images)
  - [Colour Scheme](#colour-scheme)
- [Data Model](#data-model)
  - [Booking](#booking)
  - [Allergens](#allergens)
- [Technology & Resources](#technology--resources)
- [Deployment](#deployment)
  - [How to Clone Repository](#how-to-clone-repository)
  - [How to Deploy to Heroku](#how-to-deploy-to-heroku)
- [Issues/Bugs](#issuesbugs)
  - [Resolved](#resolved)
  - [Unresolved](#unresolved)
- [Testing & Validation](#testing--validation)
  - [Manual Functional Testing](#manual-functional-testing)
  - [PageSpeed Testing](#pagespeed-testing)
  - [WAVE Testing](#wave-testing)
  - [HTML Validation](#html-validation)
  - [CSS Validation](#css-validation)
  - [JS Validation](#js-validation)
  - [Python Validation](#python-validation)
- [Future Improvements/Developments](#future-improvementsdevelopments)
- [Acknowledgments](#acknowledgments)


## Goals

- To build a functioning website for an e-commerce business.\
[EPIC: Admin/Housekeeping](https://github.com/DiarmuidHenry/Restaurant-Booking/issues/20)
- To allow the shop owner to add their products to the site, ensuring these accurately represent the actual products.\
[EPIC: Products](https://github.com/DiarmuidHenry/Restaurant-Booking/issues/20)
- To allow users to easily make purchases online.\
[EPIC: Purchasing](https://github.com/DiarmuidHenry/Restaurant-Booking/issues/20)
- To allow users to create an account, allowing them to see any current orders they have.\
[EPIC: User Account](https://github.com/DiarmuidHenry/Restaurant-Booking/issues/28)
- Users can easily and clearly navigate the site, with the sight remaining attractive and user friendly.


## Key Features

- A clean, light _Home_ page with the company's name clearly visible in the header, alongside a search bar for users to look up particular items. Underneath, a navbar, which users can use to guide them through the site. A subtle botanical background image adds to the eco-friendly tone of the website.

![Home Page](/media/readme-images/homepage_top.png)

- Navbar clearly differentiates when users are logged in or not.

![Navbar Not Logged In](/media/readme-images/not_logged_in.png)

![Navbar Logged In](/media/readme-images/logged_in.png)

- Products clearly displayed with an image, alongside their name, price, category and rating. Clicking on the image leads to mroe product details; clicking on the category leads to all items in that category.

![Product List](/media/readme-images/product_list.png)

- Product details shown on a new page, with a larger image, as well as the product's description. The option to add to cart now appears, as well as an option to give a rating.

![Product Details](/media/readme-images/product_details.png)

- A logged in user can give a rating of between 1 and 5 stars. If 4 is chosen (as in the image), the first 4 stars become selected. The user can then confirm this by seleceting *Submit Rating*.

![New Rating](/media/readme-images/new_rating.png)

The user's rating then remains, unless they change and resubmit. Every time a new rating is submitted, the average rating of the item is recalculated: this is simply the mean of all ratings for that item.

![Rating Updated](/media/readme-images/rating_updated.png)

- A dropdown list of different options for that particular item give the user different choices of colours, patterns, scents etc (dependent on the product).

![Dropdown Options](/media/readme-images/dropdown_options.png)

- A success message appears when a user adds an item to their cart.

![Add to Cart Success](/media/readme-images/add_to_cart_success.png)

- The cart clearly shows all chosen items - along with their respective subtotal - as well as the delivery cost, and whether the user has purchased enough for a free tote bag. These order thresholds can be changed as necessary.

![Cart](/media/readme-images/cart.png)

![Order Under Threshold](/media/readme-images/order_under_threshold.png)

![Order Over Threshold](/media/readme-images/order_over_threshold.png)

- Checkout is straightforward: the user (whether signed in or not) enters their personal details, then their bank card details, and the order is created. If the user is signed in and clicks 'Save to My Orders', they can later access this order from the *My Orders* page.

![Checkout 1](/media/readme-images/checkout_1.png)

![Checkout 2](/media/readme-images/checkout_2.png)

- When an order is completed, a popup message appears and an order confirmation page details the order.

![Order Confirmed](/media/readme-images/order_confirmed.png)

![Order Confirmation](/media/readme-images/order_confirmation.png)

- Users can then view this order and its details in the *My Orders* section (if they are logged in and chose to save it).

![My Orders](/media/readme-images/my_orders.png)

![My Order Details](/media/readme-images/my_order_details.png)

## UX Design & Development

### 5 Layers of UX

I began the development by considering the 5 layers of UX and how those would shape the content and appearance of the website.

#### Strategy

The site is designed to balance business goals with user needs. The primary objective is to facilitate product sales by offering a simple and intuitive shopping experience. Additionally, the site promotes sustainability by displaying the CO2 footprint of products, aligning with the values of an evergrowing population of consumers becoming more conscientious of their everyday purchases.

#### Scope

Key features include product browsing with options for filtering by categories; a detailed product page with ratings; a dynamic shopping cart that handles multiple item variations and a streamlined checkout process with payment integration. Authenticated users can view previous orders and submit product ratings.

#### Structure

The site is structured to ensure easy navigation, with a clear hierarchy for product categories and intuitive flows for adding items to the cart, viewing the cart, and completing checkout. Account-related features such as past orders and ratings are easily accessible from the user's account section in the navbar.

#### Skeleton

The site’s layout includes a responsive design that is optimised for both larger and smaller devices. Product details, a simple 'Add to Cart' button and checkout forms are placed for maximum usability, ensuring a smooth user journey from product search/selection to order confirmation. To plan the skeleton of the site, I used wireframes. Theses wireframes are a close representation of the finished site.

[See Wireframes below](#wireframes).

#### Surface

The surface design uses a clean, minimalist aesthetic to ensure clarity and focus on the products. The site employs consistent typography and an earthy colour palette that aligns with the brand’s eco-friendly message, while ensuring key elements like buttons and forms are easily accessible and actionable. A leaf favicon (similar to this: 🌿) again reinforces the ethos of the site.

![Colour Palette](/media/readme-images/colour_palette.png)

### Wireframes

**Home Page**

![Wireframe - Home](/media/readme-images/wireframe_home.png)

**Products**

![Wireframe - Products](/media/readme-images/wireframe_products.png)

**Product Details**

![Wireframe - Product Details](/media/readme-images/wireframe_product_details.png)

**Cart**

![Wireframe - Cart](/media/readme-images/wireframe_cart.png)

**Checkout**

![Wireframe - Checkout](/media/readme-images/wireframe_checkout.png)

**Order Confirmation**

![Wireframe - Order Confirmation](/media/readme-images/wireframe_order_confirmation.png)

**My Orders**

![Wireframe - My Orders](/media/readme-images/wireframe_my_orders.png)

**Order Details**

![Wireframe - Order Details](/media/readme-images/wireframe_order_details.png)

### Agile Development

The project was planned, tracked and process using the AGILE methodology throughout.

I initially created a small number of epics, each of which consisted of multiple user stories. In turn, these user stories were defined and checked based on multiple acceptance criteria, ensuring that the desired result from that user story was acheived.

[The Kanban board for this project can be seen here.](https://github.com/users/DiarmuidHenry/projects/6) Below are direct links to all epics and the user stories they consist of:

[EPIC: Admin/Housekeeping](https://github.com/DiarmuidHenry/PP5/issues/5)

 - [USER STORY: Project Creation](https://github.com/DiarmuidHenry/PP5/issues/1)
 - [USER STORY: README.md](https://github.com/DiarmuidHenry/PP5/issues/2)
 - [USER STORY: Heroku Deployment](https://github.com/DiarmuidHenry/PP5/issues/3)
 - [USER STORY: Testing](https://github.com/DiarmuidHenry/PP5/issues/4)

[EPIC: User Accounts](https://github.com/DiarmuidHenry/PP5/issues/8)

 - [USER STORY: User Accounts](https://github.com/DiarmuidHenry/PP5/issues/6)
 - [USER STORY: My Orders](https://github.com/DiarmuidHenry/PP5/issues/7)

[EPIC: Products](https://github.com/DiarmuidHenry/PP5/issues/9)

 - [USER STORY: Browsing Products](https://github.com/DiarmuidHenry/PP5/issues/10)
 - [USER STORY: Product Details](https://github.com/DiarmuidHenry/PP5/issues/11)
 - [USER STORY: Ratings](https://github.com/DiarmuidHenry/PP5/issues/12)
 - [USER STORY: Product Management](https://github.com/DiarmuidHenry/PP5/issues/13)
 - [USER STORY: Stock](https://github.com/DiarmuidHenry/PP5/issues/19)
 
[EPIC: Purchasing](https://github.com/DiarmuidHenry/PP5/issues/14)

 - [USER STORY: Shopping Cart](https://github.com/DiarmuidHenry/PP5/issues/16)
 - [USER STORY: Checkout](https://github.com/DiarmuidHenry/PP5/issues/17)


[EPIC: Marketing & Outreach](https://github.com/DiarmuidHenry/PP5/issues/20)

 - [USER STORY: Social Media](https://github.com/DiarmuidHenry/PP5/issues/21)
 - [USER STORY: External Websites](https://github.com/DiarmuidHenry/PP5/issues/22)
 - [USER STORY: Newsletter](https://github.com/DiarmuidHenry/PP5/issues/23)


All __must have__ user stories were acheived, as well as almost all __should have__ user stories. The only __could have__ task was not completed, as the amount of time and resources needed in order to fulfill it would vastly outweigh the minor benefit it would bring.


## Data Models

Below is an ERD of the models in the project.

![Entity Relationship Diagram](/media/readme-images/erd.png)

## Technology & Resources

- **Django**: Web framework for backend development, providing a structured approach to building the restaurant website.
- **PostgreSQL**: Database management system for storing and managing data securely.
- **Cloudinary**: Cloud-based image and video management service used for handling images of menu items.
- **HTML/CSS/JavaScript**: Frontend technologies for creating interactive and responsive user interfaces.
- **Bootstrap**: Frontend framework for designing mobile-first and responsive websites.
- **Git/GitHub**: Version control system and platform for project management.
- **Heroku**: Cloud platform for deploying the application.
- **GitPod**: Online IDE for coding and devloping project.
- **Python Libraries**: Various Python libraries used for additional functionalities.
- **WAVE Accessibility Tool**: Web accessibility evaluation tool for ensuring accessibility inclusive design practices.
- **W3C Validator**: Tools for validating HTML, CSS, and web standards used in website development.
- **dbdiagram.io**: ERD design.
- **Pexels**: Royalty free images.
- **Microsoft Designer**: Creating the product images (due to lack of real photos available).
- **Kaggle**: Helpful source for database populating.

## Deployment

### Heroku

### How to Clone Repository

1. Go to the [GitHub repository](https://github.com/DiarmuidHenry/PP5/).
2. Click the green **Code** drop down button.
3. Click **HTTPS** and copy the URL.
4. Open your IDE, and open a terminal.
5. Enter `git clone url`, replacing `url` with the URL copied in step 3.

### How to deploy to Heroku

1. Log in to [Heroku](https://www.heroku.com/). If you do not already have an account, you can [sign up here](https://signup.heroku.com/).
2. Click **Create new app** on the Heroku Dashboard. Give the app a unique name. Select your region, click **Create app**.
3. Go to the **Settings** tab, click on **Reveal Config Vars**.
4. In the **KEY** field, enter the secret/sensitive variable names that you have/will store in your `env.py` file. For example, `DATABASE_URL`, `CLOUDINARY_URL`. \
In the corresponding `VALUE` field, enter the value for these variables. For example, `postgres://<sensitive_information_included_here>/<your_database_name>`, `cloudinary.url/details`.
5. Go to the **Deploy** tab. Beside **Deployment method**, click **GitHub**, then confirm by clicking **Connect to GitHub**.
6. Under **Search for a repository to connect to**, type the name of the repo (whether that be the name of this repo, or of the one you have cloned). Click **Search**, then click **Connect** when the repo name appears. The Heroku app is now linked to the GitHub repo.
7. If you would like Heroku to manually update the app every time you push chances to GitHub, click on **Enable Automatic Deploys**. (This is optional).
8. Deploy the app by scrolling down and clicking **Deploy Branch**. Heroku will show you the deployment logs as it builds the app. This will take a few seconds.
9. When the app is finished being built, a message will appear saying **Your app was successfully deployed**. Click the **View** button to view the app (opens in a new tab).

## Issues/Bugs

### Resolved

- **Resolved Bug Example**

  ![Image title](/media/readme-images/image_name.png)

  Information about the bug and how it was fixed.

  ![Chosen allergens stored](/media/readme-images/bug_filter_choices_lost_1.png)

### Unresolved

- Unresolved bug example. Explanation of bug and why it wasn't fixed. How will it be addressed in future development?

## Testing & Validation

### Manual Functional Testing

Below are the records for the manual testing of all functionalities of the application.

**Navbar**

|Test Item|Test Carried Out|Result|Pass/Fail|
|-------------|------------------|-----------|-------|

**Home**

|Test Item|Test Carried Out|Result|Pass/Fail|
|-------------|------------------|-----------|-------|

**Products Page**

|Test Item|Test Carried Out|Result|Pass/Fail|
|-------------|------------------|-----------|-------|

**Product Details**

|Test Item|Test Carried Out|Result|Pass/Fail|
|-------------|------------------|-----------|-------|

**Cart**

|Test Item|Test Carried Out|Result|Pass/Fail|
|-------------|------------------|-----------|-------|

**Checkout**

|Test Item|Test Carried Out|Result|Pass/Fail|
|-------------|------------------|-----------|-------|

**My Orders**

|Test Item|Test Carried Out|Result|Pass/Fail|
|-------------|------------------|-----------|-------|

**Error Pages**

|Test Item|Test Carried Out|Result|Pass/Fail|
|-------------|------------------|-----------|-------|
|404 Error|Force a 404 error by adding `/doesnotexist` to url|404.html loads with link to Home page|PASS|
|500 Error|Force a 500 error by removing `ALLOWED_HOST` from `settings.py`|500.html loads with link to Home page|PASS|

### PageSpeed Testing

The website receieves high score on all pages. Below is the result from the *Home* page.

![PageSpeed Result - Home](/media/readme-images/pagespeed_test.png)

### WAVE Testing

Web Accessibility Evaluation Tools revealed a few errors: it repeatedly gave 'Missing Form Label' and 'Empty Link'. However, after further inspection, I could see that this was due to the structure of the code, not the lacj of labels. All forms are labelled and there are no empty link; the inclusion of divs and spans inside forms/anchors led to this. Since this is standard practise and not an accessibility issue, I did not make any changes. No other errors were obtained. the styling and appearance of the navbar.

### HTML

The site passed the W3C HTML Validator with no issues.

![HTML Validation](/media/readme-images/html_validatino.png)

### CSS

The site passed the W3C CSS Validator with no issues.

![CSS Validation](/media/readme-images/css_validation.png)
## Future Improvements/Developments

- Add more functionality to the Product Development page, allowing the site owner to edit and remove products without having to access the admin panel.
- Incorporate the 'stock' attribute into the orders logic. This would automatically update stock levels for individual items, which would be necessary for a large scale shop. For a smaller scale, this is somewhat unnecessary.
- Add confirmation emails, order dispatch emails etc to be in line with features on other high end e-commerce sites.