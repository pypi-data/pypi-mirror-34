#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/5/28

"""
    desc:pass
"""
from dueros.directive.AudioPlayer.Control.RadioButton import RadioButton
from dueros.directive.AudioPlayer.Control.ThumbsUpDownButtonEnum import ThumbsUpDownButtonEnum

class ThumbsUpDownButton(RadioButton):

    def __init__(self, selectedValue=ThumbsUpDownButtonEnum.THUMBS_UP.value):
        super(ThumbsUpDownButton, self).__init__('THUMBS_UP_DOWN', selectedValue)

    def setSelectedValue(self, selectedValue=ThumbsUpDownButtonEnum.THUMBS_UP):
        if ThumbsUpDownButtonEnum.inEnum(selectedValue):
            self.data['selectedValue'] = selectedValue.value
        else:
            self.data['selectedValue'] = ThumbsUpDownButtonEnum.THUMBS_UP.value

    pass


if __name__ == '__main__':
    pass