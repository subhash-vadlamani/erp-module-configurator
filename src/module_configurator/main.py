import sys
from module_configurator.crew import ERPCrew

def run():

    inputs = {
         'company_name': 'BuildFast Mnufacturing Inc.',
         'Industry': 'Manufacturing',
         'Region': 'United States',
         'Number of Employees': '120',
         'Business Goals': """
Improve inventory management and reduce stockouts. Automate payroll processing and employee leave tracking.
Enhance financial reporting and budgeting. Implement a customer support system to track complaints and resolutions.
Enable basic CRM capabilities to manage leads and client relationships.
"""
    }
    ERPCrew().crew().kickoff(inputs = inputs)

def train():
    """
        Train the crew for a given number of iterations.
    
    """

    inputs = {
         'company_name': 'BuildFast Mnufacturing Inc.',
         'Industry': 'Manufacturing',
         'Region': 'United States',
         'Number of Employees': '120',
         'Business Goals': """
Improve inventory management and reduce stockouts. Automate payroll processing and employee leave tracking.
Enhance financial reporting and budgeting. Implement a customer support system to track complaints and resolutions.
Enable basic CRM capabilities to manage leads and client relationships.
"""
    }

    
    try:
        ERPCrew().crew().train(n_iterations = int(sys.argv[1]), inputs = inputs)
    
    except Exception as e:
            raise Exception(f"An error occurred while training the crew: {e}")



