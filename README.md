# Scrolller Downloader
## Introduction
Scrolller is a web app owned by Twitter that uses the Reddit API to display Reddit images and videos in a format similar to Tumblr or Instagram. At the moment Scrolller has no way to download images or videos without a premium membership. Scrolller Downloader allows you to download images and videos from Scrolller.

## Installation
To use ScrolllerDownloader you will need >Python 3.10.x
Once you have installed the latest version of Python, you can download the repo and unzip `scrolllerdownload.zip`. 
Then run `setup.py` which will make sure that you have the correct version of python and will install the required dependencies.

## Running
To use ScrolllerDownloader run the `app.py` file in `src` folder. A flask server will start (usually on `127.0.0.1:5000`) and you will be able to use ScrolllerDownloader.

### Errors

#### Scrolller Connection Errors
| Error | Reason  |  Fix |
|--|--|--|
| `Connection timed out` | The connection between the program and the servers have timed out | Retry. If still fails raised issue. |
| `Invalid Schema` | The URL provided is invalid | Make sure the URL is a valid URL |
| `Missing Schema` | The URL provided has missing components | Try adding `http` or `https` to the URL |
| `URL Required` | The URL has not been provided | Provide a URL | 
| `Request Timed-out` | The request timed out | Try again. If issue persists raise an issue |
| `Unknown Error` | There is an unknown error. The error's details are in the error message | Try again. if issue persists raise an issue |

#### HTTP Errors
| Error | Reason | Fix |
|--|--|--|
| `404` | The image doesn't exist | nil |
| `403` | You don't have permission/are forbidden to access this image | nil |
| `429` | The server has received too many requests | Try again later |
| `500` | There has been a server-side error | Try again later |
| `Other` | There has been some other error | Try again. If error persists, raise an issue |


## Copyright disclaimer

_ScrolllerDownloader is an independent software application developed by @tommiecc and it is not affiliated with or endorsed by Twitter, Reddit, Tumblr, Instagram, or any other third-party services mentioned herein._

_ScrolllerDownloader is intended for personal and non-commercial use only. The software is provided "as is," without warranty of any kind, expressed or implied. @tommiecc shall not be held responsible for any unauthorized use, distribution, or downloading of copyrighted material, including but not limited to images and videos displayed on Scrolller._

_Users of ScrolllerDownloader are responsible for ensuring that their use of the software complies with all applicable copyright laws and regulations. It is essential to respect the intellectual property rights of content creators and the terms of service of the platforms from which the content is accessed._

_By using ScrolllerDownloader, you acknowledge and agree that @tommiecc and any contributors are not responsible for any legal consequences or actions resulting from your use of the software in violation of copyright laws or platform terms of service._

_Furthermore, @tommiecc reserves the right to modify, suspend, or discontinue Scrolller Downloader at any time without prior notice._

_Any trademarks, logos, or names mentioned in this software are the property of their respective owners._
