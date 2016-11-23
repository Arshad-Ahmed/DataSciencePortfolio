## 1. Data munging ##

/home/dq$ ls -la

## 2. Data exploration ##

/home/dq$ head *.csv

## 3. Filtering ##

/home/dq$ tail -n 46853 Hud_2005.csv >> combined_hud.csv

## 4. Consolidating datasets ##

/home/dq$ tail -n 42729 Hud_2007.csv >>combined_hud.csv ;tail -n 64535 Hud_2013.

## 5. Counting ##

/home/dq$ grep '1980-1989' combined_hud.csv| wc -l