# Communication-Buddy

## Inspiration

Due to the lack of exposure to communication skills in youth, many people struggle with a lack of confidence and develop various phobias such as glossophobia and social phobia. We could solve this problem by providing them with a platform where they could practice and sharpen their communication skills. This application would allow them to practice their communication skills without anyone's interference and without feeling shy**. The application could be very helpful to students from rural areas or anyone who wishes to improve his or her communication skills. This application could be used for interview preparation as well as facial emotions and pitch emotions are very important there. They should be in sync. These emotions play a crucial role in you cracking an interview. Our application would help users to sharpen those skills.

## What it does

This application analyzes the facial expression of users with voice modulation and checks whether they are perfectly in sync with each other or not based on that, then it will generate a report which gives feedback to the user based on his communication skills. To make this application more user-friendly we have created an interactive website where users can use this functionality very easily. The feedback that we are providing is frequent so that users can interpret the results accordingly and try to improve his/her actions eventually.

## How we built it

We have trained a facial expression recognition model using CNN over the FER-2013 dataset. Which takes the input of human faces and predicts the emotion based on facial expressions. We also build a model which detects emotion based on voice modulation using LSTM. To train this model we have used Toronto emotional speech set (TESS) dataset. We are taking input from users' webcams and microphones and checking whether both of them are in sync with each other. Based on this it generates a report which contains feedback to the user which contains points for improvement.

## What's next for Communication buddy

Here in this application, we can bring functionality like user can give his sentence and we could be suggesting him better vocabulary which would make him stand out from the rest of the crowd. We also have plans to add some features like speech to emotion detection for premium members and prepare a mobile application for Communication Buddy. One of the main functionalities that we will be trying to integrate is the identification of the body language of the user, as the way in which a person appears while conversing with any other person matters to create a good impression since not only the way in which we talk is important but how we communicate is also one of the most essential factors. The motive will be to detect the body language of the user and accordingly provide feedback.
