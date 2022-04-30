# The more you help people learn, improve, and achieve new heights in their lives, the more you contribute to the Educational World.

![Group 23](https://user-images.githubusercontent.com/78098329/165950326-db000636-8243-491a-852c-036c5d5c3807.svg)

## Inspiration

- Nowadays, as a result of a lack of exposure to communication skills in youth, many individuals struggle with a lack of confidence and develop various phobias such as glossophobia and social phobia. 
- We could solve this problem by providing them with a platform where they could practice and sharpen their communication skills. 
- This application would allow them to practice their communication skills without anyone's interference and without feeling shy. 
- The application could be very helpful to students from rural areas or anyone who wishes to improve his/her communication skills. 
- This application could be useful for interview preparation, as facial emotions and pitch emotions are crucial in interviews. They should be in sync. These emotions are very important in cracking an interview. Our application could enhance those skills.

## What it does

- This application analyzes the facial expression of users with voice modulation and checks whether they are perfectly in sync with each other or not.
- Based on that, then it will generate a report which gives feedback to the user based on his communication skills. 
- To make this application more user-friendly we have created an interactive website where users can use this functionality very easily. 
- We provide frequent feedback so that users can interpret the results appropriately and try to improve their communication skills over time.

## How we built it

- Using CNN, we have trained a facial expression recognition model on the FER-2013 dataset, which uses the input of human faces to predict emotions based on facial expressions.
- LSTM is used to build a model that detects emotion from voice modulation. To train the model we used the Toronto emotional speech set (TESS).
- We are taking input from users' webcams and microphones and checking whether both of them are in sync with each other. 
- It generates a report containing feedback to the user, along with suggestions for improvement.


## Challenges we ran into

- It was a bit difficult to run two machine learning models simultaneously in real-time.
- Creating a robust machine learning algorithm that can be used in real-time is another challenging task.
- It was pretty challenging to integrate the models in the website with a user interface with the capability of considering inputs from the users and then displaying the results after processing those inputs.

## Accomplishments that we're proud of
- We are proud that we were able to capture audio and video and process them simultaneously. 
- This project has helped us to learn GitHub and apply that knowledge on a Professional level. We were able to build this application in 48 hours which was challenging but it makes us proud to have a look at what we have developed. 
- The most important thing for us is that students will be able to use our application and improve their verbal and nonverbal communication skills.

## What we learned

- Applying CNN and LSTM to real-life problems. 
- Basics of Image and Audio processing and their applications. 
- Implementation of two Deep Learning algorithms simultaneously in the real-time software application.
- Deployment of models using flask on web applications 
- Embedding the OpenCV window in the web page in real-time 

## What's next for Communication buddy

- Here in this application, we planning to bring a functionality like a user can give his sentence and we could be - suggesting him better vocabulary which would make him stand out from the rest of the crowd.
- We also have plans to add some features like text to emotion detection for premium members and prepare a mobile application for Communication Buddy. 
- One of the main functionalities that we will be trying to integrate is the identification of the body language of the user.
- The way in which a person appears while conversing with another person matters to create a good impression since not only the way in which we talk is important but how we communicate is also one of the most essential factors. 
- The motive will be to detect the body language of the user and accordingly provide feedback.
