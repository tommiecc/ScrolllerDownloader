from flask import Flask, request, render_template, flash
from bs4 import BeautifulSoup
import requests, re, os, time, secrets

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY=secrets.token_hex()
)

def link_response(link: str) -> requests.Response:
    try:
        response = requests.get(link) 
        return response
    except requests.exceptions.ConnectTimeout:
        flash(f"{bcolors.FAIL}ERR" + ": Connection Timed Out")
        quit(1)
    except requests.exceptions.InvalidSchema:
        flash(f"{bcolors.FAIL}ERR" + ": The URL schema provided is invalid")
        quit(1)
    except requests.exceptions.MissingSchema:
        flash(f"{bcolors.FAIL}ERR" + ": The URL schema provided has missing components. 'http' or 'https' may be missing.")
        quit(1)
    except requests.exceptions.URLRequired:
        flash(f"{bcolors.FAIL}ERR" + ": A URL is rsequired")
        quit(1)
    except requests.exceptions.Timeout:
        flash(f"{bcolors.FAIL}ERR" + ": The request timed out")
        quit(1)
    except requests.exceptions.ConnectionError as e:
        flash(f"{bcolors.FAIL}ERR" + f": An unknown error occured: {e}")
        quit(1)



@app.route("/", methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        isVideo = False
        try:
            isVideo = request.form['isVideo']
            print(isVideo)
        except:
            pass
        link = request.form['link']
        output = request.form['output']

        response = link_response(link)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            prettified_html = soup.prettify()
            if isVideo:
                pattern = r',\{\\"url\\":\\"([^"]*.mp4)\\",'
                flash(f"WARN: This might take a while, please be patient...")
            else:
                pattern = r'<meta\s+content="([^"]*)" property="og:image"/>'
            match = re.search(pattern, prettified_html)
            if match:
                try:
                    match_group = match.group(1)
                    if isVideo:
                        media_response = requests.get(match_group.replace("\\", ""))
                    else:
                        media_response = requests.get(match_group)
                except requests.exceptions.ConnectTimeout:
                    flash("ERR: Connection Timed Out")
                except requests.exceptions.InvalidSchema:
                    flash("ERR: The URL schema provided is invalid")
                except requests.exceptions.MissingSchema:
                    flash("ERR: The URL schema provided has missing components. 'http' or 'https' may be missing.")
                except requests.exceptions.URLRequired:
                    flash("ERR: A URL is rsequired")
                except requests.exceptions.Timeout:
                    flash("ERR: The request timed out")
                except requests.exceptions.ConnectionError as e:
                    flash(f"ERR: An unknown error occured: {e}")
                
                try:
                    if media_response.status_code == 200:
                        if not os.path.exists(os.path.dirname(output)):
                            flash(f"The directory '{os.path.dirname(output)}' does not exist.")
                        else:
                            if isVideo:
                                with open(output + (str(time.time()) + 'video.mp4'), 'wb') as f:
                                    f.write(media_response.content)
                                    f.close()
                                flash(f"INFO: Image saved to {output} as {str(time.time())}video.mp4")   
                            else:
                                with open(output + (str(time.time()) + 'image.png'), 'wb') as f:
                                    f.write(media_response.content)
                                    f.close()
                                flash(f"INFO: Video saved to {output} as {str(time.time())}image.png")
                    elif media_response.status_code == 404:
                        flash("ERR: This media does not exist (404)")
                    elif media_response.status_code == 403:
                        flash("ERR: You are forbidden from accessing this image (403)")
                    elif media_response.status_code == 429:
                        flash("ERR: The server has recieved too many requests (429)")
                    elif media_response.status_code == 500:
                        flash("ERR: There has been a server-side error (500)")
                    else:
                        flash(f"ERR: There has been an error with the request ({media_response.status_code})")
                except:
                    pass
            else:
                flash(f"ERR: No match was found. Try again")

    return render_template('index.html')

        

if __name__ == "__main__":
    app.run(debug=True)