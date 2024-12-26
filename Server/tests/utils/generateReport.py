import os
from jinja2 import Template

def generate_report(template_path="template.html", output_file="report.html", data=None):
    
    with open(os.path.join(os.path.dirname(__file__), "reportTemplates", template_path), "r", encoding="utf-8") as f:
        HTML_TEMPLATE = f.read()
        
    """
    Generate an HTML report using Jinja2 with sample data.
    """

    # Create a Jinja2 Template object from the string
    template = Template(HTML_TEMPLATE)

    # Render the template with our sample data
    rendered_html = template.render(**data)

    # Write the rendered HTML to an output file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(rendered_html)
    
    print(f"Report generated: {output_file}")
    
    
def generate_basic_report(data):
    generate_report("CompareLLMReportBasic.html", "report.html", data)

if __name__ == "__main__":
    # Run the function to generate the report
    generate_basic_report()