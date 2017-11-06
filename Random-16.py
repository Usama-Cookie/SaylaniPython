def city_country(city,country):
    print('"' + city.title() + ', ' + country.title() + '"')
city_country('karachi','pakistan')
city_country('dhaka','bangladesh')
city_country('newyork','america')

def make_album(album_title,artist_name,tracks=''):
    album = {'album_title':album_title.title(),'artist_name':artist_name.title()}
    if tracks:
        album['tracks'] = tracks
    return album
album = make_album('Losing sleep','cris young')
print(album)
album = make_album('divide','ed sheran',7)
print(album)

while True:
    album_title = input('Enter album title(q to quit): ')
    if album_title == 'q':
        break
    artist_name = input('Enter artist name(q to quit): ')
    if artist_name == 'q':
        break
    album = make_album(album_title,artist_name)
    print(album)