# Rerun-SDK for python resource leak

This repo is used to replicate the leak when repeatedly connecting and initialization of rerun in python.

## How to run

### Start the rerun server

`VSCode -> Run Task -> Rerun Serve`

or run the following command in the terminal

```bash
rerun --serve-web
```

### Run the python script

Run the following command in the terminal

```bash
python main.py
```

## What does the script do

The script will connect to the rerun server and initialize a new recording. It will log some text and then disconnect and repeat the process.

## Leak

The process starts with around 70 MiB of memory usage. After ~3780 iterations, the application crashes and the memory usage has increased to 2.1 GiB, 7550 connections and 15149 threads.
Also the CPU usage increases linearly over time up to 100% just before the crash.

### The crash

The crash is **not** due to the memory usage exceeding the limit of the system, but *i think* due to hitting the limit of the number of threads or connections that can be spawned.

```
Run 3784, time=9.801387786865234e-07 ms, memory=2134.6640625 MiB, connections=7585, threads=15149
Traceback (most recent call last):
  File "/workspaces/python/main.py", line 16, in <module>
    rr.init(application_id="MyPythonApplication", recording_id=f"Run{i}")
  File "/home/vscode/.local/lib/python3.12/site-packages/rerun_sdk/rerun/__init__.py", line 345, in init
    new_recording(
  File "/home/vscode/.local/lib/python3.12/site-packages/rerun_sdk/rerun/recording_stream.py", line 144, in new_recording
    bindings.new_recording(
RuntimeError: Failed to spawn the underlying batcher: Failed to spawn background thread 'ChunkBatcher::cmds_to_chunks': Resource temporarily unavailable (os error 11)
```