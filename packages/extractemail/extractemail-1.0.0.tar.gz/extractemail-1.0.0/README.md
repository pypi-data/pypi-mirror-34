## Extract E-Mail

> Extract E-Mail from String

## Screenshot

<img src="https://gitlab.com/yoginth/extractemail/raw/master/Screenshot.png" width="550">

## Install

```
$ pip install extractemail
```

## Usage

```python
import extractemail

text = """
    Yoginth is very productive person he has multiple emails
    like yoginth@zoho.com but he likes yoginth@gmail.com
    but the username has already taken, yoginth wants to
    get yoginth@gitlab.com but he want to work there.
"""

extractemail.extract(text)
#=> ['yoginth@zoho.com', 'yoginth@gmail.com', 'yoginth@gitlab.com']
```

## Get Help

There are few ways to get help:

 1. Please [post questions on Stack Overflow](https://stackoverflow.com/questions/ask). You can open issues with questions, as long you add a link to your Stack Overflow question.

 2. For bug reports and feature requests, open issues.

 3. For direct and quick help, you can [email me](mailto://yoginth@zoho.com).

## How to contribute
Have an idea? Found a bug? See [how to contribute][contributing].

Thanks!

## License

[MIT][license]

[LICENSE]: https://yoginth.mit-license.org/
[contributing]: /CONTRIBUTING.md
