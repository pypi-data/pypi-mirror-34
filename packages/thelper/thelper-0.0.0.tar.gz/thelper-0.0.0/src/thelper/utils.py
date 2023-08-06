import glob
import importlib
import inspect
import logging
import math
import os
import re
import sys

import matplotlib.pyplot as plt
import numpy as np

utils_logger = logging.getLogger("thelper.utils")


def import_class(fullname):
    modulename,classname = fullname.rsplit('.',1)
    module = importlib.import_module(modulename)
    return getattr(module,classname)


def get_logger(skip=0):
    """Shorthand to get logger for current function frame."""
    return logging.getLogger(get_caller_name(skip+1))


def get_caller_name(skip=2):
    # source: https://gist.github.com/techtonik/2151727
    """Get a name of a caller in the format module.class.method

       `skip` specifies how many levels of stack to skip while getting caller
       name. skip=1 means "who calls me", skip=2 "who calls my caller" etc.

       An empty string is returned if skipped levels exceed stack height
    """

    def stack_(frame):
        framelist = []
        while frame:
            framelist.append(frame)
            frame = frame.f_back
        return framelist

    stack = stack_(sys._getframe(1))
    start = 0+skip
    if len(stack)<start+1:
        return ''
    parentframe = stack[start]
    name = []
    module = inspect.getmodule(parentframe)
    # `modname` can be None when frame is executed directly in console
    # TODO(techtonik): consider using __main__
    if module:
        name.append(module.__name__)
    # detect classname
    if 'self' in parentframe.f_locals:
        # I don't know any way to detect call from the object method
        # XXX: there seems to be no way to detect static method call - it will
        #      be just a function call
        name.append(parentframe.f_locals['self'].__class__.__name__)
    codename = parentframe.f_code.co_name
    if codename!='<module>':  # top level usually
        name.append(codename)  # function or a method
    del parentframe
    return ".".join(name)


def str2bool(s):
    if isinstance(s,bool):
        return s
    if isinstance(s,(int,float)):
        return s!=0
    if isinstance(s,str):
        positive_flags = ["true","1","yes"]
        return s.lower() in positive_flags
    raise AssertionError("unrecognized input type")


def lreplace(string,old_prefix,new_prefix):
    return re.sub(r'^(?:%s)+'%re.escape(old_prefix),lambda m:new_prefix*(m.end()//len(old_prefix)),string)


def keyvals2dict(keyvals):
    if not isinstance(keyvals,list):
        raise AssertionError("expected key-value pair vector")
    out = {}
    for idx in range(len(keyvals)):
        item = keyvals[idx]
        if not isinstance(item,dict):
            raise AssertionError("expected items to be dicts")
        elif "name" not in item or "value" not in item:
            raise AssertionError("expected 'name' and 'value' fields in each item")
        out[item["name"]] = item["value"]
    return out


def draw_histogram(data,bins=50,xlabel="",ylabel="Proportion"):
    fig,ax = plt.subplots()
    ax.hist(data,density=True,bins=bins)
    if len(ylabel)>0:
        ax.set_ylabel(ylabel)
    if len(xlabel)>0:
        ax.set_xlabel(xlabel)
    ax.set_xlim(xmin=0)
    fig.show()


def draw_popbars(labels,counts,xlabel="",ylabel="Pop. Count"):
    fig,ax = plt.subplots()
    xrange = range(len(labels))
    ax.bar(xrange,counts,align="center")
    if len(ylabel)>0:
        ax.set_ylabel(ylabel)
    if len(xlabel)>0:
        ax.set_xlabel(xlabel)
    ax.set_xticks(xrange)
    ax.set_xticklabels(labels)
    ax.tick_params(axis="x",labelsize="8",labelrotation=45)
    fig.show()


def draw_classifs(images,labels_gt,labels_pred=None,labels_map=None):
    nb_imgs = len(images) if isinstance(images,list) else images.shape[images.ndim-1]
    if nb_imgs<1:
        return
    grid_size_x = int(math.ceil(math.sqrt(nb_imgs)))
    grid_size_y = int(math.ceil(nb_imgs/grid_size_x))
    if grid_size_x*grid_size_y<nb_imgs:
        raise AssertionError("bad gridding for subplots")
    fig,axes = plt.subplots(grid_size_y,grid_size_x)
    plt.tight_layout()
    if nb_imgs==1:
        axes = np.array(axes)
    for ax_idx,ax in enumerate(axes.reshape(-1)):
        if isinstance(images,list):
            ax.imshow(images[ax_idx],interpolation='nearest')
        else:
            ax.imshow(images[ax_idx,...],interpolation='nearest')
        curr_label_gt = labels_map[labels_gt[ax_idx]] if labels_map else labels_gt[ax_idx]
        if labels_pred:
            curr_label_pred = labels_map[labels_pred[ax_idx]] if labels_map else labels_pred[ax_idx]
            xlabel = "GT={0}\nPred={1}".format(curr_label_gt,curr_label_pred)
        else:
            xlabel = "GT={0}".format(curr_label_gt)
        ax.set_xlabel(xlabel)
        ax.set_xticks([])
        ax.set_yticks([])
    fig.show()


def draw_errbars(labels,min,max,stddev,mean,xlabel="",ylabel="Raw Value"):
    if min.shape!=max.shape or min.shape!=stddev.shape or min.shape!=mean.shape:
        raise AssertionError("input dim mismatch")
    if len(min.shape)!=1 and len(min.shape)!=2:
        raise AssertionError("input dim unexpected")
    if len(min.shape)==1:
        np.expand_dims(min,1)
        np.expand_dims(max,1)
        np.expand_dims(stddev,1)
        np.expand_dims(mean,1)
    nb_subplots = min.shape[1]
    fig,axs = plt.subplots(nb_subplots)
    xrange = range(len(labels))
    for ax_idx in range(nb_subplots):
        ax = axs[ax_idx]
        ax.locator_params(nbins=nb_subplots)
        ax.errorbar(xrange,mean[:,ax_idx],stddev[:,ax_idx],fmt='ok',lw=3)
        ax.errorbar(xrange,mean[:,ax_idx],[mean[:,ax_idx]-min[:,ax_idx],max[:,ax_idx]-mean[:,ax_idx]],fmt='.k',ecolor='gray',lw=1)
        ax.set_xticks(xrange)
        ax.set_xticklabels(labels,visible=(ax_idx==nb_subplots-1))
        ax.set_title("Band %d"%(ax_idx+1))
        ax.tick_params(axis="x",labelsize="6",labelrotation=45)
    plt.tight_layout()
    fig.show()


def get_glob_paths(input_glob_pattern,can_be_dir=False):
    glob_file_paths = glob.glob(input_glob_pattern)
    if not glob_file_paths:
        raise AssertionError("invalid input glob pattern '%s'"%input_glob_pattern)
    for file_path in glob_file_paths:
        if not os.path.isfile(file_path) and not (can_be_dir and os.path.isdir(file_path)):
            raise AssertionError("invalid input file at globbed path '%s'"%file_path)
    return glob_file_paths


def get_dataset_file_paths(input_path,dataset_root,allow_glob=False,can_be_dir=False):
    if os.path.isabs(input_path):
        if '*' in input_path and allow_glob:
            return get_glob_paths(input_path)
        elif not os.path.isfile(input_path) and not (can_be_dir and os.path.isdir(input_path)):
            raise AssertionError("invalid input file at absolute path '%s'"%input_path)
    else:
        if not os.path.isdir(dataset_root):
            raise AssertionError("invalid dataset root directory at '%s'"%dataset_root)
        input_path = os.path.join(dataset_root,input_path)
        if '*' in input_path and allow_glob:
            return get_glob_paths(input_path)
        elif not os.path.isfile(input_path) and not (can_be_dir and os.path.isdir(input_path)):
            raise AssertionError("invalid input file at path '%s'"%input_path)
    return [input_path]
