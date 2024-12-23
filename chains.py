import os
from langchain_groq  import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

load_dotenv()


class Chain:
    def __init__(self):
        self.llm = ChatGroq(
            temperature=0,
            groq_api_key = os.getenv("GROQ_API_KEY"),
            model_name='llama-3.1-70b-versatile'
        )
    def extract_jobs(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template(
            """
            SCRAPED TEXT FROM WEBSITE:
            {page_data}
            Instructions:
            The scraped text is froom the career's page of a website.
            Your job is to extract the job postings and return them in JSON format containing the following keys: 'role', 'experience', 'skills', and 'description'.
            only return the valid JSON.
            VALID JSON (NO PREAMBLE):
            """
            )

        chain_extract = prompt_extract | self.llm
        response = chain_extract.invoke(input={'page_data':cleaned_text})
        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(response.content)
        except OutputParserException:
            raise OutputParserException('Context too big, Unable to parse jobs')
        return res if isinstance(res,  list) else [res]
    
    def write_mail(self, job, des):
        prompt_email = PromptTemplate.from_template(
        """
          ###JOB DESCRIPTION:
          {job_description}

          ###INSTRUCTIONS:

           You are Shayan Qadri a 23 year old computer science undergrad graduate who is passionate towards the world of AI and data. 
           He has made several projects and has gained experince through internships with hands on industry level projects. He is also 
           currrently persuing a Certificate in Machine Learning from YorkU to gain some more knowledge and experince in this evergrowing industry. 
           Your job is to write a cold email to the client regarding the job mentioned above describing your capability in fulfilling thier needs.
           Also add the most relevant projects from the following descriptions and project names to showcase your experience: {des_list}


          Remember you are Shayan Qadri a computer science graduate with a passion for AI and data.
          Do not provide a preamble.
          ### EMAIL (NO PREAMBLE):


        """
        )
        chain_email = prompt_email | self.llm
        response = chain_email.invoke({'job_description': str(job), "des_list": des})
        return (response.content)

