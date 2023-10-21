# How to Contribute

This project is open to anyone in the community. Developers can contribute by adding code, and non-developers can contribute by improving docs. The main goal of this repository is to support open source with [hacktoberfest](http://hacktoberfest.digitalocean.com).

Follow the steps below to start contributing:

1. Fork this repository and clone your fork.

2. Create a new branch with the name as follows - `<Your name>/<Issue Number>`

3. Add all the relevant code and tests. We encourage everyone to improve our docs as well! :)

4. Push your code to your branch.

5. Finally, open a PR against the `master` branch of this repository.

Good luck!


# A Guide for Complete Beginners

Congratulations on choosing this project to go forward with it please-

1] Fork the Repository:
On the GitHub page of the project you're interested in, click the "Fork" button in the top right corner to create a copy of the repository under your GitHub account.

2] Clone the Repository:
Clone the forked repository to your local machine using Git. Open your terminal and use the following command:
```
git clone <repository_url>

```

3] Create a New Branch:
Create a new branch to work on your contribution. Use a descriptive name for the branch related to the changes you'll be making.
```
git checkout -b <branch_name>
```

4] Make Changes:
Make the necessary changes to the codebase locally on your machine using a code editor.

5] Commit Changes:
Commit your changes to the local repository. Use meaningful commit messages to describe the changes you've made.

```
git add .
git commit -m "Your descriptive commit message"
```

6] Push Changes:
Push your changes to your forked repository on GitHub.
```
git push origin <branch_name>
```

7] Create a Pull Request:
Go to your forked repository on GitHub and click the "New Pull Request" button. Select the branch you want to merge into the original repository's branch. Provide a clear and detailed description of your changes in the pull request.

8] Review and Collaborate:
Collaborate with other contributors and maintainers of the project. Address any feedback or requests for changes.

9] Merge the Pull Request:
Once your changes are reviewed and approved, the project maintainers will merge your pull request into the main repository.

10] Sync Your Fork:
Periodically sync your forked repository with the original repository to ensure your local repository is up to date with the latest changes in the project.

Remember to always follow the project's contribution guidelines and code of conduct. Communication and collaboration with the project maintainers and other contributors are key to successful contributions on GitHub.


# Steps to create a virtual environment and to activate it

To create and activate a virtual environment in Python, you can follow these steps. A virtual environment is a self-contained directory that contains its own Python interpreter and packages, allowing you to isolate your project dependencies from the system-wide Python installation. This is useful for managing dependencies and avoiding conflicts between different projects.

Step 1: Install Python (if not already installed)
If you don't have Python installed on your system, you can download and install it from the official Python website (https://www.python.org/downloads/). Make sure to install Python 3.x, as Python 2.x is no longer supported.

Step 2: Install virtualenv (if not already installed)
virtualenv is a tool used to create isolated Python environments. If you don't have it installed, you can do so using pip, which is the Python package manager. Open your command prompt or terminal and run:
```
pip install virtualenv
```
Step 3: Create a Virtual Environment
Now that you have virtualenv installed, you can create a virtual environment. Replace myenv with the desired name for your virtual environment:
```
virtualenv myenv
```
This will create a directory named myenv in your current working directory with its own Python interpreter and library.

Step 4: Activate the Virtual Environment
Activation is different depending on your operating system.
On Windows:
```
myenv\Scripts\activate
```
On macOS and Linux:
```
source myenv/bin/activate
```
After activation, your command prompt or terminal should change to indicate the name of the virtual environment, such as (myenv).

Step 5: Deactivate the Virtual Environment
To deactivate the virtual environment and return to the system-wide Python installation, simply run the following command, regardless of your operating system:
```
deactivate
```
That's it! You've created a virtual environment and activated it. You can now install packages and work on your project within this isolated environment. When you're done with your project, don't forget to deactivate the virtual environment using deactivate.
