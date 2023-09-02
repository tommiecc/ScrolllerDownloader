import platform
import subprocess

def setup():
    dependencies = ['click', 'BeautifulSoup4', 're', 'requests']

    python_version = platform.version()

    major, minor1, _ = map(int, python_version.split('.'))

    if major >= 3 and minor1 >= 10:
        for count, dependence in enumerate(dependencies):
            try:
                subprocess.check_call(['pip', 'install', dependence])
                dependencies.pop(count)
            except Exception as e:
                raise Exception(e)
        if dependencies is not None:
            raise Exception("Not all dependencies have been installed, please try again")
        else:
            print("All dependencies have been installled. You can now run the program.")

    else:
        raise Exception("Minium python version not installed. ScrolllerDownloader required >=3.10.x")