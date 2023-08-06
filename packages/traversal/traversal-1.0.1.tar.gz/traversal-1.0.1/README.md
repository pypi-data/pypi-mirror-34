## Matrix Traversals

> Famous Matrix Traversals

## Install

```
$ pip install traversal
```

## Usage

```python
import traversal

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

traversal.zigzag(3, 3, matrix)
#=> [1, 2, 4, 7, 5, 3, 6, 8, 9]

traversal.spiral(3, 3, matrix)
#=> [1, 2, 3, 6, 9, 8, 7, 4, 5]

traversal.row(3, 3, matrix)
#=> [1, 2, 3, 4, 5, 6, 7, 8, 9]

traversal.column(3, 3, matrix)
#=> [1, 4, 7, 2, 5, 8, 3, 6, 9]
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
[contributing]: CONTRIBUTING.md
