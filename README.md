
## Authors

- [conflicted](https://www.github.com/trojaninfect)


## Features

- encoding
- decoding


## Usage/Examples

encoding:
```bash
python main.py encode base64 "Hello World"
```
```bash
python main.py encode xor "payload123" --key secret


```
decoding:
```bash
python main.py decode base64 --file input.txt
```
```bash
python main.py decode base64 "SGVsbG8gV29ybGQ="
