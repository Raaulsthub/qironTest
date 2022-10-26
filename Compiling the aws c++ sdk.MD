# COMPILING THE AWS C++ SDK

### First of all, we should download the dependencies needed to compile and run the aws c++ sdk

#### 1. cmake
  sudo apt-get -y install cmake
#### 2. libcurl
  sudo apt-get install -y libcurl-dev
#### 3. libssl
  sudo apt-get install -y libssl-dev
  
#### There can be one or more dependencies that you might not have, so, if the compilation points an error, just paste the output on the web, and you find a topic telling you what you are expected to have

### The compilation requires about 14G of memory, if your machine does not contain enough, we should first allocate more swap space, if it does have enought, you can just ignore this part

#### Check whats the current swap partition
  ![image](https://user-images.githubusercontent.com/85199336/198057425-e727b28a-f4b0-49b3-a776-aeb177ebe5d6.png)
#### Creating a new swap archive
  ![image](https://user-images.githubusercontent.com/85199336/198058873-46255596-945e-485b-bec3-c0a28c4f1d21.png)
#### Verifying
  ![image](https://user-images.githubusercontent.com/85199336/198059137-2df4fb56-16bd-4751-ab2a-ee443784618f.png)
#### Activating the swap file
  ![image](https://user-images.githubusercontent.com/85199336/198059325-c00ae2bc-6ce6-4656-81ce-fb676c1c0719.png)
  ![image](https://user-images.githubusercontent.com/85199336/198059626-59248b83-fed0-4b61-8971-bdc2fa31f3b7.png)
  ![image](https://user-images.githubusercontent.com/85199336/198059825-3a759e90-34e0-48ce-8e4c-01cf717fc4b1.png)
#### To see if it worked, just paste the free -h command again
#### If you want to make this swap file permanent (otherwise it will reset to no swap when the machine reboots)
  ![image](https://user-images.githubusercontent.com/85199336/198060404-edf496ef-077e-4368-8c20-4e7d390c63cf.png)
  ![image](https://user-images.githubusercontent.com/85199336/198060683-b8bcb7d2-cee3-4497-aed7-a21dfe94ef8a.png)
  
### Now, we create a build directory for your lib

#### 1. Go to a directory of your choice using the "cd" command
#### 2. Create a directory
  (sudo) mkdir aws
#### 3. Clone the github aws sdk for c++ repository
  If you do not have git on your environment, you should download it using: sudo apt-get -y install git
  Paste the following command:
  git clone git@github.com:aws/aws-sdk-cpp.git
#### 3.1. Now go to the directory you've just downloaded
  cd aws-sdk-cpp
#### 3.2. Update the source code using
  git checkout main
  git pull origin main
  git submodule update --innit --recursive
#### 5. Create the build directory
  mkdir build
#### 6. Go to the build directory
  cd build
#### 7. Configure cmake
  cmake "path to the aws sdk directory" -DCMAKE_BUILD_TYPE=Debug -DCMAKE_PREFIX_PATH="path to the build directory (the one you are currently in"
#### 8. Build
  make
#### 9. Install
  make install


