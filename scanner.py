import glob
import gzip
import plyvel
import pickle
import sys
import concurrent.futures


def _make1(arr):
  try:
    en, names = arr
    keyword_day_impression = {}
    for name in names:
      print( name )
      with gzip.open(name, 'rt') as f:
        next(f)
        keys = next(f).strip().split(',')
        for ii, line in enumerate(f):
          if ii%100000 == 0:
            print(en, ii, line.strip())
          vals = line.strip().split(',')
          obj = dict( zip(keys, vals) )
          # print( obj )
          day = obj['Day']
          keyword = obj['Keyword']
          impressions = obj['Impressions']
          if keyword_day_impression.get(keyword) is None:
            keyword_day_impression[keyword] = {}
          if keyword_day_impression[keyword].get( day ) is None:
            keyword_day_impression[keyword][day] = 0
          try:
            keyword_day_impression[keyword][day] += float( impressions )
          except ValueError as e:
            continue
    #db = plyvel.DB('make1_memory/keyword_data_{}_imps.ldb'.format(en), create_if_missing=True)
    #for keyword, day_impression in keyword_day_impression.items():
    #  db.put( bytes(keyword, 'utf8'), pickle.dumps(day_impression) )
    #  print( en, keyword )
    open('make1_memory/keyword_data_imps_{}.pkl'.format(en), 'wb').write( pickle.dumps(keyword_day_impression) )
  except Exception as e:
    print('Deep Error ', e)


if '--make1' in sys.argv:
  e_names = {}
  for en, name in enumerate( glob.glob('../StormRuler/server/download/ADWORDS_KEYWORDS_PERFORMANCE_REPORT_*.csv.gz') ):
    en //= 10
    if e_names.get(en) is None:
      e_names[en] = []
    e_names[en].append( name )
  
  arr = [(e, names) for e, names in e_names.items()]
  print( arr )
  _make1(arr[0])
  with concurrent.futures.ProcessPoolExecutor(max_workers=10) as executor:
    executor.map( _make1, arr )

if '--make2' in sys.argv:
  db = plyvel.DB('make2_memory/db.ldb', create_if_missing=True)
  for name in glob.glob('./make1_memory/*.pkl'):
    print( name )
    keyword_day_impression = pickle.loads( open(name, 'rb').read() )
    for keyword, day_impression in keyword_day_impression.items():
      if db.get( bytes(keyword, 'utf8') ) is not None:
        _day_impression = pickle.loads( db.get( bytes(keyword, 'utf8') ) )
        # merge
        for day, impression in day_impression.items():
          if _day_impression.get(day) is None:
            _day_impression[day] = 0
          _day_impression[day] += impression
      else:
        _day_impression = day_impression

      db.put( bytes(keyword, 'utf8'), pickle.dumps(_day_impression) )

from datetime import date
from datetime import datetime
import calendar
if '--make3' in sys.argv:
  db = plyvel.DB('make2_memory/db.ldb', create_if_missing=True)

  db_3 = plyvel.DB('make3_memory/db.ldb', create_if_missing=True)
  for en, (keyword, day_impression) in enumerate(db):
    if en%1000 == 0:
      print( en, keyword.decode('utf8') )
    if db_3.get(keyword) is not None:
      continue
    keyword = keyword.decode('utf8')
    day_impression = pickle.loads( day_impression )
    weekday_imps = {}
    for day, impression in day_impression.items():
      try:
        date = datetime.strptime(day, '%Y-%m-%d')
      except ValueError as e:
        continue
      weekday = calendar.day_name[date.weekday()]
      if weekday_imps.get(weekday) is None:
        weekday_imps[weekday] = []
      weekday_imps[weekday].append( impression )
    db_3.put( bytes(keyword, 'utf8'), pickle.dumps( weekday_imps ) )
import statistics

if '--make4' in sys.argv:
  db = plyvel.DB('make3_memory/db.ldb', create_if_missing=True)
  db_4 = plyvel.DB('make4_memory/db.ldb', create_if_missing=True)
  SW = {'Monday': '1_Monday', 'Tuesday':'2_Tuesday', 'Wednesday':'3_Wednesday', 'Thursday':'4_Thursday', 'Friday':'5_Friday', 'Saturday':'6_Saturday', 'Sunday':'7_Sunday'}
  for keyword, weekday_imps in db:
    keyword = keyword.decode('utf8')
    weekday_imps = pickle.loads( weekday_imps )
    weekday_mean = {}
    for weekday, imps in weekday_imps.items():
      weekday_mean[SW[weekday]] = statistics.mean( imps )
    if sum(weekday_mean.values()) < 7000:
      continue
    print( keyword, weekday_mean )
    db_4.put( bytes(keyword, 'utf8'), pickle.dumps(weekday_mean) )

if '--make5' in sys.argv:
  db = plyvel.DB('make4_memory/db.ldb', create_if_missing=True)
  for keyword, weekday_mean in db:
    keyword = keyword.decode('utf8')
    weekday_mean = pickle.loads( weekday_mean )

    print( keyword )
    print( ' '.join([k for k,v in sorted( weekday_mean.items(), key=lambda x:x[0])]) )
    print( ' '.join([str(int(v)) for k,v in sorted( weekday_mean.items(), key=lambda x:x[0])]) )
  
