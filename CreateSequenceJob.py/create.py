
import os
import configparser as cfg
import regex


conf_file = 'config.ini'
conf = cfg.ConfigParser()
conf.read(conf_file)
ds_parameters = conf['ds']
file_path = conf['filepath']


def read_facet():
    with open(file=file_path['facet'], mode='r') as facet:
        top_level = regex.compile(r'^   END DSRECORD$')
        record = []
        records = []
        for line in facet.readlines():
            record.append(line)
            if top_level.match(line):
                records.append(record)
                record = []
    return records


def rep_list(lst, pattern, rep_str):
    for line in lst:
        if pattern.search(line):
            print(line)
    pass


def generate():
    job_stage = open(file='facets/job_stage.txt', mode='r').read()
    fail01 = open(file='facets/fail_link_01.txt', mode='r').read()
    fail02 = open(file='facets/fail_link_02.txt', mode='r').read()
    notification = open(file='facets/notification_stage.txt', mode='r').read()
    terminator01 = open(file='facets/terminator_link_01.txt', mode='r').read()
    terminator02 = open(file='facets/terminator_link_02.txt', mode='r').read()
    terminator = open(file='facets/terminator_stage.txt', mode='r').read()
    header = open(file='facets/header.txt', mode='r').read()
    tail = open(file='facets/tail.txt', mode='r').read()
    dependency = open(file='facets/dependencies.txt', mode='r').read()
    job = open(file='job.dsx', mode='w')
    jobs = []
    header_stages = ''
    dependency_jobs = ''
    job.write('')

    with open(file='jobs.txt', mode='r') as job_names:
        for index, name in enumerate(job_names.readlines()):
            # header
            if index == 0:
                header_stages += name.rstrip('\n')
            else:
                header_stages += '|' + name.rstrip('\n')
            dependency_reg = regex.compile(r'{.+}')
            dependency_str = dependency_reg.sub(repl=name.rstrip('\n'), string=dependency)
            dependency_jobs += dependency_str + '\n'
            # job stage
            job_stage_str = job_stage
            j_name = regex.compile(r'(?<=\n      Name ").+(?=")')
            job_name = regex.compile(r'(?<=      Jobname ").+(?=")')
            job_stage_content = j_name.sub(repl=name.rstrip('\n'), string=job_stage_str)
            job_stage_content = job_name.sub(repl=str(name).rstrip('\n'), string=job_stage_content)

            # notification stage
            notification_stage = notification
            notification_name = regex.compile(r'1{.+}')
            notification_subject = regex.compile(r'2{.+}')
            notification_content = notification_name.sub(repl='Notification_' + name.rstrip('\n'),
                                                         string=notification_stage)
            notification_content = notification_subject.sub(repl=name.rstrip('\n'), string=notification_content)

            # terminator stage
            terminator_stage = terminator
            terminator_name = regex.compile(r'{.+}')
            terminator_content = terminator_name.sub(repl='Terminator_' + name.rstrip('\n'),
                                                     string=terminator_stage)

            # now put them together
            one_job = job_stage_content + fail01 + notification_content + fail02 + terminator01 + terminator_content \
                      + terminator02
            # appnend to job dsx file
            jobs.append(one_job)
        header_stage_reg = regex.compile(r'{.+}')
        dependencies_reg = regex.compile(r'#dependency#')
        header = dependencies_reg.sub(repl=dependency_jobs, string=header)
        header = header_stage_reg.sub(repl=header_stages, string=header)
        job.write(header)
        for job_content in jobs:
            job.write(job_content)
        job.write(tail)


def get_m(obj):
    rtn = ''
    cnt = 0
    for m in dir(obj):
        if cnt <= 5:
            rtn += str(m) + ', '
        else:
            cnt = 0
            rtn += '\n' + str(m)
        cnt += 1
    print(rtn)


def execute(command=''):
    rs = os.popen(cmd=command, mode='r')
    return rs


def get_job_names(project_name='WWPRT_Dev', reg=''):
    cmd = 'dsjob -domain {0} -user {1} -password {2} -server {3}  -ljobs {4}'
    cmd = cmd.format(ds_parameters['domain'], ds_parameters['user'], ds_parameters['passwd'],
                             ds_parameters['host'], project_name)
    job_names = execute(command=cmd)
    pattern = regex.compile(reg)
    jobs_file = open(name=file_path['jobfile'], mode='w')
    for job in job_names.readlines():
        if pattern.match(job) is not None:
            jobs_file.write(job)


#generate()
for i in range(49):
    print('CJobActivity')
