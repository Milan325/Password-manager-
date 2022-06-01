# Password manager
The program is used to generate and store passwords for various websites and return stored password upon request.

## Use
When the program is run, window is displayed with 3 entry boxes and two buttons. If the user wants to generate new password, in the first enrty box site's URL or name shoud be written. Next, email address or username tied to an account shoud be provided. Then, "Napravi" button shoud be pressed to generate the password. If the user wants generated password, "Dodaj" button should be pressed, and the data will be stored in json file.
To retrieve password for a particular site, user needs to write URL (or name, if the site was registered by name) and press "Pretrazi" button, and a messagebox will display wanted data.

## Modules and functions
Modules used for this program are: `tkinter` for GUI, `random` for password generating, `pyperclip` function `copy()` to copy generated password to temporarily memory so it can be pasted as password on wanted site, `json` for creating and managing .json file.
```python
gen_password()
```
This function firstly deletes any previous characters from password entry box, then takes, using Python list comprehension:
- random number of characters from `letters` list (random between 8 and 10 chars)
- random number of characters from `numbers` list (random between 2 and 4 chars)
- random number of characters from `symbols` list (random between 2 and 4 chars).
Lists are, then, added as `pass_list` and shuffled using `shuffle()` function, and joined using `join()` function and inserted in entrybox and copied to temporary memory.

```python 
save_pass()
```
This function gets email, site and password inputs from entry boxes, formatting them and, after checking if all the boxes are filled out, saves it to data.json file. If the file does not exist, using `json` module, file is created and data is written. If any of the entry boxes are empty, messagebox will pop up warning the user about it.

```python
find_pass()
```
This function searches for password in data.json file by entry in "Sajt" entrybox and displays requried data, or tells the user that the password for required site doesn't exist, in a messagebox. If the file isn't found, error messagebox warns the user that the file is empty, and creates the file.

## Program engine
The program runs as a part of `Tk()` `Tk.mainloop()` loop.

## Running the program
This game is intended to be run by Python IDE or other Python interpeter. 
To install Python 3 see [Tutorials Point page](https://www.tutorialspoint.com/how-to-install-python-in-windows).
