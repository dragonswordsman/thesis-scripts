#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import shutil
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

"""
Util for generating cpu model folders with different parameters.
"""

template_folder = Path('./templates/')
init_template = template_folder / '__init__.py'
out_folder = Path('./models/')
out_list = Path('./configs.txt')
out_extra_list = Path('./configs_extra.txt') 

env = Environment(loader=FileSystemLoader(str(template_folder)))

cpus = ['A76', 'HP']
template_files = {'A76':'A76.py.jinja', 'HP':'HP.py.jinja'}
simdFU = {'A76':[1, 2], 'HP':[1, 2, 3]}
penalty = [0, 1]
fuseCap = [0, 3]

extra = True
try_param = ['HP']
extra_param = ['dispatch', 'queues', 'regfile']
scale = [0.75, 1.25]

out_folder.mkdir(parents=True, exist_ok=True)
with open(str(out_folder / '__init__.py'), 'w') as f:
    f.write('')

folder_list = []
extra_list = []
for cpu in cpus:
    template = env.get_template(template_files[cpu])

    # Generate empty init.
    path = out_folder / cpu
    path.mkdir(parents=True, exist_ok=True)
    with open(str(path / '__init__.py'), 'w') as f:
        f.write('')

    for fu in simdFU[cpu]:
        for pen in penalty:
            for cap in fuseCap:
                parsed = template.render(simdFU=fu, penalty=pen, fuseCap=cap, extra={})

                # Create cpu model.
                folder_name = '{0}/{0}_{1}fu_{2}pen_{3}cap'.format(cpu, fu, pen, cap)
                path = out_folder / folder_name
                path.mkdir(parents=True, exist_ok=True)
                with open(str(path / 'O3_ARM_v7a.py'), 'w') as f:
                    f.write(parsed)

                # Copy __init__.py.
                init = path / '__init__.py'
                shutil.copy(init_template, init)

                # Add path to list.
                folder_list.append(folder_name.replace('/', '.'))

                # Test more parameters.
                if extra and (cpu in try_param):
                    for param in extra_param:
                        for s in scale:
                            parsed = template.render(simdFU=fu, penalty=pen, fuseCap=cap, extra={param:s})

                            # Create cpu model.
                            folder_name = '{0}/{0}_{1}fu_{2}pen_{3}cap_{4}{5}'.format(cpu, fu, pen, cap,
                                                                                      str(s).replace('.', '_'),
                                                                                      param)
                            path = out_folder / folder_name
                            path.mkdir(parents=True, exist_ok=True)
                            with open(str(path / 'O3_ARM_v7a.py'), 'w') as f:
                                f.write(parsed)

                            # Copy __init__.py.
                            init = path / '__init__.py'
                            shutil.copy(init_template, init)

                            # Add path to list.
                            extra_list.append(folder_name.replace('/', '.'))

# Print modules list.
with open(str(out_list), 'w') as f:
    f.write('\n'.join(folder_list))

if extra:
    with open(str(out_extra_list), 'w') as f:
        f.write('\n'.join(extra_list))
