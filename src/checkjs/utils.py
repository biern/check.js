# -*- coding: utf-8 -*-

from collections import defaultdict


def to_dep_dict(file_data, analyzers, skip_prefixes=[]):
    result = defaultdict(set)
    undefined = set()

    # Maps defined components to filenames
    define_to_file = defaultdict(dict)

    # Creates component -> filename mapping
    for name in analyzers:
        for filename, data in file_data.items():
            for defined in data[name]['defines']:
                define_to_file[name][defined] = filename

    for name in analyzers:
        for filename, data in file_data.items():
            # Extend file's dependecies with files containing
            # components that it depends on, unless they start with disallowed
            # prefix
            result[filename]
            for d in data[name]['depends']:
                if any(d.startswith(p) for p in skip_prefixes):
                    continue

                try:
                    dep = define_to_file[name][d]
                except KeyError:
                    undefined.add(d)
                    continue

                if dep != filename:
                    result[filename].add(dep)

    return dict(result), undefined


def remove_prefix(files_deps, prefix):
    def cut(name):
        if name.startswith(prefix):
            name = name.replace(prefix, '', 1)

        return name

    res = {}
    for filename, deps in files_deps.items():
        filename = cut(filename)
        res[filename] = []
        for name in deps:
            name = cut(name)
            res[filename].append(name)

    return res
