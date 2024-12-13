# RoadHouse BJJ



## Introduction
Welcome to my opensourcenews project. This project incorporates all aspect of full stack development as is a fully functioning news website.

You can access the page live via github pages on the url below.
https://mickjitsu.github.io/roadhouse_BJJ/

![Responsive image](assets/documentation/responsive_image.png)


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


![Wireframe for top of index page](opensourcenews/documentation/homepage-top.png)
![Wireframe for bottom of index page](opensourcenews/documentation/homepage-bottom.png)
![Wireframe for categories page](opensourcenews/documentation/categories.png)
![Wireframe for article page](opensourcenews/documentation/article.png)


## Features

### Responsive Navigation Bar toggle
This code was the base code from bootstraps website allowing for a responsive navbar with a dropdown menu for categories.

![nav bar toggle](opensourcenews/documentation/nav.png)


### Comment section
Comment sections on articles which allow for users to create, edit and delete their own comments as well as upvote/downvote others.
![Comments](opensourcenews/documentation/comment.png)


### Footer with working social mediahyperlinks
Basic footer with social media links that direct to the social media site hompages


### Working category dropdown lists that direct to new webpage

![hyperlink to contact form](opensourcenews/documentation/dropdown.png)


### Working pagination 

![contact form](opensourcenews/documentation/pagination.png)



### Working 404 page.
![404 page](opensourcenews/documentation/404.png)

### Article validation.
Validation to ensure that a new article is published (If not, then it is a draft and won't be shown), along with options to choose whether it should also be a headline in it's respected category or if it is a breaking news story that should be front and centre of the index page. Breaking news stories should be approved by the site owner before updating.
![Article Validation](opensourcenews/documentation/articlevalidation.png)



## Features to be Added
We are currently working on a feature for a dedicated UI for journalists. This will allow journalists to log on to the website directly and have their own dedicated page only visible to them, which contains their current posts and drafts, and will allow for them to edit/delete posts.

We will also enable a registration option for new users to request to become a journalist, which will require approval from an admin before continuing.


## Testing

### Validation of Code
Index w3 validator
Due to the use of django, w3 validator was not used in this project

CSS Validator

Base html CSS
![CSS validator pass](opensourcenews/documentation/basecss.png)

Index html CSS
![CSS validator pass](opensourcenews/documentation/indexcss.png)



### Lighthouse
Lighthouse results, due to the nature of django projects and the dynamic use of images and URLs, many of the elements did not pass however accessibility and SEO maintained a very high rating.

![Lighthouse results for index page](opensourcenews/documentation/seo.png)
![Lighthouse results for index page](opensourcenews/documentation/accessibility.png)


Common issue seems to be with image size and type used for mobile versions of the website.

### Wave Webaim - accessibility testing
Initially there was one error due to the label tag used for the nav toggle. More information on bug section.
![Accessibility testing review from Wave](assets/documentation/wave_response.jpg)


### Manual Testing

Here I have tested all the features on each and every page of my website. Please see the results below.

Our goals were met in this testing as all pages are directly accessible and easy to find for the user, with clear descriptions where to find certain information along with an acknowledgement when a contact form is sent.

This was tested using a google pixel 6 pro, iphone 11 and responsive mode on a large PC monitor.

Format of the table below is as follows:

| Feature being tested| Expected Outcome | Testing Performed | Actual Outcome | Result (Pass or fail) |
| -------------------- | ---------------- | ----------------- | -------------- | --------------------- |
| Header hyperlink index page| Refreshes current page | manually clicked | page refreshed | Result PASS|
| Header hyperlink about page | directs to index page | manually clicked| directed to index page | Result PASS |
| Header hyperlink gallery page | Directs to Index page | manually clicked | Directed to index page | Result PASS |
| Header hyperlink contact page | directs to index page | manually clicked | directed to index page | result PASS |
| Facebook hyperlink on index page| direct to social media sites | manually clicked all | All directed | Result PASS |
| Youtube hyperlink on index page| direct to social media sites | manually clicked all | All directed | Result PASS |
| Instagram hyperlink on index page| direct to social media sites | manually clicked all | All directed | Result PASS |
| Twitter hyperlink on index page| direct to social media sites | manually clicked all | All directed | Result PASS |
| Facebook hyperlink on about page| direct to social media sites  | manually clicked | All Directed | Results PASS |
| Youtube hyperlink on about page| direct to social media sites  | manually clicked | All Directed | Results PASS |
| Instagram hyperlink on about page| direct to social media sites  | manually clicked | All Directed | Results PASS |
| Twitter hyperlink on about page| direct to social media sites  | manually clicked | All Directed | Results PASS |
| Facebook hyperlink on Gallery page| direct to social media sites | manually clicked| All Directed  | Result PASS |
| Youtube hyperlink on Gallery page| direct to social media sites | manually clicked| All Directed  | Result PASS |
| Instagram hyperlink on Gallery page| direct to social media sites | manually clicked| All Directed  | Result PASS |
| Twitter hyperlink on Gallery page| direct to social media sites | manually clicked| All Directed  | Result PASS |
| Facebook hyperlink on contact page| direct to social media sites  | manually clicked | All Directed | Reult PASS |
| Youtube hyperlink on contact page| direct to social media sites  | manually clicked | All Directed | Reult PASS |
| Instagram hyperlink on contact page| direct to social media sites  | manually clicked | All Directed | Reult PASS |
| Twitter hyperlink on contact page| direct to social media sites  | manually clicked | All Directed | Reult PASS |
| Facebook hyperlink on signed-up page| direct to social media sites  | manually clicked | All Directed | Reult PASS |
| Youtube hyperlink on signed-up page| direct to social media sites  | manually clicked | All Directed | Reult PASS |
| Instagram hyperlink on signed-up page| direct to social media sites  | manually clicked | All Directed | Reult PASS |
| Twitter hyperlink on signed-up page| direct to social media sites  | manually clicked | All Directed | Reult PASS |
| Facebook hyperlink on 404 page| direct to social media sites  | manually clicked | All Directed | Reult PASS |
| Youtube hyperlink on 404 page| direct to social media sites  | manually clicked | All Directed | Reult PASS |
| Instagram hyperlink on 404 page| direct to social media sites  | manually clicked | All Directed | Reult PASS |
| Twitter hyperlink on 404 page| direct to social media sites  | manually clicked | All Directed | Reult PASS |
| Dropdown toggle index page| menu drops down and hyperlinks work | manually clicked | menu appears | Result PASS |
| Dropdown toggle about page | menu drops down and hyperlinks work | manually clicked  | menu appears  | Result PASS |
| Dropdown toggle Gallery page| menu drops down and hyperlinks work| manually clicked | menu appears  | Result PASS |
| Dropdown toggle contact page | menu drops down and hyperlinks work| manually clicked  | menu appears | Result PASS  |
| Youtube video about page| Video plays but not automatically | opened about page and clicked play | video only plays when clicked | Result PASS |
| contact form submission required fields | Can't submit form unless all requried fields are checked| Tested every combination | Required fields prompted if not submitted correctly | result PASS |
| contact form submission| redirected to thank you page | completed form and submitted | redireted to signedup.html | Result PASS |



## Bug resolutions

When writing the html and CSS code for this website, some bugs were found and rectified along the way.

A major bug was the stretching of the Hero image on the index.html page. Due to the size of the image being used, on large screens this image would become stretched and off centre.

To fix this, I used a larger version of the same image (900x) and updated the CSS in a media query for screens of 900px and more to use this image, and update the positional values of the image. The CSS used to overcome this bug is shown below.


![Media query to fix hero image bug](assets/documentation/bug_1.jpg)

Another bug that was found was on the contact form. The contact form page would submit regardless of whether any class choices or contact information was added or not. This was due to the HTML code for the form not containing a required field. This was amended upon finding the issue when conducting manual testing.

When validating the page using wave, a bug was found due to the label tag being empty in the form that was used to create the navigation toggle as it was done purely using html and css. This was fixed due to help from the documentation below.
https://css-tricks.com/inclusively-hidden/


![CSS code used for this fix](assets/documentation/bug_2.jpg)

The final bug noticed when creating this website was that the schedule listed in the about page shows as pixelated when testing the responsiveness for smaller screens. This has been tested using 3 different mobile devices however and the image does not appear pixelated, and can be viewed/zoomed in as most images of this type would be on a mobile device.


## Technologies Used

This project was done solely using HTML and CSS, along with vs code and gitpod.


**Cloning the repository**

To clone the repository, you'll need Git installed on your computer. I

Open your terminal or command prompt.
Navigate to the directory where you want to clone the repository.
Run the clone command:

**Forking the repository**

To Fork this repository and have a version of this on your personal account to make changes, customisation and amendments, please do the following.

Go to the GitHub page of the repository : https://github.com/Mickjitsu/roadhouse_BJJ
Click on the "Fork" button, usually found at the top-right corner of the page.

After forking, you will have a copy of the repository in your GitHub account. You can then clone your forked version to your local machine by following the "Cloning the Repository" steps, using the URL of your fork.

To view the repository on the local machine:

1. Navigate to the Project Directory: : cd /roadhouse_BJJ

2. Open the Website: Open the main index.html page in a browser or the folder in a code editory


## Deployment

**Deploying on Github Pages**
Firstly clone or fork the repository following the steps above. Once that is done, you will need to set up GitHub Pages. To do this:
 In your repository, navigate to the "Settings" tab.
   - Click on the "Pages" section on the left sidebar.
   - Under the "Source" section, select the branch you want to deploy from (usually `main` or `master`) and click "Save".
   - GitHub will provide you with a link to your live site.


## Credits

The images of this site came from pexels.com , sherdog.com, bjjfanactics.com and fittinsider.com.

The video came from the grappling academys youtube channel. The schedule was created using Abode.com free schedule maker

## Acknowledgements
I would like to thank my partner for encouraging me to continue on when I was struggling at the start of the course, my family for encouraging me to keep studying despite going through a bereavement, and my mentor Matt for helping me along the way with pre, mid point and final calls!

[Back to top](#introduction)