# python 验证码生成

## 参数

* 输入

| 名称 | 类型 | 说明 | 
| - | :-: | -: | 
| number | int| 生成验证码的字符串长度 | 
| line_num | int | 干扰线条数 | 
| character | int | 生成验证码用到的字符集1:数字 2:字母 else:数字&字母 |

实例
`python create.py 5 2 3`

* 5个字符,2条干扰线组成的验证码,由字母和数字组成

* 输出

| 名称 | 类型 | 说明 | 
| - | :-: | -: | 
| 图片 | png| 生成的验证码图片 | 
| text| string | 验证码的字符串 | 

## 方法

| 名称 | 类型 | 功能 | 
| - | :-: | -: | 
| `__init__` | 构造函数| 接受命令行传来的三个参数`number`,`line_num`,`character`,并生成验证码字符串 | 
| gene_text | 成员函数 | 根据参数`character`指定的字符集生成验证码字符串 | 
| rnd_dis | 成员函数 | 添加干扰字符到验证码图片 |
| gene_line | 成员函数 | 根据参数`line_num`,添加指定条数的干扰线到验证码图片 |
| gene_code | 成员函数 | 调用其它成员函数,绘制图片 |
| get_text | 成员函数 | 输出验证码字符串`text` |


由AuthCode类实例化验证码对象,从命令行接收三个参数,调用gene_code()方法生成验证码图片,调用get_text()给出验证码字符串

## 样例

`>python create.py 5 2 3`

`>A6O0J`

![验证码图片](A6O0J.png)
