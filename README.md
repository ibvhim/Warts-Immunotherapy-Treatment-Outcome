# <u><b>Warts Immunotherapy - Treatment Outcome Prediction</u></b>

### <b>Table of Contents</b>
- [Warts Immunotherapy - Treatment Outcome Prediction](#warts-immunotherapy---treatment-outcome-prediction)
    - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Preview](#preview)
  - [Softwares and Tools](#softwares-and-tools)
  - [Steps to Run](#steps-to-run)

 ***
 ## <b>Introduction</b>

This is a project that uses a predictive model with a <b>Random Forest Classifier</b> to predict whether a wart can be treated using immunotherapy. Immunotherapy is a type of medical treatment that boosts the body's natural defenses to fight disease. It is used to treat a wide range of diseases, including cancer, viral infections, and autoimmune disorders. There are several different types of immunotherapies, including monoclonal antibody therapy, cancer vaccines, and immune checkpoint inhibitors.

My project has the potential to be a valuable tool for healthcare professionals. By using machine learning to analyze data on the characteristics of warts and the outcomes of previous immunotherapy treatments, the model may be able to accurately predict which warts will respond to immunotherapy and which will not. This information could help healthcare providers make more informed treatment decisions, leading to better outcomes for patients. Additionally, <b>by potentially reducing the need for trial-and-error approaches to treatment, my project could also help reduce healthcare costs and improve patient quality of life.</b>

***
## <b>Preview</b>
![image](data/wart_immunotherapy_preview.gif)
***

## <u><b>Softwares and Tools</u></b>

- [Jupyter Notebook](https://jupyter.org/)
- [VS Code IDE](https://code.visualstudio.com/)
- [Flask](https://flask.palletsprojects.com/en/2.2.x/)
- [GitHub](https://www.github.com/ibvhim)
- [GitCLI](https://git-scm.com/docs/gitcli)
- [Heroku](https://heroku.com) <i>[NOT SUPPORTED ANYMORE! ☹ ]</i>
  
***
## <b>Steps to Run</b>
 The data has been cleaned and processed and can be found in the `data` folder. <b>[Random Forest Classifier - 94%]</b>. To run the program follow these steps:

1. Clone the repository using the following command
    <i><pre><code> git clone https://github.com/ibvhim/Warts_Immunotherapy.git </pre></code></i>

2. Create a new virtual environment (<i>REMEMBER TO <u><b>ALWAYS</b></u> CREATE VIRTUAL ENVIRONMENTS FOR NEW PROJECTS</i>)
    <i><pre><code> conda create -p [virtual_environment_name] python==3.7 -y </pre></code></i>

3. Once you're done creating a virtual environment, install the prerequisites listed in the `requirements.txt` file
    <i><pre><code> pip install -r requirements.txt </pre></code></i>
    
4. You can find the FLASK API in the `app.py` file; and the stucture of the landing page in the `templates/index.html` file. 

5. Run the program
    <i><pre><code> python app.py </pre></code></i>
    
<b>IMPORTANT NOTE:</b> The docker container was previously succesfully deployed in Heroku! However, due to the recent update Heroku stopped supporting free containers and hence the app went down! Sorry about that ☹!

***


    


