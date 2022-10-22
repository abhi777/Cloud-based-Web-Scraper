# GUI based Web Scraper v1.0.7

This is a Web Scraping Tool developed using Python which can scrap Data from the web and save the extracted Data in Google Cloud Storage. It's also very convenient to use, even for a Non-Technical Person as it provides a GUI. 

It needs a text file as an input containing a list of links of webpages line by line, name of the GCS Bucket and the types of Data to be scraped.
Executing the script after providing the inputs would start saving the required data into the GCS Bucket.        

![11](https://user-images.githubusercontent.com/74459400/197361183-6cf81a5d-07e3-41ff-946b-d7c4b669b27b.png)


# Requirements

* Windows OS             
* Python  (v3.6 or above)             
* webpage_links.txt (a text file containg links of webpages)
* requirements.txt
* key.json (credentials of GCS Bucket)

![2](https://user-images.githubusercontent.com/74459400/197361214-987e48c2-5401-4b6d-9f78-331649c5e6b4.png)



# Usage    

1. Download the Repository using the command given below from the terminal or by downloading the archive from above.      
```$ git clone https://github.com/abhi750/GUI-based-Web-Scraper.git```
2. Install modules in requirements.txt by executing the command given below in cmd or in the terminal of your Code Editor.                          
 ```$ pip install -r requirements.txt```
3. A Google Cloud Account must be created before executing the script and the credentials of the GCS Bucket must be kept in the same directory.

![4](https://user-images.githubusercontent.com/74459400/197361328-2601c0e8-40f1-4539-9ed7-5398a232fbd9.png)


5. Run the Python Script using terminal or cmd.                         
```$ python Web Scraper (GUI).py```
6. Provide inputs to the script and execute it.


#Working 
On executing the script, the marked data would be scraped from the specified webpages and would be stored in the GCS Bucket of the user.

![3](https://user-images.githubusercontent.com/74459400/197361414-78a14542-5823-41b7-8000-5b22c8548408.png)
![5](https://user-images.githubusercontent.com/74459400/197361424-2cee8ea0-2a80-42f1-9c8e-d98b5d059ebe.png)
![6](https://user-images.githubusercontent.com/74459400/197361433-c8d386ba-b21b-40a2-b88e-51cdbfa49424.png)
![7](https://user-images.githubusercontent.com/74459400/197361435-327bd55d-8d9c-42dc-915a-602b29777728.png)




# Updates

1. A Progress Bar to show the current status of the application.
2. Improved Performance and Bug fixes.
3. Cloud Storage 



                      
