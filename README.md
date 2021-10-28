## This is utility function for the AWS Secrets Manager functions used across collinson
To install the packages run the following syntax <br>
<b>pip install git+https://github.com/{ Company repo name }/{ reponame }.git@{ tag name }#egg={ project }</b><br>
e.g pip install `git+https://github.com/iclp-ds/tcg_package.git@v1.0.4#egg=tcgsecret`<br>

## Usage 
import module<br>
`from tcgsecrets.tcg_secret import tcg_secret`<br>
initialize the secret class<br>
`secrets = tcg_secret()`

## Dependency

## TODO
1. Create the delete utility