wedding.py
==========

Utility csv library for wedding planning and management

## Available actions

### `count`
Calculates the guest count. Assumes guest list items are comma-separated strings.
Example: 
``` bash
export GUEST_COL=4 # identifies the column with guest list items
python wedding.py wedding.csv count
```
