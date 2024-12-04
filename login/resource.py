from .models import CustomUser
from import_export.resources import ModelResource

class CustomUserResource(ModelResource):
    class Meta:
        model = CustomUser
        fields = ('id','username','phone_number','password')  # 指定要导入导出的字段
        export_order = ('id','username','phone_number','password')  # 指定导出字段的顺序
