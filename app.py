#!/usr/bin/env python3
from bs4 import BeautifulSoup
import re, os, time, click, requests

@click.command()
@click.option('-l', '--link', help="The scrolller link")
@click.option('-o', '--output', help="The output location")
@click.option('--v', is_flag=True, show_default=True, default=False, help="If the media is a video or not.")
def scroller_downloader(link, output, v):
    try:
        response = requests.get(link) 
    except requests.exceptions.ConnectTimeout:
        click.echo(click.style("ERR", fg='red') + ": Connection Timed Out")
        quit(1)
    except requests.exceptions.InvalidSchema:
        click.echo(click.style("ERR", fg='red') + ": The URL schema provided is invalid")
        quit(1)
    except requests.exceptions.MissingSchema:
        click.echo(click.style("ERR", fg='red') + ": The URL schema provided has missing components. 'http' or 'https' may be missing.")
        quit(1)
    except requests.exceptions.URLRequired:
        click.echo(click.style("ERR", fg='red') + ": A URL is rsequired")
        quit(1)
    except requests.exceptions.Timeout:
        click.echo(click.style("ERR", fg='red') + ": The request timed out")
        quit(1)
    except requests.exceptions.ConnectionError as e:
        click.echo(click.style("ERR", fg='red') + f": An unknown error occured: {e}")
        quit(1)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        prettified_html = soup.prettify()
        if v:
            pattern = r',\{\\"url\\":\\"([^"]*)\",'
            click.echo(click.style("WARN", fg="orange") + ": This might take a while, please be patient...")
        else:
            pattern = r'<meta\s+content="([^"]*)" property="og:image"/>'
        match = re.search(pattern, prettified_html)
        if match:
            try:
                match_group = match.group(1)
                if v:
                    media_response = requests.get(match_group.replace("\\", ""))
                else:
                    media_response = requests.get(match_group)
            except requests.exceptions.ConnectTimeout:
                click.echo(click.style("ERR", fg='red') + ": Connection Timed Out")
                quit(1)
            except requests.exceptions.InvalidSchema:
                click.echo(click.style("ERR", fg='red') + ": The URL schema provided is invalid")
                quit(1)
            except requests.exceptions.MissingSchema:
                click.echo(click.style("ERR", fg='red') + ": The URL schema provided has missing components. 'http' or 'https' may be missing.")
                quit(1)
            except requests.exceptions.URLRequired:
                click.echo(click.style("ERR", fg='red') + ": A URL is rsequired")
                quit(1)
            except requests.exceptions.Timeout:
                click.echo(click.style("ERR", fg='red') + ": The request timed out")
                quit(1)
            except requests.exceptions.ConnectionError as e:
                click.echo(click.style("ERR", fg='red') + f": An unknown error occured: {e}")
                quit(1)
            
            if media_response.status_code == 200:
                if not os.path.exists(os.path.dirname(output)):
                    raise FileNotFoundError(f"The directory '{os.path.dirname(output)}' does not exist.")
                else:
                    if v:
                        with open(output + (str(time.time()) + 'image.mp4'), 'wb') as f:
                            f.write(media_response.content)
                            f.close()
                        click.echo(click.style("INFO", fg="blue") + f": Image saved to {output}")   
                    else:
                        with open(output + (str(time.time()) + 'video.png'), 'wb') as f:
                            f.write(media_response.content)
                            f.close()
                        click.echo(click.style("INFO", fg="blue") + f": Video saved to {output}")
            elif media_response.status_code == 404:
                click.echo(click.style("ERR", fg="red") + ": This media does not exist (404)")
                click.echo(media_response)
            elif media_response.status_code == 403:
                click.echo(click.style("ERR", fg="red") + ": You are forbidden from accessing this image (403)")
            elif media_response.status_code == 429:
                click.echo(click.style("ERR", fg="red") + ": The server has recieved too many requests (429)")
            elif media_response.status_code == 500:
                click.echo(click.style("ERR", fg="red") + ": There has been a server-side error (500)")
            else:
                click.echo(click.style("ERR", fg="red") + f": There has been an error with the request ({media_response.status_code})")


if __name__ == "__main__":
    scroller_downloader()