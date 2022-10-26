# COMPILING THE AWS C++ SDK

### First of all, we should download the dependencies needed to compile and run the aws c++ sdk

#### 1. cmake
  sudo apt-get -y install cmake
#### 2. libcurl
  sudo apt-get install -y libcurl-dev
#### 3. libssl
  sudo apt-get install -y libssl-dev

#### There can be one or more dependencies that you might not have, so, if the compilation points an error, just paste the output on the web, and you find a topic telling you what you are expected to have

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


