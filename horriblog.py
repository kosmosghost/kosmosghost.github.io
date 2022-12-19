#!/bin/python3
import os
import subprocess

mdBlogPath = '_md'
filelist = os.listdir(mdBlogPath)


def parse_blog_filename_string(filename):
    filename_split = filename.split(".md")
    filename_split = filename_split[0]
    filename_split = filename_split.split("-")
    blog_year = filename_split[0]
    blog_month = filename_split[1]
    blog_day = filename_split[2]
    blog_title = ""
    for i in range(3, len(filename_split)):
        blog_title += filename_split[i]
        blog_title += " "
    return(blog_year, blog_month, blog_day, blog_title)


def blog_md_to_html(filename):
    filename = filename.split(".md")
    filename = filename[0]
    pandoc = "pandoc -s --template _template/dark-template.html -o blog/"
    pandoc += filename
    pandoc += ".html _md/"
    pandoc += filename
    pandoc += ".md"
    subprocess.Popen(pandoc, shell=True)

def md_index_to_html():
    pandoc = "pandoc -s --template _template/dark-template.html -o index.html md_index.md"
    subprocess.Popen(pandoc, shell=True)

def create_homepage():
    sorted_list = sort_blogs_by_date(filelist)
    create_md_index(sorted_list)
    for i in range(len(sorted_list)):
        blog_md_to_html(sorted_list[i])
    md_index_to_html()


def create_md_index(sorted_list):
    blogs_md_list = "---\ntitle: kosmosghost blog\n---\n  \n"
    for i in range(len(sorted_list)):
        filename = parse_blog_filename_string(sorted_list[i])
        blogs_md_list += create_html_link(sorted_list[i], filename[3])
        blogs_md_list += "\n\nPosted: "
        blogs_md_list += filename[0]
        blogs_md_list += "-"
        blogs_md_list += filename[1]
        blogs_md_list += "-"
        blogs_md_list += filename[2]
        blogs_md_list += "\n  \n  \n"
        write_to_index_md(blogs_md_list)

def create_html_link(filename, blog_title):
    md_link = "## ["
    md_link += blog_title
    md_link += "]"
    md_link += "("
    md_link += "blog/"
    html_link = filename.split(".md")
    md_link += html_link[0]
    md_link += ".html)"
    return md_link

def write_to_index_md(md_list):
    file = open("md_index.md", "w")
    file.write(md_list)

def sort_blogs_by_date(filelist):
    sorted_list = sort_by_year(filelist)
    sorted_list = sort_by_month(sorted_list)
    sorted_list = sort_by_day(sorted_list)
    return sorted_list

def sort_by_year(filelist):
    sorted_list = filelist
    continue_loop = False

    while True:
        for i in range(len(filelist)-1):
            buffer_a = parse_blog_filename_string(sorted_list[i])
            buffer_b = parse_blog_filename_string(sorted_list[i + 1])
            sort_buffer_a = sorted_list[i]
            sort_buffer_b = sorted_list[i+1]
            if buffer_a[0] < buffer_b[0]:
                sorted_list[i] = sort_buffer_b
                sorted_list[i+1] = sort_buffer_a
                continue_loop = True
            elif buffer_a[0] >= buffer_b[0]:
                if continue_loop == True:
                    continue_loop = True
                else:
                    continue_loop == False
        if continue_loop == False:
            break
        continue_loop = False

    return sorted_list


def sort_by_month(filelist):
    sorted_list = filelist
    continue_loop = False

    while True:
        for i in range(len(filelist)-1):

            buffer_a = parse_blog_filename_string(sorted_list[i])
            buffer_b = parse_blog_filename_string(sorted_list[i + 1])
            sort_buffer_a = sorted_list[i]
            sort_buffer_b = sorted_list[i+1]

            if buffer_a[0] == buffer_b[0]:
                if buffer_a[1] < buffer_b[1]:
                    sorted_list[i] = sort_buffer_b
                    sorted_list[i+1] = sort_buffer_a
                    continue_loop = True
                elif buffer_a[1] >= buffer_b[1]:
                    if continue_loop == True:
                        continue_loop = True
                    else:
                        if continue_loop != True:
                            continue_loop == False

        if continue_loop == False:
            break
        
        continue_loop = False
    return sorted_list


def sort_by_day(filelist):
    sorted_list = filelist
    continue_loop = False

    while True:
        for i in range(len(filelist)-1):

            buffer_a = parse_blog_filename_string(sorted_list[i])
            buffer_b = parse_blog_filename_string(sorted_list[i + 1])
            sort_buffer_a = sorted_list[i]
            sort_buffer_b = sorted_list[i+1]

            if buffer_a[0] == buffer_b[0]:
                if buffer_a[1] == buffer_b[1]:
                    buffer_a = parse_blog_filename_string(sorted_list[i])
                    buffer_b = parse_blog_filename_string(sorted_list[i + 1])
                    sort_buffer_a = sorted_list[i]
                    sort_buffer_b = sorted_list[i+1]
                    if buffer_a[2] < buffer_b[2]:
                        sorted_list[i] = sort_buffer_b
                        sorted_list[i+1] = sort_buffer_a
                        continue_loop = True
                    elif buffer_a[2] >= buffer_b[2]:
                        if continue_loop == True:
                            continue_loop = True
                        else:
                            continue_loop == False

        if continue_loop == False:
            break
        continue_loop = False

    return sorted_list

create_homepage()