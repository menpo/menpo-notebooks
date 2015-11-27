Menpo Notebooks
===============

This repository contains IPython notebooks that demonstrate the features
and functionality of [Menpo](https://github.com/menpo/menpo). Please see
the Menpo repository for more information on Menpo itself.

Menpo Book
==========

This repo also contains the Menpo Book documentation. The Menpo Book is a gitbook built from the notebooks in this repo mixed with some other markdown text.

To build The Menpo Book locally, you will need `npm` installed.
```
npm install gitbook-cli -g
cd ./book
gitbook install
gitbook serve
```
Visit [localhost:4000](http://localhost:4000) to see the Book. The page will automatically update as changes are made to the Markdown files.
