# Creating a BOT using AWS Lex

This document shows how to create an AWS Lex BOT. This service will be integrated into Qiron robots soon.

## What is Lex 

Amazon Lex is a service used to build talking interfaces in any application using voice and text. The service is used to feed Amazon Alexa, for example. This will be integrated into Qiron Robots due to its capabilities and ease of administrating complex tasks and conversations.

## How does it Work

A bot is built to fulfill a to-be-chosen quantity of intents. An intent is basically what the user want's the bot to answer or to perform. The Natural Language Processing algorithms provided by amazon will work on recognizing an intent from user input. For that to happen, we need to provide sample utterances for that intent, that is, sentences that will likely be used by the user on that intent. With a reasonable number of samples, the bot will be very precise in identifying an intent.

The conversation between a bot and a user is preprogrammed. First, each intent can have slots (optional), that is, information necessary to fulfill an intent. For example, if we want the bot to calculate a person's Body mass index (BMI), the user would need to provide basic information like the person's age, height, and weight. Those three will be the slots.

It all starts with a user input representing the intent, "Beo, calculate a person's BMI," for example. This will be sent to the Bot on a .json formatted file. The Bot will recognize the intent and will notice that there is missing information (slots). It will answer with an output asking for this information (this is also a .json, pre-programmed). The user will answer the information. If the information makes sense, the Bot will search for other missing information. If the information provided is not possible, the Bot will ask for it again. When all slots are filled, the Bot enters the fulfillment state. Basically, this fulfillment state will be used to do a task the user asked for or just finish the conversation. The fulfillment can be hooked with an Amazon Lambda Function, which is a code that runs on the cloud. Documentation on AWS lambda can be found <a href="https://aws.amazon.com/pt/lambda/">here</a>.

## Creating an account on Amazon AWS Services
First of all, you will need to register on AWS Services Console, wich can be found <a href="https://aws.amazon.com/pt/console/" target="_blank">here</a>.

AWS services recommend not to use your root account (the one you registered with). To improve the security of your projects, it is wiser to use IAM users. The documentation for those can be found <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users.html">here</a>. This is also used when creating and communicating with bots by command line, which will not be covered in this file, but it might be important for the ROS/Lex integration.

## Creating the BOT

### First of all, we will be logging into the <a href="https://aws.amazon.com/pt/lex/"> Lex Console </a> and changing it to the old version. This can be done in the upper left region of the initial page.

![image](https://user-images.githubusercontent.com/85199336/189988423-2b153f1a-d74f-4ceb-92ac-7a119ad5c864.png)

### Then, we will select the create button on the bots section

![image](https://user-images.githubusercontent.com/85199336/189989186-73424d62-0467-439a-99d0-1359cc0ded98.png)

### Fill in the basic information

![image](https://user-images.githubusercontent.com/85199336/189990093-56e758d0-e760-4d28-aefb-9cabdce3fe1d.png)

### With the BOT created, we are ready to create our first intent

![image](https://user-images.githubusercontent.com/85199336/189990511-df502122-ad0f-4a16-9174-30628ec23533.png)


### After giving it a self-explaining name, we can fill in basic information

![image](https://user-images.githubusercontent.com/85199336/189998312-f8efd533-9f2b-47e8-b23a-d9ae7b710c72.png)

![image](https://user-images.githubusercontent.com/85199336/189998342-d29beacf-9dcf-494f-b09c-51939bc9a0bf.png)

### Build

![image](https://user-images.githubusercontent.com/85199336/189998432-184fe108-87f3-4e3d-8ffc-d33b12082d39.png)


### Test

![image](https://user-images.githubusercontent.com/85199336/189998554-2e353d93-036f-469a-962b-91c0c0dfecb9.png)


###  That's it. Your bot is now created. The next step is creating new intents and conversations, or even lambda functions to hook to your new intents fulfillment



