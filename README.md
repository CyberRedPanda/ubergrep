# ubergrep
search files for multiple patterns all at once. Create two text files files:

`patterns_to_use.txt` should be the pattern input.
`file_to_search.txt` should be the file to be searched.
Output will be written to `results.txt`, which will be automatically created.

By default, search is case insensitive. remove `re.IGNORECASE` from the regex to make case sensitive.

The script will update it's progress on the thousandth line of every pattern; you can change remainder value in the last print statement of `grep()` to make updates occur more or less frequently. the results file will contain a dictionary with the pattern as a key and all matches as a list values.

