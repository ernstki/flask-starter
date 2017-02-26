# Flask-Starter

A [Blueprint][]-based Flask starter app.

## Installation

```
# clone from this GitHub repository (sub <githost> for real hostname)
git clone git@<githost>:ernstki/path/to/this/repo
cd flask_starter

# install the 'flask_starter' library and 'starter' command-line tool
pip install -e .

# install JavaScript / CSS assets for the front-end
cd flask_starter
bower install
```

## Customization

At this point, there's quite a lot of places where you'll need to
search-and-replace `flask_starter` with whatever you rename your project to
be.

A few you don't want to forget are:

* `.env` in the repository parent directory
* `.bowerrc` in the `flask_starter` directory
* `setup.py`, specifically the `entry_points=` setting

## License

&copy;2017 Kevin Ernst (ernstki -at- mail.uc.edu), under the
[MIT license](LICENSE.txt)

[blueprint]: http://flask.pocoo.org/docs/0.12/blueprints/
