## 2. Csvstack ##

/home/dq$ head -n10 Combined_hud.csv

## 3. Csvlook ##

/home/dq$ head -n10 Combined_hud.csv | csvlook

## 4. Csvcut ##

/home/dq$ csvcut -c 2 Combined_hud.csv | head -n 10 | csvlook

## 5. Csvstat ##

/home/dq$ csvstat Combined_hud.csv --mean

## 6. Csvcut | csvstat ##

/home/dq$ csvcut -c 2 Combined_hud.csv | csvstat

## 7. Csvgrep ##

/home/dq$ csvgrep -c 2 -m -9 Combined_hud.csv| head -n 10 |csvlook

## 8. Filtering out problematic rows ##

/home/dq$ csvgrep -c 2 -m -9 -i Combined_hud.csv > positive_ages_only.csv