#!/bin/sh

safe_append() {
    local new_path=$1
    local envvar=${2:-PATH}

    if ! command -v pathdiag > /dev/null ; then
        >&2 echo 'Command `pathdiag` not found'
        return 1
    fi

    if pathdiag --var $envvar --can-add $new_path 2> /dev/null ; then
        local command="export ${envvar}=\"\$$envvar:$new_path\""
        eval `echo $command`
    else
        pathdiag --var $envvar --can-add $new_path
    fi
}

safe_prepend() {
    local new_path=$1
    local envvar=${2:-PATH}

    if ! command -v pathdiag > /dev/null ; then
        >&2 echo 'Command `pathdiag` not found'
        return 1
    fi

    if pathdiag --var $envvar --can-add $new_path 2> /dev/null ; then
        local command="export ${envvar}=\"$new_path:\$$envvar\""
        eval `echo $command`
    else
        pathdiag --var $envvar --can-add $new_path
    fi
}
