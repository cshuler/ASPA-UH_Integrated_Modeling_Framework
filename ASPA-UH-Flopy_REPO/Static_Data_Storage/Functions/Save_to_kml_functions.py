###### Write a KML file from a projected shapefile ######

def poly_shp_to_kml(IN_SHP, OUT_SHP, colorstring = "50ff0000"):
    kml = simplekml.Kml(open=1)       # create the kml file
    pfol = kml.newfolder(name="folder")
    openShape = ogr.Open(IN_SHP)

    layers = openShape.GetLayerByIndex(0)
    i = 0
    for element in layers:
        geom = loads(element.GetGeometryRef().ExportToWkb())
        i=i+1
        arrcoords = geom.to_wkt()
        pol = pfol.newpolygon() # the part that creates the kml
        pol.visibility = 50
        pol.style.polystyle.color = colorstring     # 'hexadecimal color string'
        pol.altitudemode = 'relativeToGround'
        pol.extrude = 1
        coords = arrcoords.replace('POLYGON','').replace('(','').replace(')','')
        coords = coords.replace('MULTI','')
        coords = coords.split(',')
        asize = 1
        pol.outerboundaryis = ([(float(coords[j].split()[0]),float(coords[j].split()[1]),asize) for j in range(len(coords))])

    kml.save(OUT_SHP)  # save the kml
    
    
    
    
    
    
    
    
    
###### Write a KML overlay from a numpy array input to the model  ######
    
def nparray_to_kml(input_array, out_name, ncol=ncol, nrow=nrow, xll=xll, yll=yll, cellsize = np.mean([delc, delr]), colorbar=None, **kw):
    
    from osgeo import gdal, osr
    from mpl_toolkits.basemap import Basemap
    from simplekml import (Kml, OverlayXY, ScreenXY, Units, RotationXY, AltitudeMode, Camera)

# turn the numpy array into an asc raster in UTM zone 2S
    the_asc = os.path.join(workspace, "{}.asc".format(out_name))
    np.savetxt(the_asc, input_array)

    new_first = ('NCOLS {}\n'                        # these are the parameters for the .asc file
                 'NROWS {}\n'
                 'XLLCENTER {}\n'
                 'YLLCENTER {}\n'
                 'CELLSIZE {}\n'
                 'NODATA_value -999.0\n'.format(ncol,nrow, xll, yll, np.mean([delc, delr]) ))  

    with open(the_asc, 'r+') as file:                # add in new first line and save file  
        file_data = file.read()
        file. seek(0, 0)
        file. write(new_first + '\n' + file_data)
        
        
# turn the new .asc file into a geo-tiff 
    the_tif = os.path.join(workspace, "{}.tif".format(out_name))
    in_raster = gdal.Open(the_asc)
    gdal.Warp(the_tif ,in_raster, srcSRS='EPSG:{}'.format(model_epsg), dstSRS='EPSG:4326')
    
    
    
# plotting function to plot and format the tif into a Gearth image that doesnt look like crap
    # Note This plotting function is clunky and not very good, but it is the best example I could find so far, probably should do better
    # One of its main issues is that it reads the data upside down and it needs to be flipped with a command, obviously something is wrong
    # from https://gis.stackexchange.com/questions/184727/plotting-raster-maps-in-python
    
    the_png = os.path.join(workspace, "{}.png".format(out_name))

    ds = gdal.Open(the_tif)              # tif file in
    data = ds.ReadAsArray()

    data = np.flipud(data)    # this is where that sketchy data flip happens

    gt = ds.GetGeoTransform()   
    proj = ds.GetProjection()

    xres = gt[1]
    yres = gt[5]
    xmin = gt[0] + xres * 0.5
    xmax = gt[0] + (xres * ds.RasterXSize) - xres * 0.5
    ymin = gt[3] + (yres * ds.RasterYSize) + yres * 0.5
    ymax = gt[3] - yres * 0.5
    x_center=(xmin+xmax)/2
    y_center=(ymin+ymax)/2  

    m = Basemap(llcrnrlon=xmin,llcrnrlat=ymin,urcrnrlon=xmax,urcrnrlat=ymax, projection='merc', lat_0 = y_center, lon_0 = x_center)
    x = np.linspace(0, m.urcrnrx, data.shape[1])
    y = np.linspace(0, m.urcrnry, data.shape[0])
    xx, yy = np.meshgrid(x, y)

    # create the igure object scaled for google earth   from https://ocefpaf.github.io/python4oceanographers/blog/2014/03/10/gearth/
    aspect = np.cos(np.mean([ymin, ymax]) * np.pi/180.0)
    xsize = np.ptp([xmax, xmin]) * aspect
    ysize = np.ptp([ymax, ymin])
    aspect = ysize / xsize

    if aspect > 1.0:
        figsize = (10.0 / aspect, 10.0)
    else:
        figsize = (10.0, 10.0 * aspect)

    if False:

        plt.ioff()  # Make `True` to prevent the KML components from poping-up.
    fig = plt.figure(figsize=figsize,
                     frameon=False,
                     dpi=1024//10)
    # KML friendly image.  If using basemap try: `fix_aspect=False`.
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)

    cs = m.pcolormesh(xx, yy, data, cmap=plt.cm.jet) # alpha = .9)                              ########################   make a cmap option  
    fig.savefig(the_png,  transparent=False, format='png', dpi=600)  
    

# this is the save KML overlay part, there are some options in here that can be changed for visualization stuff
    # from https://ocefpaf.github.io/python4oceanographers/blog/2014/03/10/gearth/
    
    the_kml = os.path.join(workspace, "{}.kmz".format(out_name))
    
    kml = Kml()
    altitude = kw.pop('altitude', 2e4)
    roll = kw.pop('roll', 0)
    tilt = kw.pop('tilt', 0)
    altitudemode = kw.pop('altitudemode', AltitudeMode.relativetoground)
    camera = Camera(latitude=np.mean([ymax, ymin]),
                    longitude=np.mean([xmax, xmin]),
                    altitude=altitude, roll=roll, tilt=tilt,
                    altitudemode=altitudemode)

    kml.document.camera = camera
    draworder = 0
    for fig in [the_png]:  # NOTE: Overlays are limited to the same bbox.
        draworder += 1
        ground = kml.newgroundoverlay(name='GroundOverlay')
        ground.draworder = draworder
        ground.visibility = kw.pop('visibility', 1)
        ground.name = kw.pop('name', 'overlay')
        ground.color = kw.pop('color', '9effffff')
        ground.atomauthor = kw.pop('author', 'ocefpaf')
        ground.latlonbox.rotation = kw.pop('rotation', 0)
        ground.description = kw.pop('description', 'Matplotlib figure')
        ground.gxaltitudemode = kw.pop('gxaltitudemode',
                                       'clampToSeaFloor')
        ground.icon.href = fig
        ground.latlonbox.east = xmin
        ground.latlonbox.south = ymin
        ground.latlonbox.north = ymax
        ground.latlonbox.west = xmax

    # now make a legend for the kml file 
    the_ledg = os.path.join(workspace, "legend_{}.png".format(out_name))
    
    fig = plt.figure(figsize=(1.5, 4.0), facecolor=None, frameon=False)
    ax = fig.add_axes([0.0, 0.05, 0.2, 0.9])
    cb = fig.colorbar(cs, cax=ax)
    cb.set_label(out_name, rotation=-90, color='k', labelpad=20)
    fig.savefig(the_ledg, transparent=True, format='png')  # Change transparent to True if your colorbar is not on space :)

    screen = kml.newscreenoverlay(name='ScreenOverlay')
    screen.icon.href = the_ledg
    screen.overlayxy = OverlayXY(x=0, y=0,
                                 xunits=Units.fraction,
                                 yunits=Units.fraction)
    screen.screenxy = ScreenXY(x=0.015, y=0.075,
                               xunits=Units.fraction,
                               yunits=Units.fraction)
    screen.rotationXY = RotationXY(x=0.5, y=0.5,
                                   xunits=Units.fraction,
                                   yunits=Units.fraction)
    screen.size.x = 0
    screen.size.y = 0
    screen.size.xunits = Units.fraction
    screen.size.yunits = Units.fraction
    screen.visibility = 1

    kmzfile = kw.pop('kmzfile', the_kml)
    kml.savekmz(kmzfile)   

    
# note here are soome mappings that might be useful for this function 
#   xmin,        ymin,        xmax,         ymax
# llcrnrlon,   llcrnrlat,   urcrnrlon,   urcrnrlat 
    
    

    
# reproject existing asc raster to a new coordinate system, not used currently but is part of the above function
def asc_to_prj_tiff(input_asc, output_tiff, ncol=ncol, nrow=nrow, xll=xll, yll=yll, cellsize = np.mean([delc, delr])):
    in_raster = gdal.Open(input_asc)
    gdal.Warp(output_tiff ,in_raster, srcSRS='EPSG:{}'.format(model_epsg), dstSRS='EPSG:4326') 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    