def nyc_crime_map(table_id, select, startPageToken = None):
    if startPageToken:
        pageToken = startPageToken
    else:
        logger.info('Loading data for the initial search, without pageToken')
        results = table_features_first(table_id, select).json()
        yield from results.get('features', [])
        pageToken = results.get('nextPageToken')

    while pageToken:
        logger.info('Loading data for pageToken %s' % pageToken)
        results = table_features_tail(table_id, select, pageToken).json()
        yield from results.get('features', [])
        pageToken = results.get('nextPageToken')

def cli():
    for table_id, select in [
         ('02378420399528461352-17772055697785505571', 'YR,MO,geometry,X,Y,TOT,CR'),
         ('02378420399528461352-11853667273131550346', 'YR,MO,geometry,X,Y,TOT'),
    ]:
        data = nyc_crime_map(table_id, select)
        head(table_id, select)
        to_csv(table_id, select)
        to_geojson(table_id, select)

if __name__ == '__main__':
    main()
