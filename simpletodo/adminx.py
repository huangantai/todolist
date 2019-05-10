from xadmin import views
import xadmin

class BaseSetting(object):
    """xadmin的基本配置"""
    enable_themes = True  # 开启主题切换功能
    use_bootswatch = True
 
 
 
class GlobalSettings(object):
    """xadmin的全局配置"""
    site_title = "todolist"  # 设置站点标题
    site_footer = "-todolist-"  # 设置站点的页脚
    menu_style = "accordion"  # 设置菜单折叠
 
 
xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(views.BaseAdminView, BaseSetting)

from simpletodo.models import Todo

# Register your models here.
class TodoAdmin(object):
    list_display = ['user', 'todo', 'priority', 'flag', 'pubtime']
    list_filter = ['pubtime','priority']
    ordering = ['-pubtime']
    list_editable=['todo','priority','flag']

xadmin.site.register(Todo, TodoAdmin)  
