# Creating a BOT using AWS Lex

This document shows how to create a AWS Lex BOT, this service will be integrated to Qiron robots soon.

## What is Lex 

Amazon Lex is a service used to build talking interfaces in any kind of application using voice and text. He is used to feed Amazon Alexa, for example. This will be integrated to Qiron Robots due to it's capabilities and ease to administrate complex tasks and converstations.

## How does it Work

A bot is built to fulfill a to be chosen quantity of intents. An intent is basically what the user want's the bot to answer or to perform. The Natural Lenguage Processing algorythims provided by amazon will work on recognizing an intent from a user input. For that to happen, we need to provide sample utterances for that intent, that is, sentences that will likely be used by the user on that intent, with a reasonable number of samples, the bot will be very precise on identifing an intent.

## Creating an account on Amazon AWS Services
First of all, you will need to register on AWS Services Console, wich can be found in <a href="https://aws.amazon.com/pt/console/" target="_blank"> AWS Console </a>.

AWS services recommend to not use your root account (the one you registered with), to improve the security of your projects, it is wise to use IAM users, the documentation for those can be found in <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users.html"> IAM Users </a>. This is also used when creating and communicating with bots by command line, wich will not be covered in this file, but it might be important for the ROS/Lex integration.
