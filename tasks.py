from crewai import Task
from agents import Data_Loader, Question_Crawler, Answer_Crawler, Data_Formatter, Manager
from main import website_link

# Define the tasks that will be used in the project
class Tasks(website_link):
    Manager = Task(
        description = "Manage the team of agents and provide tasks to each agent that will help further guide the project to sucess.",
        expected_output = "A well managed team and project.",
        agent = Manager
    )

    Load_Example_Data = Task(
        description = "Read files and directories to get example data that can be used to provide the agents with the kind of data they are looking to complete the project.",
        expected_output = "Example data that can be used to test the project.",
        agent = Data_Loader
    )
    
    Question_Crawler = Task(
        description = """Crawl the provided website {website_link} and all of its sublinks to come up with questions that students would have about the school.
        This could include gerneral information about the school, the programs offered, the campus life, different majors, food offered on campus, building and facility 
        locations, fraternity and sorority information, club information, teacher and faculty information.""",
        expected_output = "A list of questions that students would have about the school.",
        agent = Question_Crawler
    )

    Answer_Crawler = Task(
        description = "Crawl the provided website {website_link} and all of its sublinks to come up with answers to the questions that the question crawler agent came up with.",
        expected_output = "A list of answers to the questions that the question crawler agent came up with.",
        agent = Answer_Crawler
    )

    Data_Formatter = Task(
        description = """Format the data that was collected by the question and answer crawler agents so that it can be used to create a datset to finetune a model.
        Format it so that you have a Question on one line and the answer on the next line.
        """,
        expected_output = "Formatted data that can be used to create a chatbot.",
        agent = Data_Formatter
    )
