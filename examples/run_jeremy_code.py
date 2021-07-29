import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from api import GPT, Example, UIConfig
from api import demo_web_app
# Construct GPT object
# gpt = GPT(engine="davinci",
#           temperature=0.05,
#           max_tokens=100)

gpt = GPT(engine="davinci",
          temperature=0.05,
          max_tokens=100,
          frequency_penalty=0.25,
          presence_penalty=0.03)

input_1 = 'A complete web application that provides Flight Search, Payment, Booking and Loyalty points including ' \
          'end-to-end testing, GraphQL and CI/CD'
output_1 = 'Amplify, DynamoDB, AppSync, API Gateway, Cognito, SNS, Step Functions'

input_2 = 'Application to automatically generate and edit subtitles and audio transcriptions in multiple languages'
output_2 = 'Rekognition, Transcribe, Translate, Cognito, Polly, Elemental MediaConvert,  Elasticsearch Service'

input_3 = 'An office sensor application and a web application to monitor weather patterns in the office'
output_3 = 'IoT Core Console, IoT Device SDK for Python, IoT API, IoT Broker, IoT Analytics, IAM, Sagemaker'

input_4 = 'A tool to search over a large number of documents such as pdf files'
output_4 = 'Comprehend, Elasticsearch, S3, Cognito, CodeBuild, Lambda, SAM, CloudFormation, IAM, Textract'

input_5 = 'Company and Editor'
output_5 = 'Handshake Management Consulting and Chinonso Kalu'

gpt.add_example(Example(input_1, output_1))
gpt.add_example(Example(input_2, output_2))
gpt.add_example(Example(input_3, output_3))
gpt.add_example(Example(input_4, output_4))
gpt.add_example(Example(input_5, output_5))
config = UIConfig(
    description='Enter a description of your app',
    button_text="Architect for me.",
    placeholder='app description..'
)
demo_web_app(gpt, config)