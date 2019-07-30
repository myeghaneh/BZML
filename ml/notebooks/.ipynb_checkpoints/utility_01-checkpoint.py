import pandas as pd
import seaborn as sns
import matplotlib.pylab as plt

from sklearn.feature_extraction import DictVectorizer
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import cross_val_score, GridSearchCV
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import confusion_matrix,classification_report
from sklearn.model_selection import KFold
from sklearn.metrics import roc_curve  
from sklearn.metrics import roc_auc_score 



def Color_Confusion_Matrix(y, y_test, y_pred):
    cm=confusion_matrix(y_test, y_pred)
    l=len(set(y))
    df_cm = pd.DataFrame(cm, range(l), range(l))
    sns.set(font_scale=1.4)
    sns.heatmap(df_cm,cmap="Blues", annot=True,annot_kws={"size": 16},fmt='g')
    plt.ylabel('True label');
    plt.xlabel('Predicted label');
    plt.title("Confusion Matrix", size = 16)
    plt.savefig('CM_Test_01.png')
    
def plotConfMatrix(cm):
    sns.set(font_scale=1.4)
    cm_df = pd.DataFrame(cm,columns= cm.keys(),index=cm.keys())
    #cm_df.index.name = 'Predicted'
    #cm_df.columns.name = 'Actual'
    sb.heatmap(cm_df, annot=True,annot_kws={"size": 16},fmt='d')
    plt.xlabel('Actual labels')
    plt.ylabel('Predicted labels') 
    plt.title('Confusion Matrix' )
    plt.show()
    

def plot_roc_curve(fpr, tpr,auc):  
    plt.plot(fpr, tpr, color='orange', label='ROC')
    plt.plot([0, 1], [0, 1], color='darkblue', linestyle='--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic (ROC) Curve with AUC {:.3f}'.format(AUC))
    plt.legend()
    plt.show()