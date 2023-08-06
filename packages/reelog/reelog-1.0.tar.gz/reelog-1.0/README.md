# reelog
## python log best practices

example : 
```
import reelog

# root logger
logger = reelog.get_logger()
logger.info("hello world!")

# reelog name logger
logger = reelog.get_logger("reelog")
logger.error("hello world!")

# output to stdout and file
logger = reelog.get_logger("reelog", outputs=["stdout", "file"])
logger.warning("hello world!")

```