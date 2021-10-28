## This is utility function for the AWS Secrets Manager functions used across collinson
To install the packages run the following syntax 
<b>pip install git+https://github.com/{ Company repo name }/{ reponame }.git@{ tag name }#egg={ project }</b>
e.g pip install `git+https://github.com/iclp-ds/tcg_package.git@v1.0.4#egg=tcgsecret`

## Usage 
import module
`from tcgsecrets.tcg_secret import tcg_secret`
initialize the secret class
`secrets = tcg_secret()`

## Dependency

## TODO
1. Create the delete utility