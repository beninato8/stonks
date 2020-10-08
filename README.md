# stonks

## Training LSTMs for use with Alpaca

## Config
Add your keys to `config.py.example` and rename it to `config.py` to use

## Twitter Data
 - Historical Twitter Data is from [http://www.trumptwitterarchive.com/](http://www.trumptwitterarchive.com/)
 - `tw.py` will check for new tweets every 60 seconds and add to it [trump.csv](twitter-data/trump.csv)
   - Only the timestamps are saved