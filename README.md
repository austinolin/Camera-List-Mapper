# Camera Duplicates

Attached is a list of camera values taken from a database. Users were initially allowed to enter any value, but to make filtering easier for searches we want to only allow a predefined set.

The first step is to sanitize the existing data (in the included camera_list.txt) by merging near duplicates into single values. Here is a sample:

    Canon 5D mark II
    Canon 5d MKII
    Canon 5dMKII
    Canon 5D Mk III

There are three variations on the Canon 5D MK II. Note that the last entry, "Canon 5D Mk III" is not the same camera, and should not be merged with these others. The process you create should pick the best version (or create a new one), and then create a mapping of existing values to the new value:

    {
        'Canon 5D mark II': 'Canon 5D Mark II',
        'Canon 5d MKII': 'Canon 5D Mark II',
        'Canon 5dMKII': 'Canon 5D Mark II'
    }

Python preferred but not required, as long as we can run your code. An explanation of your thought process either as a separate file or in detailed comments in code would be appreciated. Please **don't spend more than an hour on this** unless it interests you, in which case indicate how much longer you worked on this.

When you are done, you can upload to a github repo (but DON'T fork this one because other applicants will view your work), or if you don't have a github account you may tar or zip your script and all related materials. Email your link or attachments to alec@nimia.com. 

Bonus points: Some values are not camera models, such as "Quicktime Pro Res" and should be removed entirely. 