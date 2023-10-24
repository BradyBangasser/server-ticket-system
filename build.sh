#!/usr/bin/env sh

run='true'
debug='true'

printHelp() {
    echo "[subcommand]: build, init, clean"
    echo "-r: Builds Release Code"
    echo "-R: Builds Release Code and Runs it"
    echo "-h: prints this"
}

# cmd, label, newThread
ex() {
    if [ "$3" == "true" ]; then
        ( eval $1 | while read line ; do echo "$2: $line"; done & )
    else
        eval $1 | while read line ; do echo "$2: $line"; done
    fi
}

build() {
    while getopts 'rRh' flag; do
        case "${flag}" in 
            r) run='false' debug='false';;
            R) debug='false';;
        esac
    done

    python3 configer.py

    cd ./client

    if [ "$debug" == "true" ]; then 
        ex 'yarn dev' client true
        cd ../server
        ex 'go run .' server
    else
        ex "yarn build" client-build
        cd ../server
        ex "echo 'Server Build Start' ; go build . ; echo 'Server Build Complete'" server-build

        if [ "$run" == "true" ]; then
            ex ./server.exe server true
            cd ../client
            ex "yarn start" client
        fi
    fi
}

init() {
    cd server
    go get
    cd ../client
    yarn
    yarn install
    cd ..
}

clean() {
    cd server
    rm -f go.sum
    cd ../client
    rm -rf node_modules next-env.d.ts .next *.log.* .vercel build .yarn
}

case "$1" in 
    clean) clean ;;
    init) init ;;
    *) build ;;
esac