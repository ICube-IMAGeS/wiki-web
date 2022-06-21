# HPC

---
<div align='right' class="result" markdown>
*Luc Vedrenne, june 2022*
</div>



## Introduction

The University of Strasbourg is equiped with a HPC (High performance computing). This huge computing server allows for many simultaneous users to share available ressources and run jobs remotely. You can find their documentation (in french only because ???) [here](https://hpc.pages.unistra.fr/).

It is composed of 2,8 Po of storage, 14792 computing cores, 73 To of RAM, and 250 GPUs (details [here](https://hpc.pages.unistra.fr/equipment)).

In order to use it, you must first get an account. You can then submit jobs, which is a rather tedious task. Hopefully this guide will help you through. 

## I - Getting an account


### SSH key

First, you must have an ed25519 SSH key. You can create one by running

`$ ssh-keygen -t ed25519 -C "your_email@example.com"`

While it isn't mandatory, you should add your ssh key to the ssh-agent by running:

`$ eval "$(ssh-agent -s)"` <br>
`$ ssh-add ~/.ssh/id_ed25519`


### Making the account request 

You can then send an email to `support@unistra.fr` with `HPC account` as object containing the following informations:

- name
- surname
- professional email
- laboratory / team 
- research field
- PhD advisors coordinates
- end of thesis date
- ressources requested: this should be a number of CPU & GPU hours. This only acts as an indicator and hasn't to be really accurate.

Attach to the mail the **public** ed25519 ssh key (usually id_ed25519.pub). 

!!! tip

    Remember the email address. This is the one to contact for any troubles while using the HPC.





## II - Understanding how the HPC and SLURM work

### SLURM

Once you have an account, you can SSH into the login server. The core principle to have in mind while using the HPC is that **this account is not made to run anything, but only to submit jobs to be ran**. The HPC makes all available ressources shareable accross all users. This is done thanks to a tool called SLURM (Simple Linux Utility for Resource Management). So what you must do on the login server in only to create bash script(s) that will basically:

1. request ressources

2. request external modules (see bellow)

2. tell which job(s) to run, and how

3. tell some other minor informations, such as input/output paths 

This script(s) will be queued by SLURM and wait until the requested ressources are available. 


### Modules

In order to execute jobs, you'll often need external libraries. The available modules are listed [here](https://hpc.pages.unistra.fr/modules).
Those modules aren't usable by default and you must load them with the `module load [module name]` command. For instance, if you want to use conda to manage your python environment, you should run:

`$ module load python/Anaconda`


## III - Submit your first job

There are many ways to create and submit SLURM jobs. This guide focuses on one only, perhaps cleaner. 

Let's say we want to execute a file called `main.py` inside a conda environment. This file will execute code that relies on CUDA. We need to create a bash script that will:

1. request ressources

2. set up the necessary environment

3. launch the python code.

Check out the annotated example script:

??? example "Slurm job script"

    ```bash
    #! /bin/bash

    # +------------------------------------------------------------------------------------+ #
    # |                                  SLURM PARAMETERS                                  | #
    # +------------------------------------------------------------------------------------+ #
    # (1)

    #SBATCH -p publicgpu -A miv                         # Partition publicgpu et compte miv
    #SBATCH -N 1                                        # 1 node
    #SBATCH -n 1                                        # 1 task
    #SBATCH -c 1                                        # 1 CPU
    #SBATCH -o path/to/output.out                       # (2)
    #SBATCH --gres=gpu:1                                # 1 GPU
    #SBATCH --mem=16G                                   # 16 Go RAM
    #SBATCH --constraint="gpua100|gpurtx6000|gpurtx5000|gpuv100" # (3)


    # +------------------------------------------------------------------------------------+ #
    # |                                ENVIRONNEMENT SET UP                                | #
    # +------------------------------------------------------------------------------------+ #

    module load python/Anaconda
    module load cuda/11.3
    source /usr/local/Anaconda/Anaconda3-2019.07/etc/profile.d/conda.sh # (4)
    conda deactivate
    conda activate myenv
    cd path/to/working/directory # (5)


    # +------------------------------------------------------------------------------------+ #
    # |                                 RUN PYTHON SCRIPT                                  | #
    # +------------------------------------------------------------------------------------+ #

    python main.py # (6)

    ```

    1. All the SLURM parameters should be adapted to your need of course.
    2. Any output usually displaying inside your terminal (e.g. `#!python print()` calls) will render inside the output file.  
    3. Many constraints are available for all kind of hardware request.
    4. The lines bellow prevent weird behavior when activating an environment inside an environment
    5. This is of course the folder containing the `main.py` file.
    6. Here we kept things simple with a single python call but this part could contain multiple instructions.


And that's it. Not so hard right ? Now we can store this script inside a file (usually with the `.job` extension), let's call it `example.job`.
Now we need to submit this job. This is done with the `sbatch [filename]` command, in our case:

`$ sbatch example.job`

You should see something like `Submitted job with id ...`. You can check your job's status by running:

`$ squeue -u yourusername`

You should create one file and one sbatch submit per job, though you can submit as many jobs as you like simultaneously. 


---

This should help you get started with the basics of the HPC and SLURM. Bellow is provided a list of the most used SLURM commands.



## IV - SLURM cheat sheet


??? summary "Action"

    | Action               | Command                           |
    | :------------------: | :-------------------------------: |
    | Job submission       | `sbatch [script_file]`            |
    | Job deletion         | `scancel [job_id]`                |
    | Job status (by job)  | `squeue [job_id]`                 |
    | Job status (by user) | `squeue -u [user_name]`           |
    | Job hold             | `scontrol hold [job_id]`          |
    | Job release          | `scontrol release [job_id]`       |
    | Queue list           | `squeue`                          |
    | Node list            | `sinfo -N OR scontrol show nodes` |
    | Cluster status       | `sinfo`                           |
    | GUI                  | `sview`                           |



??? summary "Environment"
    
    | Environment      | Value                |
    | :--------------: | :------------------: |
    | Job ID           | $SLURM_JOBID         |
    | Submit Directory | $SLURM_SUBMIT_DIR    |
    | Submit Host      | $SLURM_SUBMIT_HOST   |
    | Node List        | $SLURM_JOB_NODELIST  |
    | Job Array Index  | $SLURM_ARRAY_TASK_ID |


??? summary "Parameter"

    | Parameter            | Value                                                       |
    | :------------------: | :---------------------------------------------------------: |
    | Script directive     | #SBATCH                                                     |
    | Queue                | -p [queue]                                                  |
    | Node Count           | -N [min[-max]]                                              |
    | CPU Count            | -n [count]                                                  |
    | Wall Clock Limit     | -t [min] OR -t [days-hh\:mm:ss]                             |
    | Standard Output FIle | -o [file_name]                                              |
    | Standard Error File  | e [file_name]                                               |
    | Combine stdout/err   | (use -o without -e)                                         |
    | Copy Environment     | --export=[ALL | NONE | variables]                           |
    | Event Notification   | --mail-type=[events]                                        |
    | Email Address        | --mail-user=[address]                                       |
    | Job Name             | --job-name=[name]                                           |
    | Job Restart          | --requeue OR --no-requeue <br> (NOTE: configurable default) |
    | Working Directory    | --workdir=[dir_name]                                        |
    | Resource Sharing     | --exclusive OR--shared                                      |
    | Memory Size          | --mem=[mem][M|G|T] OR <br> --mem-per-cpu=[mem][M|G|T]       |
    | Tasks Per Node       | --tasks-per-node=[count]                                    |
    | CPUs Per Task        | --cpus-per-task=[count]                                     |
    | Job Dependency       | --depend=[state:job_id]                                     |
    | Job Project          | --wckey=[name]                                              |
    | Job host preference  | --nodelist=[nodes] AND/OR <br> --exclude=[nodes]            |
    | Job Arrays           | --array=[array_spec] (Slurm version 2.6+)                   |
    | Generic Resources    | --gres=[resource_spec]                                      |
    | Licenses             | --licenses=[license_spec]                                   |
    | Begin Time           | --begin=YYYY-MM-DD[THH:MM[:SS]]                             |
