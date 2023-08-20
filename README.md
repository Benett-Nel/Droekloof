
## How to run project:
In the terminal in the base folder called droekloof, run `dar\scripts\activate` to activate the virtual environment
Next `cd backend`
now `python manage.py runserver` to start up the backend server.

With the backend server left running, open a new terminal.
In this terminal you will start the frontend.
In the new terminal in the base directory:
`cd frontend`
Then `yarn start` 
This will start up the development server at localhost:3000

## Disictiveness and Complexity

This project is clearly distinct from the previous projects in this course, it is not a social network like in project 4 and alos differs from an e-commerce website like in project 2. 

I have built a website for a guesthouse, to show their offerings, facilitate bookings and accept payments. The structure of my project is different from the other projects dealt with in the course, I made use of a react app with create-react-app and added the tailwind package for styling, the front end is created in its own folder and then I created the back end on its own with django, the third folder dar stands for "django and react", this is for the environment which is necessary to run the backend. With the front end and back end being separated, they need to communicate via an api that I created in the backend using the rest framework. This structure is more complex than the structure of loading the html pages directly from django previously dealt with in the course but it has advantages and improved security and functionality in some areas which I deemed necesarry for my project use case.

The guesthouse site displays all the offerings of the guesthouse in an effective way, making use of automatic image carousels and blocks of information alternating sides. I also made use of Parallax Layers and sticky styling to let the page snap to the start of different sections when scrolled, this aids the ease of use and look of the website. 

For styling of the website I made use of the tailwind library, this styling library allowed me to style components in the javascript itself by making use of class names, these different class names then have pre-written css styling assigned to them, I first had to get use to this library, but it improved the speed at which I styled my components greatly.

My guesthouse website also allowed users to create their own account nd book their stay on the website, including completing payment directly on the website by credit/debit card. The booking flow starts by selecting a house to rent and then selecting check in and check out dates and after confirming the dates the user is directed to the payments page. On the date selection page, I created a pop-up calendar to make it easier for the user to see which dates are available, to select their own dates with ease and decrease the chance of human input error by reducing hands-on-keyboard. The calendar component introduced complexity not previously dealt with in the course. The calendar consists of many different clickable buttons for each day on the calendar. The calendar shows the correct number of days in the month, 28, 29, 30 or 31.The component receives data from the bookings database in django and updates the calendar by making the days that have already been booked red and disabling those buttons. All days before the current date are also greyed out and disabled. The calendar is also responsive in that it highlights the day block that the mouse is currently hovering over, if a day is selected, the check in input box ias filled with the date and then the user must select a second day which is for checkout and all days before the selected check out is greyed out but not disabled, if the user clicks such a date, he is prompted to select the check in date as the check out can not be before the chek in. During the selection of the check out date the calendar uses on-hover to highlight the day over which the mouse is and all days between that day and the check in day to highlight the length of the stay. 

After valid dates are selected and confirmed, the user is directed to the payments page, here I included a payments processor api, this will allow users to enter their debit/credit card details and the guest house to accept payment directly on their own website. The payment details are saved in an encryptes token, an api call is then made to the backend and the processing of the payment is done in python making calls to the payments processor's api. If the payment is succesful, then the dates that the user selected are saved into the database and the booking is complete.


## What is contained in each file:

### Backend
There are 2 subfolders here, `backend` and `guesthouse`

-    #### backend:
        Regular django folder structure, within urls.py is and admin path and then an api path that I created with the rest framework, this allows the frontend to communicate with the backend, the empty path includes all urls in the guesthouse folder

-    #### guesthouse 
        models.py contains my django models for the database Guest - for all users, Booking - for storing bookings, and Review - for guest reviews made on the site.
        views.py contains views for creating records and reading from the database and there is also a pay view used for authorising payments.
        urls.py contains url paths to call the functions created in views.py.

### Frontend
All files worked on for the frontend is contained in the src folder, the rest of the files are for config and settings.
There are several different folders within the frontend/src forlder:

- #### assets

    - ##### data
    This folder contains information and text explanations about the different houses or activities on offer, each in their own js file. The text is read from here so that if information needs to be updated it can all be done in one place and it is not necessary to scroll through the code to get to it.

    - ##### images
    This folder contains several js files with lists of all the images to be used on different parts of the websites, this is useful to import all the images in one place and also eases updating the photos.

- #### components
    This folder contains several jsx files for react components which are used on one or more pages, they are split into their own files to make editing and error finding easier and make it possible to use the same component in more than one page.

    - arrowIcons.jsx - arrows used in the photo carousels for navigation to the next or previous photo.  
    - carousel.jsx - the physical carousel that takes a list of photos as an argument and places them in a navigateable, moving carousel.
    - navbar.jsx - the top navbar containing the name and basic navigation between some of the main pages
    - navDropdown.jsx - this component is for the mobile version of the navbar, it contains the navbar items in a popup platform that appears if the navbar burger dropdown is clicked.
    - popup.jsx - contains a component that allows other components or info to be placed inside it and can be changed to appear or dissapear according to the state of a boolean variable.
    - profileDropdown.jsx -  this contains the dropdown platform that appears when the profile icon is clicked, showing options and info regarding the user profile.
    - reviews.jsx - this component contains all the reviews, placed in divs and already rendered with styling, can be placed on any page where the reviews wants to be displayed.
    - stay.jsx - the block component which shows info of the house stay on one side and photos on the other, has props that changes on which side info is displayed. This component takes in data about the house and places it in a structured pre-styled block.

- #### functions
    - windowsize.jsx - this file contains fucntions for checking and returning the window size on the device / browser being use. This is used to adjust components for mobile reactiveness.

- #### pages
    This folder contains several jsx files for all of the pages in the website.

    - activities.jsx - this page displays all the activities available on the guesthouse farm in component simmilar to the one displaying the different houses.
    - bookdate.jsx - this is the page allowing the user to pick a date for their stay, containing the pop-up calendar.
    - checkout.jsx - contains block with summary of booking details and price and pop-up allowing user to make payment for their booking. Call to backend payment api is made from here
    - home.jsx - this is the home page, making use of the stay component to display all houses and it has a big front page photo carousel, also making use of review component to show reviews at the bottom.
    - noMatch.jsx - This page shows a message that the requested page was not found, in case an invalid page url was requested or a page has been removed.
    - signup.jsx - This page contains form and input boxes allowing the user to input their personal details and create a user account, this page is used for registration and login, accepting a parameter to show or hide certain boxes as necessary.
    - staySelect.jsx - This page is shown when the user clicks on Book now in the navbar, it shows more detail about all three houses with photos in platforms next to eachother to be compared and then the user picks one of the stays before being directed to the date selection page. On this page the photo carousels are set to not switch photos automatically.
    - thanks.jsx - Basic page showing a thank you message to confirm with the user that their booking is complete and has a button to redirect to the view bookings page.
    - viewbookings.jsx - Page showing a summary of all the users current and upcoming bookings which have been confirmed and paid on platforms.

- #### App.jsx
    This file contains an app component with the navbar at the top and space at the bottom, in which all other pages and components are to be rendered, where all the routes of the website are declared with their respective page components inside the route components, rendering based on the url.

- #### index.css 
    This file contains some personal styling classes that I wanted to separate from the js code or reuse the exact styling in some components. It also contains styling class for an input component that I copied from stack overflow (cited in the code comments).
