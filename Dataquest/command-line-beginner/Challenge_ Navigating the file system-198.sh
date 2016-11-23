## 1. Exploring the file system ##

/home/dq$ ls -lrth

## 2. Moving problematic files to a separate folder ##

/home/dq$ mv legislators forest_fires.cssv crime_rates.json problematic/

## 3. Fixing file extensions ##

/home/dq/problematic$ ls

## 4. Consolidating files ##

/home/dq$ mv problematic/ csv_datasets/

## 5. Restricting permissions ##

/home/dq$ chmod -664 csv_datasets/