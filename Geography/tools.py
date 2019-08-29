import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from bokeh.plotting import figure, output_file, show, ColumnDataSource
from bokeh.io import output_notebook, output_file, save
output_notebook()
from bokeh.models import HoverTool,BoxZoomTool,ResetTool, WheelZoomTool,Legend, LegendItem
from bokeh.layouts import row, gridplot, layout

class Geography(object):
    def __init__(self,fs_dict,gs_dict,df_dict,select_recension=None):
        self.fs_dict=fs_dict
        self.gs_dict=gs_dict
        self.df_dict=df_dict
        self.select_recension=select_recension

    def plot_recension(self,fs_dict,gs_dict,df_dict,select_recension):
        
        """This function returns the map based on the entered values as follows:
        fs_dic ~ dictiornay of  coastal localities in Omega  -->dict
        gs_dict ~dictiornay of  coastal localities in Xi  -->dict
        df_dic ~ dictiornay of all localities -->dict
        title ~ either 'Omega ' or -'Xi '  -->string
        pay attention to capitalization 
        """
        
        p = figure(title=self.select_recension, width=1000, height=800, x_range=(1.5, 22), y_range=(35.5, 47))
        if select_recension== 'Omega':
            for i in self.fs_dict.values():
                p.line(i[:,0],i[:,1], color="grey")
                inn_1=p.line([4.083,6.333,9,12], [37.667,39,39,37.25], line_alpha=0.8, color="grey")
                inn_2=p.line([5.333,9.167,9,9], [41.833,41.333,40.167,39], line_alpha=0.8, color="grey")
                inn_3=p.line([15,17,19,20.333], [45.833,43,43.167,42.333], line_alpha=0.8, color="grey")
                co="dfTemp"
                p.circle(np.array(self.df_dict[co]['longitude']),np.array(self.df_dict[co]['latitude']), fill_color="blue",size=6, fill_alpha=.9, line_color="blue",line_alpha=0.6)
        elif select_recension== 'Xi':
            for i in self.gs_dict.values():
                p.line(i[:,0],i[:,1], color="grey")
                inn_1=p.line([4.083,6.333,9,12], [37.667,39,39,37.25], line_alpha=0.8, color="grey")
                inn_2=p.line([5.333,9.333,9,9], [41.833,41.833,40.5,39], line_alpha=0.8, color="grey")
                inn_3=p.line([15.167,17,19,20.333], [45.833,43,43.167,42.333], line_alpha=0.8, color="grey")
                co='dfTempX'
                p.circle(np.array(self.df_dict[co]['longitude']),np.array(self.df_dict[co]['latitude']), fill_color="red",size=6, fill_alpha=.9, line_color="red",line_alpha=0.6)
        show(p)

    def plot_compare_recension(self,fs_dict,gs_dict,df_dict):
        
        """This function returns the comparsion map based on the entered values as follows:
        fs_dic ~ dictiornay of all coastal localities in Omega
        gs_dic ~ dictiornay of all coastal localities in Xi
        df_dic ~ dictiornay of all localities -->dict
        """
        
        a=self.df_dict['dfTempX'].reset_index(level=['chap_ID','sec_ID','ID'])
        a=a[a.longitude.apply(lambda row: row not in [0])]
        a=a[['ID','longitude','latitude']].dropna()

        b=self.df_dict['dfTemp'].reset_index(level=['chap_ID','sec_ID','ID'])
        b=b[b.longitude.apply(lambda row: row not in [0])]
        b=b[['ID','longitude','latitude']].dropna()

        c = pd.merge(left=a, right=b,how='inner')

        IbEq = c[c["longitude"]==c["longitude"]]
        IbEq = IbEq[IbEq["latitude"]==IbEq["latitude"]]
        r = figure(title='Comparison between Xi (red) and Omega (blue)', width=1000, height=800, x_range=(1.5, 22), y_range=(35.5, 47))
        r.circle(np.array(IbEq["longitude"]),np.array(IbEq["latitude"]), size=5.5,fill_color='lightgrey', fill_alpha=1, line_color='lightgrey',line_alpha=0.8,legend="Same coordinate (Xi and Omega)")
        #r.segment(x0=c["longitude"], y0=c["latitude"], x1=c["longitude"],y1=c["latitude"], color="grey", line_width=1)
            # Xi 
        r.circle(np.array(self.df_dict['dfTempX']["longitude"]),np.array(self.df_dict['dfTempX']["latitude"]), size=5,fill_color='red', fill_alpha=.7,                         line_color='Crimson',line_alpha=0,legend="Different coordinate (Xi)")
        for i in self.gs_dict.values():
                r.line(i[:,0],i[:,1], color='Crimson')
        r.line([4.083,6.333,9,12], [37.667,39,39,37.25], line_alpha=0.8, color='Crimson')
        r.line([5.333,9.333,9,9], [41.833,41.833,40.5,39], line_alpha=0.8, color='Crimson')
        r.line([15.167,17,19,20.333], [45.833,43,43.167,42.333], line_alpha=0.8, color='Crimson')

            # Omega
        r.circle(np.array(self.df_dict['dfTemp']["longitude"]),np.array(self.df_dict['dfTemp']["latitude"]), size=5,fill_color='DodgerBlue', fill_alpha=0.8,   line_color='DodgerBlue',line_alpha=0,legend="Different coordinate  (Omega)")
        for i in self.fs_dict.values():
                r.line(i[:,0],i[:,1], color='DodgerBlue')
        r.line([4.083,6.333,9,12], [37.667,39,39,37.25], line_alpha=0.8, color='DodgerBlue')
        r.line([5.333,9.167,9,9], [41.833,41.333,40.167,39], line_alpha=0.8, color='DodgerBlue')
        r.line([15,17,19,20.333], [45.833,43,43.167,42.333], line_alpha=0.8, color='DodgerBlue')
        r.circle(np.array(IbEq["longitude"]),np.array(IbEq["latitude"]), size=5.5,fill_color='lightgrey', fill_alpha=1, line_color='lightgrey',line_alpha=1)


        show(r);

    def plot_border_compare_recension(self,fs_dict,gs_dict,df_dict):
        
        """This function returns the comparsion map based on the entered values as follows:
        fs_dic ~ dictiornay of all coastal localities in Omega -->dict
        gs_dic ~ dictiornay of all coastal localities in Xi -->dict
        df_dic ~ dictiornay of all localities -->dict
        
        """
        g = self.df_dict['dfTempX'][(self.df_dict['dfTempX'].type_sec == 'coast section') & (self.df_dict['dfTempX'].type == 'locality') & self.df_dict['dfTempX'].category.apply(lambda         row: row not in ['boundary','river path','river source'])]     [['longitude','latitude']]
        g2=g.reset_index(level=['chap_ID','sec_ID','ID'])
        g2=g2[g2.longitude.apply(lambda row: row not in [0])]
        g2=g2[['ID','longitude','latitude']].dropna()
        f = self.df_dict['dfTemp'][(df_dict['dfTemp'].type_sec == 'coast section') & (self.df_dict['dfTemp'].type == 'locality') & self.df_dict['dfTemp'].category.apply(lambda row: row         not in ['boundary','river path','river source'])][['longitude','latitude']]

        f2=f.reset_index(level=['chap_ID','sec_ID','ID'])
        f2=f2[f2.longitude.apply(lambda row: row not in [0])]
        f2=f2[['ID','longitude','latitude']].dropna()
        k = pd.merge(left=f2, right=g2,how='inner')
        IbEq2 = k[k["longitude"]==k["longitude"]]
        IbEq2 = IbEq2[IbEq2["latitude"]==IbEq2["latitude"]]
        r = figure(title='Iberian peninsula: Comparison between Xi (red) and Omega (blue)', width=1000, height=800, x_range=(1.5, 22), y_range=(35.5, 47) )
            # Xi 

            #r.circle(np.array(IbEq["longitude_Xi"]),np.array(IbEq["latitude_Xi"]), size=5.5,fill_color='lightgrey', fill_alpha=1, line_color='lightgrey',line_alpha=0.8)
            #r.segment(x0=c["longitude_Xi"], y0=c["latitude_Xi"], x1=c["longitude_Omega"],
                    #  y1=c["latitude_Omega"], color="grey", line_width=1)

            # Xi 
        r.circle(np.array(g['longitude']),np.array(g["latitude"]), size=6,fill_color='red', fill_alpha=.7, line_color='Crimson',line_alpha=0,legend="Different boundary coordinate (Xi)")
        for i in self.gs_dict.values():
                r.line(i[:,0],i[:,1], color='Crimson')
            #r.line([4.083,6.333,9,12], [37.667,39,39,37.25], line_alpha=0.8, color='Crimson')
            #r.line([5.333,9.333,9,9], [41.833,41.833,40.5,39], line_alpha=0.8, color='Crimson')
        r.line([15.167,17,19,20.333], [45.833,43,43.167,42.333], line_alpha=0.8, color='Crimson')

            # Omega
        r.circle(np.array(f["longitude"]),np.array(f["latitude"]), size=6,fill_color='blue', fill_alpha=0.8, line_color='blue',line_alpha=0,legend="Different boundary coordinate     (Omega)")

        for i in self.fs_dict.values():
                 r.line(i[:,0],i[:,1], color='blue')
            #r.line([4.083,6.333,9,12], [37.667,39,39,37.25], line_alpha=0.8, color='DodgerBlue')
            #r.line([5.333,9.167,9,9], [41.833,41.333,40.167,39], line_alpha=0.8, color='DodgerBlue')
        r.line([15,17,19,20.333], [45.833,43,43.167,42.333], line_alpha=0.8, color='navy')
        r.circle(np.array(IbEq2["longitude"]),np.array(IbEq2["latitude"]), size=6,fill_color='grey', fill_alpha=1, line_color='grey',line_alpha=1,legend="Same boundary coordinate (Xi   and Omega)")
        r.legend.location = "bottom_right"
        show(r);

    
