# -*- coding: UTF-8 -*-
from string import Template
import json
import datetime
import time

def start_response(resp="text/html"):
    return('Content-type: ' + resp + '\n\n')

def include_header(the_title):
    with open('templates/header.html') as headf:
        head_text = headf.read()
    header = Template(head_text)
    return(header.substitute(title=the_title))

def include_footer(the_links):
    with open('templates/footer.html') as footf:
        foot_text = footf.read()
    link_string = ''
    for key in the_links:
        link_string += '<a href="' + the_links[key] + '">' + key + '</a>&nbsp;&nbsp;&nbsp;&nbsp;'
    footer = Template(foot_text)
    return(footer.substitute(links=link_string))

def start_form(the_url, form_type="POST"):
    return('<form action="' + the_url + '" method="' + form_type + '">')

def end_form(submit_msg="Submit"):
    return('<p></p><input type=submit value="' + submit_msg + '"></form>')

def radio_button(rb_name, rb_value):
    return('<input type="radio" name="' + rb_name +
                             '" value="' + rb_value + '"> ' + rb_value + '<br />')

def radio_button_id(rb_name, rb_value, rb_id):
	return ('<input type="radio" name="' + rb_name +
                             '" value="' + str(rb_id) + '"> ' + rb_value + '<br />')

def u_list(items):
    u_string = '<ul>'
    for item in items:
        u_string += '<li>' + item + '</li>'
    u_string += '</ul>'
    return(u_string)

def header(header_text, header_level=2):
    return('<h' + str(header_level) + '>' + header_text +
           '</h' + str(header_level) + '>')

def para(para_text):
    return('<p>' + para_text + '</p>') 

def create_inputs(inputs_list):
        html_inputs = ''
        for each_input in inputs_list:
                html_inputs += '<input type= "Text" name="' + each_input + '" size=10> &nbsp;&nbsp;'
        return(html_inputs)

def do_form(name, the_inputs, method="POST", text="Submit"):
        with open('templates/form.html') as formf:
                form_text = formf.read()
        inputs = create_inputs(the_inputs)
        form = Template(form_text)
        return(form.substitute(cgi_name=name, http_method=method, list_of_inputs=inputs, submit_text=text))








def get_all(name, x_time, inst_num):
        with open('data_j.json', encoding='utf-8') as formf:
                form_text = formf.read()
                #print(form_text)
        form = Template(form_text)
        return(form.substitute(val=name, xaixs=x_time, num=inst_num))


def get_ins_num():
    inst_num = []
    for i in range(7) :
        inst_num.append(10 + 10*i)
    # print(inst_num)
    # jn = json.dumps(inst_num)
    # print(type(jn))
    # print(type(inst_num))
    #
    #print(test("\"审计实例总量-0----------\"", inst_num))
    return inst_num

"""
dt = (datetime.datetime.now()+datetime.timedelta(minutes=-2)).strftime("%Y-%m-%d %H:%M:%S")
dt= (datetime.datetime.now()+datetime.timedelta(days=-1)).strftime("%m/%d")
print(dt)"""
def get_x_time():
    xAxis = []
    for i in range(7) :
        xAxis.append((datetime.datetime.now()+datetime.timedelta(days=-i)).strftime("%m/%d"))
    xAxis.reverse()
    print(xAxis)
    return xAxis

# data = get_all('"实例数量-"', get_x_time(), get_ins_num())
# fs = open("data.json", "w+", encoding='utf-8')
# fs.write(data)
# print(data)


def get_ctsdb_dealy_data():
    data_list = [["126.93.23.23", 2, 0], ["23.23.32.23", 1.2, 0]]
    return data_list

def get_zk_str():
    str_zk_inf = ""
    delay_list = [["---",0,0]]
    for item in delay_list:
     str_zk_inf += ('<tr>' +
                        '<td style="width:200px"> ' + item[0] + '</td>' +
                        '<td class="table_title">'+ str(item[1]) + '</td>' +
                        '<td>'  + str(item[2]) + '</td>' +
                ' </tr>')
    return str_zk_inf

def get_list_insert_dealy(data_list):
    str_list_insert_delay = ""
    for item in data_list:
        #print(data_list)
        str_list_insert_delay += ('<tr>' + 
                                        '<td style="width:200px"> "' + item[0] + '"</td>' + 
                                        '<td class="table_title">'+ str(item[1]) + '</td>' + 
                                        '<td>'  + str(item[2]) + '</td>' +
                                ' </tr>')
    return str_list_insert_delay


def get_main(str_list_insert_dealy,  str_zk_inf):
        with open('main_t.html', encoding='utf-8') as formf:
                form_text = formf.read()
                #print(form_text)
        form = Template(form_text)
        return(form.substitute(list_insert_dealy=str_list_insert_dealy, list_zk=str_zk_inf))

print(get_main(get_list_insert_dealy(get_ctsdb_dealy_data()), get_zk_str()))


print(12342351235/1000)