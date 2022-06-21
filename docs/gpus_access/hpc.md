# HPC

!!! info "Work in progress"
    Some good documentation in the making.
    In the meantime, check the official HPC doc [here](https://hpc.pages.unistra.fr/).


---
<div align='right' class="result" markdown>
*Luc Vedrenne, june 2022*
</div>



## Introduction

## I - Getting an account

## II - Understanding SLURM

## III - Submit your first job

## IV - Cheat sheet


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
