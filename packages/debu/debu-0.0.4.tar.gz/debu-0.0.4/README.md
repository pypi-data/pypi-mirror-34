debu
===========

&copy; 2018 SiLeader.

## Overview
Automatic deployment and build tool.

You can use this package as normal python package and interpreter.

## Features
+ execute commands
+ copy files
+ execute debu script

## debu script
### Features
+ display data (print and echo)
+ execute commands
+ copy files
+ variables
+ comments

### data types
| name | expr | meaning |
|:----:|:----:|:--------|
| str | "str" | string type |
| int(hex) | 0xbeef | hexadecimal integer |
| int(dec) | 129 | decimal integer |
| int(oct) | 0o127 | octal integer |
| int(bin) | 0b101 | binary integer |
| host | user@host:port, user@host | SSH host name |

### script syntax
#### print and echo
```text
print "data"
echo "data"
```

#### comments
```text
# comment
print "data" # comment
```

#### copy files
```text
host_destination << host_source: copy /path/to/destination /path/to/source
```

#### execute command
```text
# execute ls command in host
host: ls
```

#### variables
```text
# assign
var1 = "data"

# copy variable
var2 = var1

# use in host name
host = user@example.com
host: ls
```
