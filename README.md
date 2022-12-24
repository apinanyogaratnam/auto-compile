# Auto Compile

A cli tool that executes a command when detected a file change.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Support](#support)
- [Contributing](#contributing)

## Installation

Download the cli tool

macos:
1. download the binary: https://github.com/apinanyogaratnam/auto-compile/binaries/auto-compile-macos
2. move the binary to root directory: `mv auto-compile-macos ~/ac`
3. grant permissions: `chmod +x auto-compile`
4. set alias: `echo "alias auto-compile='~/auto-compile'" >> ~/.zshrc`

Note: you may need to restart your terminal

## Usage

This will execute the `date` command when files ending with `.py`
and clear the output
```sh
auto-compile .py date --clear
```

## Support

Please [open an issue](https://github.com/apinanyogaratnam/auto-compile/issues/new) for support.

## Contributing

Please contribute using [Github Flow](https://guides.github.com/introduction/flow/). Create a branch, add commits, and [open a pull request](https://github.com/apinanyogaratnam/auto-compile/compare).
