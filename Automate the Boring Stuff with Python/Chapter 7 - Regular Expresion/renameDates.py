#! python3
# changing american date in files name to euro's format

import shutil, os, re

# regular expression for files with american date in name
datePattern = re.compile(r"""(.*?)
((0|1)?\d)-
((0|1|2|3)?\d)-
((19|20)\d\d)
(.*?)$
""",re.VERBOSE)

# TODO: interation through files in current working dicrectory
for americanFilename in os.listdir('.'):
    mo = datePattern.search(americanFilename)

    # TODO: skipping files without dates in their names
    if mo == None:
        continue

    # TODO: taking names of filtered files
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    # TODO: preparing files with date in europs format
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    # TODO: taking full path do files
    absWorkingDir = os.path.abspath('.')
    americanFilename = os.path.join(absWorkingDir, americanFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    # TODO: changing files name
    print('Renaming "%s" to "%s"...' %(americanFilename, euroFilename))
