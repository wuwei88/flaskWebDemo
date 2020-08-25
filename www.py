from application import app
from controllers.index import index_page
from controllers.member import member_page
from flask_debugtoolbar import DebugToolbarExtension
from common.libs.UrlManager import UrlManager

toolbar = DebugToolbarExtension(app)

'''
拦截器处理 和 错误处理器
'''
from interceptors.Auth import *
from interceptors.errorHandler import *

'''
蓝图
'''
app.register_blueprint(index_page, url_prefix='/')
app.register_blueprint(member_page, url_prefix='/member')

'''
模板函数
'''
app.add_template_global(UrlManager.buildStaticUrl, 'buildStaticUrl')
app.add_template_global(UrlManager.buildUrl, 'buildUrl')
