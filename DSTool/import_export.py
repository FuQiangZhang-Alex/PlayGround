
from DSTool import *
import regex
import os

host_info = conf['host']
dir_info = conf['dir']
cmd_path = conf['sys']['command_path']
jobs_dir = dir_info['jobs_dir']


def export(job_list_file=None, begin_line=0, end_line=None):
    cnt = int(conf['dir']['exported'])
    jl = open(file=jobs_list_file, mode='r').readlines()
    to_process = None
    if end_line is not None:
        if cnt > begin_line:
            to_process = jl[cnt:]
        else:
            to_process = jl[begin_line:]
    else:
        if end_line > begin_line:
            print('error')
            return None
        if cnt > begin_line & cnt < end_line:
            to_process = jl[cnt:end_line]
        else:
            to_process = jl[begin_line:end_line]
    print(len(to_process), to_process)
    for job_name in to_process:
        job_name = str(job_name).rstrip('\n')
        job_file_name = job_name + '.dsx'
        if os.access(path=jobs_dir, mode=os.R_OK):
            print('exporting ', cnt + 1, '\t:\t', job_name)
            cmd_str = cmd_path + 'dsexport /D=' + host_info['domain'] + ' /H=' + host_info['host'] + ' /U=' + host_info['user']\
                + ' /P=' + host_info['password'] + ' /JOB=' + job_name + ' /NODEPENDENTS ' + host_info['project'] \
                + ' ' + jobs_dir + '/' + job_file_name
            cmd_str += '\ndir'
            rs = os.popen(cmd=cmd_str, mode='r')
            print(rs.readlines())
            cnt += 1
            conf.set(section='dir', option='exported', value=str(cnt))
            conf.write(fp=open(file='RDF/conf.ini', mode='w'))
            print('exported: ', job_name, '\n')
        else:
            print('jobs dir is not readable')
            break


jobs_list_file = conf['dir']['job_list_file']
export(jobs_list_file, begin_line=25, end_line=62)


def import_(jobs_dir):
    job_names = os.listdir(jobs_dir)
    print(job_names)


def list_jobs(folder_name=''):
    cmd_str = '{0}dsjob -domain {1} -user {2} -password {3} -server {4} -ljobs {5}'\
        .format(cmd_path, host_info['domain'], host_info['user'],
                host_info['password'], host_info['host'], host_info['project'])
    jobs = os.popen(cmd=cmd_str, mode='r')
    for job_line in jobs.readlines():
        pattern = regex.compile('^A24T\d[A-Z]{3}$')
        if pattern.search(job_line):
            print(job_line.rstrip('\n'))

# list_jobs()
