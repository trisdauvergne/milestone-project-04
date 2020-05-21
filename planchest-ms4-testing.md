![MUSIC site logo]()

# Manual testing of 'Plan Chest' website

## Testing
- HTML validated using [W3C Validator](https://validator.w3.org/)
- CSS validated using [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
- Python validated using [Pep8 Online](http://pep8online.com/) 
- JS validated using [JSHint](https://jshint.com/)

## Testing client stories from the UX section of [Milestone Project 2 Readme](milestone-project-2-readme.md)

1. _"I'm a print designer and currently only work directly for clients. I've got lots of work that I've done in my free time and **I want to register on 'Plan Chest' and upload work to sell** so I can hopefully earn some extra money.”_

- The user can fulfill their mission in 3 steps to show Jax Jones's most popular songs: _Search for artist name, click on artist name, view song results_
- [User journey screenshots here](https://github.com/trisdauvergne/milestone-project-02/blob/master/assets/readme-assets/user-stories/user-story-1.jpeg)



2. _“I'm registered as a designer on 'Plan Chest' and have uploaded some of my work on to the site. **I want to charge more so want to edit the price**”_

- The user can easily fulfill the first part of their mission in 3 steps: _Search for artist name, click on artist name, view song results_
- To fulfill the second part of their mission, they need to add 2 more steps: _Click on song title, click play in audio source_
- [User journey screenshots here](https://github.com/trisdauvergne/milestone-project-02/blob/master/assets/readme-assets/user-stories/user-story-2.jpeg)



3. _“I'm a designer and need to buy some print for a new collection. I have no idea who I want to work with so **I want to do a bit of exploration before making a decision**.”_

- The user can easily fulfill their mission in 5 steps: _Search for artist name, click on artist name, view song results, click on song title, click play in audio source_
- [User journey screenshots here](https://github.com/trisdauvergne/milestone-project-02/blob/master/assets/readme-assets/user-stories/user-story-3.jpeg)



4. _“I've purchased lots of prints from 'Plan Chest' but can't remember which one I ordered in March as I want to buy from that designer again. **I need to look through my order history so I can find the details of the print**.”_

- The user can easily fulfill their mission in 3 steps (which would need to be repeated for different artists): _Search for artist name, click on artist name, view song results_ (the user could now potentially see the song title in this list)
- The user may need to take 2 additional steps to listen to the songs to jog their memory (these steps may need to be repeated for different artists): _Click on song title, click play in audio source_
- [User journey screenshots here](https://github.com/trisdauvergne/milestone-project-02/blob/master/assets/readme-assets/user-stories/user-story-4.jpeg)



5. _“**I work for a design company and want to buy a print, but want to create an account first**.”_

- The user can easily fulfill their mission in 3 steps (which would need to be repeated for different artists): _Search for artist name, click on artist name, view song results_ (the user could now potentially see the song title in this list)
- The user may need to take 2 additional steps to listen to the songs to jog their memory (these steps may need to be repeated for different artists): _Click on song title, click play in audio source_
- [User journey screenshots here](https://github.com/trisdauvergne/milestone-project-02/blob/master/assets/readme-assets/user-stories/user-story-4.jpeg)



6. _“I'm a print designer and am stuck for ideas. **I want to see other print design work that will hopefully give me some inspiration**. I don't want to join 'Plan Chest' as I don't have any plans of buying or selling anything.”_

- The user can easily fulfill their mission in 3 steps (which would need to be repeated for different artists): _Search for artist name, click on artist name, view song results_ (the user could now potentially see the song title in this list)
- The user may need to take 2 additional steps to listen to the songs to jog their memory (these steps may need to be repeated for different artists): _Click on song title, click play in audio source_
- [User journey screenshots here](https://github.com/trisdauvergne/milestone-project-02/blob/master/assets/readme-assets/user-stories/user-story-4.jpeg)



7. _“**I need to buy a design for a collection my company is designing. I'm a business so will need to print the order confirmation with all the price details on it**.”_

- The user can easily fulfill their mission in 3 steps (which would need to be repeated for different artists): _Search for artist name, click on artist name, view song results_ (the user could now potentially see the song title in this list)
- The user may need to take 2 additional steps to listen to the songs to jog their memory (these steps may need to be repeated for different artists): _Click on song title, click play in audio source_
- [User journey screenshots here](https://github.com/trisdauvergne/milestone-project-02/blob/master/assets/readme-assets/user-stories/user-story-4.jpeg)



8. _“Someone has bought a print from me and wants to use it exclusively. **I need to stop selling that print on 'Plan Chest' so need to delete it**.”_

- The user can easily fulfill their mission in 3 steps (which would need to be repeated for different artists): _Search for artist name, click on artist name, view song results_ (the user could now potentially see the song title in this list)
- The user may need to take 2 additional steps to listen to the songs to jog their memory (these steps may need to be repeated for different artists): _Click on song title, click play in audio source_
- [User journey screenshots here](https://github.com/trisdauvergne/milestone-project-02/blob/master/assets/readme-assets/user-stories/user-story-4.jpeg)


## Manual (logical) testing of all elements and functionality on every page.

### Permanently visible elemennts
1. **Navigation Bar** 
- Open the page and see that the navigation bar is visible on all screen sizes and always at the top of the screen
- Reduce the screen size to check navigation bar slightly in size

2. **Designers**
- Click on the 'Designers' button in the navigation bar to check it loads the 'all designers' page that shows all designers' names

3. **Prints**
- Click on the 'Prints' button in the navigation bar to check it loads the page showing prints

4. **Register**
- Click on the 'Register' button in the navigation bar to check it loads the registration page

5. **Footer**
- Check that the footer is always at the bottom of the screen
- Visit different pages within the site to check it's beneath the content on the screen
- Scroll up and down to see that there is a slight gradient behind the footer which content sits behind

6. **Email address**
- Click on the email address in the bottom right hand corner and check that it opens a new email window
- Reduce the screen size to check that the email address always sits in the bottom right hand corner

7. **Logo**
- Click on the 'Plan Chest' logo in the top right hand corner and check that it returns you to the home page
- Reduce the screen size to check the logo remains in the top right hand corner
- Visit other pages on the site and click on the logo to ensure it works across every page

8. **Hamburger icon**
- Reduce screen size to check that menu items in navigation bar condense into collapsible icon
- Click on the collapsible icon to expand the menu and click on it again to collapse the menu
- Scroll up and down to check that there is a gradient behind the navigation bar 
- Reduce screen size, click on the collapsible hamburger icon and click on 'Designers' in the dropdown to check that it loads the 'all designers' page showing all the designers' names
- Reduce screen size, click on the collapsible hamburger icon and click on 'Register' in the dropdown to check that it loads the registration page and from

### Login system
1. **Login**
- Click on login
- Check that the registration form loads and is offset with a blank column to the left
- Check that this column disappears on a small screen
- Check that the form is centred on a small screen
- Enter only an email address and password (without a username) into the form, then press submit to check that the form won't submit without the fields being submitted
- Check that a **success message** appears in the corner confirming that a confirmation has been sent
- Check that a **verification email** is sent to the provided email address
- Try to register again with a different email address but same username to check that duplicate usernames aren't allowed on the site
- Try to register again with the same address but different username to check that the same email can't be used on the site
- Click the Submit button to check it redirects to the page saying an email has been sent
- Verify your email address and check that a **success message** appears when you have logged in with the correct username 

2. **Logout**
- Whilst logged in, check that the login button in the navigation bar is not visible but the 'Logout' button has appeared
- Reduce screen size to check that the 'Logout' button is contained in the collapsible menu
- Click on the 'Logout' button to check that it takes you to the sign out page
- Click the 'Sign Out' button and check that 'Login' now reappears in the navigation bar
- Check that a **success message** appears confirming you have been signed out

### Homepage
1. **Introduction**
- Check that the introduction loads on the page and is offset with a blank column to the left
- Reduce the screen size to check that the column disappears on a small screen

2. **Register link**
- Whilst logged out, click on the 'registering as a designer' link in the body copy to check it takes you to the sign up page

3. **Register as designer or customer**
- Repeat the registration process but tick 'register as designer' 
- When logged into the page, check that 'Add work' is visible in the navigation bar
- Go into 'Your profile' on the navigation bar and update your profile by checking 'register as customer' to check that 'Add work' is no longer visible 

### 'Designers' pages
1. **Designers names** 
- Click on the button 'Designers' in the navigation bar and check it loads the page showing the designers' on Plan Chest
- Check that the page loads and is offset with a blank column to the left
- Reduce the screen size to check that the column disappears on a small screen 
- Click on a name in the list and check it goes to the correct designer's page

2. **Designer detail page**
- Check that the correct designer's page has showed up
- Check that the content loads and is offset with a blank column to the left
- Reduce the screen size to check that the column disappears on a small screen 
- If the designer has uploaded images, check they sit beneath the text on a small screen
- Check that the designer's first name and last name are displayed as a heading with a short bio and country code beneath with email beneath the country
- Click on the **designer's email** address to check it loads in a new window
- Click on the 'Back to designers' button to check it goes back to the list of names
- Click on one of the **designer's prints** to check that it takes you to a **print detail** page
- Click on the **see more** button to check this also loads the **print detail** page

### 'Prints' pages
1. **All prints page**
- Click on 'Prints' in the navigation bar and check it takes you to the page displaying all prints on Plan Chest
- Check the images load in rows on a desktop
- Shrink the screen size to check that the images stack in rows of 2 on a tablet and single rows on a mobile
- Click on a print to check it takes you to the **print detail** page
- Click on **see more** underneath the print to check that it also takes you to the **print detail** page

2. **Arrange prints by designer**
- From the all prints page, click on **'Arrange prints by designer'** underneath the heading and check this takes you to a new page which shows the designers' names with rows of prints beneath the name
- Shrink the screen size to check that the images stack in rows of 2 on a tablet and single rows on a mobile
- Click on a designer's name to check it takes you to the **designer detail** page with further information about that designer and all of their prints
- On the prints by designer page, click on an image of a print and check it takes you to the **print detail** page
- Click on **see more** underneath the print information and check it takes you to the **print detail** page

3. **View prints by price**
- On either of the prints pages, click on **View prints by ascending price** to check it 
loads a page with all prints now arranged by price, from the lowest price to highest price
- Check the images load in rows on a desktop
- Shrink the screen size to check that the images stack in rows of 2 on a tablet and single rows on a mobile
- Click on **see more** underneath the print to check that it also takes you to the **print detail** page

4. **Print details**
- Click on a print to check it loads a page focusing on that print with a large preview of the print in the center with an empty column to the left. The image should sit underneath the print's title with smaller information to the right hand side 
- There will be a button to **see more of the designer's work** of the artist's work, click on that to check it goes back to the correct designer's page
- Click on the **back to all prints** button to check it goes back to the all prints page
- Click on **Add to bag** to check that the 'Bag' button appears in the navigation bar with a quantity for the number of prints added to the bag
- Type a number over 99 into the quantity box and press add to check that a maximum of 99 can be added to the box
- Type 0 into the box to check that a number higher than 1 has to be added
- Press the '-' and '+' icons to **adjust the quantity** and to check that the number in the quantity box is updated 
- Whilst logged in as a designer, upload a sample of work. Navigate to the **print detail** page for the print just uploaded and check that the **edit the print** and **delete print** buttons have appeared
- Check that the **Add to bag** and **adjust quantity** buttons aren't visible on this page
- Check that the items stack on a screen smaller than a tablet size
- Click on **edit the print** to check it takes you to the upload form where you can update the information. Leave one field purposely blank to check that the form can't be submitted without all fields having an input
- Try to input over 254 characters into the description as well as the title to check the character limit works
- Try to insert a character into the price to check that the decimals field works
- Try to upload a file forma
- On the **print detail** page, click on the **delete print** button to check that it removes a print

### 'Your Profle' page
1. **Your Profile**
- Whilst logged in, click on 'Your profile' in the navigation bar
- Check that the page loads with a form that is prepopulated with username and email address
- If you have populated the additional fields already, first name, last name and a bio should also be populated
- Change the details and press **Submit** to check that your data is updated
- Try to select 'Country' in the country field and submit to check that a country is required
- Try to leave any of the fields blank to check that all fields are required (other than register as designer and register as customer)
 
###  'Add Work' page
1. **Add work**
- Whilst logged in and after having registered as a designer, check that the **'Add work'** button is visible in the navigation bar
- Click on the **submit** button to check that a page with a form loads
- Try to submit the form and leave fields blank to check that the form requires all fields to have a value
- Try to upload a non-image format file in the image field to check that only image formats are allowed
- Click **submit** and go to the **all prints** page to check that the print has been uploaded to the database
- Click on the print to go to the print details page and check that all data has been uploaded

### 'Bag' page
1. **Bag** 
- Whilst logged in, add a print to the bag to ensure that the bag is visible in the navigation bar
- Click on the bag to load the page and check that it loads with a preview, the title of the print and a link to the designer's **designer detail** page, the price x actual quantity in the bag as well as the **update quantity** and **remove items** buttons
- Reduce the screen size to check that the order summary remains in a row with all elements stacked beneath it on a smaller screen 
- Press the plus icon to try get a value over 99 to check the max value is working
- Update the quantity to 0 to check this removes the item from the bag
- Press the remove item button to check this also removes items from the bag
- Click on **keep shopping** to check that it takes you back to the all prints page
- On the bag page, click on **checkout securely** to check that it takes you to the checkout page
- Logout and add a print to the bag to check that the **checkout securely** and **keep shopping** buttons aren't visible but a message reminding users to register is visible

### 'Checkout' page
1. **Checkout**
- Whilst logged in, check that the checkout page loads when the **checkout securely** button is pressed while in the bag page
- Check that order summary is displayed at the top
- Check that when images are responsive in a smaller screen and that all elements stack above the checkout form below
- Fill out the form but leave one of the fields blank to check the form can't be submitted without all fields 
- Enter an insufficient number of card digits in the payment input and press **complete order** to check that card details are being checked
- Use Stripe test card details to confirm an order: Number - 4242424242424242, CVC - 424, Date - Any future date 
- Check that a **success message** appears when the order has gone through
- Check the details in the success message match with the data that was input into the checkout form
- Check that a spinner appears while the payment is processing
- Check that the **checkout success** page has loaded after the purchase has been made
- Check that an email has been sent to the email address provided when completing the purchase
- Check that the email features the correct name, the order number is consistent with the order number in the **checkout success** message and the order summary and shipping details are correct

2. **Checkout success**
- Check that you are redirected automatically to this page after a purchase has been completed
- Check responsiveness and that the column to the left disappears on a small screen
- Check that the details in the order summary match the purchase that was made
- Check that the **success message** uses the correct email address provided in the form
- Click on the **Look at some more prints** button to check it takes you back to the all prints page

### 'Order History' page
- After an order has been made and whilst logged in as the same user who placed the order, click on the 'Order history' button in the navigation bar
- Check that your order has appeared on the page and that the order date and time shows up with a black underline as an **order details button**
- Click on the button to check that this expands with a brief order summary
- Click on the button again to check that this collapses and only displays the order date again

## Further testing:

1. Asked fellow students to look at the site and report any issues they encountered. Issues spotted include:
- No error message when unknown bands were searched for (NOTE:_This feature was added after this feedback was received_)
- Found issue when trying to play songs which have an apostrophe in the title (_NOTE: Realised that any apostrophes in song titles in the template literal onclick function caused the string to prematurely end, so had to replace apostrophes with '&apos' instead_)
2. Asked friends and family to test the site for ease of use
3. The website has been viewed on different browsers, no issues were found 

## Bugs and problems

1. Users can currently register as designer and customer.