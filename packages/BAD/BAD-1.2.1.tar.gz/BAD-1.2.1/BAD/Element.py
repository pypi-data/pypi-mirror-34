# coding=utf-8
import time
import re

'''
 :Description:    控件类
 :author          80071482/bony
 :@version         V1.0
 :@Date            2016年11月
'''


class Element(object):
    def __init__(self, xmlElement, ParentElement, device=None):
        self._ELEMENT_LIST_ = []  # 子控件列表
        self._ELEMENT_TYPE_ = xmlElement.attrib  # 控件的属性
        self._PARENT_ELEMENT_ = ParentElement  # 控件的父元素
        self._DEVICE_ = device  # 控件绑定设备方法
        bound = re.compile(r"\d+").findall(self._ELEMENT_TYPE_["bounds"])
        self._ELEMENT_TYPE_["x0"] = int(bound[0])
        self._ELEMENT_TYPE_["y0"] = int(bound[1])
        self._ELEMENT_TYPE_["x1"] = int(bound[2])
        self._ELEMENT_TYPE_["y1"] = int(bound[3])
        self._ELEMENT_TYPE_["width"] = self._ELEMENT_TYPE_["x1"] - self._ELEMENT_TYPE_["x0"]  # 控件的宽
        self._ELEMENT_TYPE_["high"] = self._ELEMENT_TYPE_["y1"] - self._ELEMENT_TYPE_["y0"]  # 控件的高
        self._ELEMENT_TYPE_["center_x"] = (self._ELEMENT_TYPE_["x0"] + self._ELEMENT_TYPE_["x1"]) / 2  # 控件的中心坐标X
        self._ELEMENT_TYPE_["center_y"] = (self._ELEMENT_TYPE_["y0"] + self._ELEMENT_TYPE_["y1"]) / 2  # 控件的中心坐标Y

    def get_parent_element(self):
        """
        获取控件的父元素
        """
        return self._PARENT_ELEMENT_

    def crop(self, path=None, region_path=None):
        self._DEVICE_.crop(
            path = path,
            x0=self._ELEMENT_TYPE_["x0"],
            y0=self._ELEMENT_TYPE_["y0"],
            x1=self._ELEMENT_TYPE_["x1"],
            y1=self._ELEMENT_TYPE_["y1"],
            region_path=region_path
        )

    def get_type(self, _type):
        """
        获取控件属性
        """
        return self._ELEMENT_TYPE_[_type]

    def find_type_element(self, _type, _value):
        """
        根据控件属性获取控件
        """
        for element in self._ELEMENT_LIST_:
            if element.get_type(_type) == _value:
                return element
            ele = element.find_type_element(_type, _value)
            if ele is not None:
                return ele
        return None

    def add_element(self, element):
        """
        给控件添加子控件
        """
        self._ELEMENT_LIST_.append(element)

    def get_elements(self):
        """
        获取子控件列表
        """
        return self._ELEMENT_LIST_

    def click(self):
        """
        点击控件
        """
        self._DEVICE_.click(self._ELEMENT_TYPE_["center_x"], self._ELEMENT_TYPE_["center_y"])

    def input(self, text):
        """
        控件输入
        """
        self.click()
        time.sleep(1)
        self._DEVICE_.input(text)

    def long_click(self):
        """
        控件输入
        """
        self._DEVICE_.longPress(self._ELEMENT_TYPE_["center_x"], self._ELEMENT_TYPE_["center_y"])

    def swipe_left(self):
        """
        向左滑动控件
        """
        self._DEVICE_.swipe(
            int(_ELEMENT_TYPE_["x1"]),
            self._ELEMENT_TYPE_["center_y"],
            int(_ELEMENT_TYPE_["x0"]),
            self._ELEMENT_TYPE_["center_y"],
        )

    def swipe_right(self):
        """
        向右滑动控件
        """
        self._DEVICE_.swipe(
            int(_ELEMENT_TYPE_["x0"]),
            self._ELEMENT_TYPE_["center_y"],
            int(_ELEMENT_TYPE_["x1"]),
            self._ELEMENT_TYPE_["center_y"],
        )

    def swipe_up(self):
        """
        向上滑动控件
        """
        self._DEVICE_.swipe(
            self._ELEMENT_TYPE_["center_x"],
            int(_ELEMENT_TYPE_["y1"]),
            self._ELEMENT_TYPE_["center_x"],
            int(_ELEMENT_TYPE_["y0"]),
        )

    def swipe_down(self):
        """
        向下滑动控件
        """
        self._DEVICE_.swipe(
            self._ELEMENT_TYPE_["center_x"],
            int(_ELEMENT_TYPE_["y0"]),
            self._ELEMENT_TYPE_["center_x"],
            int(_ELEMENT_TYPE_["y1"]),
        )
