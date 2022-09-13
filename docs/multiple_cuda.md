# Manage multiple CUDA

---
<div align='right' class="result" markdown>
*Luc Vedrenne, june 2022*
</div>



!!! info

    There are many ways to achieve this. Experts will say the way described here is not "clean".
    Feel free to update this guide to a cleaner version if you want to. I'll be glad !


Takeaways: </br>
1. The key is to install the latest version compatible with the driver first, otherwise each CUDA install
will replace the driver. </br>
2. Installing cuDNN through tar archive and not deb file allows to have multiple installs coexisting.
3. CUDA compiler nvcc needs compatible version of C and C++ compiler. Multiple versions of those
compilers can be installed and linked to their nvcc counterparts through symlink. </br>
4. Paths can be setted up so that all CUDA versions are available for any task. </br>



## I - Install latest driver

Many ways to do it. If your're on Ubuntu, I recommand:

```
sudo ubuntu-drivers devices
ubuntu-drivers devices
sudo apt install nvidia-driver-[version number]
```

Then reboot and check install with `nvidia-smi`


!!! warning 

    Check the CUDA version displayed on the top right by `nvidia-smi`. **This is absolutely not the CUDA version
    installed on your computer. It is the latest version compatible with the installed driver. This is the version
    you must install fist.**


## II - Install CUDA

!!! warning

    You can repeat steps II to V as many times as you need to install different versions of CUDA/cuDNN.
    But first, install the latest compatible version of CUDA Toolkit for the Nvidia driver you installed.
    If you start to install the CUDA Toolkit from the smaller version it will replace the driver.


- Go to the [CUDA toolkit archive](https://developer.nvidia.com/cuda-toolkit-archive)
- Download the version you want and follow the instructions on Nvidia website until the second to last step
- At the last step, instead of running `sudo apt install cuda`, run `sudo apt install cuda-[version]`, e.g.
`sudo apt install cuda-11.6`. 

Check your CUDA versions: they are in `/usr/local/`. You should see several folder named `cuda-M.m` and some symlinks,
with one named `cuda` pointing to the default CUDA version. </br>
**You can change your default CUDA version by updating this symlink:
`sudo ln -sfT /usr/local/cuda/cuda-M.m/ /usr/local/cuda`**


## III - Install cuDNN

!!! info

    You need an Nvidia developper account to download tar cuDNN. The procedure to create one is straightforward.


- Go to the [cuDNN archive](https://developer.nvidia.com/rdp/cudnn-archive)
- **Download the tar version and not the deb one**. If you install cuDNN using .deb file, it will replace
existing installs.
- Extract the archive: `tar -xzvf cudnn-x.x-linux-x64-v8.x.x.x.[tgz|tar.xz]` (if it throws an error,
retry with `tar -xvf`, it depends on the archive extension).
- Copy the cuDNN libraries to **the appropriate CUDA**:
```
cd cudnn-x.x-linux-x64-v8.x.x.x
sudo cp include/cudnn*.h /usr/local/cuda-M.m/include
sudo cp lib[64]/libcudnn* /usr/local/cuda-M.m/lib64
sudo chmod a+r /usr/local/cuda-M.m/include/cudnn*.h /usr/local/cuda-M.m/lib64/libcudnn*
```

Depending on the cuDNN version, folders to copy can be named `lib` or `lib64`. Just check the existing paths.


## IV - Install compatible C/C++ compilers

CUDA code needs to be compiled, using nvcc, shipped with the CUDA toolkit install. You can check your nvcc version
by running `nvcc --version` (note that this uses the version with the cuda pointed by the `cuda` symlink in `usr/local`).
Try to update the `cuda` symlink to check it reflects on the `nvcc --version` output. </br>
When using multiple versions of CUDA, you'll run into compilation errors due to C/C++ compiler compatibility:
`error -- unsupported GNU version! gcc M.m and up are not supported!`

Fortunately, you can very easily install multiple version of those C/C++ compilers, for instance:
```
sudo apt install build-essential
sudo apt -y install gcc-7 g++-7 gcc-8 g++-8 gcc-9 g++-9
```

Of course, adjust the specified version for your need.

gcc and g++ are installed in `/usr/bin/`. You can link one version of gcc and one version of g++ with one version of CUDA
by creating the following symlinks:
```
sudo ln -s /usr/bin/gcc-M.m /usr/local/cuda-M.m/bin/gcc
sudo ln -s /usr/bin/g++-M.m /usr/local/cuda-M.m/bin/g++
```

Again, don't forget to adjust the specified version to your need.  


*A this point, we have created several compatible bundles of CUDA, cuDNN, nvcc, gcc, g++. We're almost there, we'll done !*


## V - Set paths

Last step: we'll add every installed version of CUDA to `PATH` so that when a specific version of CUDA library
is required by a task it will simply search through all the paths listed here one by one and finds it.

Open `~/.bashrc` with your favorite editor `sudo [gedit|subl|vim|whatever] ~/.bashrc`.
Add those lines:

```
export PATH=/usr/local/cuda/bin${PATH:+:${PATH}}
export LD_LIBRARY_PATH="/usr/local/cuda/lib64:/usr/local/cuda-11/lib64:/usr/local/cuda-11.3/lib64:/usr/local/cuda-11.7/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}"
```

**Make sure you add all your cuda-M.m lib64 paths here, with the symlinks as well**.



Thats it ! Reboot and you're good to go !



