
# coding: utf-8

# In[1]:

### Define basic plot types ###


# In[2]:

import matplotlib.pyplot as plt
import matplotlib.colors as colors
from matplotlib.ticker import FixedLocator, FixedFormatter, FormatStrFormatter
from matplotlib.colors import ListedColormap
from matplotlib import gridspec
import pandas as pd
import numpy as np
from IPython.display import display, HTML

def print_df_no_index( df ):
    display(HTML(df.to_html(index=False)))

def discrete_cmap(N, base_cmap=None):
    """
    Create an N-bin discrete colormap from the specified input map.
    Based on code from https://gist.github.com/jakevdp/91077b0cae40f8f8244a
    """
    base = plt.cm.get_cmap(base_cmap)
    color_list = base(np.linspace(0, 1, N))
    cmap_name = base.name + str(N)
    return base.from_list(cmap_name, color_list, N)

def discrete_irreg_cmap(discrete_vals, base_cmap=None):
    base = plt.cm.get_cmap(base_cmap)
    normalized_vals = discrete_vals / np.max( discrete_vals )
    color_list = base(normalized_vals)
    cmap_name = base.name + "discrete"
    return base.from_list(cmap_name, color_list, len( discrete_vals ) )

def make_side_by_side_plots( var1, var2, title1='Title 1', title2='Title 2', barlabel='Bar label',
                             cmap='jet', each=False, figsize_x=16, figsize_y=8,
                             minz=-1.0e-12, maxz=-1.0e-12, n=7, x=(0,1), y=(0,1) ):

    # see: http://stackoverflow.com/questions/10388462/matplotlib-different-size-subplots
    # for a nice treatment of multiple plots with varying widths

    plt.figure(num=None, figsize=(figsize_x, figsize_y), dpi=200, facecolor='w', edgecolor='k')

    # create a "grid" of plots: 1 row, by 2 columns wide
    gs = gridspec.GridSpec(1,2,width_ratios=[4,5])

    ax0=plt.subplot(gs[0])
    ax1=plt.subplot(gs[1])

    if ( minz < 1.0e-11 ):
        minz = np.nanmin(var1)

    if ( maxz < 1.0e-11 ):
        maxz = np.nanmax(var1)

    vals=np.linspace(minz, maxz, n, endpoint=True )
    plot0 = ax0.imshow( var1, interpolation='nearest', cmap=cmap, extent=(np.nanmin(x),
                                    np.nanmax(x), np.nanmin(y), np.nanmax(y)),
                                    vmin=minz, vmax=maxz )
    #ax.  .clim(minz, maxz)

    ax0.set_title(title1)
    plot1 = ax1.imshow( var2, interpolation='nearest', cmap=cmap, extent=(np.nanmin(x),
                                np.nanmax(x), np.nanmin(y), np.nanmax(y)),
                                vmin=minz, vmax=maxz )
    ax1.set_title(title2)
    bar1 = plt.colorbar( plot1 )
    bar1ax = bar1.ax
    bar1ax.text(2.1,0.5,barlabel,rotation=90,size=15)

    plt.show()

def make_plot( var, title='', barlabel='', cmap='jet', discrete=False, minz=-1.0e+12, maxz=-1.0e+12, n=7,
              tick_factor=1.0, tick_offset=0.0, x=(0,1), y=(0,1) ):
    plt.figure(num=None, figsize=(8, 5), dpi=100, facecolor='w', edgecolor='k')
    plt.title( title )

    if ( minz < -1.0e+11 ):
        minz = np.nanmin(var)

    if ( maxz < -1.0e+11 ):
        maxz = np.nanmax(var)

    if ( discrete ):
        vals=np.unique( var.flatten() )
        #myplot = plt.contourf(x, y, var, vals, cmap=cmap)
        myplot = plt.imshow( var, interpolation='nearest', cmap=cmap, extent=(np.nanmin(x),
                                    np.nanmax(x), np.nanmin(y), np.nanmax(y)),
                                    vmin=0.0, vmax=1.0 )
        delta = np.max( vals ) - np.min( vals )
        inc = delta / len( vals )
        #tickvals = range( int( np.min( vals)) , int( np.max( vals )) , int( inc ) )
        adj_tickvals = [tick_factor * i + tick_offset for i in vals ]
        mybar = plt.colorbar( myplot )# , ticks= vals )
        myax = mybar.ax
        myax.set_yticklabels( vals )

    else:
        vals=np.linspace(minz, maxz, n, endpoint=True )
        #myplot = plt.contourf(x, y, var, vals, cmap=cmap)
        myplot = plt.imshow( var, interpolation='nearest', cmap=cmap, extent=(np.nanmin(x),
                                    np.nanmax(x), np.nanmin(y), np.nanmax(y)) )
        mybar = plt.colorbar( myplot )
        myax = mybar.ax


    plt.clim(minz, maxz)
    myax.text(3.0,0.65,barlabel,rotation=90,size=15)
    plt.show()

def make_diffplot( var, title, barlabel, cmap='seismic', minz=-36., maxz=36., n=10, x=(0,1), y=(0,1) ):
    plt.figure(num=None, figsize=(16, 9), dpi=200, facecolor='w', edgecolor='k' )
    plt.title( title )
    vals=np.linspace(minz, maxz, n, endpoint=True)
#    myplot = plt.contourf(x, y, var, vals, cmap=cmap)
    myplot = plt.imshow( var, interpolation='nearest', cmap=cmap, extent=(np.nanmin(x),
                            np.nanmax(x), np.nanmin(y), np.nanmax(y)) )
    #mybar = plt.colorbar( myplot, ticks=vals)
    plt.clim(minz, maxz)
    mybar = plt.colorbar( myplot)
    myax = mybar.ax
    myax.text(3.,.7,barlabel,rotation=90,size=15)
    plt.show()

def make_scatter( x, y, color, cmap, barlabel='none', title='none', xlab='none', ylab='none',
    xmax=1.0e-36, ymax=1.0e-36, xmin=1.0e-36, ymin=1.0e-36 ):
    if xmax < 1.0e-35:
        xmax=np.nanmax(x)
    if ymax < 1.0e-35:
        ymax=np.nanmax(y)
    if xmin < 1.0e-35:
        xmin=np.nanmin(x)
    if ymin < 1.0e-35:
        ymin=np.nanmin(y)

    plot_minmaxvals = [xmin, ymin, xmax, ymax]

    fig1 = plt.figure(figsize=[20,12])
    gs = plt.GridSpec(100,100,bottom=0.18,left=0.18,right=0.88)

    ax1 = fig1.add_subplot(gs[:,:90])
    axC = fig1.add_subplot(gs[:,95:])

    ax1.set_title( title )
    ax1.set_xlabel( xlab )
    ax1.set_ylabel( ylab )
    ax1.set_xlim( ( xmin, xmax ) )
    ax1.set_ylim( ( ymin, ymax ) )

    p1 = ax1.scatter(x=x.flatten(), y=y.flatten(), c=color.flatten() , cmap=cmap, edgecolors='none' )
    p2 = ax1.plot([xmin,xmax], [ymin,xmax], "r--" )

    mincol = np.nanmin( color.flatten() )
    maxcol = np.nanmax( color.flatten() )
    n=maxcol - mincol + 1

    tick_labels=np.unique( color.flatten() )
    n=tick_labels.count()

#    tick_locs = tick_labels * 0.96 + 0.5
    tick_locs = np.linspace( mincol, maxcol, n ) * 0.98 + 0.75

    cbar = fig1.colorbar(p1, ax=ax1, cax=axC )

    cbar.locator = FixedLocator(tick_locs)
    cbar.formatstrformatter = FormatStrFormatter('%.f')
    cbar.formatter = FixedFormatter(tick_labels)
    cbar.update_ticks()

    axC.text(2.1,0.5,barlabel,rotation=90,size=15)

    plt.show()

def make_comparison_table( x, y, factor, description, lookup_vals, xlab, ylab, calc_difference=True ):
    count_x=len(x.flatten())
    count_y=len(y.flatten())

    xmean = []
    ymean = []
    lu = []
    desc = []
    count = []
    modeldiff = []

    for index in range( len(lookup_vals) ):

        count_x=len(x[ factor == lookup_vals[index] ])
        count_y=len(y[ factor == lookup_vals[index] ])
        if count_x > 0:
            x_mean = np.nanmean(x[ factor == lookup_vals[index] ])
        else:
            x_mean = np.nan

        if count_y > 0:
            y_mean = np.nanmean(y[ factor == lookup_vals[index] ])
        else:
            y_mean = np.nan
        if x_mean is not np.nan and y_mean is not np.nan:
            mean_both = np.nanmean((x_mean, y_mean ))
            abs_diff = (x_mean - y_mean )
            xmean.append( x_mean )
            ymean.append( y_mean )
            lu.append( lookup_vals[ index ] )
            count.append( count_x )
            desc.append( description[ index ] )
            modeldiff.append( str( abs_diff ) )
        else:
            abs_diff = np.nan

    if calc_difference:

        d = { 'Code': lu, 'Description' : desc, 'Count' : count, xlab : xmean, ylab : ymean, 'Difference' : modeldiff }
        df = pd.DataFrame( d )
        df = df[[ 'Code', 'Description', 'Count', xlab, ylab, 'Difference']]
        df = df.dropna()
        pd.options.display.float_format = '{:,.3f}'.format
        display( df )

    else:

        d = { 'Code': lu, 'Description' : desc, 'Count' : count, xlab : xmean, ylab : ymean }
        df = pd.DataFrame( d )
        df = df[[ 'Code', 'Description', 'Count', xlab, ylab ]]
        df = df.dropna()
        pd.options.display.float_format = '{:,.3f}'.format
        display( df )

def read_raster(rasterfile):
    '''
    reads a GDAL raster into numpy array for plotting
    also returns meshgrid of x and y coordinates of each cell for plotting
    based on code stolen from:
    http://stackoverflow.com/questions/20488765/plot-gdal-raster-using-matplotlib-basemap
    '''
    try:
        import gdal
    except:
        print('This function requires gdal.')
    try:
        ds = gdal.Open(rasterfile)
    except:
        raise IOError("problem reading raster file {}".format(rasterfile))

    print('\nreading in {} into numpy array...'.format(rasterfile))
    data = ds.ReadAsArray()
    gt = ds.GetGeoTransform()
    proj = ds.GetProjection()

    xres = gt[1]
    yres = gt[5]

    # get the edge coordinates and add half the resolution
    # to go to center coordinates
    xmin = gt[0] + xres * 0.5
    xmax = gt[0] + (xres * ds.RasterXSize) - xres * 0.5
    ymin = gt[3] + (yres * ds.RasterYSize) + yres * 0.5
    ymax = gt[3] + yres * 0.5

    del ds

    print('creating a grid of xy coordinates in the original projection...')
    xy = np.mgrid[xmin:xmax+xres:xres, ymax+yres:ymin:yres]

    # create a mask for no-data values
    data[data<-999] = 0

    return data, gt, proj, xy

#
# def zonal_stats_series( x, factor, description, lookup_val, xlab ):
#
#     count_x = x.shape[0]
#
#     xmean = []
#     lu = []
#     desc = []
#     count = []
#
#     d = { 'LU_Code': lu, 'Description' : desc, 'Count' : count, xlab : xmean }
#     df = pd.DataFrame( d )
#
#     for idx in range( countx ):
#
#         xmean = []
#         lu = []
#         desc = []
#         count = []
#
#
#         for index in range( len(lookup_vals) ):
#
#             count_x=len(x[ factor == lookup_vals[index] ])
#             if count_x > 0:
#                 x_mean = np.nanmean(x[ factor == lookup_vals[index] ])
#             else:
#                 x_mean = np.nan
#
#             xmean.append( x_mean )
#             lu.append( lookup_vals[ index ] )
#             count.append( count_x )
#             desc.append( description[ index ] )
#
#     d = { 'LU_Code': lu, 'Description' : desc, 'Count' : count, xlab : xmean }
#     df = pd.DataFrame( d )
#     df = df[ [ 'LU_Code', 'Description', 'Count', xlab ] ]
#     df = df.dropna()
#
#     return( xmean )
