# coding=utf-8

import requests
from lxml import html

url = 'https://www.cs.mcgill.ca/academic/courses'
r = requests.get(url).content
sel = html.fromstring(r)

# totally 115 courses
# list of course_full＿name
course_full＿name=sel.xpath('//div[@id="courses"]/a[@class="list-group-item"]/text()[1]')
# print (len(course_full＿name));
# print(course_full＿name)
# print(len(course_full＿name))

# list of course id
course_id = sel.xpath('//div[@id="courses"]/a[@class="list-group-item"]/@id')
# print(course_id)
# print(len(course_id))


def get_course_des(course_id):
    global course_des
    course_des = sel.xpath('//div[@id="collapse-' + str(course_id) + '"]/p/text()')
    return course_des

# print (get_course_des(102))


def get_credits(course_id):
    global credits
    credits = sel.xpath('//div[@id="collapse-' + str(course_id) + '"]/div[@class="list-group-item"]/p[1]/text()[2]')
    return credits


# credits in number
# test
# credits=sel.xpath('//div[@id="collapse-102"]/div[@class="list-group-item"]/p[1]/text()[2]')

# print(get_credits(102))


def get_terms_offered(course_id):
    global terms_offered
    terms_offered = sel.xpath(
        '//div[@id="collapse-' + str(course_id) + '"]/div[@class="list-group-item"]/p[2]/text()[2]')
    return terms_offered

# print(get_terms_offered(102))


def get_instructor(course_id):
    global instructor
    instructor = sel.xpath('//div[@id="collapse-' + str(course_id) + '"]/div[@class="list-group-item"]/p[3]/text()[2]')
    return instructor

# print (get_instructor(102))


def get_prerequisites(course_id):
    global prerequisites
    prerequisites = sel.xpath(
        '//div[@id="collapse-' + str(course_id) + '"]/div[@class="list-group-item"]/p[4]/text()[2]')
    return prerequisites
# print(get_prerequisites(102))

# ----------------------------------
for i in range(0,len(course_full＿name)):
    print(course_full＿name[i], course_id[i], get_course_des(course_id[i]), get_credits(course_id[i]), get_instructor(course_id[i]), get_terms_offered(course_id[i]))





# write into file
with open("/home/ning/Documents/mcgill_course_python/output","w") as f:
    for i in range(0, len(course_full＿name)):
        f.write(course_full＿name[i])
        f.write(course_id[i])
        f.write(get_course_des(course_id[i])[0])
        f.write(get_credits(course_id[i])[0])
        f.write(get_instructor(course_id[i])[0])
        f.write(get_terms_offered(course_id[i])[0])






