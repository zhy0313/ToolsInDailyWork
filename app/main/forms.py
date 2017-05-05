#-*-coding:utf-8-*-
from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *
from .. import files
from flask_wtf.file import FileAllowed,FileField

class ProjectNameForm(FlaskForm):
	name = SelectField(u'选择项目')
	confirm = SubmitField(u'确定')
	
	def __init__(self,*args,**kwargs):
		super(ProjectNameForm,self).__init__(*args,**kwargs)
		self.name.choices = [('naruto',u'火影'),('dragonball',u'龙珠')]
		
class PathForm(FlaskForm):
	path = StringField(u'请输入目标文件夹路径',validators=[Required()])
	submit = SubmitField(u'提交')

class ItemForm(FlaskForm):
	name = StringField(u'道具名',validators=[Optional()])
	item_id = IntegerField(u'道具id',validators=[Optional(),NumberRange(10000000,20000000)])
	function_id = IntegerField(u'功能id',validators=[Optional(),NumberRange(0,12000000)])
	language = SelectField(u'语言版本',choices=[('ALL',u'全部'),('CN',u'国内'),('US','NA'),('FR',u'法语'),('BR',u'巴西'),('TH',u'泰语')])
	submit = SubmitField(u'查询')
	
class ImportForm(FlaskForm):
	csv = FileField(u'请提交csv文件',validators=[Required(),FileAllowed(files,u'只限csv文件！')])
	submit = SubmitField(u'提交')
	
class ItemEditForm(FlaskForm):
	name = StringField(u'道具名称',validators=[Required()])
	item_id = IntegerField(u'道具id',validators=[Required(),NumberRange(0,20000000)])
	function_id = IntegerField(u'功能id',validators=[Required(),NumberRange(0,12000000)])
	language = SelectField(u'语言版本',choices=[('CN',u'国内'),('US','NA'),('FR',u'法语'),('BR',u'巴西'),('TH',u'泰语')])
	project = RadioField(u'项目',choices=[('naruto',u'火影'),('dragonball',u'龙珠')])
	submit = SubmitField(u'提交')
	
class ActivitySearchForm(FlaskForm):
	name = StringField(u'活动名称',validators=[Optional()])
	activity_id = IntegerField(u'活动id',validators=[Optional(),NumberRange(0,200)])
	submit = SubmitField(u'查询')
	
class ActivityEditForm(FlaskForm):
	name = StringField(u'活动名称',validators=[Required()])
	activity_id = IntegerField(u'道具id',validators=[Required(),NumberRange(0,200)])
	art_id = IntegerField(u'艺术字id',validators=[Optional(),NumberRange(0,100)])
	project = RadioField(u'项目',choices=[('naruto',u'火影'),('dragonball',u'龙珠')])
	submit = SubmitField(u'提交')