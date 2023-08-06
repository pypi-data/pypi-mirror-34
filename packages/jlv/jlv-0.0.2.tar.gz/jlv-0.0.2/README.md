[![Build Status](https://travis-ci.org/stelabr/jlv.svg?branch=master)](https://travis-ci.org/stelabr/jlgitv)

# jlv (journal)
## Mission
`jlv` is an *extremely* straightforward command line app for keeping a journal on your local machine
## Audience
Users who enjoy using the terminal and keeping personal information on their local machine
## Usage
`jlv`
Starts up vim with an untitled entry

`jlv Birthday!`
Starts up vim with an entry titled *Birthday!*

`jlv "I had an amazing birthday!!"`
Starts up vim with an entry titled *I had an amazing birthday!!*
## Features
- Opportunity to provide journal entry title before and after writing
- The journal entry title appears on the first line of every entry.
- The journal entry filename becomes "\<title>.txt"
- If no title is given, the title becomes "untitled" and the filename
becomes "untitled_YYYY-MM-DD_HH:MM:SS"
- Each journal entry receives a "created YYYY-MM-DD_HH:MM:SS" subheader
- `jlv -p` opens the previous journal entry with the cursor already on the last line
