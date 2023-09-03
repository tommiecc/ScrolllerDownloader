import subprocess, sys, platform

def setup():
    dependencies = ['click', 'BeautifulSoup4', 'requests', 'flask']

    python_version = platform.python_version()

    major, minor1, _ = map(int, python_version.split('.'))

    if major >= 3 and minor1 >= 10:
        for count, dependence in enumerate(dependencies):
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", dependence])
            except Exception as e:
                raise Exception(e)
    else:
        raise Exception("Minium python version not installed. ScrolllerDownloader required >=3.10.x")
    
if __name__ == "__main__":
    setup()