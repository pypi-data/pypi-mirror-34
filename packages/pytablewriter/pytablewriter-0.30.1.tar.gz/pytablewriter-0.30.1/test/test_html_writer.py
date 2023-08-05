# encoding: utf-8

"""
.. codeauthor:: Tsuyoshi Hombashi <tsuyoshi.hombashi@gmail.com>
"""

from __future__ import absolute_import, print_function, unicode_literals

import pytablewriter
import pytest

from ._common import print_test_result
from .data import (
    Data,
    header_list,
    mix_header_list,
    mix_value_matrix,
    null_test_data_list,
    value_matrix,
    value_matrix_with_none,
)


normal_test_data_list = [
    Data(
        table="",
        indent="  ",
        header=header_list,
        value=value_matrix,
        expected="""<table>
  <thead>
    <tr>
      <th>a</th>
      <th>b</th>
      <th>c</th>
      <th>dd</th>
      <th>e</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="right">1</td>
      <td align="right">123.1</td>
      <td align="left">a</td>
      <td align="right">1.0</td>
      <td align="right">1</td>
    </tr>
    <tr>
      <td align="right">2</td>
      <td align="right">2.2</td>
      <td align="left">bb</td>
      <td align="right">2.2</td>
      <td align="right">2.2</td>
    </tr>
    <tr>
      <td align="right">3</td>
      <td align="right">3.3</td>
      <td align="left">ccc</td>
      <td align="right">3.0</td>
      <td align="left">cccc</td>
    </tr>
  </tbody>
</table>
""",
    ),
    Data(
        table=None,
        indent="  ",
        header=None,
        value=value_matrix,
        expected="""<table>
  <tbody>
    <tr>
      <td align="right">1</td>
      <td align="right">123.1</td>
      <td align="left">a</td>
      <td align="right">1.0</td>
      <td align="right">1</td>
    </tr>
    <tr>
      <td align="right">2</td>
      <td align="right">2.2</td>
      <td align="left">bb</td>
      <td align="right">2.2</td>
      <td align="right">2.2</td>
    </tr>
    <tr>
      <td align="right">3</td>
      <td align="right">3.3</td>
      <td align="left">ccc</td>
      <td align="right">3.0</td>
      <td align="left">cccc</td>
    </tr>
  </tbody>
</table>
""",
    ),
    Data(
        table="tablename",
        indent="    ",
        header=header_list,
        value=[],
        expected="""<table id="tablename">
    <caption>tablename</caption>
    <thead>
        <tr>
            <th>a</th>
            <th>b</th>
            <th>c</th>
            <th>dd</th>
            <th>e</th>
        </tr>
    </thead>
    <tbody></tbody>
</table>
""",
    ),
    Data(
        table=None,
        indent="    ",
        header=header_list,
        value=None,
        expected="""<table>
    <thead>
        <tr>
            <th>a</th>
            <th>b</th>
            <th>c</th>
            <th>dd</th>
            <th>e</th>
        </tr>
    </thead>
    <tbody></tbody>
</table>
""",
    ),
    Data(
        table="",
        indent="  ",
        header=header_list,
        value=value_matrix_with_none,
        expected="""<table>
  <thead>
    <tr>
      <th>a</th>
      <th>b</th>
      <th>c</th>
      <th>dd</th>
      <th>e</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="right">1</td>
      <td align="left"></td>
      <td align="left">a</td>
      <td align="right">1.0</td>
      <td align="left"></td>
    </tr>
    <tr>
      <td align="left"></td>
      <td align="right">2.2</td>
      <td align="left"></td>
      <td align="right">2.2</td>
      <td align="right">2.2</td>
    </tr>
    <tr>
      <td align="right">3</td>
      <td align="right">3.3</td>
      <td align="left">ccc</td>
      <td align="left"></td>
      <td align="left">cccc</td>
    </tr>
    <tr>
      <td align="left"></td>
      <td align="left"></td>
      <td align="left"></td>
      <td align="left"></td>
      <td align="left"></td>
    </tr>
  </tbody>
</table>
""",
    ),
    Data(
        table="tablename",
        indent="    ",
        header=mix_header_list,
        value=mix_value_matrix,
        expected="""<table id="tablename">
    <caption>tablename</caption>
    <thead>
        <tr>
            <th>i</th>
            <th>f</th>
            <th>c</th>
            <th>if</th>
            <th>ifc</th>
            <th>bool</th>
            <th>inf</th>
            <th>nan</th>
            <th>mix_num</th>
            <th>time</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td align="right">1</td>
            <td align="right">1.10</td>
            <td align="left">aa</td>
            <td align="right">1.0</td>
            <td align="right">1</td>
            <td align="left">True</td>
            <td align="left">Infinity</td>
            <td align="left">NaN</td>
            <td align="right">1</td>
            <td align="left">2017-01-01 00:00:00</td>
        </tr>
        <tr>
            <td align="right">2</td>
            <td align="right">2.20</td>
            <td align="left">bbb</td>
            <td align="right">2.2</td>
            <td align="right">2.2</td>
            <td align="left">False</td>
            <td align="left">Infinity</td>
            <td align="left">NaN</td>
            <td align="left">Infinity</td>
            <td align="left">2017-01-02 03:04:05+09:00</td>
        </tr>
        <tr>
            <td align="right">3</td>
            <td align="right">3.33</td>
            <td align="left">cccc</td>
            <td align="right">-3.0</td>
            <td align="left">ccc</td>
            <td align="left">True</td>
            <td align="left">Infinity</td>
            <td align="left">NaN</td>
            <td align="left">NaN</td>
            <td align="left">2017-01-01 00:00:00</td>
        </tr>
    </tbody>
</table>
""",
    ),
]

table_writer_class = pytablewriter.HtmlTableWriter


class Test_HtmlTableWriter_write_new_line(object):
    def test_normal(self, capsys):
        writer = table_writer_class()
        writer.write_null_line()

        out, _err = capsys.readouterr()
        assert out == "\n"


class Test_HtmlTableWriter_write_table(object):
    @pytest.mark.parametrize(
        ["table", "indent", "header", "value", "expected"],
        [
            [data.table, data.indent, data.header, data.value, data.expected]
            for data in normal_test_data_list
        ],
    )
    def test_normal(self, capsys, table, indent, header, value, expected):
        writer = table_writer_class()
        writer.table_name = table
        writer.indent_string = indent
        writer.header_list = header
        writer.value_matrix = value
        writer.write_table()

        out, err = capsys.readouterr()
        print_test_result(expected=expected, actual=out, error=err)

        assert out == expected

    @pytest.mark.parametrize(
        ["table", "indent", "header", "value", "expected"],
        [
            [data.table, data.indent, data.header, data.value, data.expected]
            for data in null_test_data_list
        ],
    )
    def test_exception(self, table, indent, header, value, expected):
        writer = table_writer_class()
        writer.table_name = table
        writer.indent_string = indent
        writer.header_list = header
        writer.value_matrix = value

        with pytest.raises(expected):
            writer.write_table()


class Test_HtmlTableWriter_write_table_iter(object):
    def test_exception(self):
        writer = table_writer_class()

        with pytest.raises(pytablewriter.NotSupportedError):
            writer.write_table_iter()
