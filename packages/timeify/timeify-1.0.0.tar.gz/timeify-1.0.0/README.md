## Timeify

> Convert Millisecond to human readable format

## Screenshot

<img src="https://gitlab.com/yoginth/timeify/raw/master/Screenshot.png" width="550">

## Install

```
$ pip install timeify
```

## Usage

```python
import timeify as time

print (time.humanize(180000))
#=> (2, 2, 0, 0) # (days, hours, minutes, seconds)

print (time.humanize(158692)[2])
#=> 4 # (minutes)
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
