try:
    import simplejson as json
except ImportError:
    import json

from django.db import models


class ModelWithExtraInfo(models.Model):
    """
    抽象model，提供一json格式的字典的extra_info域。
    """

    class Meta:
        abstract = True

    extra_info = models.TextField(blank=True, default="", help_text="json字典形式的额外信息")

    def get_extra_info_dict(self):
        """
        将extra_info json形式的字符串转换成一dict
        :return: dict
        """
        return json.loads(self.extra_info) if self.extra_info else {}

    def set_extra_info_dict(self, extra_info_dict):
        """
        设置extra_info的值。
        注意: 不会主动保存到数据库，如需更新到数据库，需额外调用save方法
        """
        self.extra_info = json.dumps(extra_info_dict, ensure_ascii=False)

    def update_extra_info_dict(self, update_dict):
        """
        将update_dict字典更新到extra_info
        """
        extra_info_dict = self.get_extra_info_dict()
        extra_info_dict.update(update_dict)
        self.set_extra_info_dict(extra_info_dict)

    # 为了兼容函数名差异
    def get_extra_info(self, key, default=None):
        return self.get_extra_info_with_key(key, default)

    def set_extra_info(self, key, value):
        """
        向extra_info里添加对应域
        """
        self.set_extra_info_with_key(key, value)

    def delete_extra_info(self, key):
        """
        向extra_info里删除对应域
        """
        return self.delete_extra_info_with_key(key)

    def update_extra_info(self, update_dict):
        self.update_extra_info_dict(update_dict)

    @staticmethod
    def simple_property(property_name, default):
        def get_property(self):
            return self.get_extra_info_with_key(property_name, default)

        def set_property(self, value):
            self.set_extra_info_with_key(property_name, value)

        return property(get_property, set_property)
