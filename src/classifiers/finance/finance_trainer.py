import joblib
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

def train_finance_classifier():
    # Currently logistic regression is used for the classifier, but more advanced models like neural networks could be used to improve accuracy.
    current_dir = os.path.dirname(os.path.abspath(__file__))
        
    vectorizer = TfidfVectorizer(max_features=1000, stop_words='english')
    model = LogisticRegression(multi_class='ovr')
    # Training data with bank statement and invoice samples, can be further expanded to improve accuracy
    training_data = [
        "BANK STATEMENT Account Number: 1234-5678-9012 Statement Period: 01/01/2023 - 01/31/2023 Opening Balance: $5,432.10 DEPOSITS: 01/05 Direct Deposit EMPLOYER INC $2,145.67 01/15 Transfer from Savings $500.00 WITHDRAWALS: 01/10 Check #1234 $350.00 01/20 ATM Withdrawal $200.00 Closing Balance: $7,527.77",
        "Monthly Statement Bank of America Account: *****6789 Statement Date: 02/28/2023 Previous Balance: $3,241.89 Credits: Payroll Deposit $2,567.89 ATM Deposit $1,000.00 Debits: POS Purchase GROCERY STORE $156.78 Bill Pay UTILITIES $245.90 Ending Balance: $6,407.10",
        "Chase Bank Statement Account Holder: John Smith Account: xxxxxx4321 Period: 03/01/2023-03/31/2023 Beginning Balance: $8,765.43 Deposits: 03/10 Wire Transfer $5,000.00 03/25 Cash Deposit $1,200.00 Withdrawals: Online Payment $2,345.67 Ending Balance: $12,619.76",
        "Wells Fargo Statement Summary Account: 9876543210 Date Range: 04/01/2023-04/30/2023 Starting Balance: $4,567.89 Total Credits: $3,456.78 Total Debits: $2,789.45 Service Charges: $12.00 Interest Paid: $0.23 Ending Balance: $5,223.45",
        "Citibank Account Statement Account: *****5432 Statement Date: 05/15/2023 Previous Balance: $6,789.12 Deposits and Credits: Direct Deposit SALARY $3,234.56 Transfer from Account #9876 $1,000.00 Withdrawals and Debits: Check #2345 $567.89 ATM Withdrawal $300.00 Final Balance: $10,155.79",
        "TD Bank Monthly Statement Account Number: 2468-1357-9012 Period: 06/01/2023-06/30/2023 Opening Balance: $7,890.12 Credits: Payroll $2,987.65 Interest Earned $1.23 Debits: Debit Card Purchase RESTAURANT $89.99 ATM Fee $2.50 Closing Balance: $10,786.51",
        "PNC Bank Statement Account: ****7890 Date: 07/31/2023 Beginning Balance: $5,678.90 Deposits: Check Deposit $1,234.56 ACH Credit EMPLOYER $2,345.67 Withdrawals: Bill Payment RENT $1,500.00 Debit Card GROCERY $234.56 Ending Balance: $7,524.57",
        "US Bank Account Summary Account: 1357-2468-9012 Statement Period: 08/01/2023-08/31/2023 Prior Balance: $9,012.34 Credits: Mobile Deposit $2,500.00 Cash Deposit $750.00 Debits: Check #3456 $1,234.56 ATM Withdrawal $400.00 Current Balance: $10,627.78",
        "Capital One Bank Statement Account: *****3456 Period: 09/01/2023-09/30/2023 Starting Balance: $4,321.98 Deposits: Direct Deposit SALARY $2,789.45 Transfer In $1,000.00 Withdrawals: Online Transfer $500.00 POS Purchase $156.78 Ending Balance: $7,454.65",
        "Bank Statement Regions Bank Account: xxxxxx6789 Date Range: 10/01/2023-10/31/2023 Beginning Balance: $6,543.21 Credits: ACH Deposit $3,456.78 Interest Payment $0.45 Debits: Check Card Purchase $234.56 ATM Withdrawal $100.00 Final Balance: $9,665.88",
        "INVOICE #12345 Date: 01/15/2023 Bill To: ABC Corporation 123 Business St From: XYZ Services Items: Professional Services $2,500.00 Equipment Rental $500.00 Materials $750.00 Subtotal: $3,750.00 Tax (8%): $300.00 Total Due: $4,050.00 Due Date: 02/15/2023",
        "Tax Invoice No: INV-789 Issue Date: 02/20/2023 Customer: Smith Industries Supplier: Tech Solutions LLC Services Rendered: IT Consulting (40 hrs) $4,000.00 Hardware Installation $1,500.00 Subtotal: $5,500.00 VAT (10%): $550.00 Total: $6,050.00 Payment Terms: Net 30",
        "Invoice Number: 2023-456 Date: 03/10/2023 To: Global Corp From: Office Supplies Inc Product: Printer Paper (10 boxes) $200.00 Ink Cartridges (5 units) $375.00 Desktop Organizers (3 units) $90.00 Subtotal: $665.00 Tax: $53.20 Total Amount: $718.20",
        "Commercial Invoice #789-456 Invoice Date: 04/05/2023 Buyer: Johnson & Co Seller: Industrial Parts Ltd Description: Machine Parts $3,000.00 Labor Hours $800.00 Shipping $200.00 Subtotal: $4,000.00 Sales Tax: $320.00 Total Due: $4,320.00",
        "Service Invoice INV-2023-789 Date: 05/12/2023 Client: City Services Provider: Maintenance Pro LLC Service: Annual Maintenance $5,000.00 Emergency Repairs $1,200.00 Parts Replacement $800.00 Subtotal: $7,000.00 Tax (7%): $490.00 Total: $7,490.00",
        "Invoice #456-789 Billing Date: 06/25/2023 To: Healthcare Corp From: Medical Supplies Inc Items: Surgical Supplies $3,500.00 Medical Equipment $2,000.00 PPE Supplies $500.00 Subtotal: $6,000.00 Tax: $480.00 Total Amount Due: $6,480.00",
        "Professional Invoice INV#: 2023-321 Date: 07/15/2023 Client: Legal Corp Services: Legal Consultation $2,500.00 Document Preparation $1,500.00 Court Filing Fees $750.00 Total Hours: 25 Rate: $200/hr Subtotal: $4,750.00 Total Due: $4,750.00",
        "Sales Invoice No: SI-456 Date: 08/30/2023 Customer: Retail Solutions Vendor: Electronics Wholesale Description: Laptops (5 units) $5,000.00 Monitors (10 units) $2,000.00 Accessories $500.00 Subtotal: $7,500.00 Tax (8.5%): $637.50 Total: $8,137.50",
        "Construction Invoice #2023-987 Date: 09/20/2023 Client: Property Management LLC Services: Labor (80 hrs) $4,000.00 Materials $2,500.00 Equipment Rental $1,000.00 Subtotal: $7,500.00 Tax: $600.00 Total Due: $8,100.00",
        "Consulting Invoice INV-654 Date: 10/05/2023 To: StartUp Inc From: Business Consultants LLC Services: Strategic Planning $3,000.00 Market Analysis $2,500.00 Report Preparation $1,500.00 Subtotal: $7,000.00 Tax: $560.00 Amount Due: $7,560.00"
    ]
    labels = ['bank statement', 'bank statement','bank statement','bank statement','bank statement',
              'bank statement','bank statement','bank statement','bank statement','bank statement',
              'invoice', 'invoice', 'invoice', 'invoice', 'invoice',
              'invoice', 'invoice', 'invoice', 'invoice', 'invoice',]
    
    # Train and save
    # Transform text to TF-IDF features
    X = vectorizer.fit_transform(training_data)
    # Train the model
    model.fit(X, labels)
    # Save both vectorizer and model
    joblib.dump(vectorizer, os.path.join(current_dir, 'vectorizer.joblib'))
    joblib.dump(model, os.path.join(current_dir, 'model.joblib'))

if __name__ == "__main__":
    train_finance_classifier()