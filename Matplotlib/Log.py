"""
@Author: Swapnil Bhoyar
@Date: 2021-07-11 22:53:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-11 22:53:00
@Title : this program consist log configuration.
"""
import logging

class Log:
    logging.basicConfig(filename="Output.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
  
    #Creating an object
    logger=logging.getLogger()
    
    #Setting the threshold of logger to ERROR
    logger.setLevel(logging.DEBUG)