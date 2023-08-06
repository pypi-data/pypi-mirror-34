# -*- coding: utf-8 -*-
# Created by restran on 2017/7/30
from __future__ import unicode_literals, absolute_import

import hashlib
import os
import shutil
import subprocess
import zipfile
from optparse import OptionParser

from mountains import text_type, force_text
from ..utils import find_ctf_flag, file_strings

parser = OptionParser()
parser.add_option("-f", "--file_name", dest="file_name", type="string",
                  help="read from file")
parser.add_option("-s", "--flag_strict_mode", dest="flag_strict_mode", default=False,
                  action="store_true", help="find flag strict mode")

"""
自动检测文件可能的隐写，需要在Linux下使用 Python3 运行
一些依赖还需要手动安装

TODO 文件中可见字符的处理，对于 \00 这种分隔开的字符，需要能够分离
"""


class WhatStego(object):
    def __init__(self, file_path, flag_strict_mode=True):
        self.file_path = file_path
        self.current_path = os.path.dirname(file_path)
        base_name = os.path.basename(file_path)
        # 文件的扩展名
        self.file_ext = os.path.splitext(base_name)[1]

        # 文件类型
        self.file_type = None

        self.output_path = os.path.join(self.current_path, 'output_%s' % base_name)
        self.flag_strict_mode = flag_strict_mode
        # 需要强调输出的结果内容
        self.result_list = []

        self.extract_file_md5_dict = {}
        self.log_file_name = 'log.txt'
        self.log_file = None

    def run_shell_cmd(self, cmd):
        try:
            (stdout, stderr) = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                                                stderr=subprocess.PIPE, shell=True,
                                                universal_newlines=True).communicate()
            if stdout is None:
                stdout = ''
            if stderr is None:
                stderr = ''
            return '%s%s' % (stdout, stderr)
        except Exception as e:
            self.log(e)
            self.log('!!!error!!!')
            self.log(cmd)
            return ''

    def strings(self):
        self.log('\n--------------------')
        self.log('run strings')
        out_file = os.path.join(self.output_path, 'strings_1.txt')
        cmd = 'strings %s > %s' % (self.file_path, out_file)
        self.run_shell_cmd(cmd)
        out_file = os.path.join(self.output_path, 'strings_2.txt')
        file_strings.file_2_printable_strings(self.file_path, out_file)

    def check_strings(self):
        file_path = os.path.join(self.output_path, 'strings_1.txt')
        with open(file_path, 'r') as f:
            string_data = f.read()

        if 'Adobe Fireworks' in string_data and self.file_type == 'png':
            self.result_list.append('[*] 很可能是 Fireworks 文件，请用 Fireworks 打开')
        if 'Adobe Photoshop' in string_data:
            self.result_list.append('[*] 可能存在 Photoshop 的 psd 文件，请检查是否有分离出 psd 文件')

    def png_check(self):
        if self.file_type == 'png':
            self.log('\n--------------------')
            self.log('run pngcheck')
            cmd = 'pngcheck -vv %s' % self.file_path
            stdout = self.run_shell_cmd(cmd)
            self.log(stdout)
            if 'CRC error' in stdout:
                self.result_list.append('[*] PNG 文件 CRC 错误，请检查图片的大小是否有被修改')

            out_list = stdout.split('\n')
            last_length = None
            for t in out_list:
                t = t.strip()
                t = force_text(t)
                if t.startswith('chunk IDAT'):
                    try:
                        length = int(t.split(' ')[-1])
                        if last_length is not None and last_length < length:
                            self.result_list.append('[*] PNG 文件尾部可能附加了数据')
                            break
                        else:
                            last_length = length
                    except:
                        pass

    def log(self, text):
        text = text_type(text)
        print(text)
        self.log_file.write(text)
        self.log_file.write('\n')

    def check_file(self):
        self.log('\n--------------------')
        self.log('run file')
        cmd = 'file %s' % self.file_path
        stdout = self.run_shell_cmd(cmd)
        if 'PNG image data' in stdout:
            self.file_type = 'png'
        elif 'JPEG image data' in stdout:
            self.file_type = 'jpg'
        elif 'bitmap' in stdout:
            self.file_type = 'bmp'
        stdout = stdout.replace(self.file_path, '').strip()
        stdout = stdout[2:]
        self.result_list.append('[*] 文件类型: %s' % self.file_type)
        self.result_list.append('[*] 文件类型: %s' % stdout)

        file_size = os.path.getsize(self.file_path) / 1024.0
        self.result_list.append('[*] 文件大小: %.3fKB' % file_size)

    def zsteg(self):
        """
        检测 png 和 bmp 的隐写
        :return:
        """
        if self.file_type in ['bmp', 'png']:
            self.log('\n--------------------')
            self.log('run zsteg')
            out_file = os.path.join(self.output_path, 'zsteg.txt')
            cmd = 'zsteg -a -v %s > %s' % (self.file_path, out_file)
            self.run_shell_cmd(cmd)

    def stegdetect(self):
        """
        用于检测 jpg 的隐写
        :return:
        """
        if self.file_type == 'jpg':
            self.log('\n--------------------')
            self.log('run stegdetect')
            # -s 表示敏感度，太低了会检测不出来，太大了会误报
            cmd = 'stegdetect -s 5 %s' % self.file_path
            stdout = self.run_shell_cmd(cmd)
            self.log(stdout)
            stdout = stdout.lower()
            if 'negative' not in stdout.lower():
                self.result_list.append('\n')

            if 'appended' in stdout:
                text = '[*] 图片后面可能附加了文件，请尝试将 jpg 的文件尾 FFD9 后面的数据组成新的文件'
                self.result_list.append(text)
                text = '    请用 WinHex 打开，搜索 FFD9 并观察后面的数据'
                self.result_list.append(text)
                text = '    若没有分离出文件，很可能需要手动修复文件头'
                self.result_list.append(text)
            if 'jphide' in stdout:
                text = '[*] 使用了 jphide 隐写，如果没有提供密码，可以先用 Jphswin.exe 试一下空密码，再用 stegbreak 用弱口令爆破'
                text = '[*] 也有可能是 steghide 隐写，如果没有提供密码，可以用 steg_hide_break 用弱口令爆破'
                text = '[*] 也有可能是 outguess 隐写，outguess -r in.jpg out.txt'
                self.result_list.append(text)
                text = '    注意，jphide 的检测很可能会出现误报，可以尝试'
                self.result_list.append(text)
            if 'outguess' in stdout:
                text = '[*] 使用了 outguess 隐写'
                self.result_list.append(text)
            if 'f5' in stdout:
                text = '[*] 使用了 F5 隐写'
                self.result_list.append(text)
            if 'jsteg' in stdout:
                text = '[*] 使用了 jsteg  隐写'
                self.result_list.append(text)
            if 'invisible secrets' in stdout:
                text = '[*] 使用了 invisible secrets 隐写'
                self.result_list.append(text)

    @classmethod
    def check_file_md5(cls, file_path):
        with open(file_path, 'rb') as f:
            md5 = hashlib.md5(f.read()).hexdigest()
            return md5

    def unzip(self, file_path, destination_path):
        tmp_file_path = file_path.replace(self.current_path, '')
        try:
            with zipfile.ZipFile(file_path, "r") as zip_ref:
                try:
                    zip_ref.extractall(destination_path)
                    return True
                except Exception as e:
                    if 'password required' in e:
                        self.log('压缩包 %s 需要密码' % tmp_file_path)
                    else:
                        self.log('压缩包 %s 解压失败' % tmp_file_path)
                    return False
        except Exception as e:
            self.log('压缩包 %s 解压失败' % tmp_file_path)
            return False

    def unzip_archive(self):
        for root, dirs, files in os.walk(self.output_path):
            for f_name in files:
                path = os.path.join(root, f_name)
                if path.endswith('.zip'):
                    zip_path = path + '_unzip'
                    self.unzip(path, zip_path)

    def check_extracted_file(self):
        # 排除这些文件
        exclude_file_list = [
            'foremost/audit.txt',
            'strings_1.txt',
            'strings_2.txt',
            'zsteg.txt',
            'log.txt'
        ]
        exclude_file_list = [
            os.path.join(self.output_path, t)
            for t in exclude_file_list
        ]
        self.extract_file_md5_dict = {}
        file_type_dict = {}

        # 解压出压缩包
        self.unzip_archive()

        for root, dirs, files in os.walk(self.output_path):
            for f_name in files:
                path = os.path.join(root, f_name)
                if path in exclude_file_list:
                    continue

                md5 = self.check_file_md5(path)
                file_ext = os.path.splitext(path)[1].lower()
                if file_ext != '':
                    # 去掉前面的.
                    file_ext = file_ext[1:]

                if md5 in self.extract_file_md5_dict:
                    old_file = self.extract_file_md5_dict[md5]
                    # 如果是有扩展名的，则替换没有扩展名的
                    if file_ext == '' or old_file['ext'] != '':
                        continue

                self.extract_file_md5_dict[md5] = {
                    'path': path,
                    'ext': file_ext
                }

        for k, v in self.extract_file_md5_dict.items():
            if v['ext'] in file_type_dict:
                item = file_type_dict[v['ext']]
                item.append(v['path'])
            else:
                file_type_dict[v['ext']] = [v['path']]

        total_num = len(self.extract_file_md5_dict.keys())
        self.result_list.append('\n')
        self.result_list.append('[+] 分离出的文件数: %s' % total_num)
        has_zip = False
        # 把所有不重复的文件，按文件类型重新存储
        for file_type, v in file_type_dict.items():
            if file_type == '':
                file_type = 'unknown'

            path = os.path.join(self.output_path, file_type)
            if not os.path.exists(path):
                os.mkdir(path)

            self.result_list.append('[+] %s: %s' % (file_type, len(v)))
            for i, f_p in enumerate(v):
                if file_type != 'unknown':
                    f_name = '%s.%s' % (i, file_type)
                else:
                    f_name = '%s' % i

                p = os.path.join(path, f_name)
                # 移动文件
                shutil.move(f_p, p)
                file_size = os.path.getsize(p) / 1024.0
                self.result_list.append('    %s: %.3fKB' % (i, file_size))

            if file_type == 'zip':
                has_zip = True

        # 自动删除这些文件夹
        path = os.path.join(self.output_path, 'foremost')
        self.remove_dir(path)
        path = os.path.join(self.output_path, 'what_format')
        self.remove_dir(path)
        path = os.path.join(self.output_path, 'binwalk')
        self.remove_dir(path)

        if has_zip:
            self.result_list.append('[!] 如果 zip 文件打开后有很多 xml，很可能是 docx')

    @classmethod
    def remove_dir(cls, dir_path):
        if os.path.exists(dir_path):
            shutil.rmtree(dir_path)

    def binwalk(self):
        self.log('\n--------------------')
        self.log('run binwalk')
        out_path = os.path.join(self.output_path, 'binwalk')
        self.remove_dir(out_path)
        # binwalk 会自动对 zlib 文件解压缩，可以进一步对解压缩后的文件类型进行识别
        cmd = 'binwalk -v -M -e -C %s %s' % (out_path, self.file_path)
        stdout = self.run_shell_cmd(cmd)
        self.log(stdout)
        self.process_binwalk_unknown(out_path)

    def process_binwalk_unknown(self, binwalk_path):
        self.log('\n--------------------')
        self.log('process binwalk unknown files')
        for root, dirs, files in os.walk(binwalk_path):
            for f_name in files:
                path = os.path.join(root, f_name)
                file_ext = os.path.splitext(path)[1].lower()
                if file_ext == '':
                    out_path = os.path.join(root, 'out_' + f_name)
                    cmd = 'what_format %s %s' % (path, out_path)
                    stdout = self.run_shell_cmd(cmd)
                    self.log(out_path)
                    self.log(stdout)

    def foremost(self):
        self.log('\n--------------------')
        self.log('run foremost')
        out_path = os.path.join(self.output_path, 'foremost')
        self.remove_dir(out_path)
        cmd = 'foremost -o %s %s' % (out_path, self.file_path)
        stdout = self.run_shell_cmd(cmd)
        self.log(stdout)

    def what_format(self):
        self.log('\n--------------------')
        self.log('run what_format')
        out_path = os.path.join(self.output_path, 'what_format')
        self.remove_dir(out_path)
        cmd = 'what_format %s %s' % (self.file_path, out_path)
        stdout = self.run_shell_cmd(cmd)
        self.log(stdout)

    def run_exif_tool(self):
        if self.file_type not in ['bmp', 'png', 'jpg', 'jpeg', 'gif']:
            return

        self.log('\n--------------------')
        self.log('run exiftool')
        cmd = 'exiftool %s' % self.file_path
        stdout = self.run_shell_cmd(cmd)
        self.log(stdout)

    def run(self):
        # 删除旧的数据
        self.remove_dir(self.output_path)
        # 创建输出路径
        if not os.path.exists(self.output_path):
            os.mkdir(self.output_path)

        log_file = os.path.join(self.output_path, self.log_file_name)
        self.log_file = open(log_file, 'w')

        self.check_file()
        self.strings()
        self.zsteg()
        self.binwalk()
        self.foremost()
        self.what_format()
        self.png_check()
        self.stegdetect()
        self.check_strings()
        self.check_extracted_file()
        self.run_exif_tool()

        self.log('\n--------------------')
        for t in self.result_list:
            self.log(t)

        self.log('\n--------------------')
        self.log('尝试从文件文本中提取 flag')
        find_flag_result_dict = {}
        zsteg_file = os.path.join(self.output_path, 'zsteg.txt')
        result = find_ctf_flag.get_flag_from_file(zsteg_file, self.flag_strict_mode, find_flag_result_dict)
        self.log(result)
        strings_file = os.path.join(self.output_path, 'strings_1.txt')
        result = find_ctf_flag.get_flag_from_file(strings_file, self.flag_strict_mode, find_flag_result_dict)
        self.log(result)
        strings_file = os.path.join(self.output_path, 'strings_2.txt')
        result = find_ctf_flag.get_flag_from_file(strings_file, self.flag_strict_mode, find_flag_result_dict)
        self.log(result)
        self.log('=======================')
        self.log_file.close()


def main():
    (options, args) = parser.parse_args()

    if options.file_name is not None:
        file_name = options.file_name
    elif len(args) > 0:
        file_name = args[0]
    else:
        parser.print_help()
        return

    file_path = os.path.join(os.getcwd(), file_name)
    WhatStego(file_path, options.flag_strict_mode).run()


if __name__ == '__main__':
    main()
