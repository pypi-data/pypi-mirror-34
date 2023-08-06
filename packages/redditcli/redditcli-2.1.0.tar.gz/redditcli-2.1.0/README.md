# RedditCLI
`RedditCLI` brings Reddit to the terminal, allowing you to do the following without leaving your command line:

* Browse public subreddits, posts, comments, and users.
* Iterate through comments and post indexes.
* Search for posts, comments, and users.
* Clear all the commands on the screen.

## Installation

### Pip Installation

The following command will install `RedditCLI`:

    $ pip3 install redditcli

If you are not installing in a virtualenv, run with `sudo`:

    $ sudo pip3 install redditcli

Once installed, run the `RedditCLI` auto-completer with interactive help:

    $ reddit

Run commands:

    $ rdt <command> [options] [args]


### Auto-Completer and Interactive Help

You can enable fish-style completions and an auto-completion menu with interactive help:

    $ reddit

If available, the auto-completer also automatically displays commands through a pager.

Within the auto-completer, the following syntax applies:

    redditcli:$>> rdt <command> [options] [args]

## Commands:

* **rdt ls**
* Description: list posts front page and sorts by optional hot(default), new, rising, top, controversial.
  * Options:
    * **--sort [hot|new|rising|top|controversial]** - sort the list based on categories
    * **--move [next|previous]** - can only be used on result set
    * **--subreddits** - list all public subreddits available on reddit
    * **--subreddits --move [next|previous]** - can only be used on result set

* **view**
* Description: opens the permalink of the specified post index in a browser window.
  * Options:
    * **--index [Integer Value]** - can only be used on result set
    * **--comments --index [Integer Value]** - loads the comments of the specified post index. can only be used on result set
    * **--more-comments --index [Integer Value]** - Loads more comments from the post scope if there are posts to load.

* **search**
* Description: Searches reddit for the specified search term.
  * Options:
    * **[Search Term]**
    * **ls --move [next|previous]** - can only be used on result set

* **clear**
  * Description: Clears the screen

### Supported Python Versions

Python 3 and above.

## Libraries Used

- [Click](https://github.com/pallets/click)
- [python-prompt-toolkit](https://github.com/jonathanslenders/python-prompt-toolkit)
- [Praw](https://github.com/praw-dev/praw)
