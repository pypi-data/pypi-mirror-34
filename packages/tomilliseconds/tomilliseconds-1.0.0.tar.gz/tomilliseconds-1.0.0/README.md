## Compare URLs

> Convert an object of time properties to milliseconds: {'seconds': 10} → 10000

## Demo

Demo on [Repl.it](https://repl.it/@yoginth/tomilliseconds)

## Screenshot

<img src="https://gitlab.com/yoginth/tomilliseconds/raw/master/Screenshot.png" width="550">

## Install

```
$ pip install tomilliseconds
```

## Usage

```python
from tomilliseconds import toMilliseconds

toMilliseconds({
	'days': 28,
	'hours': 8,
	'minutes': 30,
	'seconds': 50,
	'milliseconds': 1
})

#=> 2449850001
```

## API

### toMilliseconds(input)

#### input

Type: `Dictionary`

Specify an object with any of the following properties:

- `days`
- `hours`
- `minutes`
- `seconds`
- `milliseconds`
- `microseconds`
- `nanoseconds`

## Thanks

- [Sindresorhus's to-milliseconds](https://github.com/sindresorhus/to-milliseconds)

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
