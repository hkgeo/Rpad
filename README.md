# Rpad

## What is Rpad?
- Rpad is a light/python-based Rmarkdown Editor which supports PANDOC documants export.
- This software is now under development and very unstable. Please use it just for testing.

## How to use?
- Open the code block with ``{r} and close the code block with ```.
- Execute the current code block with Ctrl+R.
- Select the entire document with Ctrl+A and execute the code block at the same time.
- Save the document with Ctrl+S.
- Open the document with Ctrl+O.
- Reset R with Ctrl+E (empty temp.r, temp.r).)
- temp.r : Temporary file where commands to be executed by R will be entered.
- temps.r : Temporary file where pre-processing document text will be entered when the full code block is executed.
- template.Rmd : Default Rmarkdown document header format to be entered when creating a new document.
- render.r : Temporary file where the command to be used when converting to docx/html document will be entered.
- r.txt : The file entered the location of Rscript.exe to process the r code. It is currently geared to R 4.2.2 version.
- Other grammar is the same as markdown.

## Download Beta Release
https://hkgeo.netlify.app/
