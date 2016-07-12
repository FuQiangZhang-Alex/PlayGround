
from DSTool import *
import os

host_info = conf['host']
dir_info = conf['dir']
cmd_path = conf['sys']['command_path']
jobs_dir = dir_info['jobs_dir']
# os.chdir(jobs_dir)


def export(job_list_file=None):
    cnt = int(conf['dir']['exported'])
    jl = open(file=jobs_list_file, mode='r').readlines()
    to_process = jl[cnt:]
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
export(jobs_list_file)


def import_(jobs_dir):
    job_names = os.listdir(jobs_dir)
    print(job_names)
