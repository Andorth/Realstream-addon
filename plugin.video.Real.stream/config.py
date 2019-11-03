# -*- coding: utf-8 -*-

# Realstream Configs - 

import os, sys, re
import xbmc, xbmcaddon
import base64

import plugintools,config


addon = xbmcaddon.Addon('plugin.video.Real.stream')
addon_version = addon.getAddonInfo('version')
plugin_handle = int(sys.argv[1])
mysettings = xbmcaddon.Addon(id = 'plugin.video.Real.stream')
profile = mysettings.getAddonInfo('profile')
home = mysettings.getAddonInfo('path')
#Imagenes
fanart = xbmc.translatePath(os.path.join(home, 'fanart.jpg'))
icon = xbmc.translatePath(os.path.join(home, 'icon.png'))
extended = xbmc.translatePath(os.path.join(home, 'extended_info.png'))
buscar = xbmc.translatePath(os.path.join(home, 'buscar.png'))
pair = xbmc.translatePath(os.path.join(home, 'pair.png'))
theMovieDB = xbmc.translatePath(os.path.join(home, 'theMovieDB.png'))
novedades = xbmc.translatePath(os.path.join(home, 'estrenos.png'))
estrenos = xbmc.translatePath(os.path.join(home, 'encines.png'))
recomendadas = xbmc.translatePath(os.path.join(home, 'recomendadas.png'))
p_accion = xbmc.translatePath(os.path.join(home, 'accion.png'))
animacion = xbmc.translatePath(os.path.join(home, 'animacion.png'))
aventuras = xbmc.translatePath(os.path.join(home, 'aventuras.png'))
belico = xbmc.translatePath(os.path.join(home, 'belico.png'))
cifi = xbmc.translatePath(os.path.join(home, 'ciencia-ficcion.png'))
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
#Menus
 
menu_pelis = xbmc.translatePath(os.path.join(home, 'peliculas.png'))
ajustes = xbmc.translatePath(os.path.join(home, 'ajustes.png'))
vid = xbmc.translatePath(os.path.join(home, 'videoteca.png'))
favicon = xbmc.translatePath(os.path.join(home, 'favorites.png'))
resolver = xbmc.translatePath(os.path.join(home, 'resolver.png'))
test = xbmc.translatePath(os.path.join(home, 'test.png'))
videotutoriales = xbmc.translatePath(os.path.join(home, 'video-tutoriales.png'))
buscarseries = xbmc.translatePath(os.path.join(home, 'buscar-serie.png'))
seriestodas = xbmc.translatePath(os.path.join(home, 'series-todas.png'))
emision = xbmc.translatePath(os.path.join(home, 'emision.png'))
mejores = xbmc.translatePath(os.path.join(home, 'mejores.png'))
favorites = xbmc.translatePath(os.path.join(home, 'favoritos.png'))
Mb_peliculas = xbmc.translatePath(os.path.join(home, 'BuscadorPeliculas.png'))
Mb_series = xbmc.translatePath(os.path.join(home, 'BuscadorSeries.png'))
nuevos_no = xbmc.translatePath(os.path.join(home, 'Novedades_series.png'))
nuevos_si = xbmc.translatePath(os.path.join(home, 'Novedades_Episodios.png'))
#Ajustes
mostrar_cat = addon.getSetting('mostrar_cat')
videos = addon.getSetting('videos')
activar = addon.getSetting('activar')
favcopy = addon.getSetting('favcopy')
anticopia = addon.getSetting('anticopia')
notificar = addon.getSetting('notificar')
mostrar_bus = addon.getSetting('mostrar_bus')
restante = addon.getSetting('restante')
aviso = addon.getSetting('aviso')
RealStream_Settings = addon.getSetting('RealStream_Settings')
Resolver_Settings = addon.getSetting('Resolver_Settings')
restante = addon.getSetting('restante')
fav = addon.getSetting('fav') 
texto = 'aHR0cDovL25ldGFpLmV1L3JlYWxzdHJlYW0v'.decode('base64')
txt = 'bienvenida'
txt2 = 'YmllbnZlbmlkYQ=='.decode('base64')
cat_regex = 'todas=[\'"](.*?)[\'"]\s*estrenos=[\'"](.*?)[\'"]\s*novedades=[\'"](.*?)[\'"]\s*accion=[\'"](.*?)[\'"]\s*animacion=[\'"](.*?)[\'"]\s*aventuras=[\'"](.*?)[\'"]\s*belico=[\'"](.*?)[\'"]\s*cifi=[\'"](.*?)[\'"]\s*comedia=[\'"](.*?)[\'"]\s*crimen=[\'"](.*?)[\'"]\s*drama=[\'"](.*?)[\'"]\s*familiar=[\'"](.*?)[\'"]\s*fantasia=[\'"](.*?)[\'"]\s*historia=[\'"](.*?)[\'"]\s*misterio=[\'"](.*?)[\'"]\s*musical=[\'"](.*?)[\'"]\s*romance=[\'"](.*?)[\'"]\s*thriller=[\'"](.*?)[\'"]\s*suspense=[\'"](.*?)[\'"]\s*terror=[\'"](.*?)[\'"]\s*western=[\'"](.*?)[\'"]\s*spain=[\'"](.*?)[\'"]\s*superheroes=[\'"](.*?)[\'"]\s*sagas=[\'"](.*?)[\'"]\s*videotutoriales=[\'"](.*?)[\'"]\s*'


Forceupdate = addon.getSetting('Forceupdate')
if Forceupdate == 'true':  
    xbmc.executebuiltin('UpdateAddonRepos()')
    xbmc.executebuiltin('UpdateLocalAddons()')	