# <u><b>Warts Immunotherapy</u></b>
<b> Immunotherapy uses the patient's own immune system to fight the warts. This treatment is used when the warts remain despite other treatments. One type of immunotherapy involves applying a chemical, such as diphencyprone (DCP), to the warts. A mild allergic reaction occurs around the treated warts. <u>This is an industry ready project that allows you to enter your details and confirm if your warts the patient has been infected with is treatable using immunotherapy. </b></u>

***
## <u><b>Preview</u></b>
![image](wart_immunotherapy.gif)
***

## <u><b>Softwares and Tools</u></b>

- [GitHub](https://www.github.com/ibvhim)
- [HerokuApp](https://www.heroku.com)
- [VS Code IDE](https://code.visualstudio.com/)
- [GitCLI](https://git-scm.com/docs/gitcli)
- [Heroku](https://heroku.com) [NOT SUPPORTED ANYMORE! ☹]

***
## <u><b>Steps</u></b>
 The data has been cleaned and processed and can be found in the `data` folder. <b>[Random Forest Classifier - 94%]</b>

1. To run the program follow these steps:

2. Clone the repository using the following command
    <i><pre><code> git clone https://github.com/ibvhim/Warts_Immunotherapy.git </pre></code></i>
3. Create a new virtual environment (<i>REMEMBER TO <u><b>ALWAYS</b></u> CREATE VIRTUAL ENVIRONMENTS FOR NEW PROJECTS</i>)
    <i><pre><code> conda create -p [virtual_environment_name] python==3.7 -y </pre></code></i>

4. Once you're done creating a virtual environment, install the prerequisites listed in the `requirements.txt` file
    <i><pre><code> pip install -r requirements.txt </pre></code></i>
    
5. You can find the FLASK API in the `app.py` file; and the stucture of the landing page in the <b>templates/`index.html`</b> file. 

6. Run the program
    <i><pre><code> python app.py </pre></code></i>
    
7. The docker container was previously succesfully deployed in Heroku! However, due to the recent update Heroku stopped supporting free containers and hence the app went down! Sorry for that ☹!

***


    


