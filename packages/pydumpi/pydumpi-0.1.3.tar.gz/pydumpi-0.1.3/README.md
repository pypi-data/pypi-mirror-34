# SST-DUMPI Python Bindings
Python bindings for the SST-DUMPI Trace Library.

## Install
Pydumpi is available at [PyPi](https://pypi.org/project/pydumpi):

```bash
pip install pydumpi
```

**Note**: The PyPI package contains a prebuilt shared library, this might not 
work on very old systems, and is linux only. If this does not work for you
installing from source is your only option.

## Install from Source
Clone this repository and install the package with pip in a virtual environment, e.g:

```bash
git clone http://github.com/justacid/pydumpi
cd myproject
source venv/bin/activate
pip install ../pydumpi
```

The install might take some time - if the dumpi library can not be found
on the path it will be downloaded and compiled during the install
process. You can also install libundumpi globally, for more 
information on how to install globally refer to the
[sst-dumpi repository](https://github.com/sstsimulator/sst-dumpi).

## Usage Examples
Inherit from DumpiTrace and override the callbacks you are interested in.
Every MPI function has an available callback. A complete list can be found 
in *dumpi/callbacks.py*.

```python
from pydumpi import DumpiTrace


class MyTrace(DumpiTrace):

    def __init__(self, file_name):
        super().__init__(file_name)
        self.message_count = 0

    def on_send(self, data, thread, cpu_time, wall_time, perf_info):
        self.message_count += 1
        time_diff = wall_time.stop - wall_time.start
        print(f"Time elapsed in 'MPI_Send': {time_diff.to_ms()} milliseconds.")

    def on_recv(self, data, thread, cpu_time, wall_time, perf_info):
        print(f"Message received on thread '{thread}' from thread '{data.source}'.")


with MyTrace("path/to/some/trace.bin") as trace:
    trace.print_header()
    trace.read_stream()
    print(trace.message_count)
```

**Important:** Since the C backend frees the data after a callback returns,
it is only valid *within* a callback (including wall and cpu time). If you
need to store it perform a deep copy, otherwise you get garbage values.

### Meta Data
You can inspect the meta data of a dumpi trace by printing the header and
footer. In particular the footer prints a list of all MPI functions that 
were called during a trace - this information can help guide you in deciding
which callbacks need to be overriden for further analysis.

```python
with DumpiTrace("path/to/some/trace.bin") as trace:
    trace.print_header()
    trace.print_footer()
```

There also is a utilty function to read all binary traces in a folder. The 
function will search for a meta file in a given directory, do some basic sanity
checks and return a list with all binary traces.

```python
from pydumpi.util import trace_files_from_dir

for fname in trace_files_from_dir("path/to/data_dir"):
    print(fname)
```
