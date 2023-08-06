# gscPack

This package is used to assist in the creation and manipulation of **Gravestroke Seperated Columns** files. These files are saved as plain text files.
A gsc.txt file is, essentially, a fixed space file. The difference is that the first line in a gsc.txt is a series of columns, seperated by gravestrokes (`).
The following is an example line: 

`This is column number one.      `Column number two starts at the capitol C `One final column `

It is important that the top row ends with a gravestrock before the new line character.
Any data in the rows below this row will be read by this package and stored in a list. When the .save() function is called, the gsc.txt is updated, and the object
	is reinitialized. 