from motion_detector import df
from bokeh.plotting import figure,show,output_file
from bokeh.models import HoverTool,ColumnDataSource

cds=ColumnDataSource(df)

p=figure(x_axis_type='datetime',height=100,width=500,title='Motion Graph',sizing_mode='scale_both')
p.yaxis.minor_tick_line_color=None
p.yaxis.ticker = [0, 1]

hover = HoverTool(
    tooltips = [
        ("Start", "@Start{%Y-%m-%d %H:%M:%S}"), 
        ("End", "@End{%Y-%m-%d %H:%M:%S}")
    ],
    formatters = {
        "@Start" : "datetime",
        "@End" : "datetime"
    }
)
p.add_tools(hover)

q=p.quad(left='Start',right='End',bottom=0,top=1,color='green',source=cds)

output_file('Graph.html')
show(p)