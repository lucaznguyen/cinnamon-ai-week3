# cinnamon-ai-week-3

## Introduction

This repo is the week-03-homework's source code at Cinnamon AI Bootcamp. In this project, we created a tool to convert files (.png, .heic, .diff, .pdf) to images.

**Problem**

  - **Input**: file (.png, .heic, .diff, .pdf)
  - **Output**: image (.png)

## Prepare the environment

1. python==3.8.16
2. Install the necessary dependencies by running

        pip install -r requirements.txt

2. Setup ```pdf2image``` [Poppler](https://pypi.org/project/pdf2image/) dependencies to install Poppler and save the directory to PATH environment variable.

## Structure of workspace

```
Main-folder/
│
├── README.md
├── converter.py - This file contains the source code of the tool
├── example.heic - The example file (.heic)
├── test.py - Unit test
├── main.py
└── requirements.txt
```

## Running the code

### Conversion process

        python main.py --f <directory to input file> --o <folder of output image(s)>

## Author

This repo is made by 1Vision Team, a team consists of 4 people in Cinnamon Bootcamp 2023

| Name | Github |
|-|-|
| Nguyễn Tư Thành Nhân | [ngtuthanhan](https://github.com/ngtuthanhan) |
| Lê Nhật Kha | [khalee2307](https://github.com/KhaLee2307) |
| Nguyễn Trần Hữu Thịnh | [lucaznguyen](https://github.com/lucaznguyen) |
| Đinh Ngọc Ân | [andythetechnerd03](https://github.com/andythetechnerd03) |
| Võ Hoàng Bảo Duy | [vhbaoduy](https://github.com/vhbaoduy) |
