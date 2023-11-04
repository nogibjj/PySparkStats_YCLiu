from fpdf import FPDF
import pandas as pd
import statsYC

def makeSummary():
    SummaryReport = FPDF()
    
    # Add a page
    SummaryReport.add_page()

    # set style and font size
    SummaryReport.set_font("Arial", size = 12)

    TestCase1 = pd.read_csv('TestCase1.csv', header = 0)
    SummaryReport.cell(200, 12, txt = statsYC.printNumStats(TestCase1, 'Age'),ln = 1, align = 'L')
    SummaryReport.cell(200, 12, txt = statsYC.printOccStats(TestCase1, 'Sex', 'M'),ln = 2, align = 'L')
    SummaryReport.output("SummaryReport.pdf")  