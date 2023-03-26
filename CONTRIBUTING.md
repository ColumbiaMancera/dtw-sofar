# Contributing to dtw-sofar

## Prerequisites:
Before starting your contribution, please make sure to have Python instaled. This project requires Python 3.7 and above.

## Development Dependencies:
To install development dependencies, execute `make develop`. This will install and build this library and its dependencies using `pip`.

## Contribution Instructions:
### Fork and Clone:
You will need your own fork to work on the code. Go to the `dtw-sofar project
page <https://github.com/egeozguroglu/dtw-sofar>` and hit the ``Fork`` button. You will
want to clone your fork to your machine::

    git clone https://github.com/your-user-name/dtw-sofar.git dtw-sofar-yourname
    cd dtw-sofar-yourname
    git remote add upstream https://github.com/egeozguroglu/dtw-sofar.git
    git fetch upstream

### Branch
You may create a new branch for your contribution as follows:

    git checkout -b new-feature

## Commit and push your changes:

After making your changes, commit them to your new-feature branch. Then, push your forked feature branch's commits::

    git push origin new-feature

## Create a Pull Request:
When you're ready to ask for a code review, file a pull request:
    - Navigate to your repository on GitHub -- https://github.com/your-user-name/dtw-sofar
    - Click on ``Branches``
#. Click on the ``Compare`` button for your feature branch
#. Select the ``base`` and ``compare`` branches, if necessary. This will be ``main`` and
   ``new-feature``, respectively.