"""nc5ng.gmt.plotter

module that defines GMT Plotting Utilities for nc5ng conversions
"""

from numpy import array
from .options import GMTOptions, PLOT_OPTS    
        


class GMTPlotter(object):
    """GMTPlotter

    Wrapper for GMT/Python plotter

    """

    @property
    def figure(self):
        return getattr(self, '_figure', None)

    def __init__(self, base_plot_options=PLOT_OPTS['default']):
        import gmt
        self._figure = gmt.Figure()
        self.gmt_meta = base_plot_options

    def plot(self, *args, **kwargs):
        self.figure.plot(*args, **kwargs)

    def show(self, *args, **kwargs):
        self.figure.show(*args, **kwargs)

    @staticmethod
    def plot_conversion(conversion, coverage='all', vector='all', plotter=None, **kwargs):
        if plotter is None:
            plotter = GMTPlotter()
            
        if (coverage == 'all'):
            cpoints = [_pointstore,]
        elif not(coverage):
            cpoints = []
        elif coverage[0] == 'c' and coverage in conversion.output_data:
            cpoints = [conversion.output_data[coverage],]
        else:
            cpoints = []
            for c in coverage:
                cpoints.append(conversion.output_data[c])

        if (vector == 'all'):
            vpoints = [_vectorstore,]
        elif not(vector):
            vpoints = []
        elif vector[0] == 'v' and vector in conversion.output_data:
            vpoints = [conversion.output_data[vector],]
        else:
            vpoints = []
            for c in vector:
                vpoints.append(conversion.output_data[c])
        

        plotter.__base__(conversion, **kwargs)
        plotter.__coast__(conversion, **kwargs)
        plotter.__plot__(conversion, *cpoints, symbol="p4p",**kwargs)
        plotter.__plot__(conversion, *vpoints, symbol="v", **kwargs)
        plotter.show()
        return plotter


    def __base__(self, conversion, **kwargs):
        # Apply conversion options onto base options with any explicit keywords
        opts = self.gmt_meta(**conversion.gmt_meta)(**kwargs).basemap

        # passthrough shorthand we assume people know what they are doing
        _filter_base_kwargs =  { x:y for x,y in kwargs.items() if x in GMTOptions.BASEMAP_FILTER_OUT}
        opts.update(_filter_base_kwargs)
        
        print (_filter_base_kwargs, opts, conversion.gmt_meta)
                 
        #execute the command
        self.figure.basemap(**opts)

    def __coast__(self, conversion, **kwargs):
        # Apply conversion options onto base options with any explicit keywords
        opts = self.gmt_meta(**conversion.gmt_meta)(**kwargs).coast

        # passthrough shorthand we assume people know what they are doing
        _filter_base_kwargs =  { x:y for x,y in kwargs.items() if x in GMTOptions.COAST_FILTER_OUT}
        opts.update(_filter_base_kwargs)
        
        print (_filter_base_kwargs, opts, conversion.gmt_meta)
                 
        #execute the command
        self.figure.coast(**opts)
        

    def __plot__(self, conversion, *points,**kwargs):
                # Apply conversion options onto base options with any explicit keywords
        
        opts = self.gmt_meta(**conversion.gmt_meta)(**kwargs).plot

        # passthrough shorthand we assume people know what they are doing
        _filter_base_kwargs =  { x:y for x,y in kwargs.items() if x in GMTOptions.PLOT_FILTER_OUT}
        opts.update(_filter_base_kwargs)
        
        print (_filter_base_kwargs, opts, conversion.gmt_meta)
                 
        #execute the command
        for point_set in points:
            self.figure.plot(data = point_set.plot_data, **opts)

            
            
            
            
            
        

    
        
    

    
        
