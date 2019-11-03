# -*- coding: utf-8 -*-
# Real stream by Netai 2019 
# Version 1.2.0
#
############################################
# Dependencias 
# Script ExtendedInfo
# Script Urlresolver de TVAddons
# Script ResolveURL Por Jsergio.
#
############################################
#
# Agregar sinopsis a Peliculas y series.
# Supresion de Licencia
# Novedades en episodios agregados en series.
#
############################################

import urllib, urllib2, sys, re, os, unicodedata
import xbmc, xbmcgui, xbmcplugin, xbmcaddon
import cookielib,webbrowser
import traceback,datetime,HTMLParser,httplib
import urlresolver
import cookielib,base64
import requests	
import plugintools
import config


addon = xbmcaddon.Addon('plugin.video.Real.stream')
addon_version = addon.getAddonInfo('version')
plugin_handle = int(sys.argv[1])
user = 'gruponetai/'   
mysettings = xbmcaddon.Addon(id = 'plugin.video.Real.stream')
profile = mysettings.getAddonInfo('profile')
home = mysettings.getAddonInfo('path')
iconos = addon.getSetting('iconos')


if iconos == 'true':

	fanart = xbmc.translatePath(os.path.join(home, 'fanart.png'))
	icon = xbmc.translatePath(os.path.join(home, 'icon.png'))
	extended = xbmc.translatePath(os.path.join(home, 'extended_info.png'))
	buscar = xbmc.translatePath(os.path.join(home, 'buscar.png'))
	pair = xbmc.translatePath(os.path.join(home, 'pair.png'))
	theMovieDB = xbmc.translatePath(os.path.join(home, 'theMovieDB.png'))
	novedades = xbmc.translatePath(os.path.join(home, 'novedades.png'))
	estrenos = xbmc.translatePath(os.path.join(home, 'estrenos.png'))
	recomendadas = xbmc.translatePath(os.path.join(home, 'recomendadas.png'))
	p_accion = xbmc.translatePath(os.path.join(home, 'accion.png'))
	animacion = xbmc.translatePath(os.path.join(home, 'animacion.png'))
	aventuras = xbmc.translatePath(os.path.join(home, 'aventuras.png'))
	belico = xbmc.translatePath(os.path.join(home, 'belico.png'))
	cifi = xbmc.translatePath(os.path.join(home, 'ciencia-ficcion.png'))
	clasico = xbmc.translatePath(os.path.join(home, 'clasicos.png'))
	comedia = xbmc.translatePath(os.path.join(home, 'comedia.png'))
	crimen = xbmc.translatePath(os.path.join(home, 'crimen.png'))
	drama = xbmc.translatePath(os.path.join(home, 'drama.png'))
	familiar = xbmc.translatePath(os.path.join(home, 'familiar.png'))
	fantasia = xbmc.translatePath(os.path.join(home, 'fantasia.png'))
	historia = xbmc.translatePath(os.path.join(home, 'historia.png'))
	superheroes = xbmc.translatePath(os.path.join(home, 'marvel.png'))
	misterio = xbmc.translatePath(os.path.join(home, 'misterio.png'))
	musical = xbmc.translatePath(os.path.join(home, 'musical.png'))
	romance = xbmc.translatePath(os.path.join(home, 'romance.png'))
	spain = xbmc.translatePath(os.path.join(home, 'spain.png'))
	suspense = xbmc.translatePath(os.path.join(home, 'suspense.png'))
	terror = xbmc.translatePath(os.path.join(home, 'terror.png'))
	thriller = xbmc.translatePath(os.path.join(home, 'thriller.png'))
	western = xbmc.translatePath(os.path.join(home, 'western.png'))
	sagas = xbmc.translatePath(os.path.join(home, 'sagas_cine.png'))
	calidad4k = xbmc.translatePath(os.path.join(home, '4k.png'))
	torrent = xbmc.translatePath(os.path.join(home, 'torrent.png'))
	buscarseries = xbmc.translatePath(os.path.join(home, 'buscar-serie.png'))
	seriestodas = xbmc.translatePath(os.path.join(home, 'series-todas.png'))
	favorites = xbmc.translatePath(os.path.join(home, 'favorites.png'))
	artesmarciales = xbmc.translatePath(os.path.join(home, 'artesmarciales.png'))
	emision = xbmc.translatePath(os.path.join(home, 'emision.png'))
	mejores = xbmc.translatePath(os.path.join(home, 'mejores.png'))
	seriesreto = xbmc.translatePath(os.path.join(home, 'seriesretro.png'))
	Mb_peliculas = xbmc.translatePath(os.path.join(home, 'BuscadorPeliculas.png'))
	Mb_series = xbmc.translatePath(os.path.join(home, 'BuscadorSeries.png'))
	nuevos_no = xbmc.translatePath(os.path.join(home, 'Novedades_series.png'))
	nuevos_si = xbmc.translatePath(os.path.join(home, 'Novedades_Episodios.png'))
	
else:

	#Imagenes
	artesmarciales = xbmc.translatePath(os.path.join(home, 'artesmarciales.png'))
	seriesreto = xbmc.translatePath(os.path.join(home, 'seriesretro.png'))
	iconos = addon.getSetting('iconos')
	fanart = xbmc.translatePath(os.path.join(home, 'fanart.jpg'))
	icon = xbmc.translatePath(os.path.join(home, 'icon.png'))
	extended = xbmc.translatePath(os.path.join(home, 'extended_info.png'))
	buscar = xbmc.translatePath(os.path.join(home, 'buscar.png'))
	pair = xbmc.translatePath(os.path.join(home, 'pair.png'))
	theMovieDB = xbmc.translatePath(os.path.join(home, 'theMovieDB.jpg'))
	novedades = xbmc.translatePath(os.path.join(home, 'novedades.jpg'))
	estrenos = xbmc.translatePath(os.path.join(home, 'encines.jpg'))
	recomendadas = xbmc.translatePath(os.path.join(home, 'recomendadas.jpg'))
	p_accion = xbmc.translatePath(os.path.join(home, 'accion.jpg'))
	animacion = xbmc.translatePath(os.path.join(home, 'animacion.jpg'))
	aventuras = xbmc.translatePath(os.path.join(home, 'aventuras.jpg'))
	belico = xbmc.translatePath(os.path.join(home, 'belico.jpg'))
	cifi = xbmc.translatePath(os.path.join(home, 'ciencia-ficcion.jpg'))
	clasico = xbmc.translatePath(os.path.join(home, 'clasicos.png'))
	comedia = xbmc.translatePath(os.path.join(home, 'comedia.jpg'))
	crimen = xbmc.translatePath(os.path.join(home, 'crimen.jpg'))
	drama = xbmc.translatePath(os.path.join(home, 'drama.jpg'))
	familiar = xbmc.translatePath(os.path.join(home, 'familiar.jpg'))
	fantasia = xbmc.translatePath(os.path.join(home, 'fantasia.jpg'))
	historia = xbmc.translatePath(os.path.join(home, 'historia.jpg'))
	superheroes = xbmc.translatePath(os.path.join(home, 'superheroes.jpg'))
	misterio = xbmc.translatePath(os.path.join(home, 'misterio.jpg'))
	musical = xbmc.translatePath(os.path.join(home, 'musical.jpg'))
	romance = xbmc.translatePath(os.path.join(home, 'romance.jpg'))
	spain = xbmc.translatePath(os.path.join(home, 'spain.jpg'))
	suspense = xbmc.translatePath(os.path.join(home, 'suspense.jpg'))
	terror = xbmc.translatePath(os.path.join(home, 'terror.jpg'))
	thriller = xbmc.translatePath(os.path.join(home, 'thriller.jpg'))
	western = xbmc.translatePath(os.path.join(home, 'western.jpg'))
	sagas = xbmc.translatePath(os.path.join(home, 'sagas_cine.jpg'))
	calidad4k = xbmc.translatePath(os.path.join(home, '4k.jpg'))
	torrent = xbmc.translatePath(os.path.join(home, 'torrent.jpg'))
	buscarseries = xbmc.translatePath(os.path.join(home, 'buscar-serie.png'))
	seriestodas = xbmc.translatePath(os.path.join(home, 'series-todas.png'))
	emision = xbmc.translatePath(os.path.join(home, 'emision.png'))
	mejores = xbmc.translatePath(os.path.join(home, 'mejores.png'))
	favorites = xbmc.translatePath(os.path.join(home, 'favoritos.png'))
	Mb_peliculas = xbmc.translatePath(os.path.join(home, 'BuscadorPeliculas.png'))
	Mb_series = xbmc.translatePath(os.path.join(home, 'BuscadorSeries.png'))
	nuevos_no = xbmc.translatePath(os.path.join(home, 'Novedades_series.png'))
	nuevos_si = xbmc.translatePath(os.path.join(home, 'Novedades_Episodios.png'))
	
#Menus:

menu_pelis = xbmc.translatePath(os.path.join(home, 'peliculas.png'))
menu_series = xbmc.translatePath(os.path.join(home, 'series.png'))
ajustes = xbmc.translatePath(os.path.join(home, 'ajustes.png'))
vid = xbmc.translatePath(os.path.join(home, 'videoteca.png'))
favicon = xbmc.translatePath(os.path.join(home, 'favorites.png'))
resolver = xbmc.translatePath(os.path.join(home, 'resolver.png'))
test = xbmc.translatePath(os.path.join(home, 'test.png'))
videotutoriales = xbmc.translatePath(os.path.join(home, 'video-tutoriales.png'))
proxys = xbmc.translatePath(os.path.join(home, 'proxy.png'))


#Ajustes
mostrar_cat = addon.getSetting('mostrar_cat')
sel_tobox = addon.getSetting('sel_tobox')
videos = addon.getSetting('videos')
activar = addon.getSetting('activar')
favcopy = addon.getSetting('favcopy')
anticopia = addon.getSetting('anticopia')
licencia_addon = addon.getSetting('licencia_addon')
notificar = addon.getSetting('notificar')
mostrar_bus = addon.getSetting('mostrar_bus')
restante = addon.getSetting('restante')
selecton = addon.getSetting('selecton')
aviso = addon.getSetting('aviso')
RealStream_Settings = addon.getSetting('RealStream_Settings')
Resolver_Settings = addon.getSetting('Resolver_Settings')
restante = addon.getSetting('restante')
fav = addon.getSetting('fav')
Fontcolor = addon.getSetting('Fontcolor')
MenuColor = addon.getSetting('MenuColor')
texto = 'aHR0cDovL25ldGFpLmV1L3JlYWxzdHJlYW0v'.decode('base64')
txt = 'bienvenida'
txt2 = 'bienvenida' #.decode('base64')
copyright = addon.getSetting('copyright')
myaddon = 'cGx1Z2luLnZpZGVvLg=='.decode('base64') + copyright
pluginname = 'cGx1Z2luLnZpZGVvLlJlYWwuc3RyZWFt'.decode('base64')
Forceupdate = addon.getSetting('Forceupdate')
if Forceupdate == 'true':  
    xbmc.executebuiltin('UpdateAddonRepos()')
    xbmc.executebuiltin('UpdateLocalAddons()')
extension = 'LnR4dA=='.decode('base64')	
es_hallowen = 'aHR0cHM6Ly9wYXN0ZWJpbi5jb20vcmF3L1NQOUpRZExS'.decode('base64')

#Regexs			
Rtrailer = 'aHR0cDovL2JpdC5seS8yU1FOSnlP'.decode('base64')
bienvenida = texto + txt + extension
u_tube = 'http://www.youtube.com'
urly = 'aHR0cDovL3kzei5zag=='.decode('base64')
realweb = 'http://bit.ly/2ImelUx'
decode32 = '.xsl.pt'
lnk3 = 'L21hc3Rlci8='.decode('base64')
myurl = urly + decode32
texto_regex = 'texto1=[\'"](.*?)[\'"]\s*texto2=[\'"](.*?)[\'"]\s*'
m3u_thumb_regex = 'tvg-logo=[\'"](.*?)[\'"]'
#m3u_regex ='#(.+?),(.+)\s*(.+)\s*(.+)\s*(.*)'
m3u_regex = '#(.+?),(.+)\s*(.+)\s*(.+)\s*(.+)\s*(.+)\s*(.*)'
m3u_trailers='(.+),(.+),(.+),(.+),(.+),(.+),(.+),(.+),(.+),(.+),(.+),(.+),(.+),(.+),(.+)'
m3u_series = 'img="(.+?)",(.+)\s*fanart="(.+)"\s*(.+)\s*(.*)\s*'
m3u_serie = 'img="(.+?)",(.+)\s*fanart="(.+)"\s*(.+)\s*(.*)\s*'
m3u_capitulos = 'img="(.+?)",(.+)\s*fanart="(.+)"\s*(.+)\s*'
multi_regex = '#(.+?),(.+)\s*(.+)\s*(.+)\s*(.*)\s*(.*)\s*(.+)'
tutoriales_regex = '#(.+?),(.+)\s*(.+)'
url_regex = 'lk=[\'"](.*?)[\'"]\s*lk1=[\'"](.*?)[\'"]\s*lk2=[\'"](.*?)[\'"]\s*lk3=[\'"](.*?)[\'"]\s*lk4=[\'"](.*?)[\'"]\s*lk5=[\'"](.*?)[\'"]\s*lk6=[\'"](.*?)[\'"]\s*lk7=[\'"](.*?)[\'"]\s*lk8=[\'"](.*?)[\'"]\s*lk9=[\'"](.*?)[\'"]\s*lk10=[\'"](.*?)[\'"]\s*lk11=[\'"](.*?)[\'"]\s*lk12=[\'"](.*?)[\'"]\s*lk13=[\'"](.*?)[\'"]\s*lk14=[\'"](.*?)[\'"]\s*lk15=[\'"](.*?)[\'"]\s*lk16=[\'"](.*?)[\'"]\s*lk17=[\'"](.*?)[\'"]\s*lk18=[\'"](.*?)[\'"]\s*lk19=[\'"](.*?)[\'"]\s*lk20=[\'"](.*?)[\'"]\s*lk21=[\'"](.*?)[\'"]\s*lk22=[\'"](.*?)[\'"]\s*lk23=[\'"](.*?)[\'"]\s*'
#rapidvideo = 'source src=[\'"](.*?)[\'"]'
rapidvideo = 'source src=[\'"](.*?)[\'"]\s*title=[\'"](.*?)[\'"]'
lnk_regex = 'db=[\'"](.*?)[\'"]\s*db0=[\'"](.*?)[\'"]\s*db1=[\'"](.*?)[\'"]\s*db2=[\'"](.*?)[\'"]\s*db3=[\'"](.*?)[\'"]\s*db4=[\'"](.*?)[\'"]\s*db5=[\'"](.*?)[\'"]\s*db6=[\'"](.*?)[\'"]\s*db7=[\'"](.*?)[\'"]\s*db8=[\'"](.*?)[\'"]\s*db9=[\'"](.*?)[\'"]\s*db10=[\'"](.*?)[\'"]\s*db11=[\'"](.*?)[\'"]\s*db12=[\'"](.*?)[\'"]\s*db13=[\'"](.*?)[\'"]\s*db14=[\'"](.*?)[\'"]\s*db15=[\'"](.*?)[\'"]\s*db16=[\'"](.*?)[\'"]\s*db17=[\'"](.*?)[\'"]\s*db18=[\'"](.*?)[\'"]\s*db19=[\'"](.*?)[\'"]\s*db20=[\'"](.*?)[\'"]\s*db21=[\'"](.*?)[\'"]\s*db22=[\'"](.*?)[\'"]\s*db23=[\'"](.*?)[\'"]\s*db24=[\'"](.*?)[\'"]\s*'
visita_regex = '[\'"](.*?)[\'"]'
vregex = r'066">\s*(.+)</f'
admin_regex = '[\'"](.*?)[\'"]'
server_regex = '#(.+?),(.+)\s*"(.+?)","(.+)","(.+)","(.+)"\s*(.+)\s*(.+)\s*'
event_regex = '[\'"](.*?)[\'"]'
upto_regex = 'src":"(.*?)"label":"(.*?)"lang":"(.*?)"'
evento = 'https://pastebin.com/raw/SP9JQdLR'
limit_reg = '[\'"](.*?)[\'"]'
server = 'aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tLw=='.decode('base64')
lnk = server + user
mydb = '[\'"](.*?)[\'"]'
lnk2 = 'UmVhbHN0cmVhbQ=='.decode('base64')
ong_regex = 'video=[\'"](.*?)[\'"]'
key_master = '0110nhu'.replace('0110nhu', 'nhu')
keygen = 'aHR0cDovL2JpdC5seS8yUjQx'.decode('base64') + key_master
addon_id = 'cGx1Z2luLnZpZGVvLlJlYWwuc3RyZWFt'.decode('base64')
bit = '0110R0N'.replace('0110R0N', 'R0N') 
todas = 'aHR0cDovL2JpdC5seS8yWEIx'.decode('base64') + bit 
bit1 = '0110pEJ'.replace('0110pEJ', 'pEJ') 
db = 'aHR0cDovL2JpdC5seS8yd1Nh'.decode('base64') + bit1
bit2 = 'ABBAOb5'.replace('ABBAOb5', 'Ob5') 
db1 = 'aHR0cDovL2JpdC5seS8yRVhV'.decode('base64') + bit2 
bit3 = '0110jaw'.replace('0110jaw', 'jaw') 
db3 = 'aHR0cDovL2JpdC5seS8yd01M'.decode('base64') + bit3
bit4 = '01109DI'.replace('01109DI', '9DI') 
db4 = 'aHR0cDovL2JpdC5seS8ySXgz'.decode('base64') + bit4
bit5 = '01103hs'.replace('01103hs', '3hs') 
db5 = 'aHR0cDovL2JpdC5seS8zMW1U'.decode('base64') + bit5 
bit6 = '01107DW'.replace('01107DW', '7DW') 
db6 = 'aHR0cDovL2JpdC5seS8yV1ln'.decode('base64') + bit6
bit7 = '0110mLl'.replace('0110mLl', 'mLl') 
db7 = 'aHR0cDovL2JpdC5seS8yS0cw'.decode('base64') + bit7
bit8 = '01102Hj'.replace('01102Hj', '2Hj') 
db8 = 'aHR0cDovL2JpdC5seS8yWEJo'.decode('base64') + bit8
bit9 = '0110fXg'.replace('0110fXg', 'fXg') 
db9 = 'aHR0cDovL2JpdC5seS8ySTVy'.decode('base64') + bit9
bit10 = '0110NMH'.replace('0110NMH', 'NMH') 
db10 = 'aHR0cDovL2JpdC5seS8yd0t6'.decode('base64') + bit10
bit11 = '0110bwQ'.replace('0110bwQ', 'bwQ') 
db11 = 'aHR0cDovL2JpdC5seS8yd01V'.decode('base64') + bit11
bit12 = '0110xzG'.replace('0110xzG', 'xzG') 
db12 = 'aHR0cDovL2JpdC5seS8yWHhz'.decode('base64') + bit12
bit13 = '0110x64'.replace('0110x64', 'x64') 
db13 = 'aHR0cDovL2JpdC5seS8yRVlF'.decode('base64') + bit13
bit14 = '0110vUE'.replace('0110vUE', 'vUE') 
db14 = 'aHR0cDovL2JpdC5seS8yWmhW'.decode('base64') + bit14
bit15 = '01107ZL'.replace('01107ZL', '7ZL') 
db15 = 'aHR0cDovL2JpdC5seS8yWm4w'.decode('base64') + bit15
bit16 = '01106cf'.replace('01106cf', '6cf') 
db16 = 'aHR0cDovL2JpdC5seS8yRVlk'.decode('base64') + bit16
bit17 = '0110Jtp'.replace('0110Jtp', 'Jtp') 
db17 = 'aHR0cDovL2JpdC5seS8yV3Nq'.decode('base64') + bit17
bit18 = '0110a5b'.replace('0110a5b', 'a5b') 
db18 = 'aHR0cDovL2JpdC5seS8yV3dj'.decode('base64') + bit18
bit19 = '0110Q7u'.replace('0110Q7u', 'Q7u') 
db19 = 'aHR0cDovL2JpdC5seS8yV3NL'.decode('base64') + bit19
bit20 = '0110rsq'.replace('0110rsq', 'rsq') 
db20 = 'aHR0cDovL2JpdC5seS8ySzhE'.decode('base64') + bit20
bit21 = '0110DDR'.replace('0110DDR', 'DDR') 
db21 = 'aHR0cDovL2JpdC5seS8ySzd5'.decode('base64') + bit21
bit22 = '0110feQ'.replace('0110feQ', 'feQ') 
db22 = 'aHR0cDovL2JpdC5seS8yS0cz'.decode('base64') + bit22
bit23 = '0110MHY'.replace('0110MHY', 'MHY')  
db23 = 'aHR0cDovL2JpdC5seS8ySXVo'.decode('base64') + bit23
bit24 = '0110xdb'.replace('0110xdb', 'xdb') 
db24 = 'aHR0cDovL2JpdC5seS8yWEJu'.decode('base64') + bit24
visitante = 'aHR0cDovL2JpdC5seS8yS0pZZVVp'.decode('base64')
contador = 'aHR0cHM6Ly9uZXRhaS5ldS92aXNpdGFzL2luZGV4LnBocA=='.decode('base64')
myaddon = 'cGx1Z2luLnZpZGVvLlJlYWwuc3RyZWFt'.decode('base64')
bit25 = '0110lxu'.replace('0110lxu', 'lxu')
db25 = 'aHR0cDovL2JpdC5seS8yV1Bj'.decode('base64') + bit25 
bit26 = '0110pzp'.replace('0110pzp', 'pzp') 
db26 = 'aHR0cDovL2JpdC5seS8yVHpB'.decode('base64') + bit26  
bit27 = '01105yt'.replace('01105yt', '5yt') 
db27 = 'aHR0cDovL2JpdC5seS8yTVpp'.decode('base64') + bit27

#Series: 
Lserie = '1001DTs'.replace('1001DTs', 'DTs') 
dbserie = 'aHR0cDovL2JpdC5seS8ySzhP'.decode('base64') + Lserie
Tserie = '1001Hky'.replace('1001Hky', 'Hky') 
dbtserie = 'aHR0cDovL2JpdC5seS8yTGVL'.decode('base64') + Tserie
Eserie = '1001VFU'.replace('1001VFU', 'VFU') 
dbeserie = 'aHR0cDovL2JpdC5seS8zMERx'.decode('base64') + Eserie
Rserie = '3545OMZ'.replace('3545OMZ','OMZ') 
dbrserie = 'aHR0cDovL2JpdC5seS8yazhk'.decode('base64') + Rserie 
Nserie = '4224tZO'.replace('4224tZO','tZO') 
dbnserie = 'aHR0cDovL2JpdC5seS8zNXd4'.decode('base64') + Nserie  



			


def search(): 


	try:
			content = make_request(todas)
			match = re.compile(mydb).findall(content)
			for m3u in match:
				try:
				
					db = m3u
					
					keyb = xbmc.Keyboard('', 'Busqueda por titulo')
					keyb.doModal()
					if (keyb.isConfirmed()):
						dp = xbmcgui.DialogProgress()
						dp.create('Realstream:','Buscando ...')
						x = range(0,76)
						for n in x:
							n = n+1
							
						searchText = urllib.quote_plus(keyb.getText()).replace('+', ' ')
						content2 = make_request(db)
						match = re.compile(m3u_regex).findall(content2)
						for thumb, name, url, id, trailer, description, fanart in match:
								
							dp.update(n ,'[COLOR orange]Realstream: Buscando ...[/COLOR]',' [COLOR yellow] %s [/COLOR]' % name)
							xbmc.sleep(1)
							if dp.iscanceled(): break;
							if re.search(searchText, removeAccents(name.replace(' ', ' ')), re.IGNORECASE):

								dp.update(80 ,' [COLOR orange]Busqueda finalizada[/COLOR] ')
								xbmc.sleep(1000)
								xbmc.executebuiltin("XBMC.Notification(Real Stream, [COLOR gold]Generando listado ...  [/COLOR][COLOR orange] Por favor espere ![/COLOR] ,1000)")
								dp.update(100 ,'[COLOR orange]Realstream: [/COLOR]', '[COLOR gold] Busqueda finalizada ...[/COLOR]')
								dp.close()
								m3u_playlist2(name, url, thumb, id, trailer, description, fanart)
	
									
						add_dir('[COLOR %s]Buscar Pelicula[/COLOR]' % MenuColor, 'search', 111, Mb_peliculas, fanart)
						xbmc.executebuiltin("XBMC.Notification(Real Stream, Resultados para: [COLOR orange]" +searchText+ "[/COLOR] ,2000)")
				
				except: add_dir('[COLOR %s]Buscar Pelicula[/COLOR]' % MenuColor, 'search', 111, Mb_peliculas, fanart)
										
	except:
		pass
		
def mensaje():
	
	aviso = addon.getSetting('aviso')
	
	if aviso == 'true':
		
		try:
			content = make_request(bienvenida)
			match = re.compile(texto_regex).findall(content)
			for texto1,texto2 in match:
				try:
		
		
					msg1 = texto1
					msg2 = texto2


					from datetime import datetime
				
					now = datetime.now()
					fecha = now.strftime('%d/%m/%Y')
				
					content3 = make_request(contador)
					match = re.compile(vregex).findall(content3)
					for visit in match:
				
						line1 = "[B]" + msg1 + "[/B]"
						line2 = "" + msg2 + ""
						line3 = "[COLOR white]Hoy: " +fecha+ ", Es usted el visitante numero: [B][COLOR gold]" + visit + "[/B][/COLOR]"

						xbmcgui.Dialog().ok("Real Stream", line1, line2, line3)
				except:
					pass
							
		except:
			pass
			
		try:
			content2 = make_request(visitante)
			match = re.compile(visita_regex).findall(content2)
			for version in match:
				
				import xbmc
				import xbmcaddon

				__addon__ = xbmcaddon.Addon()
				__addonname__ = __addon__.getAddonInfo('name')
				__icon__ = __addon__.getAddonInfo('icon')
					
				addon_version = addon.getAddonInfo('version')
				upd_version = version
 
				line1 = "[COLOR orange]Version instalada: [COLOR gold][B] " +addon_version+ "[/B] [/COLOR][/COLOR][COLOR white] Disponible: [B]" +version+ " [/B][/COLOR]" 
				time = 4000 #in miliseconds
				xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(__addonname__,line1, time, __icon__))
							
				if addon_version < version:
								
					xbmcgui.Dialog().ok("Real Stream", "[COLOR white] Existe una nueva version de [/COLOR][COLOR fuchsia]Realstream[/COLOR]", "[COLOR orange]Actualimete tiene instalada la version[/COLOR] [COLOR white][B] %s [/B][/COLOR]" %addon_version, " [COLOR white]Ya esta disponible la[/COLOR] [COLOR gold][B] %s [/B][/COLOR]" % version)
					
						
		except:
			pass
							
					

			if not xbmc.getCondVisibility('System.HasAddon(script.extendedinfo)'):
				xbmcgui.Dialog().ok("El Script ExtendedInfo No esta instalado" , "[COLOR cyan]Necesario AddOn externo para ver informacion de peliculas[/COLOR]","[COLOR yellow]AddOns -> Instalar desde repositorio -> KODI add-on repository -> Add-ons de programas -> ExtendedInfo Script\n[COLOR lime]Despues de instalarlo configuralo para español.[/COLOR]")
	

	
def removeAccents(s):
## Nos cargamos los acentos, phyton no los usa ni los reconoce. 
	return ''.join((c for c in unicodedata.normalize('NFD', s.decode('utf-8')) if unicodedata.category(c) != 'Mn'))
					
def read_file(file):
## FUNCION QUE LEE LOS FICHEROS:
    try:
        f = open(file, 'r')
        content = f.read()
        f.close()
        return content
    except:
        pass

def make_request(url):
##ESTA FUNCION lee las url declaradas donde estan los videos. ||
	try:
		req = urllib2.Request(url)
		req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0')
		response = urllib2.urlopen(req)	  
		link = response.read()
		response.close()  
		return link
	except urllib2.URLError, e:
		print 'We failed to open "%s".' % url
		if hasattr(e, 'code'):
			print 'We failed with error code - %s.' % e.code	
		if hasattr(e, 'reason'):
			print 'We failed to reach a server.'
			print 'Reason: ', e.reason
			
def OPEN_URL(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36')
        req.add_header('Referer', '%s'%url)
        req.add_header('Connection', 'keep-alive')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        return link


def conf_menu():

    MenuColor = addon.getSetting('MenuColor')

    if activar == 'true':
		
	add_dir('[COLOR %s]Buscar Pelicula[/COLOR]' % MenuColor, 'search', 111, Mb_peliculas, fanart)
	add_dir('[COLOR %s]Buscar Serie[/COLOR]' % MenuColor,'search',145, Mb_series,fanart)	
	add_dir('[COLOR %s]Peliculas[/COLOR] ' % MenuColor, 'movieDB', 116, menu_pelis, fanart)
	add_dir('[COLOR %s]Series[/COLOR] ' % MenuColor, 'movieDB', 117, menu_series, fanart)

	
    if RealStream_Settings == 'true':
        add_dir('[COLOR %s]Ajustes[/COLOR]' % MenuColor, 'Settings', 119, ajustes, fanart)

    		
	if mostrar_cat == 'true':
		peliculas()
		
	if Resolver_Settings == 'true':
		menu_resolver_set()
		menu_resolveurl_set()
        
	if anticopia == 'false':

		line1 = "[COLOR=red][B]Activacion del Addon:[/B][/COLOR]"
		line2 = "[COLOR aqua]Este addon necesita las siguientes dependencias, Script.extendedinfo, Script.UrlResolver, Script.ResolveURL para su correcto funcionamiento. Puede descargarlas desde http://netai.eu/netai[/COLOR]"
		line3 = "[COLOR gold]Por favor, vaya a ajustes y active las pestañas: Activar addon, Y la opcion tengo las siguientes depencencias, Script.extendedinfo, y script.Urlresolver instaladas. Muchas gracias, Netai Team.[/COLOR]"

		xbmcgui.Dialog().ok("Real Stream", line1, line2, line3)
		
def buscar_id():
    add_dir('[COLOR orange]Buscador por id[/COLOR]', u_tube, 127, theMovieDB, fanart)
	
def extra_menu():
	MenuColor = addon.getSetting('MenuColor')
	add_dir('[COLOR %s]The movie DB[/COLOR]' % MenuColor, 'movieDB', 99, theMovieDB, fanart)
#	add_dir('[COLOR %s]Buscador por id[/COLOR]' % MenuColor, u_tube, 127, theMovieDB, fanart)
	add_dir('[COLOR %s]Video tutoriales[/COLOR]' % MenuColor,u_tube,125,videotutoriales,fanart)
#	add_dir('[COLOR %s]Autorizar OPENLOAD[/COLOR]' % MenuColor, 'movieDB', 97, pair, fanart)


def menu():
	
	conf_menu()
	extra_menu()
	
def salir():

    menu()

def favoritos():
	if xbmc.getCondVisibility('System.HasAddon(script.favourites)'):
		try:
			xbmc.executebuiltin( "RunScript(script.favourites)" )	
		except:
			pass
def Real_stream_settings():
    addon.openSettings()
	
	
def urlresolver_settings():
    urlresolver.display_settings()
	
def menu_resolver_set():
    add_dir('[COLOR %s]Ajustes URL RESOLVER[/COLOR]' % MenuColor, 'resolve', 120, resolver, fanart)	

def resolveurl_settings():

    xbmcaddon.Addon('script.module.resolveurl').openSettings()
	
def menu_resolveurl_set():
    add_dir('[COLOR %s]Ajustes RESOLVE URL[/COLOR]' % MenuColor, 'resolve', 140, resolver, fanart)
	
def peliculas():

	MenuColor = addon.getSetting('MenuColor')
	add_dir('[COLOR %s]Buscador[/COLOR]' % MenuColor, 'search', 111, buscar, fanart)
	add_dir('[COLOR %s]Estrenos[/COLOR]' % MenuColor,u_tube,3,estrenos,fanart)
	add_dir('[COLOR %s]Todas[/COLOR]' % MenuColor,u_tube,26,recomendadas,fanart)
	add_dir('[COLOR %s]4K[/COLOR]' % MenuColor,u_tube,141,calidad4k,fanart)
	add_dir('[COLOR %s]Novedades[/COLOR]' % MenuColor,u_tube,2,novedades,fanart)
	add_dir('[COLOR %s]Accion[/COLOR]' % MenuColor,u_tube,5,p_accion,fanart)
	add_dir('[COLOR %s]Animacion[/COLOR]' % MenuColor,u_tube,6,animacion,fanart)
	add_dir('[COLOR %s]Artes Marciales[/COLOR]' % MenuColor,u_tube,29,artesmarciales,fanart)
	add_dir('[COLOR %s]Aventuras[/COLOR]' % MenuColor,u_tube,7,aventuras,fanart)
	add_dir('[COLOR %s]Belico[/COLOR]' % MenuColor,u_tube,8,belico,fanart)
	add_dir('[COLOR %s]Ciencia Ficcion[/COLOR]' % MenuColor,u_tube,9,cifi,fanart)
	add_dir('[COLOR %s]Cine Clasico[/COLOR]' % MenuColor,u_tube,30,clasico,fanart)
	add_dir('[COLOR %s]Comedia[/COLOR]' % MenuColor,u_tube,10,comedia,fanart)
	add_dir('[COLOR %s]Crimen[/COLOR]' % MenuColor,u_tube,11,crimen,fanart)
	add_dir('[COLOR %s]Drama[/COLOR]' % MenuColor,u_tube,12,drama,fanart)
	add_dir('[COLOR %s]Familiar[/COLOR]' % MenuColor,u_tube,13,familiar,fanart)
	add_dir('[COLOR %s]Fantasia[/COLOR]' % MenuColor,u_tube,14,fantasia,fanart)
	add_dir('[COLOR %s]Historia[/COLOR]' % MenuColor,u_tube,15,historia,fanart)
	add_dir('[COLOR %s]Misterio[/COLOR]' % MenuColor,u_tube,16,misterio,fanart)
	add_dir('[COLOR %s]Musical[/COLOR]' % MenuColor,u_tube,17,musical,fanart)
	add_dir('[COLOR %s]Romance[/COLOR]' % MenuColor,u_tube,18,romance,fanart)
	add_dir('[COLOR %s]Thriller[/COLOR]' % MenuColor,u_tube,19,thriller,fanart)
	add_dir('[COLOR %s]Suspense[/COLOR]' % MenuColor,u_tube,20,suspense,fanart)
	add_dir('[COLOR %s]Terror[/COLOR]' % MenuColor,u_tube,21,terror,fanart)
	add_dir('[COLOR %s]Western[/COLOR]' % MenuColor,u_tube,22,western,fanart)
	add_dir('[COLOR %s]Spain[/COLOR]' % MenuColor,u_tube,23,spain,fanart)
	add_dir('[COLOR %s]Super heroes[/COLOR]' % MenuColor,u_tube,24,superheroes,fanart)
	add_dir('[COLOR %s]Sagas[/COLOR]' % MenuColor,u_tube,25,sagas,fanart)

def series():

	add_dir('[COLOR %s]Buscar Serie[/COLOR]' % MenuColor,'search',145,buscarseries,fanart)
	
	nuevos_episodios()
	
	add_dir('[COLOR %s]En emision[/COLOR]' % MenuColor,u_tube,150,emision,fanart)
	add_dir('[COLOR %s]Mejor valoradas[/COLOR]' % MenuColor,u_tube,151,mejores,fanart)
	add_dir('[COLOR %s]Series Retro[/COLOR]' % MenuColor,u_tube,152,seriesreto,fanart)	
	add_dir('[COLOR %s]Todas[/COLOR]' % MenuColor,u_tube,142,seriestodas,fanart)
	
def nuevos_episodios():

	novedad = 'aHR0cHM6Ly9uZXRhaS5ldS9yZWFsc3RyZWFtLw=='.decode('base64')
	fileN = 'Y29uZGljaW9uLnR4dA=='.decode('base64')
	link = novedad + fileN
	novedad_regex = '[\'"](.*?)[\'"]'
	series = make_request(link)
	match = re.compile(novedad_regex).findall(series)
	for condicion in match:
		try:
			
			if condicion == 'si':
			
				add_dir('[COLOR %s]Hay Nuevos Episodios[/COLOR]' % MenuColor,u_tube,155,nuevos_si,fanart)
				
			elif condicion == 'no':
			
				add_dir('[COLOR %s]No hay Nuevos Episodios[/COLOR]' % MenuColor,u_tube,155,nuevos_no,fanart)
			
			return
			
		except:
			pass
		
def searchs(): 


	try:
		
		lista_series = make_request(dbserie)
		match = re.compile(mydb).findall(lista_series)
		for m3u in match:
		
			try:
		
				op = m3u
				keyb = xbmc.Keyboard('', 'Buscar')
				keyb.doModal()
				if (keyb.isConfirmed()):
					dp = xbmcgui.DialogProgress()
					dp.create('Realstream:','Buscando ...')
					x = range(0,69)
					for n in x:
						 n = n+1
					searchText = urllib.quote_plus(keyb.getText()).replace('+', ' ')
					content2 = make_request(op)
					match = re.compile(m3u_series).findall(content2)
					for iconimage, name, fanart, url, description in match:
						dp.update(n ,'[COLOR orange]Realstream: Buscando ...[/COLOR]', '[COLOR gold] %s [/COLOR]' % name)
						xbmc.sleep(5)
						if dp.iscanceled(): break;
						if re.search(searchText, removeAccents(name.replace(' ', ' ')), re.IGNORECASE):

							xbmc.executebuiltin("XBMC.Notification(Real Stream, Generando listado ...  [COLOR orange] Por favor espere ![/COLOR] , 4000)")
							add_dir2(name, url, 143, iconimage, fanart, description)
							dp.update(100 ,'[COLOR orange]Realstream: [/COLOR]', '[COLOR gold] Busqueda finalizada ...[/COLOR]')
							xbmc.sleep(2000)
							dp.close()
					add_dir('[COLOR %s]Buscar Serie[/COLOR]' % MenuColor,'search',145,buscarseries,fanart)
					xbmc.executebuiltin("XBMC.Notification(Real Stream, Sin Resultados para: [COLOR orange]" +searchText+ "[/COLOR] , 2000)")

			
			except: add_dir('[COLOR %s]Buscar Serie[/COLOR]' % MenuColor,'search',145,buscarseries,fanart)
		
	except: 
		pass
		
def novedades_series():
	
	try:
		
		lista_series = make_request(dbnserie)
		match = re.compile(mydb).findall(lista_series)
		for m3u in match:
		
			try:
		
				op = m3u
				
			except:
				pass
				
		content2 = make_request(op)
		match = re.compile(m3u_series).findall(content2)
		for iconimage, name, fanart, url, description in match:
			try:
				
				add_dir2(name, url, 143, iconimage, fanart, description)
			
			except:
				pass
	except:
		pass	
		
def seriesretro():

	try:
		
		lista_series = make_request(dbrserie)
		match = re.compile(mydb).findall(lista_series)
		for m3u in match:
		
			try:
		
				op = m3u
				
			except:
				pass
				
		content2 = make_request(op)
		match = re.compile(m3u_series).findall(content2)
		for iconimage, name, fanart, url, description in match:
			try:
				
				add_dir2(name, url, 143, iconimage, fanart, description)
			
			except:
				pass
	except:
		pass	
	
	
def emitiendo():

	try:
		
		lista_series = make_request(dbeserie)
		match = re.compile(mydb).findall(lista_series)
		for m3u in match:
		
			try:
		
				op = m3u
				
			except:
				pass
				
		content2 = make_request(op)
		match = re.compile(m3u_series).findall(content2)
		for iconimage, name, fanart, url, description in match:
			try:
				
				add_dir2(name, url, 143, iconimage, fanart, description)
			
			except:
				pass
	except:
		pass	

def top15():

	try:
		
		lista_series = make_request(dbtserie)
		match = re.compile(mydb).findall(lista_series)
		for m3u in match:
		
			try:
		
				op = m3u
				
			except:
				pass
				
		content2 = make_request(op)
		match = re.compile(m3u_series).findall(content2)
		for iconimage, name, fanart, url, description in match:
			try:
				
				add_dir2(name, url, 143, iconimage, fanart, description)
			
			except:
				pass
	except:
		pass
	
def Lista_Series(): 
	
	try:
		
		lista_series = make_request(dbserie)
		match = re.compile(mydb).findall(lista_series)
		for m3u in match:
		
			try:
		
				op = m3u
				
			except:
				pass
				
		content2 = make_request(op)
		match = re.compile(m3u_series).findall(content2)
		for iconimage, name, fanart, url, description in match:
			try:
				
				add_dir2(name, url, 143, iconimage, fanart, description)
			
			except:
				pass
	except:
		pass

def m3u_playseries(name,url):	

	name = name.encode('utf-8')		
	url = url.replace('"', ' ').replace('&amp;', '&').strip()
	
	content_db = make_request(url)
	match = re.compile(m3u_capitulos).findall(content_db)
	for iconimage, name, fanart, url in match:
		try:
	
			
			Fontcolor = addon.getSetting('Fontcolor')
			name = '[COLOR %s]' % Fontcolor + name + '[/COLOR]'
			add_serie(name, url, 144, iconimage, fanart)

				
		except:
			pass
		
				

def add_serie(name, url, mode, iconimage, fanart):

	try:
            name = name.encode('utf-8')
        except: pass
	
	u = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode) + "&name=" + urllib.quote_plus(name) + "&iconimage="
	liz = xbmcgui.ListItem(name, iconImage = "DefaultVideo.png", thumbnailImage = iconimage)
	liz.setInfo( type = "Video", infoLabels = { "Title": name } )
	liz.setProperty('fanart_image', fanart)
	liz.setProperty('IsPlayable', 'true') 
	ok = xbmcplugin.addDirectoryItem(handle = int(sys.argv[1]), url = u, listitem = liz)
	return ok


def PLAYSERIE(name,url):


		licencia_addon = addon.getSetting('licencia_addon')
		key_master = '0110nhu'.replace('0110nhu', 'nhu')
		keygen = 'aHR0cHM6Ly9wYXN0ZWJpbi5jb20vcmF3L1Q1ZEtzY0ww'.decode('base64')
		key_ext = addon.getSetting('key_ext')
		content = make_request(keygen)
		match = re.compile(mydb).findall(content)
		for key in match:

			try:
			
			
				licencia_addon = addon.getSetting('licencia_addon')
				
				
				if licencia_addon == key:

#					xbmcgui.Dialog().ok("Realstream Licencia:" , "[COLOR lime]Su llave es correcta![/COLOR] [COLOR gold]Sientese y disfrute de Realstream.[/COLOR]") 
					if 'https://team.com' in url:

						url = url.replace('https://team.com','https://verystream.com')
			
					if 'https://mybox.com' in url:	

						url = url.replace('https://mybox.com','https://uptostream.com')
			
		
					if 'https://vidcloud.co/' in url:
		
						url = url.replace('https://vid.co','https://vidcloud.co')
		
					if 'https://gounlimited.to' in url:
		
						url = url.replace('https://limited.to','https://gounlimited.to')
			
					if 'https://drive.com' in url:
		
						url = url.replace('https://drive.com/','https://drive.google.com/')

		
					import resolveurl
		
					hmf = urlresolver.HostedMediaFile(url)
		
					if not hmf:
						xbmc.executebuiltin("XBMC.Notification(Real Stream, Enlace no soportado para: [COLOR orange]" +name+ "[/COLOR] ,5000)")
						return False

					try:
						dp = xbmcgui.DialogProgress()
						dp.create('Realstream:','Iniciando ...')
						dp.update(30,'RESOLVEURL:','Conectando al servidor ...')
						xbmc.sleep(1000)
						stream_url = hmf.resolve()
						if not stream_url or not isinstance(stream_url, basestring):
							try: msg = stream_url.msg
							except: msg = url
							raise Exception(msg)
					
					except Exception as e:
						try: msg = str(e)
						except: msg = url
						dp.update(45,'RESOLVEURL:','Reiniciando ... ')
						xbmc.sleep(1000)
						xbmc.executebuiltin("XBMC.Notification(Real Stream, Episodio no disponible.  ,3000)")            
						dp.close()
						
					dp.update(60,'RESOLVEURL:','Comprobando que existe el enlace.')
					xbmc.sleep(500)
					dp.update(75,'RESOLVEURL:','Resolviendo enlace ...')
					xbmc.sleep(500)
					dp.update(95,'RESOLVEURL:','Encontrado ...')
					xbmc.sleep(500)
					dp.update(100,'RESOLVEURL:','Disfrute de este capitulo!')
					dp.close()
					notificar = addon.getSetting('notificar')
					listitem = xbmcgui.ListItem(path=stream_url)
					xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, listitem)

				
				else:
		
					notificar = addon.getSetting('notificar')
					if notificar == 'true':
						xbmcgui.Dialog().ok("Realstream:" , "[COLOR red]Por favor compruebe los ajustes de realstream.[/COLOR]","[COLOR white] Desde la seccion Tutoriales puede sacarle mayor partido a su Realstream, tambien puede configurarlo a su gusto. [/COLOR]", "[COLOR gold]El addon no esta activado o bien configurado.[/COLOR]")
					
						MenuColor = addon.getSetting('MenuColor')
						add_dir('[COLOR %s]Video tutoriales[/COLOR]' % MenuColor,u_tube,125,videotutoriales,fanart)
			except:
				pass
	

		

	
def get_info_movie():

    # prompt the user to input search text
    kb = xbmc.Keyboard('', 'Titulo de la pelicula')
    kb.doModal()
    if not kb.isConfirmed():
        return None;
    name = kb.getText().strip()
	

    if xbmc.getCondVisibility('system.platform.android'):
	
	opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'https://www.themoviedb.org/search?query=' +name+ '&language=es-ES'  ) )
	
        
	return 'android'

    elif xbmc.getCondVisibility('system.platform.windows'):
	
	opensite = webbrowser . open('https://www.themoviedb.org/search?query=' +name+ '&language=es-ES')
  
	
	return 'windows'
	
	
def Todas(): 
	
	try:
		
		content = make_request(todas)
		match = re.compile(mydb).findall(content)
		for m3u in match:
		
			try:
		
				all = m3u
				
			except:
				pass
				
		content_db = make_request(all)
		match = re.compile(m3u_regex).findall(content_db)
		for thumb, name, url, id, trailer, description, fanart in match:
			try:
				
				m3u_playlist2(name, url, thumb, id, trailer, description, fanart)
			
			except:
				pass
	except:
		pass
	
def Novedades(): 
	
	try:
		
		novedades = make_request(db)
		match = re.compile(mydb).findall(novedades)
		for m3u in match:
		
			try:
		
				op = m3u
				
			except:
				pass
				
		content2 = make_request(op)
		match = re.compile(m3u_regex).findall(content2)
		for thumb, name, url, id, trailer, description, fanart in match:
			try:
				
				m3u_playlist2(name, url, thumb, id, trailer, description, fanart)
			
			except:
				pass
	except:
		pass
			
def Estrenos():

	try:

		estrenos = make_request(db1)
		match = re.compile(mydb).findall(estrenos)
		for m3u in match:
		
			try:	
				op1 = m3u
			except:
				pass
		
		content = make_request(op1)
		match = re.compile(m3u_regex).findall(content)
		for thumb, name, url, id, trailer, description, fanart in match:
			try:
				
				m3u_playlist2(name, url, thumb, id, trailer, description, fanart)
			
			except:
				pass
	except:
		pass
			
def Recomendadas(): 

	try:
		
		content = make_request(db2)
		match = re.compile(mydb).findall(content)
		for m3u in match:
		
			try:
		
				op2 = m3u
				
			except:
				pass
	
	
		content = make_request(op2)
		match = re.compile(m3u_regex).findall(content)
		for thumb, name, url, id, trailer, description, fanart in match:
			try:
				m3u_playlist2(name, url, thumb, id, trailer, description, fanart)
			
			except:
				pass
	except:
		pass	
		
def Artes_Marciales(): 

	try:
		
		Artes_marciales = make_request(db26)
		match = re.compile(mydb).findall(Artes_marciales)
		for m3u in match:
		
			try:
		
				op26 = m3u
				
			except:
				pass	
	

		content = make_request(op26)
		match = re.compile(m3u_regex).findall(content)
		for thumb, name, url, id, trailer, description, fanart in match:
			try:
			
				m3u_playlist2(name, url, thumb, id, trailer, description, fanart)
			
			except:
				pass
	except:
		pass
				
def Accion(): 

	try:
		
		content = make_request(db3)
		match = re.compile(mydb).findall(content)
		for m3u in match:
		
			try:
		
				op3 = m3u
				
			except:
				pass	
	

		content = make_request(op3)
		match = re.compile(m3u_regex).findall(content)
		for thumb, name, url, id, trailer, description, fanart in match:
			try:
				m3u_playlist2(name, url, thumb, id, trailer, description, fanart)
			
			except:
				pass
	except:
		pass

def Animacion(): 
	
	try:
		
		content = make_request(db4)
		match = re.compile(mydb).findall(content)
		for m3u in match:
		
			try:
		
				op4 = m3u
				
			except:
				pass		
	
		content = make_request(op4)
		match = re.compile(m3u_regex).findall(content)
		for thumb, name, url, id, trailer, description, fanart in match:
			try:
				m3u_playlist2(name, url, thumb, id, trailer, description, fanart)
			
			except:
				pass
	except:
		pass
			
def Aventuras():

	try:
		
		content = make_request(db5)
		match = re.compile(mydb).findall(content)
		for m3u in match:
		
			try:
		
				op5 = m3u
				
			except:
				pass		
	

		content = make_request(op5)
		match = re.compile(m3u_regex).findall(content)
		for thumb, name, url, id, trailer, description, fanart in match:
			try:
				m3u_playlist2(name, url, thumb, id, trailer, description, fanart)
			
			except:
				pass
	except:
		pass
			
def Belico(): 

	try:
		
		content = make_request(db6)
		match = re.compile(mydb).findall(content)
		for m3u in match:
		
			try:
		
				op6 = m3u
				
			except:
				pass	
	

		content = make_request(op6)
		match = re.compile(m3u_regex).findall(content)
		for thumb, name, url, id, trailer, description, fanart in match:
			try:
				m3u_playlist2(name, url, thumb, id, trailer, description, fanart)
			
			except:
				pass
	except:
		pass
			
def Cifi(): 

	try:
		
		content = make_request(db7)
		match = re.compile(mydb).findall(content)
		for m3u in match:
		
			try:
		
				op7 = m3u
				
			except:
				pass		
	

		content = make_request(op7)
		match = re.compile(m3u_regex).findall(content)
		for thumb, name, url, id, trailer, description, fanart in match:
			try:
				m3u_playlist2(name, url, thumb, id, trailer, description, fanart)
			
			except:
				pass
	except:
		pass
		
def Clasico(): 

	try:
		
		content = make_request(db27)
		match = re.compile(mydb).findall(content)
		for m3u in match:
		
			try:
		
				 op27 = m3u
				
			except:
				pass		
	

		content = make_request(op27)
		match = re.compile(m3u_regex).findall(content)
		for thumb, name, url, id, trailer, description, fanart in match:
			try:
				m3u_playlist2(name, url, thumb, id, trailer, description, fanart)
			
			except:
				pass
	except:
		pass
			
			
def Comedia(): 

	try:
		
		content = make_request(db8)
		match = re.compile(mydb).findall(content)
		for m3u in match:
		
			try:
		
				op8 = m3u
				
			except:
				pass		
	

		content = make_request(op8)
		match = re.compile(m3u_regex).findall(content)
		for thumb, name, url, id, trailer, description, fanart in match:
			try:
				m3u_playlist2(name, url, thumb, id, trailer, description, fanart)
			
			except:
				pass
	except:
		pass
			
			
def Crimen(): 

	try:
		
		content = make_request(db9)
		match = re.compile(mydb).findall(content)
		for m3u in match:
		
			try:
		
				op9 = m3u
				
			except:
				pass		
	

		content = make_request(op9)
		match = re.compile(m3u_regex).findall(content)
		for thumb, name, url, id, trailer, description, fanart in match:
			try:
				m3u_playlist2(name, url, thumb, id, trailer, description, fanart)
			
			except:
				pass
				
	except:
		pass
			
			
def Drama(): 

	try:
		
		content = make_request(db10)
		match = re.compile(mydb).findall(content)
		for m3u in match:
		
			try:
		
				op10 = m3u
				
			except:
				pass		
	

		content = make_request(op10)
		match = re.compile(m3u_regex).findall(content)
		for thumb, name, url, id, trailer, description, fanart in match:
			try:
				m3u_playlist2(name, url, thumb, id, trailer, description, fanart)
			
			except:
				pass
				
	except:
		pass
			
def Familiar():
	
	try:
		
		content = make_request(db11)
		match = re.compile(mydb).findall(content)
		for m3u in match:
		
			try:
		
				op11 = m3u
				
			except:
				pass
				
		content = make_request(op11)
		match = re.compile(m3u_regex).findall(content)
		for thumb, name, url, id, trailer, description, fanart in match:
			try:
				m3u_playlist2(name, url, thumb, id, trailer, description, fanart)
			
			except:
				pass
	except:
		pass
			
			
def Fantasia(): 

	try:
		
		content = make_request(db12)
		match = re.compile(mydb).findall(content)
		for m3u in match:
		
			try:
		
				op12 = m3u
				
			except:
				pass
	

		content = make_request(op12)
		match = re.compile(m3u_regex).findall(content)
		for thumb, name, url, id, trailer, description, fanart in match:
			try:
				m3u_playlist2(name, url, thumb, id, trailer, description, fanart)
			
			except:
				pass
	except:
		pass
			
			
def Historia(): 
		
	try:
		
		content = make_request(db13)
		match = re.compile(mydb).findall(content)
		for m3u in match:
		
			try:
		
				op13 = m3u
				
			except:
				pass
		content = make_request(op13)
		match = re.compile(m3u_regex).findall(content)
		for thumb, name, url, id, trailer, description, fanart in match:
			try:
				m3u_playlist2(name, url, thumb, id, trailer, description, fanart)
			
			except:
				pass
	except:
		pass
			
def Misterio():

	try:
		
		content = make_request(db14)
		match = re.compile(mydb).findall(content)
		for m3u in match:
		
			try:
		
				op14 = m3u
				
			except:
				pass
	

		content = make_request(op14)
		match = re.compile(m3u_regex).findall(content)
		for thumb, name, url, id, trailer, description, fanart in match:
			try:
				m3u_playlist2(name, url, thumb, id, trailer, description, fanart)
			
			except:
				pass
	except:
		pass
			
			
def Musical():

	try:
		
		content = make_request(db15)
		match = re.compile(mydb).findall(content)
		for m3u in match:
		
			try:
		
				op15 = m3u
				
			except:
				pass
	

		content = make_request(op15)
		match = re.compile(m3u_regex).findall(content)
		for thumb, name, url, id, trailer, description, fanart in match:
			try:
				m3u_playlist2(name, url, thumb, id, trailer, description, fanart)
			
			except:
				pass
	except:
		pass
			
def Romance():

	try:
		
		content = make_request(db16)
		match = re.compile(mydb).findall(content)
		for m3u in match:
		
			try:
		
				op16 = m3u
				
			except:
				pass
	

		content = make_request(op16)
		match = re.compile(m3u_regex).findall(content)
		for thumb, name, url, id, trailer, description, fanart in match:
			try:
				m3u_playlist2(name, url, thumb, id, trailer, description, fanart)
			
			except:
				pass
	except:
		pass
			
			
def Thriller():

	try:
		
		content = make_request(db17)
		match = re.compile(mydb).findall(content)
		for m3u in match:
		
			try:
		
				op17 = m3u
				
			except:
				pass 
	

		content = make_request(op17)
		match = re.compile(m3u_regex).findall(content)
		for thumb, name, url, id, trailer, description, fanart in match:
			try:
				m3u_playlist2(name, url, thumb, id, trailer, description, fanart)
			
			except:
				pass
	except:
		pass
			
			
def Suspense():

	try:
		
		content = make_request(db18)
		match = re.compile(mydb).findall(content)
		for m3u in match:
		
			try:
		
				op18 = m3u
				
			except:
				pass
	

		content = make_request(op18)
		match = re.compile(m3u_regex).findall(content)
		for thumb, name, url, id, trailer, description, fanart in match:
			try:
				m3u_playlist2(name, url, thumb, id, trailer, description, fanart)
			
			except:
				pass
	except:
		pass
			
			
def Terror(): 

	try:
		
		content = make_request(db19)
		match = re.compile(mydb).findall(content)
		for m3u in match:
		
			try:
		
				op19 = m3u
				
			except:
				pass
	

		content = make_request(op19)
		match = re.compile(m3u_regex).findall(content)
		for thumb, name, url, id, trailer, description, fanart in match:
			try:
				m3u_playlist2(name, url, thumb, id, trailer, description, fanart)
			
			except:
				pass
	except:
		pass
			
			
def Western(): 
	
	try:
		
		content = make_request(db20)
		match = re.compile(mydb).findall(content)
		for m3u in match:
		
			try:
		
				op20 = m3u
				
			except:
				pass
				
		content = make_request(op20)
		match = re.compile(m3u_regex).findall(content)
		for thumb, name, url, id, trailer, description, fanart in match:
			try:
				m3u_playlist2(name, url, thumb, id, trailer, description, fanart)
			
			except:
				pass
	except:
		pass
			
			
def Spain():

	try:
		
		content = make_request(db21)
		match = re.compile(mydb).findall(content)
		for m3u in match:
		
			try:
		
				op21 = m3u
				
			except:
				pass
	

		content = make_request(op21)
		match = re.compile(m3u_regex).findall(content)
		for thumb, name, url, id, trailer, description, fanart in match:
			try:
				m3u_playlist2(name, url, thumb, id, trailer, description, fanart)
			
			except:
				pass
	except:
		pass
			
def Superheroes():

	try:
		
		content = make_request(db22)
		match = re.compile(mydb).findall(content)
		for m3u in match:
		
			try:
		
				op22 = m3u
				
			except:
				pass
		content = make_request(op22)
		match = re.compile(m3u_regex).findall(content)
		for thumb, name, url, id, trailer, description, fanart in match:
			try:
				m3u_playlist2(name, url, thumb, id, trailer, description, fanart)
			
			except:
				pass
	except:
		pass
				
def Sagas(): 
	
	try:
		
		content = make_request(db23)
		match = re.compile(mydb).findall(content)
		for m3u in match:
		
			try:
		
				op23 = m3u
				
			except:
				pass
		content = make_request(op23)
		match = re.compile(m3u_regex).findall(content)
		for thumb, name, url, id, trailer, description, fanart in match:
			try:
				m3u_playlist2(name, url, thumb, id, trailer, description, fanart)
			
			except:
				pass
	except:
		pass
		
def pelis4k(): 
	
	try:
		
		content = make_request(db25)
		match = re.compile(mydb).findall(content)
		for m3u in match:
		
			try:
		
				op25 = m3u
				
			except:
				pass
		content = make_request(op25)
		match = re.compile(m3u_regex).findall(content)
		for thumb, name, url, id, trailer, description, fanart in match:
			try:
				m3u_playlist2(name, url, thumb, id, trailer, description, fanart)
			
			except:
				pass
	except:
		pass
			
def video_tutoriales(): 
	
	try:
		
		content = make_request(db24)
		match = re.compile(mydb).findall(content)
		for m3u in match:
		
			try:
		
				op24 = m3u
				
			except:
				pass
		content = make_request(op24)
		match = re.compile(tutoriales_regex).findall(content)
		for thumb, name, url in match:
			try:
				m3u_videotutoriales(thumb, name, url)
			
			except:
				pass
				
	except:
		pass



def m3u_videotutoriales(thumb, name, url):	
## despues de obtener las url de la lista m3u las muestra.
	name = re.sub('\s+', ' ', name).strip()	
	
	url = url.replace('"', ' ').replace('&amp;', '&').strip()
	if ('youtube.com/user/' in url) or ('youtube.com/channel/' in url) or ('youtube/user/' in url) or ('youtube/channel/' in url):
		if 'tvg-logo' in thumb:				
			thumb = re.compile(m3u_thumb_regex).findall(str(thumb))[0].replace(' ', '%20')
		else:	
			add_dir(name, url, '', icon, fanart)
	else:
		name = '[COLOR white]%s[/COLOR]' % name
			
		if 'tvg-logo' in thumb:				
			thumb = re.compile(m3u_thumb_regex).findall(str(thumb))[0].replace(' ', '%20')
			
			add_video(name, url, 4, iconimage, fanart)

		else:
		
			add_video(name, url, 4, iconimage, fanart)	

def m3u_playlist(name, url, thumb, id, trailer):	
## despues de obtener las url de la lista m3u las muestra.
	name = name.encode('utf-8')		
	url = url.replace('"', ' ').replace('&amp;', '&').strip()
	trailer = trailer.replace('"', ' ').replace('&amp;', '&').strip()
		
	if ('youtube.com/user/' in url) or ('youtube.com/channel/' in url) or ('youtube/user/' in url) or ('youtube/channel/' in url):
		if 'tvg-logo' in thumb:				
			thumb = re.compile(m3u_thumb_regex).findall(str(thumb))[0].replace(' ', '%20')
		else:	
			add_dir(name, url, '', icon, fanart)
	else:
			Fontcolor = addon.getSetting('Fontcolor')
			
			name = '[COLOR %s]' % Fontcolor + name + '[/COLOR]'
			
			if 'tvg-logo' in thumb:				
				thumb = re.compile(m3u_thumb_regex).findall(str(thumb))[0].replace(' ', '%20')
				selecton = addon.getSetting('selecton')
				if selecton == 'true':
					
					add_link(name, url, 1, thumb, thumb, id, trailer)
					
				else:
				
					add_link(name, url, 130, thumb, thumb, id, trailer)

			else:
			
				if selecton == 'true':
					
					add_link(name, url, 1, thumb, thumb, id, trailer)
					
				else:
				
					add_link(name, url, 130, thumb, thumb, id, trailer)	

					
def m3u_playlist2(name, url, thumb, id, trailer, description, fanart):	
## despues de obtener las url de la lista m3u las muestra.
			
	url = url.replace('"', ' ').replace('&amp;', '&').strip()
	trailer = trailer.replace('"', ' ').replace('&amp;', '&').strip()
	Fontcolor = addon.getSetting('Fontcolor')
	fanart = fanart.replace('"', ' ').replace('&amp;', '&').strip()
	name = '[COLOR %s]' % Fontcolor + name + '[/COLOR]'
			
	if 'tvg-logo' in thumb:				
		thumb = re.compile(m3u_thumb_regex).findall(str(thumb))[0].replace(' ', '%20')
		selecton = addon.getSetting('selecton')
		if selecton == 'true':
					
			add_link2(name, url, 1, thumb, fanart, id, trailer, description)
					
		else:
				
			add_link2(name, url, 130, thumb, fanart, id, trailer, description)

	else:
			
		if selecton == 'true':
					
			add_link2(name, url, 1, thumb, fanart, id, trailer, description)
					
		else:
				
			add_link2(name, url, 130, thumb, fanart, id, trailer, description)		


           
def play_video(name,trailer):

	if notificar == 'true':	
		xbmc.executebuiltin("XBMC.Notification(Realstream, Reproduciendo Trailer de: [COLOR green]" +name+ "[/COLOR] ,5000)")

		url = 'plugin://plugin.video.youtube/play/?video_id=%s' % trailer
		media_url = url
		item = xbmcgui.ListItem(name, trailer, path = media_url)
		xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)
	else:
		url = 'plugin://plugin.video.youtube/play/?video_id=%s' % trailer
		media_url = url
		item = xbmcgui.ListItem(name, trailer, path = media_url)
		xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)
		
		
def play_box(name,url):

	if notificar == 'true':	
	
		try:
						
			dp = xbmcgui.DialogProgress()
			dp.create('Realstream:','Iniciando ...')
			dp.update(30,'Realstream:','Conectando al servidor ...')
			xbmc.sleep(1000)
			dp.update(75,'RESOLVEURL:','Resolviendo enlace ...')
			xbmc.sleep(500)
			dp.update(100,'RESOLVEURL:','Disfrute de la pelicula!')
			dp.close()
		
			media_url = url
			item = xbmcgui.ListItem(name, trailer, path = media_url)
			xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)
			
		except: xbmc.executebuiltin("XBMC.Notification(Real Stream, Enlace borrado o no encontrado. ,3000)")  
		
	else:
	
		try:
	
			dp = xbmcgui.DialogProgress()
			dp.create('Realstream:','Iniciando ...')
			dp.update(30,'Realstream:','Conectando al servidor ...')
			xbmc.sleep(1000)
			dp.update(75,'RESOLVEURL:','Resolviendo enlace ...')
			xbmc.sleep(500)
			dp.update(100,'RESOLVEURL:','Disfrute de la pelicula!')
			dp.close()
	
			media_url = url
			item = xbmcgui.ListItem(name, trailer, path = media_url)
			xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)
			
		except: xbmc.executebuiltin("XBMC.Notification(Real Stream, Enlace borrado o no encontrado. ,3000)") 
		
	return
		
		
def play_TRAILER(trailer):

	if 'https://www.youtube.com' in trailer:
	
		try:
	
			import resolveurl
		
			hmf = urlresolver.HostedMediaFile(url)
			dp = xbmcgui.DialogProgress()
			dp.create('Realstream:','Conectando al servidor ... ')
			dp.update(20,'Por favor, espere ...')
			xbmc.sleep(500)
		
			if not hmf:
				xbmc.executebuiltin("XBMC.Notification(Real Stream, Enlace borrado o no encontrado. Prueba a reiniciar el router o poner una VPN. ,5000)")            
				return False

			try:
			
				dp.update(50,'RESOLVEURL:','Comprobando que existe el enlace.')
				xbmc.sleep(500)
				stream_url = hmf.resolve()
				if not stream_url or not isinstance(stream_url, basestring):
					try: msg = stream_url.msg
					except: msg = stream_url
					raise Exception(msg)
			except Exception as e:
				try: msg = str(e)
				except: msg = stream_url
				dp.update(100,'RESOLVEURL:','Enlace borrado o no es accesible con tu actual IP. Cambia de ip o reinicia tu Router.')
				dp.close()
				xbmc.executebuiltin("XBMC.Notification(Real Stream,Enlace borrado o no encontrado. Prueba a reiniciar el router o poner una VPN. ,5000)")            

			dp.update(50,'RESOLVEURL:','Comprobando si existe el enlace.')
			xbmc.sleep(500)
			dp.update(75,'RESOLVEURL:','Resolviendo enlace ...')
			xbmc.sleep(500)
			dp.update(95,'RESOLVEURL:','Encontrado ...')
			xbmc.sleep(500)
			dp.update(100,'RESOLVEURL:','Disfrute de la pelicula!')
			dp.close()

			listitem = xbmcgui.ListItem(path=stream_url)
			xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, listitem)
		
		except:
			pass

		else:
		
			url = 'plugin://plugin.video.youtube/play/?video_id=%s' % trailer
			media_url = url
			item = xbmcgui.ListItem(trailer, path = media_url)
			xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)
			return

def PLAYVIDEO(name,url):

		if '[Youtube]' in name:
		
			url = 'plugin://plugin.video.youtube/play/?video_id=%s' % url
			media_url = url
			item = xbmcgui.ListItem(trailer, path = media_url)
			xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)
	
			
		else:
		
			import urlresolver
			from urlresolver import common
    
			hmf = urlresolver.HostedMediaFile(url)

			if not hmf:
				xbmc.executebuiltin("XBMC.Notification(Real Stream, Enlace no soportado para: [COLOR orange]" +name+ "[/COLOR] ,7500)")
				return False


			try:
				stream_url = hmf.resolve()
				if not stream_url or not isinstance(stream_url, basestring):
					try: msg = stream_url.msg
					except: msg = url
					raise Exception(msg)
			except Exception as e:
				try: msg = str(e)
				except: msg = url
				xbmc.executebuiltin("XBMC.Notification(Real Stream, [COLOR red]Enlace no encontrado:[/COLOR] [COLOR orange]" +name+ "[/COLOR] ,7500)")            
				return False
   
			notificar = addon.getSetting('notificar')
			if notificar == 'true':
				xbmc.executebuiltin("XBMC.Notification(Real Stream,[COLOR lime] reproduciendo: [/COLOR][COLOR orange]" +name+ "[/COLOR] ,7500)")	
			listitem = xbmcgui.ListItem(path=stream_url)
			xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, listitem)

		
		return
	
def PLAYVIDEO2(name,url):
		
		import resolveurl
		
		hmf = urlresolver.HostedMediaFile(url)
		dp = xbmcgui.DialogProgress()
		dp.create('Realstream:','Conectando al servidor ... ')
		dp.update(20,'Por favor, espere ...')
		xbmc.sleep(500)
		
		if not hmf:
			xbmc.executebuiltin("XBMC.Notification(Real Stream, Enlace borrado o no encontrado. Prueba a reiniciar el router o poner una VPN. ,5000)")            
			return False

		try:
			
			dp.update(50,'RESOLVEURL:','Comprobando que existe el enlace.')
			xbmc.sleep(500)
			stream_url = hmf.resolve()
			if not stream_url or not isinstance(stream_url, basestring):
				try: msg = stream_url.msg
				except: msg = stream_url
				raise Exception(msg)
		except Exception as e:
			try: msg = str(e)
			except: msg = stream_url
			dp.update(100,'RESOLVEURL:','Enlace borrado o no es accesible con tu actual IP. Cambia de ip o reinicia tu Router.')
			dp.close()
			xbmc.executebuiltin("XBMC.Notification(Real Stream,Enlace borrado o no encontrado. Prueba a reiniciar el router o poner una VPN. ,5000)")            

		dp.update(50,'RESOLVEURL:','Comprobando si existe el enlace.')
		xbmc.sleep(500)
		dp.update(75,'RESOLVEURL:','Resolviendo enlace ...')
		xbmc.sleep(500)
		dp.update(95,'RESOLVEURL:','Encontrado ...')
		xbmc.sleep(500)
		dp.update(100,'RESOLVEURL:','Disfrute de la pelicula!')
		dp.close()
		notificar = addon.getSetting('notificar')
		

		if '[Realstream]' or '[Mybox]' in name:
			restante = addon.getSetting('restante')
		elif restante == 'true':
			dialog = xbmcgui.Dialog()
			ok = dialog.ok("[COLOR orange]Real Stream: (Restriccion por IP del Servidor)[/COLOR]" , "[COLOR gold]Tiempo maximo de uso del servidor Realstream es de [/COLOR][COLOR lime]120 min. [/COLOR] [COLOR blue]Con tu actual IP.[/COLOR]" , "[COLOR gold]una vez finalizado puedes Apagar tu router y esperar 5 min.[/COLOR]" , "[COLOR gold]Tambien puedes utilizar una VPN para cambiar tu ip pública. Esto te dará otras dos horas de uso.[/COLOR]")
		listitem = xbmcgui.ListItem(path=stream_url)
		xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, listitem)
	
def PLAYVIDEO2(name,url):


	if 'https://www.rapidvideo.com/v/' in url:
				
		content = make_request(url)
		match = re.compile('rapidvideo').findall(content)
		for url in match:
		
			
			try:
				notificar = addon.getSetting('notificar')
				if notificar == 'true':
					xbmc.executebuiltin("XBMC.Notification(Real Stream,[COLOR lime] reproduciendo: [/COLOR][COLOR orange]" +name+ "[/COLOR] ,7500)")	
				listitem = xbmcgui.ListItem(path = url)
				xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, listitem)	
				
			except: xbmc.executebuiltin("XBMC.Notification(Real Stream, [COLOR red]Enlace no encontrado:[/COLOR] [COLOR orange]" +name+ "[/COLOR] ,7500)")  
		
	
	else:
	
		import urlresolver
		from urlresolver import common
    
		hmf = urlresolver.HostedMediaFile(url)

		if not hmf:
			xbmc.executebuiltin("XBMC.Notification(Real Stream, Enlace no soportado para: [COLOR orange]" +name+ "[/COLOR] ,7500)")
			return False


		try:
			stream_url = hmf.resolve()
			if not stream_url or not isinstance(stream_url, basestring):
				try: msg = stream_url.msg
				except: msg = url
				raise Exception(msg)
		except Exception as e:
			try: msg = str(e)
			except: msg = url
			xbmc.executebuiltin("XBMC.Notification(Real Stream, [COLOR red]Enlace no encontrado:[/COLOR] [COLOR orange]" +name+ "[/COLOR] ,7500)")            
			return False
   
		notificar = addon.getSetting('notificar')
		if notificar == 'true':
			xbmc.executebuiltin("XBMC.Notification(Real Stream,[COLOR lime] reproduciendo: [/COLOR][COLOR orange]" +name+ "[/COLOR] ,7500)")	
		listitem = xbmcgui.ListItem(path=stream_url)
		xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, listitem)
		
	return


	
def PLAYVIDEO3(name,url):

		stream_url = url
		notificar = addon.getSetting('notificar')
		if notificar == 'true':
			xbmc.executebuiltin("XBMC.Notification(Real Stream,[COLOR lime] reproduciendo: [/COLOR][COLOR orange]" +name+ "[/COLOR] ,7500)")	
			listitem = xbmcgui.ListItem(path=stream_url)
			xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, listitem)
		else: 
			listitem = xbmcgui.ListItem(path=stream_url)
			xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, listitem)			
		return

def PLAYVIDEO4(name,url):


	if '[Youtube]' in name:
		
		url = 'plugin://plugin.video.youtube/play/?video_id=%s' % url
			
		try:
			notificar = addon.getSetting('notificar')
			if notificar == 'true':
				xbmc.executebuiltin("XBMC.Notification(Real Stream,[COLOR lime] reproduciendo: [/COLOR][COLOR orange]" +name+ "[/COLOR] ,7500)")	
				listitem = xbmcgui.ListItem(path = url)
				xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, listitem)	
				
			
				
		except: xbmc.executebuiltin("XBMC.Notification(Real Stream, [COLOR red]Enlace no encontrado, tiempo excedido en servidor. Utilíza una vpn o apaga el router 5 min.[/COLOR] [COLOR orange]" +name+ "[/COLOR] ,7500)")  

		
	else:
	
		import xbmcgui
		import urlresolver
		from urlresolver import common
    
		hmf = urlresolver.HostedMediaFile(url)

		if not hmf:
			xbmc.executebuiltin("XBMC.Notification(Real Stream, Enlace no soportado para: [COLOR orange]" +name+ "[/COLOR] ,7500)")
			return False
		
		import resolveurl as urlresolver
		
		hmf = urlresolver.HostedMediaFile(url)
		
		
		if not hmf:
			xbmc.executebuiltin("XBMC.Notification(Real Stream, Enlace no soportado para: [COLOR orange]" +name+ "[/COLOR] ,7500)")
			return False

		try:
			stream_url = hmf.resolve()
			if not stream_url or not isinstance(stream_url, basestring):
				try: msg = stream_url.msg
				except: msg = url
				raise Exception(msg)
		except Exception as e:
			try: msg = str(e)
			except: msg = url
			xbmc.executebuiltin("XBMC.Notification(Real Stream, [COLOR red]Enlace no encontrado:[/COLOR] [COLOR orange]" +name+ "[/COLOR] ,7500)")            
			return False
				
		
			
		notificar = addon.getSetting('notificar')
		if notificar == 'true':
			xbmc.executebuiltin("XBMC.Notification(Real Stream,[COLOR lime] reproduciendo: [/COLOR][COLOR orange]" +name+ "[/COLOR] ,7500)")

			if '[Realstream]' in name:
		
				restante = addon.getSetting('restante')
				if restante == 'true':
					dialog = xbmcgui.Dialog()
					ok = dialog.ok("[COLOR orange]Real Stream: (Restriccion por IP del Servidor)[/COLOR]" , "[COLOR gold]Tiempo maximo de uso del servidor Realstream es de [/COLOR][COLOR lime]120 min. [/COLOR] [COLOR blue]Con tu actual IP.[/COLOR]" , "[COLOR gold]una vez finalizado puedes Apagar tu router y esperar 5 min.[/COLOR]" , "[COLOR gold]Tambien puedes utilizar una VPN para cambiar tu ip pública. Esto te dará otras dos horas de uso.[/COLOR]")
   
			listitem = xbmcgui.ListItem(path=stream_url)
			xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, listitem)
		
		
		
	return
	

	
def PLAYVIDEO5(name,url):


	if '[Youtube]' in name:
		
		url = 'plugin://plugin.video.youtube/play/?video_id=%s' % url
			
		try:
			notificar = addon.getSetting('notificar')
			if notificar == 'true':
				xbmc.executebuiltin("XBMC.Notification(Real Stream,[COLOR lime] reproduciendo: [/COLOR][COLOR orange]" +name+ "[/COLOR] ,7500)")	
				listitem = xbmcgui.ListItem(path = url)
				xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, listitem)	
				
			
				
		except: xbmc.executebuiltin("XBMC.Notification(Real Stream, [COLOR red]Enlace no encontrado, tiempo excedido en servidor. Utilíza una vpn o apaga el router 5 min.[/COLOR] [COLOR orange]" +name+ "[/COLOR] ,7500)")  

	else:
		
		import resolveurl
		
		hmf = urlresolver.HostedMediaFile(url)
		
		
		if not hmf:
			xbmc.executebuiltin("XBMC.Notification(Real Stream, Enlace no soportado para: [COLOR orange]" +name+ "[/COLOR] ,5000)")
			return False

		try:
			stream_url = hmf.resolve()
			if not stream_url or not isinstance(stream_url, basestring):
				try: msg = stream_url.msg
				except: msg = url
				raise Exception(msg)
		except Exception as e:
			try: msg = str(e)
			except: msg = url
			xbmc.executebuiltin("XBMC.Notification(Real Stream, [COLOR red]Enlace no encontrado:[/COLOR] [COLOR orange]" +name+ "[/COLOR] ,5000)")            
			return False
				
		
			
		notificar = addon.getSetting('notificar')
		if notificar == 'true':
			xbmc.executebuiltin("XBMC.Notification(Real Stream,[COLOR lime] reproduciendo: [/COLOR][COLOR orange]" +name+ "[/COLOR] ,7500)")

			if 'uptostream.com' or 'uptobox.com' in url:
		
				restante = addon.getSetting('restante')
				if restante == 'true':
					dialog = xbmcgui.Dialog()
					ok = dialog.ok("[COLOR orange]Real Stream: (Restriccion por IP del Servidor)[/COLOR]" , "[COLOR gold]Tiempo maximo de uso del servidor Realstream es de [/COLOR][COLOR lime]120 min. [/COLOR] [COLOR blue]Con tu actual IP.[/COLOR]" , "[COLOR gold]una vez finalizado puedes Apagar tu router y esperar 5 min.[/COLOR]" , "[COLOR gold]Tambien puedes utilizar una VPN para cambiar tu ip pública. Esto te dará otras dos horas de uso.[/COLOR]")
   
			listitem = xbmcgui.ListItem(path=stream_url)
			xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, listitem)
		
		
		
	return	
	
def PLAYVIDEO6(name,url):


	if '[Youtube]' in name:
		
		url = 'plugin://plugin.video.youtube/play/?video_id=%s' % url
			
		try:
			notificar = addon.getSetting('notificar')
			if notificar == 'true':
				xbmc.executebuiltin("XBMC.Notification(Real Stream,[COLOR lime] reproduciendo: [/COLOR][COLOR orange]" +name+ "[/COLOR] ,7500)")	
				listitem = xbmcgui.ListItem(path = url)
				xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, listitem)	
				
		except:
			xbmc.executebuiltin("XBMC.Notification(Real Stream, [COLOR red]Enlace no encontrado, tiempo excedido en servidor. Utilíza una vpn o apaga el router 5 min.[/COLOR] [COLOR orange]" +name+ "[/COLOR] ,7500)")  
			pass	
		
	else:
	
		if 'https://team.com' in url:

			url = url.replace('https://team.com','https://verystream.com')
		
			
		if 'https://drive.com' in url:
		
			url = url.replace('https://drive.com','https://drive.google.com')
		
		if 'https://vid.co' in url:
		
			url = url.replace('https://vid.co','https://vidcloud.co')
		
		if 'https://limited.to' in url:
		
			url = url.replace('https://limited.to','https://gounlimited.to')
		
		import resolveurl
		
		hmf = urlresolver.HostedMediaFile(url)
		
		
		if not hmf:
			xbmc.executebuiltin("XBMC.Notification(Real Stream, Enlace no encontrado para: [COLOR orange]" +name+ "[/COLOR] ,5000)")
			return False

		try:
			stream_url = hmf.resolve()
			if not stream_url or not isinstance(stream_url, basestring):
				try: msg = stream_url.msg
				except: msg = url
				raise Exception(msg)
		except Exception as e:
			try: msg = str(e)
			except: msg = url
			xbmc.executebuiltin("XBMC.Notification(Real Stream, [COLOR red]Enlace borrado, o no encontrado. Prueba a reiniciar el router o poner una VPN.[/COLOR]  ,5000)")            
			return False
				
		
			
			notificar = addon.getSetting('notificar')
			if notificar == 'true':
				xbmc.executebuiltin("XBMC.Notification(Real Stream,[COLOR lime] reproduciendo: [/COLOR][COLOR orange]" +name+ "[/COLOR] ,5000)")

				if 'uptostream.com' or 'uptobox.com' in url:
					restante = addon.getSetting('restante')
				elif restante == 'true':
					dialog = xbmcgui.Dialog()
					ok = dialog.ok("[COLOR orange]Real Stream: (Restriccion por IP del Servidor)[/COLOR]" , "[COLOR gold]Tiempo maximo de uso del servidor Realstream es de [/COLOR][COLOR lime]120 min. [/COLOR] [COLOR blue]Con tu actual IP.[/COLOR]" , "[COLOR gold]una vez finalizado puedes Apagar tu router y esperar 5 min.[/COLOR]" , "[COLOR gold]Tambien puedes utilizar una VPN para cambiar tu ip pública. Esto te dará otras dos horas de uso.[/COLOR]")
				
		listitem = xbmcgui.ListItem(path=stream_url)
		xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, listitem)
		
	return
	

def PLAYVIDEO7(name,url):

	if 'mybox.com' in url:
	
		url = url.replace('https://mybox.com','https://uptostream.com')
		
		try:
		
			content = make_request(url)
			match = re.compile(upto_regex).findall(content)
			for url,cal,lag in match:
			
				cal = cal.replace('","res":"1080",','').replace('","res":"720",','').replace('","res":"480",','').replace('","res":"360",','')
				url = url.replace('\/','/')
				url = url.replace(',"type":"video/mp4",',' ')
				name = '[COLOR white]' +cal+ '[/COLOR] - [COLOR gold]' +lag+ '[/COLOR]'

				options = []
				options.append('[COLOR orange]Real Stream: [/COLOR][COLOR gold]1. Mostrar mas info. [Reiniciar][/COLOR]')
				options.append('[COLOR gold]2. Mostar otras calidades disponibles [/COLOR]')
				options.append('[COLOR gold]3. Ver en: %s [/COLOR]' % name)
				

				header = 'Seleccione una calidad e idioma:'
				dialog = xbmcgui.Dialog()
				ret = dialog.select(header, options)

				
				
				if ret == 0:
					
					ok = dialog.ok("[COLOR darkpink]REALSTREAM:[/COLOR] ","[COLOR gold]  Reiniciadas las opciones.  [/COLOR]","")
					del dialog	
					return
		
				elif ret == 1:
						
					pass
					
					del dialog
					
				
				elif ret == 2:
				
					play_box(name,url)
					
					return

		except:
			pass
			
	elif 'uptostream.com' in url:

		try:
		
			content = make_request(url)
			match = re.compile(upto_regex).findall(content)
			for url,cal,lag in match:
		
				cal = cal.replace('","res":"1080",','').replace('","res":"720",','').replace('","res":"480",','').replace('","res":"360",','')
				url = url.replace('\/','/')
				url = url.replace(',"type":"video/mp4",',' ')
				name = '[COLOR white]Calidad: ' +cal+ '[/COLOR] [COLOR gold]Idioma: ' +lag+ '[/COLOR]'

				options = []
				options.append('[COLOR white]Reiniciar calidades disponibles[/COLOR]')
				options.append('[COLOR white]Otras calidades e idiomas[/COLOR]')
				options.append('[COLOR white]Ver en: %s ' % name)
				

				header = 'Seleccione una calidad e idioma:'
				dialog = xbmcgui.Dialog()
				ret = dialog.select(header, options)

				
				if ret == 0:
					
					ok = dialog.ok("[COLOR darkpink]REALSTREAM:[/COLOR] ","[COLOR gold]  Reiniciadas las opciones.  [/COLOR]","")
					del dialog	
					return
		
				elif ret == 1:
						
					pass
					
					del dialog
					
					
					
				
				elif ret == 2:
				
					play_box(name,url)
					
					return

		except:
			pass
	else:
	
		licencia_addon = addon.getSetting('licencia_addon')
		key_master = '0110nhu'.replace('0110nhu', 'nhu')
		keygen = 'aHR0cHM6Ly9wYXN0ZWJpbi5jb20vcmF3L1Q1ZEtzY0ww'.decode('base64')
		key_ext = addon.getSetting('key_ext')
		content = make_request(keygen)
		match = re.compile(mydb).findall(content)
		for key in match:

			try:
			
			
				licencia_addon = addon.getSetting('licencia_addon')
				
				
				if licencia_addon == key:


					if 'https://team.com' in url:

						url = url.replace('https://team.com','https://verystream.com')
			
					if 'https://mybox.com' in url:	

						url = url.replace('https://mybox.com','https://uptostream.com')
			
		
					if 'https://vidcloud.co/' in url:
		
						url = url.replace('https://vid.co','https://vidcloud.co')
		
					if 'https://gounlimited.to' in url:
		
						url = url.replace('https://limited.to','https://gounlimited.to')
			
					if 'https://drive.com' in url:
		
						url = url.replace('https://drive.com/','https://drive.google.com/')

		
					import resolveurl
		
					hmf = urlresolver.HostedMediaFile(url)
		
					if not hmf:
						xbmc.executebuiltin("XBMC.Notification(Real Stream, Enlace no soportado para: [COLOR orange]" +name+ "[/COLOR] ,5000)")
						return False

					try:
						
						dp = xbmcgui.DialogProgress()
						dp.create('Realstream:','Iniciando ...')
						dp.update(30,'RESOLVEURL:','Conectando al servidor ...')
						xbmc.sleep(1000)

						stream_url = hmf.resolve()
						if not stream_url or not isinstance(stream_url, basestring):
							
							try: msg = stream_url.msg
							except: msg = url
							raise Exception(msg)
					
					except Exception as e:
						try: msg = str(e)
						except: msg = url

						

						for i in [0,1,2,3,4,5]:
							a = 1
							dp.update(45,'RESOLVEURL: [COLOR orange]Reiniciando en:[/COLOR][COLOR yellow] %s Seg. [/COLOR] [COLOR blue]Puede cancelar en cualquier momento o esperar ...[/COLOR]' % i )
							xbmc.sleep(1000)
							xbmc.executebuiltin("XBMC.Notification(Real Stream, Intento %s de 5  Puede cancelar cuando desee o esperar...,  1000)" %a)
							dp.close()	
							
						for i in [0,1,2,3,4,5]:
							a = 2
							dp.update(48,'RESOLVEURL: [COLOR orange]Reiniciando en:[/COLOR][COLOR yellow] %s Seg. [/COLOR] [COLOR blue]Puede cancelar en cualquier momento o esperar ...[/COLOR]' % i )
							xbmc.sleep(1000)
							xbmc.executebuiltin("XBMC.Notification(Real Stream, Intento %s de 5 Puede cancelar cuando desee o esperar...,  1000)" %a)
							dp.close()
						for i in [0,1,2,3,4,5]:
							a = 3
							dp.update(50,'RESOLVEURL: [COLOR orange]Reiniciando en:[/COLOR][COLOR yellow] %s Seg. [/COLOR] [COLOR blue]Puede cancelar en cualquier momento o esperar ...[/COLOR]' % i )
							xbmc.sleep(1000)
							xbmc.executebuiltin("XBMC.Notification(Real Stream, Intento %s de 5 Puede cancelar cuando desee o esperar...,  1000)" %a)
							dp.close()
						for i in [0,1,2,3,4,5]:
							a = 4
							dp.update(53,'RESOLVEURL: [COLOR orange]Reiniciando en:[/COLOR][COLOR yellow] %s Seg. [/COLOR] [COLOR blue]Puede cancelar en cualquier momento o esperar ...[/COLOR]' % i )
							xbmc.sleep(1000)
							xbmc.executebuiltin("XBMC.Notification(Real Stream, Intento %s de 5 Puede cancelar cuando desee o esperar...,  1000)" %a)
							dp.close()							
						for i in [0,1,2,3,4,5]:
							a = 5
							dp.update(55,'RESOLVEURL: [COLOR orange]Reiniciando en:[/COLOR][COLOR yellow] %s Seg. [/COLOR] [COLOR blue]Puede cancelar en cualquier momento o esperar ...[/COLOR]' % i )
							xbmc.sleep(1000)
							xbmc.executebuiltin("XBMC.Notification(Real Stream, Intento %s de 5 Puede cancelar cuando desee o esperar...,  1000)" %a)
							dp.close()						
							
						if dp.iscanceled(): 
							xbmc.executebuiltin("XBMC.Notification(Real Stream, Cancelando !! , 2000)") 
							dp.close()
							break
							
					
					
					dp.update(60,'RESOLVEURL:','Comprobando que existe el enlace.')
					xbmc.sleep(500)
					dp.update(75,'RESOLVEURL:','Resolviendo enlace ...')
					xbmc.sleep(1000)
					dp.update(100,'RESOLVEURL:','Disfrute de la pelicula!')
					dp.close()
					notificar = addon.getSetting('notificar')
					listitem = xbmcgui.ListItem(path=stream_url)
					xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, listitem)

				
				else:
		
					xbmcgui.Dialog().ok("Realstream:" , "[COLOR red]Llave incorrecta o no esta vigente![/COLOR] [COLOR gold] El addon no ha podido conectar al servidor.[/COLOR]")
					return False
				
			except:
				pass
				
	return
				
		


def get_params():

	param = []
	paramstring = sys.argv[2]
	if len(paramstring)>= 2:
		params = sys.argv[2]
		cleanedparams = params.replace('?', '')
		if (params[len(params)-1] == '/'):
			params = params[0:len(params)-2]
		pairsofparams = cleanedparams.split('&')
		param = {}
		for i in range(len(pairsofparams)):
			splitparams = {}
			splitparams = pairsofparams[i].split('=')
			if (len(splitparams)) == 2:
				param[splitparams[0]] = splitparams[1]
	return param
	

def resolver_settings():
    try:
        import resolveurl
        xbmcaddon.Addon('script.module.resolveurl').openSettings()
    except:
        import urlresolver
        xbmcaddon.Addon('script.module.urlresolver').openSettings()

def ThemovieDB():
    dialog = xbmcgui.Dialog()
    list = (
        opc1,
        opc2
        )
        
    call = dialog.select('[B][COLOR=orange]The Movie db[/COLOR][/B]', [
	'[COLOR=%s]Accede a themoviedb.com[/COLOR]' % MenuColor, 
    
	'[B][COLOR=white]                           Volver al Menu [/COLOR][/B]',])

    if call:
        # esc is not pressed
        if call < 0:
            return
        func = list[call-2]
        return func()
    else:
        func = list[call]
        return func()
    return 

def platform():
    if xbmc.getCondVisibility('system.platform.android'):
        return 'android'
    elif xbmc.getCondVisibility('system.platform.linux'):
        return 'linux'
    elif xbmc.getCondVisibility('system.platform.windows'):
        return 'windows'
    elif xbmc.getCondVisibility('system.platform.osx'):
        return 'osx'
    elif xbmc.getCondVisibility('system.platform.atv2'):
        return 'atv2'
    elif xbmc.getCondVisibility('system.platform.ios'):
        return 'ios'

myplatform = platform()

def opc1():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'https://www.themoviedb.org/movie/' ) )
    else:
        opensite = webbrowser . open('https://www.themoviedb.org/movie/')

        
def opc2():

    main()
	
	
	
def PAIR():
    dialog = xbmcgui.Dialog()
    funcs = (
        functionA,
        functionB
        )
        
    call = dialog.select('[B][COLOR=yellow]Autoriza tu dispositivo[/COLOR][/B]', [
	'[COLOR=orange]                       Pair OpenLoad [/COLOR]', 
    
	'[B][COLOR=lime]                           Volver al Menu [/COLOR][/B]',])

    if call:
        # esc is not pressed
        if call < 0:
            return
        func = funcs[call-2]
        return func()
    else:
        func = funcs[call]
        return func()
    return 

def platform():
    if xbmc.getCondVisibility('system.platform.android'):
        return 'android'
    elif xbmc.getCondVisibility('system.platform.linux'):
        return 'linux'
    elif xbmc.getCondVisibility('system.platform.windows'):
        return 'windows'
    elif xbmc.getCondVisibility('system.platform.osx'):
        return 'osx'
    elif xbmc.getCondVisibility('system.platform.atv2'):
        return 'atv2'
    elif xbmc.getCondVisibility('system.platform.ios'):
        return 'ios'

myplatform = platform()

def functionA():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'https://olpair.com/' ) )
    else:
        opensite = webbrowser . open('https://olpair.com/')

        
def functionB():

    main()
	

def selector(name, url, id, trailer):
    dialog = xbmcgui.Dialog()
    funcs = (
        function1,
		play_trailer,
		function2,
		ThemovieDB,
		functionsalir
        )
        
    call = dialog.select('[COLOR=orange]REAL STREAM MENU:[/COLOR]', [
	
	'[COLOR=%s]                                                 [B]Ver Pelicula[/B] [/COLOR]' % MenuColor, 
		
	'[COLOR=%s]                                                   [B]Ver Trailer[/B][/COLOR]' % MenuColor,
    
	'[COLOR=%s]                                          [B]Abrir informacion extendida  [/B][/COLOR]' % MenuColor,
	
	'[COLOR=%s]                                           [B]Accede a la web MovieDB[/B][/COLOR]' % MenuColor,
	
	'[COLOR=%s]                                                     [B]Salir[/B][/COLOR]' % MenuColor])

    if call:
        # esc is not pressed
        if call < 0:
            return
        func = funcs[call-5]
        return func()
    else:
        func = funcs[call]
        return func()
    return 



def function1():
    
	PLAYVIDEO7(name,url)
		
def play_trailer():

	play_video(name,trailer)
		
def function2():
    
    if xbmc.getCondVisibility('System.HasAddon(script.extendedinfo)'):
	movie_id = id
	
	xbmc.executebuiltin( "RunScript(script.extendedinfo,info=extendedinfo,id=%s)" % movie_id )

    if notificar == 'true':	
	
		xbmc.executebuiltin("XBMC.Notification(Extended Info,Abriendo: [COLOR green]" +name+ "[/COLOR] ,5000)")
	
def goThemovieDB():

    ThemovieDB()
	
def functionsalir():

    menu()	
def add_dir(name, url, mode, iconimage, fanart):
## Añadre los directorios del menu. Con sus respetivos iconos y fanart y los enlaces a las acciones a enprender por el addon.
	u = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode) + "&name=" + urllib.quote_plus(name) + "&iconimage=" + urllib.quote_plus(iconimage)
	ok = True
	liz = xbmcgui.ListItem(name, iconImage = "DefaultFolder.png", thumbnailImage = iconimage)
	liz.setInfo( type = "Video", infoLabels = { "Title": name } )
	liz.setProperty('fanart_image', fanart)
	if ('youtube.com/user/' in url) or ('youtube.com/channel/' in url) or ('youtube/user/' in url) or ('youtube/channel/' in url):
		u = 'plugin://plugin.video.youtube/%s/%s/' % (url.split( '/' )[-2], url.split( '/' )[-1])
		ok = xbmcplugin.addDirectoryItem(handle = int(sys.argv[1]), url = u, listitem = liz, isFolder = True)
		return ok		
	ok = xbmcplugin.addDirectoryItem(handle = int(sys.argv[1]), url = u, listitem = liz, isFolder = True)
	return ok
	
def add_dir2(name, url, mode, iconimage, fanart, description):
## Añadre los directorios del menu. Con sus respetivos iconos y fanart y los enlaces a las acciones a enprender por el addon.
	u = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode) + "&name=" + urllib.quote_plus(name) + "&iconimage=" + urllib.quote_plus(iconimage)
	ok = True
	liz = xbmcgui.ListItem(name, iconImage = "DefaultFolder.png", thumbnailImage = iconimage)
	liz.setInfo( type = "Video", infoLabels = { "Title": name, "Plot": description } )
	liz.setProperty('fanart_image', fanart)	
	ok = xbmcplugin.addDirectoryItem(handle = int(sys.argv[1]), url = u, listitem = liz, isFolder = True)
	return ok
	
def add_dir3(name, url, mode, iconimage):
## Añadre los directorios del menu. Con sus respetivos iconos y fanart y los enlaces a las acciones a enprender por el addon.
	u = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode) + "&name=" + urllib.quote_plus(name) + "&iconimage=" + urllib.quote_plus(iconimage)
	ok = True
	liz = xbmcgui.ListItem(name, iconImage = "DefaultFolder.png", thumbnailImage = iconimage)
	liz.setInfo( type = "Video", infoLabels = { "Title": name, "Plot": description } )
	liz.setProperty('fanart_image', fanart)	
	ok = xbmcplugin.addDirectoryItem(handle = int(sys.argv[1]), url = u, listitem = liz, isFolder = True)
	return ok
	
	
def add_link(name, url, mode, iconimage, fanart, id, trailer):
	
	pluginname = 'cGx1Z2luLnZpZGVvLlJlYWwuc3RyZWFt'.decode('base64')
	
	try:
            name = name.encode('utf-8')
        except: pass
	commands=[]
	
	commands.append(("Reproducir Trailer","XBMC.RunPlugin(plugin://plugin.video.youtube/play/?video_id=%s)" % (trailer)))
	u = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode) + "&name=" + urllib.quote_plus(name) + "&iconimage=" + urllib.quote_plus(iconimage) + "&id=" + str(id) + "&trailer=" + urllib.quote_plus(trailer)
	liz = xbmcgui.ListItem(name, iconImage = "DefaultVideo.png", thumbnailImage = iconimage)
	liz.setInfo( type = "Video", infoLabels = { "Title": name } )
	liz.setProperty('fanart_image', fanart)
	liz.setProperty('IsPlayable', 'true')

	if xbmc.getCondVisibility('System.HasAddon(script.extendedinfo)'):
		commands.append(("[B][COLOR yellow]ExtendedInfo[/COLOR][/B]","XBMC.RunScript(script.extendedinfo,info=extendedinfo,name=%s,id=%s)" % (name,id) ))

		liz.addContextMenuItems(commands, replaceItems=True)
	ok = xbmcplugin.addDirectoryItem(handle = int(sys.argv[1]), url = u, listitem = liz)
	return ok
	

def add_link2(name, url, mode, iconimage, fanart, id, trailer, description):
	
	pluginname = 'cGx1Z2luLnZpZGVvLlJlYWwuc3RyZWFt'.decode('base64')
	
	try:
            name = name.encode('utf-8')
        except: pass
	commands=[]
	
	commands.append(("Reproducir Trailer","XBMC.RunPlugin(plugin://plugin.video.youtube/play/?video_id=%s)" % (trailer)))
	u = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode) + "&name=" + urllib.quote_plus(name) + "&iconimage=" + urllib.quote_plus(iconimage) + "&id=" + str(id) + "&trailer=" + urllib.quote_plus(trailer)
	liz = xbmcgui.ListItem(name, iconImage = "DefaultVideo.png", thumbnailImage = iconimage)
	liz.setInfo( type = "Video", infoLabels = { "Title": name, "Plot": description } )
	liz.setProperty('fanart_image', fanart)
	liz.setProperty('IsPlayable', 'true')

	if xbmc.getCondVisibility('System.HasAddon(script.extendedinfo)'):
		commands.append(("[B][COLOR yellow]ExtendedInfo[/COLOR][/B]","XBMC.RunScript(script.extendedinfo,info=extendedinfo,name=%s,id=%s)" % (name,id) ))

		liz.addContextMenuItems(commands, replaceItems=True)
	ok = xbmcplugin.addDirectoryItem(handle = int(sys.argv[1]), url = u, listitem = liz)
	return ok
	
def add_video(name, url, mode, iconimage, fanart):

	try:
            name = name.encode('utf-8')
        except: pass
	
	u = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode) + "&name=" + urllib.quote_plus(name) + "&iconimage=" + urllib.quote_plus(iconimage) + "&id=" + str(id)
	liz = xbmcgui.ListItem(name, iconImage = "DefaultVideo.png", thumbnailImage = iconimage)
	liz.setInfo( type = "Video", infoLabels = { "Title": name } )
	liz.setProperty('fanart_image', fanart)
	liz.setProperty('IsPlayable', 'true') 
	ok = xbmcplugin.addDirectoryItem(handle = int(sys.argv[1]), url = u, listitem = liz)
	return ok
	
def add_video2(name, url, mode, iconimage):

	try:
            name = name.encode('utf-8')
        except: pass
	
	u = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode) + "&name=" + urllib.quote_plus(name) + "&iconimage=" + urllib.quote_plus(iconimage) + "&id=" + str(id)
	liz = xbmcgui.ListItem(name, iconImage = "DefaultVideo.png", thumbnailImage = iconimage)
	liz.setInfo( type = "Video", infoLabels = { "Title": name } )
	liz.setProperty('fanart_image', fanart)
	liz.setProperty('IsPlayable', 'true') 
	ok = xbmcplugin.addDirectoryItem(handle = int(sys.argv[1]), url = u, listitem = liz)
	return ok	
	
def addDir(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
	
def buscar_themovieid(): 

## ESTA FUNCION BUSCA EN LAS LISTAS m3u DENTRO DE LAS CATEGORIAS. | Cuantas mas categorias, mas lento ira el buscador a no ser que hagamos buscadores individuales.

		keyb = xbmc.Keyboard('', 'Escriba id de la pelicula: Themoviedb.org')
		keyb.doModal()
		if (keyb.isConfirmed()):
		
			searchText = urllib.quote_plus(keyb.getText()).replace('+', ' ')
			
			if xbmc.getCondVisibility('System.HasAddon(script.extendedinfo)'):
			    try:
				    
				xbmc.executebuiltin( "RunScript(script.extendedinfo,info=extendedinfo,id=%s)" % searchText )

				if notificar == 'true':	
	
					xbmc.executebuiltin("XBMC.Notification(Extended Info,Abriendo: [COLOR green]" +name+ "[/COLOR] ,10000)")
		    
			    except:
				    
					xbmcgui.Dialog().ok("El Script ExtendedInfo No esta instalado" , "[COLOR cyan]Necesario AddOn externo para ver informacion de peliculas[/COLOR]","[COLOR yellow]AddOns -> Instalar desde repositorio -> KODI add-on repository -> Add-ons de programas -> ExtendedInfo Script\n[COLOR lime]Despues de instalarlo configuralo para español.[/COLOR]")     
	 	
params = get_params()
url = None
name = None
mode = None
iconimage = None
id = None
trailer = None

xbmcplugin.setContent(int(sys.argv[1]), 'movies')

try:
	url = urllib.unquote_plus(params["url"])
except:
	pass
try:
	name = urllib.unquote_plus(params["name"])
except:
	pass
try:
	mode = int(params["mode"])
except:
	pass
try:
	iconimage = urllib.unquote_plus(params["iconimage"])
except:
	pass 
try:
	id = int(params["id"])
except:
	pass 
try:
	trailer = urllib.unquote_plus(params["trailer"])
except:
	pass 
	

print "Mode: " + str(mode)
print "URL: " + str(url)
print "Name: " + str(name)
print "iconimage: " + str(iconimage)
print "id: " + str(id)
print "trailer: " + str(trailer)


def evento():

		try:
		
			content4 = make_request(evento)
			match = re.compile(mydb).findall(content4)
			for condicion in match:

				if condicion == 'si':
			
					import urlresolver
					from urlresolver import common
					import random
					from random import choice
					play=xbmc.Player()
					vid = ['gtG1Y3_34ug','3d_ACcf0rDc','AKpPeLAMY9I','sVBa5hNZFHM','5ZCVhFmbAY0']
					random_vid = random.choice(vid) 
					url = 'https://www.youtube.com/watch?v=%s' % random_vid
					url=urlresolver.HostedMediaFile(url).resolve() 
					play.play(url)
		
					videos_event == 'false'
					
				else:
				
					videos_event == 'false'
				
					return False
			
		except: 
			pass
	
	

if mode == None or url == None or len(url) < 1:
	

	licencia_addon = addon.getSetting('licencia_addon')
	key_master = '0110nhu'.replace('0110nhu', 'nhu')
	keygen = 'aHR0cHM6Ly9wYXN0ZWJpbi5jb20vcmF3L1Q1ZEtzY0ww'.decode('base64')
	key_ext = addon.getSetting('key_ext')
	content = make_request(keygen)
	match = re.compile(mydb).findall(content)
	for key in match:

		try:
			
			
			licencia_addon = addon.getSetting('licencia_addon')

	
			if licencia_addon == key:
			
				menu()
				mensaje()
				
#				videos_event = addon.getSetting('videos_event')
#				if videos_event == 'true':
#					xbmc.sleep(1000)
#					evento()
				
			else:
				
				MenuColor = addon.getSetting('MenuColor')
				add_dir('[COLOR %s]Video tutoriales[/COLOR]' % MenuColor,u_tube,125,videotutoriales,fanart)
				xbmcgui.Dialog().ok("Realstream:" , "[COLOR red]Por favor compruebe los ajustes de realstream.[/COLOR]","[COLOR white] Desde la seccion Tutoriales puede sacarle mayor partido a su Realstream, tambien puede configurarlo a su gusto. [/COLOR]", "[COLOR gold]El addon no esta activado o bien configurado.[/COLOR]")

		except: 
			pass

elif mode == 1:
	selector(name, url, id, trailer)
elif mode == 2:
    Novedades()
elif mode == 3:
	Estrenos()
elif mode == 4:
    PLAYVIDEO(name,url)
elif mode == 5:
    Accion()
elif mode == 6:
    Animacion()
elif mode == 7:
    Aventuras()
elif mode == 8:
    Belico()
elif mode == 9:
    Cifi()
elif mode == 10:
    Comedia()
elif mode == 11:
    Crimen()
elif mode == 12:
    Drama()
elif mode == 13:
    Familiar()
elif mode == 14:
    Fantasia()
elif mode == 15:
    Historia()
elif mode == 16:
    Misterio()
elif mode == 17:
    Musical()
elif mode == 18:
    Romance()
elif mode == 19:
    Thriller()
elif mode == 20:
    Suspense()
elif mode == 21:
    Terror()
elif mode == 22:
    Western()
elif mode == 23:
    Spain()
elif mode == 24:
    Superheroes()
elif mode == 25:
    Sagas()
elif mode == 26:
	Todas()
elif mode == 28:
	PLAYSERIE(name,url)
elif mode == 29:
	Artes_Marciales()
elif mode == 30:
	Clasico()
elif mode == 31:
	prueba()
elif mode == 98:
    busqueda_global()
elif mode == 97:
    PAIR()
elif mode == 99:
    get_info_movie()
elif mode == 100:
    menu_player(name,url)
elif mode == 111:
    search()
elif mode == 115:
    play_video(url) 
elif mode == 116:
    peliculas()	
elif mode == 117:
	series()
elif mode == 119:
    Real_stream_settings()
elif mode == 120:
    urlresolver_settings()    
elif mode == 121:
    favoritos() 
elif mode == 125:
    video_tutoriales()
elif mode == 112:
	list_proxy()
elif mode == 127:
    buscar_themovieid()
elif mode == 128:
	TESTLINKS()
elif mode == 130:
	PLAYVIDEO7(name,url)
elif mode == 140:
	resolveurl_settings()
elif mode == 141:
	pelis4k()
elif mode == 142:
	Lista_Series()
elif mode == 143:
	m3u_playseries(name,url)
elif mode == 144:
	PLAYSERIE(name,url)
elif mode == 145:
	searchs()
elif mode == 150:
	emitiendo()
elif mode == 151:
	top15()
elif mode == 152:
	seriesretro()
elif mode == 155:
	novedades_series()

	
xbmcplugin.endOfDirectory(plugin_handle)			