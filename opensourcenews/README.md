# Open Source News - Django project



## Introduction
Welcome to my opensourcenews project. This project incorporates all aspect of full stack development as is a fully functioning news website.

You can access the page live via github pages on the url below.



## Table of Contents
- [Introduction](#introduction)
- [User Experience](#user-experience)
  - [User Stories](#user-stories)
- [Design](#design)
  - [Colour Scheme](#colour-scheme)
  - [Typography](#typography)
  - [Imagery](#imagery)
  - [Wireframes](#wireframes)
- [Features](#features)
  - [Existing Features](#existing-features)
  - [Features to be Added](#features-to-be-added)
- [Testing](#testing)
  - [Validation of Code](#validation-of-code)
  - [Manual Testing](#manual-testing)
  - [Bug resolutions](#bugs)
- [Technologies Used](#technologies-used)
- [Deployment](#deployment)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)

## User Experience
### User Stories
User Goals

- Navigature clearly and effectively across the site
- Find specific information they require
- Read news articles from our top 5 news categories
- Log in to leave / vote on comments



Site Owner Goals

- Ensure the website is seamless for the user
- Ensure the user can find exactly what they need
- Ensure news stories can be updated/edited easily and displayed on the site
- Allow for users to sign up and leave comments 
- Keep all interested parties up to date with the news


## Design
### Colour Scheme
For the website I decided to use a dark colour scheme all based of the charcoal background of the body, with different shades of a darker blue/navy for the nav bar and certain article elements on the index page. These article elements were also inverted to change upon hovering.
![contrast grid of colours](/opensourcenews/documentation/colours.png)



### Typography
I chose to stick with a sans-serif font type for the entirety of the webpage as it is very clear and easy to read for all users.
### Imagery
The imagery used on this website is all dynamic depending on what the journalist/adminstrator has decided to use for the article. Due to this, we have used a small fixed image size for smaller devices as images can be uploaded in different resolutions and create an imbalance. This way, it means that images will stay relatively around the same size and not differentiate too much.

### Wireframes
I was unable to install balsamiq wireframing tool due to restrictions on the computer I am using, so I opted for a free tool online wireframe.cc . Although it was more difficult to use and didn't allow me plan as effectively as I would have liked, I made some rough wireframes for each page.


![Wireframe for top of index page](/opensourcenews/documentation/homepage-top.png)
![Wireframe for bottom of index page](/opensourcenews/documentation/homepage-bottom.png)
![Wireframe for categories page](/opensourcenews/documentation/categories.png)
![Wireframe for article page](/opensourcenews/documentation/article.png)


## Features

### Responsive Navigation Bar toggle
This code was the base code from bootstraps website allowing for a responsive navbar with a dropdown menu for categories.

![nav bar toggle](/opensourcenews/documentation/nav.png)


### Comment section
Comment sections on articles which allow for users to create, edit and delete their own comments as well as upvote/downvote others.
![Comments](/opensourcenews/documentation/comment.png)


### Footer with working social mediahyperlinks
Basic footer with social media links that direct to the social media site hompages


### Working category dropdown lists that direct to new webpage

![hyperlink to contact form](/opensourcenews/documentation/dropdown.png)


### Working pagination 

![contact form](/opensourcenews/documentation/pagination.png)



### Working 404 page.
![404 page](/opensourcenews/documentation/404.png)

### Article validation.
Validation to ensure that a new article is published (If not, then it is a draft and won't be shown), along with options to choose whether it should also be a headline in it's respected category or if it is a breaking news story that should be front and centre of the index page. Breaking news stories should be approved by the site owner before updating.
![Article Validation](/documentation/articlevalidation.png)



## Features to be Added
We are currently working on a feature for a dedicated UI for journalists. This will allow journalists to log on to the website directly and have their own dedicated page only visible to them, which contains their current posts and drafts, and will allow for them to edit/delete posts.

We will also enable a registration option for new users to request to become a journalist, which will require approval from an admin before continuing.


## Testing

### Validation of Code
Index w3 validator
Due to the use of django, w3 validator was not used in this project

CSS Validator

Base html CSS
![CSS validator pass](/opensourcenews/documentation/basecss.png)

Index html CSS
![CSS validator pass](/opensourcenews/documentation/indexcss.png)



### Lighthouse
Lighthouse results, due to the nature of django projects and the dynamic use of images and URLs, many of the elements did not pass however accessibility and SEO maintained a very high rating.

![Lighthouse results for index page](/opensourcenews/documentation/seo.png)
![Lighthouse results for index page](/opensourcenews/documentation/accessibility.png)


Common issue seems to be with image size and type used for mobile versions of the website.

### Wave Webaim - accessibility testing
Wave testing - errors shown are due to the home link and home icon both directing to home, and the social media links only directing to the social websites and not a real profile
![Accessibility testing review from Wave](/opensourcenews/documentation/wave.png)


### Manual Testing

Here I have tested all the features on each and every page of my website. Please see the results below.

Our goals are to ensure that the website is accessible, all links work and direct as expected, and each dynamic page populates correctly with correllated data from the database.

This was tested using a google pixel 6 pro, iphone 11 and a macbook.

Format of the table below is as follows:

| Feature being tested| Expected Outcome | Testing Performed | Actual Outcome | Result (Pass or fail) |
| -------------------- | ---------------- | ----------------- | -------------- | --------------------- |
| Header hyperlink index page| Refreshes current page | manually clicked | page refreshed | Result PASS|
| Categories NAV button | Provides dropdown list of categories | manually clicked | list shown and accessible | Result PASS|
| Login NAV button | Directs to login page | manually clicked | directed to page | Result PASS|
| Logout NAV button | Directs to logout page | manually clicked | directed to page | Result PASS|
| Register NAV button | Directs to register page | manually clicked | directed to page | Result PASS|
| Signup/Register | Can sign up via UI | manually signed up| account created | Result PASS|
| Breaking news | Only breaking articles show on homepage | manually selected this toggle for numeropus articles | only the latest breaking story shown | Result PASS|
| Homepage categories | articles associated to the correct category shown | checked category of each article | all are correctly correllated | Result PASS|
| Headline articles | Only articles with headline toggled show as headline | manually checked each headline article | all shown have correct setting | Result PASS|
| Comment | Ability to comment when logged in | manually logged on and commented | comment added correctly | Result PASS|
| Comment EDIT | Ability to edit own comment | manually tried editing own comment via UI | comment edited correctly | Result PASS|
| Comment DELETE | Able to delete my own comment | manually deleted own comment | worked as expected | Result PASS|
| Comment (Not logged in) | Ensure I can't comment when not logged in | logged out and tried numerous articles | Unable to comment | Result PASS|
| Comment (EDIT when not logged in) | Ensure I can't edit others comments | logged out and tried numerous comments | Unable to edit others comments | Result PASS|
| Comment (DELETE when not logged in) | Ensure I can't delete others comments | logged out and tried numerous comments | Unable to delete others comments | Result PASS|
| Comment UPVOTE | Ensure I can upvote a comment | upvoted numerous comments | votes counted correctly | Result PASS|
| Comment DOWNVOTE | Ensure I can downvote a comment | downvoted numerous comments | votes counted correctly | Result PASS|
| Images | Ensure images load correctly while using heroku | deployed with debug set to false | images hosting correctly | Result PASS|
| Article creation | Ensure only journalists can create articles | Made an article via admin page | Journalist account needs to be selected | Result PASS|






## Bug resolutions

When creating this project, I came across many bugs which proved difficult and time consuming to fix. The first of which was rendering images on the hosted application. When the application was set to Debug = True, the images would host normally however when in production and debug was set to false, this would fail to work.

To get around this, I created a bucket using AWS for storing images. This proved to be a major learning curve, with many images still failing to load even after connecting AWS to my project.

Primarily, the main issue would be that the project would not append 'media/' to the end of the aws bucker URL, even though this was clearly specified in the media URL of my project settings. After much trial and error, the best way around this I found was to move the media folders held up AWS up one level, so they were found directly at /articles/ rather than /media/articles, this allow for the urls on my website to get the correct images.


## Technologies Used

This project was made using HTML, CSS, Python, JavaScript, Django, AWS and Heroku.


**Cloning the repository**

To clone the repository, access the repository URL below.
https://github.com/Mickjitsu/opensourcenews/tree/main/opensourcenews

You well need to cd to the folder 'opensourcenews' within this project, and here you will be in the project directory.

As this project requires specific configurations to use, you will need to ensure that you add a Database URL and secret key to your env.py file if you plan to customise the web page. You will also need to install AWS if you plan to make the website into production.

Once you have cloned the repository, you can then add this information and launch the project with the comment 'python manage.py runserver'. Ensure to download all requirements by using the comment pip install -r requirements.txt.

**Forking the repository**

To Fork this repository and have a version of this on your personal account to make changes, customisation and amendments, please do the following.

Go to the GitHub page of the repository : https://github.com/Mickjitsu/opensourcenews/tree/main/opensourcenews
Click on the "Fork" button, usually found at the top-right corner of the page.

After forking, you will have a copy of the repository in your GitHub account. You can then clone your forked version to your local machine by following the "Cloning the Repository" steps, using the URL of your fork.


## Deployment

**Deploying on Heroku**
To deploy on heroku, first make sure that you have your database url and secret key added and working to your env.py file, and ensure this is functioning correctly.   Ensure to download all requirements by using the comment pip install -r requirements.txt.

Once that is done, start your heroku project with your own repository of the cloned repo. Once that is done, go to the settings of your heroku app and choose the build python, and add your DB URL and secret key to the config vars. Ensure to also add the var DISABLESTATICCOLLECT with the value 1.

When you plan to go to production and use an image hosting platform like AWS, you will also need to add your aws details as config vars here.

## Credits

The images of this site came from numerous different websites and news articles. The content of the articles came from chatGPT. The navbar came from Bootstrap documentation. Much of the styling also came from bootstrap. Database came from CodeInstitute.

## Acknowledgements
I would like to thank my partner for encouraging me to continue on when I was struggling at the start of the course, my family for encouraging me to keep studying despite going through a bereavement, and my mentor Matt for helping me along the way with pre, mid point and final calls. It has been an incredibly hard process to get here.

[Back to top](#introduction)