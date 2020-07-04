# Who are the European dataworkers?

In this repository you will find a pipeline that combines, cleans and analyzes work-related data to yield insights on data workers' amount, education and how they think regarding several socioeconomic matters across the Europe: 
- This pipeline retrieves data from a (*) database, University of Chicago's API containing data on normalized taxonomy of jobs and Eurostat country codes.  
- The tables that this pipeline produces are related with
    1. Quantity and percentage of workers having the same job in 26 EU countries and within an specific country
    2. Reasons they posit for and against a universal living wage
    3. Skills data workers exhibit in different educational level ranges
    
- Providing a specific country to the pipeline, it shows information, otherwise, the pipeline will return the result for all countries.

![Image](data/raw/kobu-agency-67L18R4tW_w-unsplash(1).jpg)

---
> Photo by KOBU Agency on Unsplash

### **Status**
Work-in-progress (Alpha)

### **Technology stack**
- Type: Standalone
- Language: Python
- Libraries:

   >[Pandas](https://pandas.pydata.org/) \
    [Sqlalchemy](https://www.sqlalchemy.org/) \
    [Request](https://requests.readthedocs.io/es/latest/) \
    [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/)
    
 

### **Core technical concepts and inspiration**
If you are thinking 

### :wrench: **Configuration**
Requeriments, prerequisites, dependencies, installation instructions.

### :see_no_evil: **Usage**
Parameters, return values, known issues, thrown errors.

### :file_folder: **Folder structure**
```
└── project
    ├── __trash__
    ├── .gitignore
    ├── .env
    ├── requeriments.txt
    ├── README.md
    ├── main_script.py
    ├── notebooks
    │   ├── notebook1.ipynb
    │   └── notebook2.ipynb
    ├── package1
    │   ├── module1.py
    │   └── module2.py
    └── data
        ├── raw
        ├── processed
        └── results
```

> Do not forget to include `__trash__` and `.env` in `.gitignore` 

### **ToDo**
Next steps, features planned, known bugs (shortlist).

### **Contact info**
For further information do not hesitate to contact cuadradobrionescarmen@gmail.com

### **Last but not Least!**
If you are interested in continuing building this project, please start to commit!