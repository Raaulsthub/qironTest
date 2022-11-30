# AWS REKOGNITION

## WHAT IS AWS REKOGNITION?

Amazon Rekognition makes it easy to add image and video analysis to your applications. You just provide an image or video to the Amazon Rekognition API,
and the service can identify objects, people, text, scenes, and activities. It can detect any inappropriate content as well. Amazon Rekognition also 
provides highly accurate facial analysis, face comparison, and face search capabilities. You can detect, analyze, and compare faces for a wide variety 
of use cases, including user verification, cataloging, people counting, and public safety.

#### IS COMUNLY USED FOR:
<ul>
  <li>Face-based user verification (comparison between a known image and a new)<li>
  <li>Sentiment detection and analysis</li>
  <li>Facial search, detecting wich person is wich in a video or image </li>
  <li>Text detection</li>
  <li>Identify custom objecets in videos or images</li>
  
</ul>

## HOW IT WORKS?

The API is divided in two. Amazon Image Rekognition and Amazon Video Rekognition. You use Amazon Rekognition Image for analyzing images, and Amazon Rekognition Video for analyzing stored and streaming videos.

### TYPES OF ANALYSIS:
  
<ul>
  <li>Labels: objects (for example, flower, tree, or table), events (for example, a wedding, graduation, or birthday party), concepts (for example, a landscape, evening, and nature) or activities (for example, getting out of a car). Amazon Rekognition can detect labels in images and videos</li>
  <li>Amazon Rekognition can detect faces in images and stored videos. With Amazon Rekognition, you can get information about where faces are detected in an image or video, facial landmarks such as the position of eyes, and detected emotions such as happy or sad. You can also compare a face in an image with faces detected in another image. </li>
  <li>Text Detection</li>
  <li>Inappropriate or Offensive Content </li>
</ul>

### IMAGE AND VIDEO

Amazon Rekognition image operations are synchronous. The input and response are in JSON format. Amazon Rekognition Image operations analyze an input image that is in .jpg or .png image format. The image passed to an Amazon Rekognition Image operation can be stored in an Amazon S3 bucket.
Amazon Rekognition Video can analyze videos stored in an Amazon S3 bucket and videos streamed through Amazon Kinesis Video Streams. Amazon Rekognition Video video operations are asynchronous. With Amazon Rekognition Video storage video operations, you start analysis by calling the start operation for the type of analysis you want. For example, to detect faces in a stored video, call StartFaceDetection. Once completed, Amazon Rekognition publishes the completion status to an Amazon SNS topic. To get the results of the analysis operation, you call the get operation for the type of analysis you requested—for example, GetFaceDetection.
With Amazon Rekognition Video streaming video operations, you can search for faces stored in Amazon Rekognition Video collections or detect labels. Amazon Rekognition Video analyzes a Kinesis video stream.
You can call Amazon Rekognition API operations using either the AWS SDK or directly by using HTTP. Unless you have a good reason not to, you should always use the AWS SDK.

### STORAGE

The analysis made can use aws storage or not.

![image](https://user-images.githubusercontent.com/85199336/204829267-7abe417a-f440-464b-9cc1-b59809a90e9d.png)

These are referred to as non-storage API operations because when you make the operation call, Amazon Rekognition does not persist any information discovered about the input image.

![image](https://user-images.githubusercontent.com/85199336/204829656-5464e1a3-bd92-4423-9242-592b8fa22178.png)
