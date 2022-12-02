import configparser
import os
from logs.logsfile import logger


class WRConfigFile(object):
    @logger.catch()
    def __init__(self):
        """
        配置ini文件路径
        strict: 是否允许单一配置文件中有相同的section或同一section中有相同option
        读写操作时需分开进行，不能用同一个实例，否则写入之前配置文件中存在的内容。
        """
        self.config_file = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\\configfile.ini'
        self.conf = configparser.ConfigParser(strict=False)

    @logger.catch()
    def read_conf(self, section, option):
        """
        读取ini文件的section和option，判断section和option是否存在，返回option字段的值
        :param section:ini文件的section字段
        :param option:ini文件section下的option字段
        :return: 返回option字段的值
        """
        self.conf.read(self.config_file, encoding='utf-8')
        if self.conf.has_section(section=section):
            if self.conf.has_option(section=section, option=option):
                result = self.conf.get(section=section, option=option)
                return result
            else:
                logger.warning('ini配置文件{sections}节点缺少{options},无法查询数据', sections=section, options=option)
        else:
            logger.warning('ini配置文件缺少{sections}节点,无法查询数据', sections=section)

    @logger.catch()
    def write_conf(self, section=None, option=None, value=''):
        """
        读取ini文件追加写入section、option、values值
        不能在原有节点上添加option，只能新建节点添加
        确定section字段是否存在时只能读取当次文件操作时是否存在相同section字段，
        save_conf文件之后，第二次操作读取不了section字段，需要read配置文件才能读取，read配置文件读写时又会写入之前配置文件中存在的内容。
        """
        # self.conf.read(self.config_file, encoding='utf-8')
        # self.conf.clear()
        section_values = self.conf.has_section(section)
        if not section_values:
            logger.warning('ini配置文件缺少{sections}节点', sections=section)
            self.conf.add_section(section)
            logger.success('ini配置文件添加{sections}节点成功', sections=section)
        self.conf.set(section=section, option=option, value=value)

    def sava_conf(self):
        """
        保存修改的ini文件
        """
        fp = open(self.config_file, 'a', encoding='utf-8')
        logger.success('正在打开文件，准备写入数据:{config_file}', config_file=self.config_file)
        self.conf.write(fp=fp)
        logger.success('数据写入文件成功:{config_file}', config_file=self.config_file)
        fp.close()
        logger.success('关闭文件:{config_file}', config_file=self.config_file)


if __name__ == '__main__':
    WRConfigFile().read_conf('database', 'host')
    WRConfigFile().read_conf('test', 'name')
    WRConfigFile().read_conf('test', 'sex')
    wrc = WRConfigFile()
    wrc.write_conf('test', 'name', '小红')
    wrc.write_conf('test', 'sex', '小白')
    wrc.write_conf('test', 'age', '小黑')
    wrc.write_conf('test', 'phone', '小绿')
    wrc.sava_conf()

