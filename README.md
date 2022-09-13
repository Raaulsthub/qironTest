# Creating a BOT using AWS Lex

This document shows how to create a AWS Lex BOT, this service will be integrated to Qiron robots soon.

## What is Lex 

Amazon Lex is a service used to build talking interfaces in any kind of application using voice and text. The service is used to feed Amazon Alexa, for example. This will be integrated to Qiron Robots due to it's capabilities and ease to administrate complex tasks and converstations.

## How does it Work

A bot is built to fulfill a to be chosen quantity of intents. An intent is basically what the user want's the bot to answer or to perform. The Natural Lenguage Processing algorythims provided by amazon will work on recognizing an intent from a user input. For that to happen, we need to provide sample utterances for that intent, that is, sentences that will likely be used by the user on that intent, with a reasonable number of samples, the bot will be very precise on identifing an intent.

The conversation between a bot and a user is preprogrammed. First, each intent can have slots (optional), that is, information necessary to fulfill an intent. For example, if we want the bot to calculate a persons Body mass index (BMI), the user would need to provide basic information like the persons age, height and weight, those tree will be the slots.

It all starts with a user input that represents the intent, "Beo, calculate a person IMC" for example. This will be sent to the bot on a .json formated file. The bot will recognize the intent, and will notice that there are missing information (slots). It will answer with a output asking for this information (this is also a .json, pre-programmed). The user will answer the information, if the information makes sense, the bot will search for another missing information. If the information provided is not possible, the bot will ask for it again. When all slots are filled, the Bot enters the fulfillment state. Basically, this fulfillment state will be used to do a task the user asked, or just finishing the conversation. The fulfillment can be hooked with and Amazon Lambda Function, wich is a code that runs on the cloud. Documentation on AWS lambda can be found <a href="https://aws.amazon.com/pt/lambda/">here</a>.

## Creating an account on Amazon AWS Services
First of all, you will need to register on AWS Services Console, wich can be found <a href="https://aws.amazon.com/pt/console/" target="_blank">here</a>.

AWS services recommend to not use your root account (the one you registered with), to improve the security of your projects, it is wise to use IAM users, the documentation for those can be found <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users.html">here</a>. This is also used when creating and communicating with bots by command line, wich will not be covered in this file, but it might be important for the ROS/Lex integration.

## Creating the BOT

### First of all, we will be logging to the <a> Lex Console </a> and changing it to the old version. This can be done in the upper left region of the initial page.

![image](https://user-images.githubusercontent.com/85199336/189988423-2b153f1a-d74f-4ceb-92ac-7a119ad5c864.png)

### Then, we will select the create button on the bots section

![image](https://user-images.githubusercontent.com/85199336/189989186-73424d62-0467-439a-99d0-1359cc0ded98.png)

### Fill the basic information

![image](https://user-images.githubusercontent.com/85199336/189990093-56e758d0-e760-4d28-aefb-9cabdce3fe1d.png)

### With the BOT created, we are ready to create our first intent

![image](https://user-images.githubusercontent.com/85199336/189990511-df502122-ad0f-4a16-9174-30628ec23533.png)





