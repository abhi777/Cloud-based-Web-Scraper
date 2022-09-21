import PySimpleGUI as sg
import re
import requests
from bs4 import BeautifulSoup
import os
import whois
import time


# funct that calls other functions and GUI
def auto():
    try:

        # Add some color
        # to the window
        sg.theme('BlueMono')

        # Very basic window.
        # Return values using
        # automatic-numbered keys
        layout = [
            [sg.Text('Please,Enter the path of Text File & path of the Directory')],
            [sg.Text("Source File ", size=(15, 1)), sg.Input(), sg.FileBrowse()],
            [sg.Text("Destination Folder ", size=(15, 1)), sg.Input(), sg.FolderBrowse()],

            [sg.Text("                             "), sg.Checkbox('Links ', default=False, key="-IN-")],
            [sg.Text("                             "), sg.Checkbox('Text Data ', default=False, key="-IN1-")],
            [sg.Text("                             "), sg.Checkbox('Images', default=False, key="-IN2-")],
            [sg.Text("                             "), sg.Checkbox('Scripts & CSS ', default=False, key="-IN3-")],
            [sg.Text("                             "), sg.Checkbox('DNS Information', default=False, key="-IN4-")],
            [sg.Text("      ")],
            [sg.Text("                            "), sg.Submit(size=(15, 1)),
             sg.Cancel(size=(15, 1))],
            [sg.Text("      ")],
            [sg.Text('Progress : ')],
            [sg.ProgressBar(1, orientation='h', size=(40, 30), key='progress', bar_color=['Green'])],
            [sg.Text("      ")]
        ]
        window = sg.Window('Web Scraper', layout).finalize()
        progress_bar = window.FindElement('progress')

        event, values = window.read()
        print(values)
        file1 = open(rf"{str(values[0])}", "r")  # opening the input text file
        filelist = file1.readlines()  # reading the text file
        print(filelist)
        no = len(filelist)
        print(no)

        def prog(x):
            val = [(x / no) * 100]
            progress_bar.UpdateBar(val, 100)
            # adding time.sleep(length in Seconds) has been used to Simulate adding your script in between Bar Updates
            time.sleep(.5)

        x = 0
        for k in filelist:  # looping the url's
            ur = (k[:-1])  # removing \n from the end

            global url  # globalizing the url
            url = 'https://' + ur
            print(url)
            path = values[1]

            fol_name = k[:-1]  # using the url to define folder name and path
            path2 = path + r'\'' + fol_name
            path_clean = path2.replace(r'\'', '\\')
            os.mkdir(path_clean)
            global true_path
            true_path = path_clean

            if values["-IN-"] == True:  # checkbox functions
                try:
                    links()
                except:
                    pass

            if values["-IN1-"] == True:
                try:
                    text_data()
                except:
                    pass

            if values["-IN2-"] == True:
                try:
                    img_data()
                except:
                    pass

            if values["-IN3-"] == True:
                try:
                    cssjs()
                except:
                    pass

            if values["-IN4-"] == True:
                try:
                    dnsinfo()
                except:
                    pass

            x = x + 1
            prog(x)





        closing_window()  # closing window func
        window.close()


    except:
        # auto()
        pass


def closing_window():
    sg.theme('BlueMono')
    layout1 = [
        [sg.Text('          Task Completed Successfully !!!!')],
        [sg.Button("Continue", size=(15, 1)), sg.Button("Exit", size=(15, 1))],

    ]

    window1 = sg.Window('Web Scraper', layout1)
    while True:
        event1, values1 = window1.read()
        if event1 == "Exit":  # activating the buttons and breaking the loop
            break

        if event1 == sg.WIN_CLOSED:
            break

        if event1 == "Continue":
            while True:
                j = 0  # breaking two loops
                auto()
                closing_window()
                if j == 0:
                    break
            break

    window1.close()


def links():
    page = requests.get(url)
    data = page.text

    soup = BeautifulSoup(data, 'html.parser')
    # links = []

    text_file = open(str(true_path) + '\\links.txt', 'w')

    for link in soup.find_all(attrs={'href': re.compile("http")}):
        # links.append(link.get('href'))
        a = link.get('href') + '\n'
        print(a)
        text_file.write(a)
    text_file.close()
    # print(links)


def text_data():
    # Make a request
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    text_file = open(str(true_path) + '\\text_data.txt', 'w')

    # Set all_h1_tags to all h1 tags of the soup
    tags = ['p', 'a', 'li', 'ul', 'td', 'tr', 'table', 'ol', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']
    for i in tags:

        for element in soup.select(i):
            txt = element.text + "\n"
            print(element.text)
            text_file.write(txt)

    text_file.close()


def img_data():
    # CREATE FOLDER
    def folder_create(images):
        try:
            folder_name = str(true_path) + "//" + 'image data'
            # folder creation
            os.mkdir(folder_name)

        # if folder exists with that name, ask another name
        except:
            print("Folder Exist with that name!")
            folder_create()

        # image downloading start
        download_images(images, folder_name)

    # DOWNLOAD ALL IMAGES FROM THAT URL
    def download_images(images, folder_name):
        # initial count is zero
        count = 0

        # print total images found in URL
        print(f"Total {len(images)} Image Found!")

        # checking if images is not zero
        if len(images) != 0:
            for i, image in enumerate(images):
                # From image tag ,Fetch image Source URL

                # 1.data-srcset
                # 2.data-src
                # 3.data-fallback-src
                # 4.src

                # Here we will use exception handling

                # first we will search for "data-srcset" in img tag
                try:
                    # In image tag ,searching for "data-srcset"
                    image_link = image["data-srcset"]

                # then we will search for "data-src" in img
                # tag and so on..
                except:
                    try:
                        # In image tag ,searching for "data-src"
                        image_link = image["data-src"]
                    except:
                        try:
                            # In image tag ,searching for "data-fallback-src"
                            image_link = image["data-fallback-src"]
                        except:
                            try:
                                # In image tag ,searching for "src"
                                image_link = image["src"]

                            # if no Source URL found
                            except:
                                pass

                # After getting Image Source URL
                # We will try to get the content of image
                try:
                    r = requests.get(image_link).content
                    try:

                        # possibility of decode
                        r = str(r, 'utf-8')

                    except UnicodeDecodeError:

                        # After checking above condition, Image Download start
                        with open(f"{folder_name}/images{i + 1}.jpg", "wb+") as f:
                            f.write(r)

                        # counting number of image downloaded
                        count += 1
                except:
                    pass

            # There might be possible, that all
            # images not download
            # if all images download
            if count == len(images):
                print("All Images Downloaded!")

            # if all images not download
            else:
                print(f"Total {count} Images Downloaded Out of {len(images)}")

    # MAIN FUNCTION START
    def main(url):
        # content of URL
        r = requests.get(url)

        # Parse HTML Code
        soup = BeautifulSoup(r.text, 'html.parser')

        # find all images in URL
        images = soup.findAll('img')

        # Call folder create function
        folder_create(images)

    # CALL MAIN FUNCTION
    main(url)


def cssjs():
    web_url = url
    html = requests.get(web_url).content

    # parse HTML Content
    soup = BeautifulSoup(html, "html.parser")

    js_files = []
    cs_files = []

    for script in soup.find_all("script"):
        if script.attrs.get("src"):
            # if the tag has the attribute
            # 'src'
            url1 = script.attrs.get("src")
            js_files.append(web_url + url1)

    for css in soup.find_all("link"):
        if css.attrs.get("href"):
            # if the link tag has the 'href'
            # attribute
            url2 = css.attrs.get("href")
            cs_files.append(web_url + url2)

    # adding links to the txt files
    with open(true_path + "\\javascript_files.txt", "w") as f:
        for js_file in js_files:
            print(js_file, file=f)

    with open(true_path + "\\css_files.txt", "w") as f:
        for css_file in cs_files:
            print(css_file, file=f)


def dnsinfo():
    domain = whois.whois(url)
    a = list(domain)
    c = dict(domain)

    # print(a)
    # print(list(c.keys()))
    text_file = open(str(true_path) + '\\dns_info.txt', 'w')
    for x in a:
        print(x + "                " + str(c[x]))
        inf = x + "                " + str(c[x]) + "\n"
        text_file.write(inf)
    text_file.close()


while True:
    try:
        i = 0  # looping the main
        auto()
        closing_window()
        if i == 0:
            break

    except:
        pass
