from typing import Optional
from technological_index import Mean_Stock_Index, Advance_Decline_Line_Market_Index
from src.Constant_Field import Index_Class_Constant

class Index_Class_Loader():
    def __init__(self):
        self.index_class_dict = \
            {
                Index_Class_Constant.MEAN_INDEX_NAME:Mean_Stock_Index.MEAN_Stock_Index,
                Index_Class_Constant.ADL_INDEX_NAME:Advance_Decline_Line_Market_Index.Advance_Decline_Line_Index
            }

    def get_class(self,class_name:str)->Optional:
        assert class_name in self.index_class_dict, "The index name is not implemented"
        return self.index_class_dict[class_name]

