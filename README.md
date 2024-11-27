# code-reviews-inm

## Forking

Let's first fork the repository to have your own copy on github. To do so, press the `fork` button on top right of the page.

Now you can clone your own fork locally (be sure to use `ssh` to avoid authentificating every time you want to push).

## Installing the package

Run the following commands to install the package and the pre-commits:
```{bash}
cd code-reviews-inm
pip install -e ".[dev]"
pre-commit install
```
## Create a new branch

Create a new branch using the following command:
```{bash}
git checkout -b the_name_of_your_new_branch
```

## Do you modifications

Add a new file in `src/inm_package` and implement a new feature (a new function). Don't forget to create a new unit test in the `tests` folder. It is common to name unit tests in the following format `test_my_function`.

Once you're finished commit and push your new changes.

## Create a PR

To open a Pull Request (PR) after pushing a new branch to a fork, navigate to the repository on GitHub. You'll see a prompt to compare and create a PR if your branch has recent changes. In the head repository, select your fork and the branch you just pushed. Add a descriptive title, write a clear explanation of the changes in the description box, and review the proposed changes. Finally, click "Create Pull Request" to submit it.
