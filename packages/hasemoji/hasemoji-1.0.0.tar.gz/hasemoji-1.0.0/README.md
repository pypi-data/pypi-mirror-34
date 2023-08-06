## Has Emoji

> Check whether a string or character has any emoji

## Screenshot

<img src="https://gitlab.com/yoginth/hasemoji/raw/master/Screenshot.png" width="550">

## Install

```
$ pip install hasemoji
```

## Usage

```python
import hasemoji

print(hasemoji.char('😃'))
#=> True

print(hasemoji.string('I 💖 emoji'))
#=> True

print(hasemoji.char('I'))
#=> False

print(hasemoji.string('I love emoji'))
#=> False
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
