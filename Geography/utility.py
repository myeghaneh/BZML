import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from bokeh.plotting import figure, output_file, show, ColumnDataSource
from bokeh.io import output_notebook, output_file, save
output_notebook()
from bokeh.models import HoverTool,BoxZoomTool,ResetTool, WheelZoomTool,Legend, LegendItem
from bokeh.layouts import row, gridplot, layout



def plot_maps(fs_dic,df_dic,co,c1,c2,title):
    """This function returns the map based on the entered values as follows:
    fs_dic ~ dictiornay of all coastal localities either fs_dict or gs_dict -->dict
    df_dic ~ dictiornay of all localities -->dict
    co ~ name of data in different coordinate  'dfTemp' or 'dfTempX'  --> string
    c1 ~ color of the point       -->string
    c2 ~ color of the lines       -->string
    title ~ either 'Omega Recension' or -'Xi Recension'  -->string
    pay attention to capitalization 
    """
    p = figure(title=title, width=1000, height=800, x_range=(1.5, 22), y_range=(35.5, 47))
    for i in fs_dic.values():
        p.line(i[:,0],i[:,1], color=c2)
    if title== "Omega Recension":
        inn_1=p.line([4.083,6.333,9,12], [37.667,39,39,37.25], line_alpha=0.8, color=c2)
        inn_2=p.line([5.333,9.167,9,9], [41.833,41.333,40.167,39], line_alpha=0.8, color=c2)
        inn_3=p.line([15,17,19,20.333], [
            45.833,43,43.167,42.333], line_alpha=0.8, color=c2)
    elif title=="Xi Recension":
        inn_1=p.line([4.083,6.333,9,12], [37.667,39,39,37.25], line_alpha=0.8, color=c2)
        inn_2=p.line([5.333,9.333,9,9], [41.833,41.833,40.5,39], line_alpha=0.8, color=c2)
        inn_3=p.line([15.167,17,19,20.333], [45.833,43,43.167,42.333], line_alpha=0.8, color=c2)
    p.circle(np.array(df_dic[co]['longitude']),np.array(df_dic[co]['latitude']), fill_color=c1,size=6, fill_alpha=.9, line_color=c1,line_alpha=0.6)
    show(p)
    
def comp_plot_map_01(fs_dict,gs_dict,df_dic,IbEq,c):
    """This function returns the comparsion map based on the entered values as follows:
    fs_dic ~ dictiornay of all coastal localities in Omega
    gs_dic ~ dictiornay of all coastal localities in Xi
    df_dic ~ dictiornay of all localities -->dict
    Ibeq 
    c
    """
    r = figure(title='Comparison between Xi (red) and Omega (blue)', width=1000, height=800, x_range=(1.5, 22), y_range=(35.5, 47))
    r.circle(np.array(IbEq["longitude"]),np.array(IbEq["latitude"]), size=5.5,fill_color='lightgrey', fill_alpha=1, line_color='lightgrey',line_alpha=0.8,legend="Same coordinate (Xi and Omega)")
    r.segment(x0=c["longitude"], y0=c["latitude"], x1=c["longitude"],
                  y1=c["latitude"], color="grey", line_width=1)
        # Xi 
    r.circle(np.array(df_dic['dfTempX']["longitude"]),np.array(df_dic['dfTempX']["latitude"]), size=5,fill_color='red', fill_alpha=.7, line_color='Crimson',line_alpha=0,legend="Different coordinate (Xi)")
    for i in gs_dict.values():
            r.line(i[:,0],i[:,1], color='Crimson')
    r.line([4.083,6.333,9,12], [37.667,39,39,37.25], line_alpha=0.8, color='Crimson')
    r.line([5.333,9.333,9,9], [41.833,41.833,40.5,39], line_alpha=0.8, color='Crimson')
    r.line([15.167,17,19,20.333], [45.833,43,43.167,42.333], line_alpha=0.8, color='Crimson')

        # Omega
    r.circle(np.array(df_dic['dfTemp']["longitude"]),np.array(df_dic['dfTemp']["latitude"]), size=5,fill_color='DodgerBlue', fill_alpha=0.8, line_color='DodgerBlue',line_alpha=0,legend="Different coordinate  (Omega)")
    for i in fs_dict.values():
            r.line(i[:,0],i[:,1], color='DodgerBlue')
    r.line([4.083,6.333,9,12], [37.667,39,39,37.25], line_alpha=0.8, color='DodgerBlue')
    r.line([5.333,9.167,9,9], [41.833,41.333,40.167,39], line_alpha=0.8, color='DodgerBlue')
    r.line([15,17,19,20.333], [45.833,43,43.167,42.333], line_alpha=0.8, color='DodgerBlue')
    r.circle(np.array(IbEq["longitude"]),np.array(IbEq["latitude"]), size=5.5,fill_color='lightgrey', fill_alpha=1, line_color='lightgrey',line_alpha=1)
    
    
    show(r);        
    
def comp_plot_map_02(fs_dic,gs_dic,f,g,IbEq2):
    """This function returns the comparsion map based on the entered values as follows:
    fs_dic ~ dictiornay of all coastal localities in Omega -->dict
    gs_dic ~ dictiornay of all coastal localities in Xi -->dict
    df_dic ~ dictiornay of all localities -->dict
    f ~ Selection of coastal localities in Omega -->pd
    g ~ Selection of coastal localities in Xi -->pd
    Ibeq2
    c
    """
    r = figure(title='Iberian peninsula: Comparison between Xi (red) and Omega (blue)', width=1000, height=800, x_range=(1.5, 22), y_range=(35.5, 47) )

        #r.circle(np.array(IbEq["longitude_Xi"]),np.array(IbEq["latitude_Xi"]), size=5.5,fill_color='lightgrey', fill_alpha=1, line_color='lightgrey',line_alpha=0.8)
        #r.segment(x0=c["longitude_Xi"], y0=c["latitude_Xi"], x1=c["longitude_Omega"],
                #  y1=c["latitude_Omega"], color="grey", line_width=1)

        # Xi 
    

    r.circle(np.array(g['longitude']),np.array(g["latitude"]), size=6,fill_color='red', fill_alpha=.7, line_color='Crimson',line_alpha=0,legend="Different boundary coordinate (Xi)")
    for i in gs_dic.values():
            r.line(i[:,0],i[:,1], color='Crimson')
        #r.line([4.083,6.333,9,12], [37.667,39,39,37.25], line_alpha=0.8, color='Crimson')
        #r.line([5.333,9.333,9,9], [41.833,41.833,40.5,39], line_alpha=0.8, color='Crimson')
    r.line([15.167,17,19,20.333], [45.833,43,43.167,42.333], line_alpha=0.8, color='Crimson')

        # Omega
    r.circle(np.array(f["longitude"]),np.array(f["latitude"]), size=6,fill_color='blue', fill_alpha=0.8, line_color='blue',line_alpha=0,legend="Different boundary coordinate (Omega)")

    for i in fs_dic.values():
             r.line(i[:,0],i[:,1], color='blue')
        #r.line([4.083,6.333,9,12], [37.667,39,39,37.25], line_alpha=0.8, color='DodgerBlue')
        #r.line([5.333,9.167,9,9], [41.833,41.333,40.167,39], line_alpha=0.8, color='DodgerBlue')
    r.line([15,17,19,20.333], [45.833,43,43.167,42.333], line_alpha=0.8, color='navy')
    r.circle(np.array(IbEq2["longitude"]),np.array(IbEq2["latitude"]), size=6,fill_color='grey', fill_alpha=1, line_color='grey',line_alpha=1,legend="Same boundary coordinate (Xi and Omega)")
    r.legend.location = "bottom_right"

   

    show(r);
    
    
    
    
    
