import yaml,json, jmespath
from nose.tools import assert_in
from ApiTest.loader import *
from debugtalk import *
from ApiTest import exceptions, loader, validator, api




f=open('udisk.yaml','r',encoding='utf-8')
data=yaml.load(f, Loader=yaml.FullLoader)
# print(type(data),data) #<class 'list'>
f.close()
for i in data:
    # print(i)
    # print(type(i))
    # print(jmespath.search('test.request.url',i))
    # print(jmespath.search('test.validators', i))
    # print(type(jmespath.search('test.validators', i)))
    variables = jmespath.search('test.validators', i)
    # print(type(variables),variables)
    #输出：
    # [{'check': 'status_code', 'expeted': 300}, 'assert_equal("status_code", 300)']
    # [{'check': 'status_code', 'expeted': 300}, {'check': 'content.errorMessage', 'comparator': 'eq', 'expected': ''}, {'check': 'content.data', 'comparator': 'ne', 'expected': ''}]
    #<class 'list'>
    # '''
    variables_dict = {}
    if variables is not None:

        for map_dict in variables:
            # print(map_dict)
            variables_dict.update(map_dict)
    # print(variables_dict)
    # print(type(variables_dict))
    # '''


#loder.py test
from ApiTest.loader import *
from debugtalk import *
# result = load_yaml_file(r'C:\Users\lilingyun01\Desktop\test_yaml\yaml_practice\udisk.yaml')
# print(result)
# print(load_file(r'C:\Users\lilingyun01\Desktop\test_yaml\yaml_practice\udisk.yaml'))
# print('load_dot_env_file()',load_dot_env_file(r'C:\Users\lilingyun01\Desktop\test_yaml\yaml_practice\.env')) #返回.enc文件中数据，字典形式
#>>>load_dot_env_file() {'run_env': 'PRODUCT', 'UserName': 'debugtalk', 'Password': '123456', 'PROJECT_KEY': 'ABCDEFGH'}

# print('locate_file()',locate_file(r'C:\Users\lilingyun01\Desktop\test_yaml\yaml_practice\udisk.yaml','debugtalk.py')) #找到对应用例文件夹的debugtalk.py文件，返回文件全路径
#>>>locate_file() C:\Users\lilingyun01\Desktop\test_yaml\yaml_practice\debugtalk.py
# print('locate_file2()',locate_file(r'C:\Users\lilingyun01\Desktop\test_yaml\yaml_practice\ApiTest\debugtalk.yaml','debugtalk.py')) #找到对应用例文件夹的debugtalk.py文件，返回文件全路径
#>>>locate_file2() C:\Users\lilingyun01\Desktop\test_yaml\yaml_practice\debugtalk.py

# print(load_module_functions(get_default_request())) #一直测试不成功


# module_functions = load_module_functions(loader) #可以检擦某个函数是否在某个文件中
# assert_in("load_module_functions1", module_functions)
#>>AssertionError: 'load_module_functions1' not found in {'_check_format': <function _check_format at 0x000001E9628A4D90>, 'load_yaml_file': <function load_yaml_file at 0x000001E9633E4BF8>, 'load_json_file': <function load_json_file at 0x000001E9633E4C80>}

# assertNotIn("is_py3", module_functions)
# print(load_builtin_functions())
# print(load_debugtalk_functions())
# resp = loader.load_tests(r'C:\Users\lilingyun01\Desktop\test_yaml\yaml_practice\udisk.yaml')
# print(type(resp),resp) #type:dict
#>>>{'project_mapping': {'env': {'run_env': 'PRODUCT', 'UserName': 'debugtalk', 'Password': '123456', 'PROJECT_KEY': 'ABCDEFGH'}, 'PWD': 'C:\\Users\\lilingyun01\\Desktop\\test_yaml\\yaml_practice', 'functions': {'get_base_url': <function get_base_url at 0x000001ABDCEA1268>, 'get_default_request': <function get_default_request at 0x000001ABDCEA12F0>, 'sum_two': <function sum_two at 0x000001ABDCEA1378>, 'sum_status_code': <function sum_status_code at 0x000001ABDCEA1400>, 'is_status_code_200': <function is_status_code_200 at 0x000001ABDCEA1488>, 'skip_test_in_production_env': <function skip_test_in_production_env at 0x000001ABDCEA1510>, 'get_user_agent': <function get_user_agent at 0x000001ABDCEA1598>, 'gen_app_version': <function gen_app_version at 0x000001ABDCEA1620>, 'get_account': <function get_account at 0x000001ABDCEA16A8>, 'get_account_in_tuple': <function get_account_in_tuple at 0x000001ABDCEA1730>, 'gen_random_string': <function gen_random_string at 0x000001ABDCEA17B8>, 'setup_hook_add_kwargs': <function setup_hook_add_kwargs at 0x000001ABDCEA1840>, 'setup_hook_remove_kwargs': <function setup_hook_remove_kwargs at 0x000001ABDCEA18C8>, 'teardown_hook_sleep_N_secs': <function teardown_hook_sleep_N_secs at 0x000001ABDCEA1950>, 'hook_print': <function hook_print at 0x000001ABDCEA19D8>, 'modify_headers_os_platform': <function modify_headers_os_platform at 0x000001ABDCEA1A60>, 'alter_response': <function alter_response at 0x000001ABDCEA1AE8>}}, 'testcases': [{'config': {'url': 'http://10.95.34.13:80/api/upload_client_conf.json?mid=517b9255227858c7810af8e6b3824286&ver=1.0', 'name': '这是测试1', 'num': {'num_1': '${random.int(10,100)}'}, 'headers': {'Accept': 'application/json, text/javascript, */*; q=0.01', 'X-Requested-With': 'XMLHttpRequest', 'Accept-Encoding': 'gzip, deflate, sdch', 'Accept-Language': 'zh-CN,zh;q=0.8'}}, 'teststeps': [{'name': 'U盘注册申请', 'request': {'url': 'http://10.95.34.13:80/api/upload_client_conf.json?mid=517b9255227858c7810af8e6b3824286&ver=1.0', 'method': 'GET', 'headers': '<<*conf_headers', 'variables': {'code': 0, 'type': 'usb', 'usb_disk_reg': {'device_id': '1dddddddddxxxxx41813234567890', 'datetime': '1625129463', 'name': 'yamlU盘测试', 'type': 1, 'reg_type': 1, 'capacity': 29510, 'vendor_id': 'Kingston', 'pid': '1666', 'vid': '0951', 'partition_system': 'vfat', 'username': '10', 'tel': '10', 'memo': '10', 'tag_id': 1, 'safe_check_status': 1}}}, 'validators': [{'check': 'status_code', 'expeted': 300}, {'check': 'content.errorMessage', 'comparator': 'eq', 'expected': ''}, {'check': 'content.data', 'comparator': 'ne', 'expected': ''}]}, {'name': 'U盘注册申请2', 'request': {'url': 'https://segmentfault.com/gateway/question/1010000009727312/related', 'method': 'GET', 'headers': '<<*conf_headers', 'variables': {'code': 0, 'type': 'usb', 'usb_disk_reg': {'device_id': '2dddddddddxxxxx41813234567890', 'datetime': '1625129463', 'name': 'yamlU盘测试2', 'type': 1, 'reg_type': 1, 'capacity': 29510, 'vendor_id': 'Kingston', 'pid': '1666', 'vid': '0951', 'partition_system': 'vfat', 'username': '10', 'tel': '10', 'memo': '10', 'tag_id': 1, 'safe_check_status': 1}}}, 'validators': [{'eq': ['status_code', 201]}, {'sum_status_code': ['status_code', 3]}, {'eq': ['$success', True]}, {'eq': ['abc$success', 'abcTrue']}, {'check': 'status_code', 'comparator': 'eq', 'expect': 201}, {'check': 'content.success', 'comparator': 'eq', 'expect': True}]}], 'path': 'C:\\Users\\lilingyun01\\Desktop\\test_yaml\\yaml_practice\\udisk.yaml', 'type': 'testcase'}]}

api.HttpRunner().run(path_or_tests=r'C:\Users\lilingyun01\Desktop\test_yaml\yaml_practice\case\AK_udisk\udisk2.yml')