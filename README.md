# Test Wiki


This repo is an example to show how to publicly host a private documentation.       
As you know, Github offers free public hostage via Github pages and private hostage via a subscription (Github Entreprise).     

This repo show how you can host a public repo and made it password encrypted, using Github secrets and actions worflow. The idea is
1. define a Github repository secret
2. make it available as an environment variable (see [ci.yml](.github/workflows/ci.yml))
3. use this environement variable within Python code to verify the password entered by a user on the Github pages. 


This is made using a tool based on [this implementation](https://github.com/coink0in/mkdocs-encryptcontent-plugin/) with the possibility to use an
environment variable added on my fork [here](https://github.com/ListIndexOutOfRange/mkdocs-encryptcontent-plugin) (a pool request has been submitted and is still pending at the time of this writing).



[Doc link](https://ListIndexOutOfRange.github.io/TestWiki/)


## Disclaimer

Note that a majority of the code in this repo has been copied from the excessively great [Equinox repo](https://github.com/patrick-kidger/equinox).


