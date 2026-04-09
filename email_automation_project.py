#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from sqlalchemy import create_engine
import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv
load_dotenv()

base_path=Path(r"C:\Users\vipas\OneDrive\Documents\project6")
report_path=Path(base_path/"report")
chart_path=Path(base_path/"chart")

report_path.mkdir(parents=True,exist_ok=True)
chart_path.mkdir(parents=True,exist_ok=True)


def send_email():
    sender=os.getenv("EMAIL_USER")
    password=os.getenv("EMAIL_PASS")
    receiver=os.getenv("EMAIL_RECEIVER")

    msg=EmailMessage()
    msg["Subject"]="Sales Report"
    msg["From"]=sender
    msg["To"]=receiver
    msg.set_content("Attached is the latest sales report.")

    file_path=report_path/"sales_report.xlsx"

    with open(file_path,"rb") as f:
        msg.add_attachment(f.read(),
                          maintype="application",
                          subtype="octet-stream",
                          filename="sales_report.xlsx")

    with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
        smtp.login(sender,password)
        smtp.send_message(msg)

    print("Email sent successfully!")

# main pipeline

def main():
    try:
        print("Running Pipeline")

        engine=create_engine("sqlite:///sales.db")

        df=pd.read_sql("select * from sales",engine)

        df["date"]=pd.to_datetime(df["date"])
        df=df.dropna()

        total_sales=df["sales_amount"].sum()

        df["month"]=df["date"].dt.to_period("M")

        monthly_sales=df.groupby(df["month"],as_index=False)["sales_amount"].sum()

        region_sales=df.groupby(df["region"],as_index=False)["sales_amount"].sum()

        monthly_sales["month"]=monthly_sales["month"].astype(str)

        plt.figure()
        plt.bar(monthly_sales["month"],monthly_sales["sales_amount"])
        plt.title("monthly sales")
        plt.xlabel("month")
        plt.ylabel("sales")
        plt.savefig(chart_path/"graph1.png")
        plt.close()


        plt.figure()
        plt.plot(region_sales["region"],region_sales["sales_amount"],marker="o")
        plt.title("region sales")
        plt.xlabel("region")
        plt.ylabel("sales")
        plt.savefig(chart_path/"graph2.png")
        plt.close()

        file_path=report_path/"sales_report.xlsx"

        with pd.ExcelWriter(file_path) as writer:
            pd.DataFrame({"Total Sales":[total_sales]}).to_excel(writer,sheet_name="Total",index=False)
            region_sales.to_excel(writer,sheet_name="Region",index=False)
            monthly_sales.to_excel(writer,sheet_name="Month",index=False)
            
        print("Pipeline Executed Successfully!")

        send_email()
    except Exception as e:
        print("Pipeline Failed:",e)

if __name__=="__main__":
    main()

