import os
import logging
from qtutils import UiLoader
from blacs.plugins import PLUGINS_DIR


name = "Dont repeat if NOREPEAT in shot name"
module = "repeat_control" # should be folder name
logger = logging.getLogger('BLACS.plugin.%s'%module)

class Plugin(object):
    def __init__(self, initial_settings):
        self.menu = None
        self.notifications = {}
        self.BLACS = None
        
    def get_menu_class(self):
        return None
        
    def get_notification_classes(self):
        return []
        
    def get_setting_classes(self):
        return []
        
    def get_callbacks(self):
        return {'shot_ignore_repeat' : self.on_shot_ignore_repeat}

    def on_shot_ignore_repeat(self,path):
        print(path)
        logger.info(f"got {path}")
        if 'NOREPEAT' in path:
            logger.info(f"NOREPEAT found in {path}")
            return True
        return False
        
    def set_menu_instance(self,menu):
        self.menu = menu
        
    def set_notification_instances(self,notifications):
        self.notifications = notifications

    def plugin_setup_complete(self, BLACS):
        self.BLACS = BLACS
        
    def get_save_data(self):
        return {}
        
    def close(self):
        pass
        
# class Menu(object):
    # pass
    
# class Notification(object):
    # pass


# class Setting(object):
#     name = "General"

#     def __init__(self,data):
#         # This is our data store!
#         self.data = data
        
#         self.var_list = [('ct_editor','','text','setText')]
#         for var in self.var_list:
#             if var[0] not in self.data:
#                 data[var[0]] = var[1]
        
#     # Create the GTK page, return the page and an icon to use on the label (the class name attribute will be used for the label text)   
#     def create_dialog(self,notebook):
#         ui = UiLoader().load(os.path.join(PLUGINS_DIR, 'general', 'general.ui'))
        
#         # get the widgets!
#         self.widgets = {}
#         for var in self.var_list:            
#             self.widgets[var[0]] = getattr(ui,var[0])
#             getattr(self.widgets[var[0]],var[3])(self.data[var[0]])
        
#         return ui,None
    
#     def get_value(self,name):
#         if name in self.data:
#             return self.data[name]
        
#         return None
    
#     def save(self):
#         # transfer the contents of the list store into the data store, and then return the data store
#         for var in self.var_list:
#             # TODO: Make more general than forcing type to string
#             self.data[var[0]] = str(getattr(self.widgets[var[0]],var[2])())
        
#         return self.data
        
#     def close(self):
        pass
        
    