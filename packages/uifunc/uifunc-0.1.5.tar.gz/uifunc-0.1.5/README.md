# uifunc basic gui convenience functions

Provides the following convenience functions

## File Dialogues
Depending on the availability, these dialogues use tk, wxpython, or qt4. If it falls back to tk, FoldersSelector multi-folder selector does not work.

```python
@FileSelector(['py', 'pyc', 'pyx'])
def open_python_file(file_path: str) -> Any:
    # here the file you select is in file_path
    with open(file_path, 'r') as fp:
        # do something
```

```python
@FilesSelector(['py', 'pyc', 'pyx'])
def open_python_file(file_paths: List[str]) -> Any:
    # here the file you select is in the list file_paths
    for file_path in file_paths:
        with open(file_path, 'r') as fp:
            # do something
```

```python
@FolderSelector
def open_python_file(folder_path: str) -> Any:
    # here the folder you select is in the list folder_path
    for file_entry in scandir(folder_path):
        # do something
```

```python
@FoldersSelector
def open_python_file(folder_paths: List[str]) -> Any:
    # here multiple folder paths in the variable
    # do something
```

Additionally

```python
SaveFolderSelector # selects a single folder for saving
SaveSelector # selects a single file for saving
```
