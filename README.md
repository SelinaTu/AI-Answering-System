# AI Food Advisor

This project provides a simple command line interface that demonstrates how to
use AWS services such as Amazon Textract and Amazon Bedrock to analyze menu
images. It extracts text from a menu image then enriches the menu with estimated
calories and ingredient information using a Bedrock model.

## Requirements
- Python 3.10+
- AWS credentials with access to Textract and Bedrock

Install dependencies with:
```bash
pip install -r requirements.txt
```

## Usage
Run the CLI and pass an image of a menu:
```bash
python -m ai_food_advisor.app path/to/menu.jpg --region us-east-1
```
