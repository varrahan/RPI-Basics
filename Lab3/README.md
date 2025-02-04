# SYSC3010 Lab3 Deliverables

Lab 3 is about setting up a firebase to support cloud database storage and facilitate read/writes from multiple RPIs without direct connection or latency that could occur when storing locally. Lab 3 was also about using the Flask library to set up basic web servers and web applications that serve HTML files while providing a Python backend service. In lab3-firebase.py, we set up the read/writes to the Firebase real-time database. For the myflaskwebserver.py, a template HTML page was served, where the name that was displayed reflected a variable we initialized in the Flask app route. The webserver.py served as an interactive HTML/JS page that displayed an interactive LED grid. It was configured so that whenever a grid was coloured on the web page, that same pixel on the sensehat was also lit up, with the same RGB as the file.

## Python Files
#### 1.)  [lab3-firebase](./lab3-firebase.py)
#### 2.)  [myflaskwebserver](./myflaskwebserver.py)
#### 3.)  [webserver](./webserver.py)

## Photos
#### 1.) [firebase cli](./firebase_cli_screenshot.png)
#### 2.) [firebase website screenshot](./firebase_website_screenshot.png)
#### 3.) [webserver sensehat](./webserver_sensehat_photo.png)
#### 4.) [webserver webpage](./webserver_webpage_screenshot.png)
#### 5.) [website with content](./website_with_content.png)
