# -*- coding: utf-8 -*-

import json
import uuid

from TM1py.Exceptions import TM1pyException
from TM1py.Objects import Process
from TM1py.Services import ObjectService


class ProcessService(ObjectService):
    """ Service to handle Object Updates for TI Processes
    
    """
    def __init__(self, rest):
        super().__init__(rest)

    def get(self, name_process):
        """ Get a process from TM1 Server
    
        :param name_process:
        :return: Instance of the TM1py.Process
        """
        request = "/api/v1/Processes('{}')?$select=*,UIData,VariablesUIData," \
                  "DataSource/dataSourceNameForServer," \
                  "DataSource/dataSourceNameForClient," \
                  "DataSource/asciiDecimalSeparator," \
                  "DataSource/asciiDelimiterChar," \
                  "DataSource/asciiDelimiterType," \
                  "DataSource/asciiHeaderRecords," \
                  "DataSource/asciiQuoteCharacter," \
                  "DataSource/asciiThousandSeparator," \
                  "DataSource/view," \
                  "DataSource/query," \
                  "DataSource/userName," \
                  "DataSource/password," \
                  "DataSource/usesUnicode," \
                  "DataSource/subset".format(name_process)
        response = self._rest.GET(request, "")
        return Process.from_dict(response.json())

    def get_all(self):
        """ Get a processes from TM1 Server
    
        :return: List, instances of the TM1py.Process
        """
        request = "/api/v1/Processes?$select=*,UIData,VariablesUIData," \
                  "DataSource/dataSourceNameForServer," \
                  "DataSource/dataSourceNameForClient," \
                  "DataSource/asciiDecimalSeparator," \
                  "DataSource/asciiDelimiterChar," \
                  "DataSource/asciiDelimiterType," \
                  "DataSource/asciiHeaderRecords," \
                  "DataSource/asciiQuoteCharacter," \
                  "DataSource/asciiThousandSeparator," \
                  "DataSource/view," \
                  "DataSource/query," \
                  "DataSource/userName," \
                  "DataSource/password," \
                  "DataSource/usesUnicode," \
                  "DataSource/subset"
        response = self._rest.GET(request, "")
        response_as_dict = response.json()
        return [Process.from_dict(p) for p in response_as_dict['value']]

    # TODO Redesign required!
    def get_all_process_names_filtered(self):
        """ Get List with all process names from TM1 Server.
            Does not return:
                - system process
                - Processes that have Subset as Datasource

        :Returns:
            List of Strings
        """
        response = self._rest.GET("/api/v1/Processes?$select=Name&$filter=DataSource/Type ne 'TM1DimensionSubset'"
                                  " and  not startswith(Name,'}')", "")
        processes = list(process['Name'] for process in response.json()['value'])
        return processes

    def get_all_names(self):
        """ Get List with all process names from TM1 Server

        :Returns:
            List of Strings
        """
        response = self._rest.GET('/api/v1/Processes?$select=Name', '')
        processes = list(process['Name'] for process in response.json()['value'])
        return processes

    def update(self, process):
        """ Update an existing Process on TM1 Server
    
        :param process: Instance of TM1py.Process class
        :return: Response
        """
        request = "/api/v1/Processes('" + process.name + "')"
        # Adjust process body if TM1 version is lower than 11 due to change in Process Parameters structure
        # https://www.ibm.com/developerworks/community/forums/html/topic?id=9188d139-8905-4895-9229-eaaf0e7fa683
        if int(self.version[0:2]) < 11:
            process.drop_parameter_types()
        response = self._rest.PATCH(request, process.body)
        return response

    def create(self, process):
        """ Create a new process on TM1 Server
    
        :param process: Instance of TM1py.Process class
        :return: Response
        """
        request = "/api/v1/Processes"
        # Adjust process body if TM1 version is lower than 11 due to change in Process Parameters structure
        # https://www.ibm.com/developerworks/community/forums/html/topic?id=9188d139-8905-4895-9229-eaaf0e7fa683
        if int(self.version[0:2]) < 11:
            process.drop_parameter_types()
        response = self._rest.POST(request, process.body)
        return response

    def delete(self, name):
        """ Delete a process in TM1
        
        :param name: 
        :return: Response
        """
        request = "/api/v1/Processes('{}')".format(name)
        response = self._rest.DELETE(request)
        return response

    def exists(self, name):
        """ Check if Process exists.
        
        :param name: 
        :return: 
        """
        request = "/api/v1/Processes('{}')".format(name)
        return self._exists(request)

    def compile(self, name):
        """ Compile a Process. Return List of Syntax errors.
        
        :param name: 
        :return: 
        """
        request = "/api/v1/Processes('{}')/tm1.Compile".format(name)
        response = self._rest.POST(request, '')
        syntax_errors = response.json()["value"]
        return syntax_errors

    def execute(self, process_name, parameters=None, **kwargs):
        """ Ask TM1 Server to execute a process. Call with parameter names as keyword arguments:
        tm1.processes.execute("Bedrock.Server.Wait", pLegalEntity="UK01")

        :param process_name:
        :param parameters: Deprecated! dictionary, for instance {"Parameters": [ { "Name": "pLegalEntity", "Value": "UK01" }] }
        :return:
        """
        request = "/api/v1/Processes('{}')/tm1.Execute".format(process_name)
        if not parameters:
            if kwargs:
                parameters = {"Parameters": []}
                for parameter_name, parameter_value in kwargs.items():
                    parameters["Parameters"].append({"Name": parameter_name, "Value": parameter_value})
            else:
                parameters = {}
        return self._rest.POST(request=request, data=json.dumps(parameters, ensure_ascii=False))

    def execute_ti_code(self, lines_prolog, lines_epilog=None):
        """ Execute lines of code on the TM1 Server

            :param lines_prolog: list - where each element is a valid statement of TI code.
            :param lines_epilog: list - where each element is a valid statement of TI code.
        """
        process_name = '}' + 'TM1py' + str(uuid.uuid4())
        p = Process(name=process_name,
                    prolog_procedure=Process.auto_generated_string + '\r\n'.join(lines_prolog),
                    epilog_procedure=Process.auto_generated_string + '\r\n'.join(lines_epilog) if lines_epilog else '')
        self.create(p)
        try:
            self.execute(process_name)
            pass
        except TM1pyException as e:
            raise e
        finally:
            self.delete(process_name)

    def get_processerrorlogs(self, process_name):
        """ Get all ProcessErrorLog entries for a process

        :param process_name: name of the process
        :return: list - Collection of ProcessErrorLogs
        """
        request = "/api/v1/Processes('{}')/ErrorLogs".format(process_name)
        response = self._rest.GET(request=request)
        return response.json()['value']

    def get_last_message_from_processerrorlog(self, process_name):
        """ Get the latest ProcessErrorLog from a process entity

            :param process_name: name of the process
            :return: String - the errorlog, e.g.: "Fehler: Prolog Prozedurzeile (9): Zeichenfolge "US772131
            kann nicht in eine reelle Zahl umgewandelt werden."
        """
        logs_as_list = self.get_processerrorlogs(process_name)
        if len(logs_as_list) > 0:
            timestamp = logs_as_list[-1]['Timestamp']
            request = "/api/v1/Processes('{}')/ErrorLogs('{}')/Content".format(process_name, timestamp)
            # response is plain text - due to entity type Edm.Stream
            response = self._rest.GET(request=request)
            return response
