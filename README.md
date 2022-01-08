## ETL - Daily Top 50 Best Selling Big Data Books on Amazon

Disclaimer: This is an overkill architecture, there are simpler ways of doing this project using less tools but the purpose was to practice and learn using different tools and techniques. 

This project consists of:
- web scraping data from Amazon using Python's BeautifulSoup
- loading the data from my local machine to GCP using secure SFTP 
- working with Compute Engine VMs
- moving data within GCP from the VM to Cloud Storage
- creating a dimensional model (Kimball) with the data
- loading it to its final destination in BigQuery


### Data Modeling

![Data Model/ERD](data-modeling.png)

### Transferring Files Securely To Remote Compute Engine VM with SFTP

![SFTP](sftp-ref.png)

### Loading Files VM To Cloud Storage Bucket

![cloud-storage](cloud-storage.png)