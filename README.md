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

- A Facebook Business page for the site has been created.

![Facebook Business Page](/media/readme-images/facebook_business.jpeg)

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


All __must have__ user stories were acheived, as well as almost all __should have__ user stories. The few __could have__ tasks were not completed, as the amount of time and resources needed in order to fulfill it would vastly outweigh the minor benefit it would bring.

## Data Models

Below is an ERD of the models in the project.

![Entity Relationship Diagram](/media/readme-images/erd.png)

## SEO (Search Engine Optimization)

To improve audience reach and search engine visibility, various SEO techniques have been employed throughout the application:

- Internal Linking: Every page is reachable via links from other pages, ensuring a logical structure that search engines can easily crawl. This helps improve the overall accessibility and ranking of the site.
- Meta Tags and Titles: Meta description tags are included on all key pages to provide search engines with relevant information about the content. Additionally, the site title is set in the parent template to ensure consistent branding and SEO-friendly structure across all pages.
- Link Attributes: The proper use of nofollow for paid or distrusted links and sponsored for sponsored content is implemented to define relationships between linked documents correctly.
- Sitemap and Robots.txt: A sitemap is included in the application to facilitate search engine bot crawling, while a robots.txt file is provided to manage how and what content should be crawled. This ensures that sensitive or unnecessary pages are excluded from search engine results.
- 404 and 500 Pages: Custom 404 error and 500 network error pages are in place with appropriate messaging and a redirect back to the home page, ensuring that users who encounter non-existent content are not left stranded.

## E-commerce & Marketing

The application incorporates key marketing strategies and follows fundamental e-commerce principles to reach and engage the target audience:

- Facebook Business Page: A dedicated [Facebook Business Page]() has been created to promote the site and expand its social media reach. This helps engage potential customers and drive traffic to the site.
- Newsletter Signup: The application includes a newsletter signup form, allowing users to subscribe for updates, offers, and news. This helps build a mailing list for direct marketing efforts and strengthens customer engagement.
- E-commerce Model: The application follows a B2C (Business-to-Consumer) e-commerce model, where users can browse products, add items to a cart, and complete purchases online. The business model is supported by features like a user-friendly checkout process and product ratings.

These strategies enhance the brand’s online presence and customer reach while ensuring a smooth and efficient e-commerce experience.


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

### How to Deploy to Heroku (Including Custom PostgreSQL Database Setup)

1. Log in to [Heroku](https://www.heroku.com/). If you do not already have an account, you can [sign up here](https://signup.heroku.com/).
2. Click **Create new app** on the Heroku Dashboard. Give the app a unique name, select your region, and click **Create app**.
3. **Configure your custom PostgreSQL database**:
   - Go to the **Settings** tab, click on **Reveal Config Vars**.
   - In the **KEY** field, enter `DATABASE_URL`.
   - In the **VALUE** field, enter the PostgreSQL URL of your database.(e.g., `postgres://<username>:<password>@<host>:<port>/<database_name>`).
4. In the **KEY** field, also enter any other secret/sensitive variables from your `env.py` file (e.g., `SECRET_KEY`, `CLOUDINARY_URL`).
   - Example: `SECRET_KEY`, `CLOUDINARY_URL`, etc.
   - In the **VALUE** field, enter the corresponding values.
5. Go to the **Deploy** tab. Beside **Deployment method**, click **GitHub**, then confirm by clicking **Connect to GitHub**.
6. Under **Search for a repository to connect to**, type the name of the repo (whether it be the name of this repo or the one you cloned). Click **Search**, then **Connect** when the repo name appears. The Heroku app is now linked to the GitHub repo.
7. If you'd like Heroku to automatically deploy the app when you push changes to GitHub, click on **Enable Automatic Deploys** (this is optional).
8. Deploy the app by scrolling down and clicking **Deploy Branch**. Heroku will show the deployment logs as it builds the app. This will take a few moments.
9. When the app has finished deploying, a message will appear saying **Your app was successfully deployed**. Click **View** to open the app in a new tab.
10. **Migrate the database**:
    - Open the **More** dropdown (top-right corner of your Heroku app's dashboard) and click on **Run Console**.
    - In the console, run the following commands to apply migrations and set up the database:
      ```bash
      python3 manage.py migrate
      python3 manage.py createsuperuser  # Optional, to create an admin user
      ```
11. If you have any initial data to load into the database (e.g., categories or product information), you can use:
    ```bash
    python3 manage.py loaddata <fixture_name>
    ```

The app is now live in Heroku.

## Issues/Bugs

### Resolved

- **No products appearing when category was clicked**

  This happened because the category name was being capitalised by the `|title` filter before being entered as a query, rather than before being displayed in the HTML. This was an easy fix.

- **New items in Product Management with no options (e.g. colours) not being accepted**

  The way in which I had defined `clean_options` led to a 500 error if there were no options added.

  ![Product Management Error - Before](/media/readme-images/bug_product_management_before.png)

  By simply addressing the case where there were no options in the code and returning nothing, this error was quickly fixed.

  ![Product Management Error - After](/media/readme-images/bug_product_management_after.png)

- **Some URLs unexpectedly returning 404 errors**

  Whilst testing the site, some urls unexpectedly returned 404 errors, even `/admin`. I read the error logs and realised that the issue was that earlier, I had set `APPEND_SLASH = False`. Return this to `True` fixed this. 

- **Error when incorporating the Ratings model**

  Once I had created and migrated the ratings model, I was having issues whenever it was being called in `views.py`:

  ![Avg Error - Before](/media/readme-images/bug_product_management_before.png)

  This was due to it using `Avg` from `django.db.models`, which had not been imported. Adding it to the initial imports quickly fixed that.

  ![Product Management Error - After](/media/readme-images/bug_product_management_after.png)

### Unresolved

There are no unresolved bugs. However, there are new features and expansions of current features that I feel are worth mentioning. [These can be found in Future Improvements/Developments](#future-improvementsdevelopments). 

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