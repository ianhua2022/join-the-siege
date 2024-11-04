import joblib
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

def train_civil_classifier():
    # Currently logistic regression is used for the classifier, but more advanced models like neural networks could be used to improve accuracy.
    current_dir = os.path.dirname(os.path.abspath(__file__))
        
    vectorizer = TfidfVectorizer(max_features=1000, stop_words='english')
    model = LogisticRegression(multi_class='ovr')
    # Training data with passport and driver licence samples, can be further expanded to improve accuracy
    training_data = [
        "PASSPORT Type P USA Nationality UNITED STATES OF AMERICA Surname DOE Given Names JOHN JAMES Date of birth 15 JAN 1980 Place of birth NEW YORK Sex M Date of issue 01 JUN 2018 Date of expiry 31 MAY 2028",
        "P<USADOE<<JOHN<JAMES<<<<<<<<<<<<<<<<<<<<<<<<< 1234567890USA8001159M2805319<<<<<<<<<<<<<<02",
        "PASSPORT UNITED STATES OF AMERICA Passport No. 123456789 DOE JANE MARIE Birth Date 23 MAR 1992 Authority US DEPARTMENT OF STATE Issued 12 APR 2019 Expires 11 APR 2029",
        "USA PASSPORT Number 987654321 Name: SMITH ROBERT WILLIAM Date of Birth: 07 DEC 1975 Place of Birth: CALIFORNIA Gender: M Issue Date: 15 SEP 2020 Expiration: 14 SEP 2030",
        "Type: P Code: USA Passport No: 456789123 Surname: JOHNSON Given Names: MARY ELIZABETH DOB: 30 JUN 1988 POB: TEXAS Sex: F Issue: 20 JUL 2017 Expiry: 19 JUL 2027",
        "PASSPORT USA Name: BROWN MICHAEL THOMAS Birth Date: 11 NOV 1983 Birthplace: FLORIDA Gender: M Issued: 05 MAY 2021 Expires: 04 MAY 2031 Passport Number: 234567891",
        "United States of America Passport WILSON SARAH ANNE DOB: 19 APR 1995 POB: ILLINOIS Female Passport No: 345678912 Date of Issue: 28 FEB 2022 Valid Until: 27 FEB 2032",
        "P USA DAVIS JAMES PATRICK Born: 03 AUG 1979 Birth Place: OHIO Male Issue Date: 10 OCT 2019 Expiration: 09 OCT 2029 Number: 567891234",
        "PASSPORT UNITED STATES Type P TAYLOR EMMA GRACE Date of Birth 25 MAY 1990 POB: VIRGINIA F Issued on 17 NOV 2020 Expires 16 NOV 2030 No. 678912345",
        "US PASSPORT ANDERSON WILLIAM HENRY DOB: 14 JUL 1985 Place of Birth: WASHINGTON Sex: M Issue: 22 AUG 2018 Expiry: 21 AUG 2028 Passport#: 789123456",
         "DRIVER LICENSE STATE OF CALIFORNIA DL A1234567 CLASS C EXP 12/15/2025 RESTR NONE ISS 12/15/2021 DOB 03/22/1990 EYES BRN HAIR BRN HGT 5'-10\" WGT 170 lb SEX M MARTINEZ CARLOS ALBERTO 123 MAIN STREET LOS ANGELES CA 90001",
        "CALIFORNIA DRIVER LICENSE LN: THOMPSON FN: SARAH MIDDLE: JANE DL# B9876543 DOB: 05/18/1988 ISSUED: 09/30/2022 EXPIRES: 09/30/2026 END: NONE CLASS: C SEX: F EYES: BLU HT: 5-06 ADDR: 456 OAK AVE SACRAMENTO CA 95814",
        "DRIVERS LICENSE FLORIDA ID#: D123-456-78-901-0 NAME: WILSON, ROBERT J DOB: 11/05/1995 EXP: 11/05/2029 ISSUED: 11/05/2021 SEX: M EYES: GRN HEIGHT: 6-00 ADDRESS: 789 BEACH BLVD MIAMI FL 33139 CLASS: E RESTRICTIONS: B",
        "NEW YORK STATE DRIVER LICENSE CLASS: D ID: W123456789012 ENDORSEMENTS: NONE WILLIAMS JENNIFER LYNN DOB: 07/12/1992 EXPIRES: 2024 HEIGHT: 5' 4\" EYES: BRO SEX: F 321 PARK AVENUE NEW YORK NY 10022",
        "TEXAS DRIVER LICENSE DL NO. 12345678 CLASS C RESTR: A DOB 09/28/1987 ISSUED 03/15/2023 EXPIRES 09/28/2031 RODRIGUEZ DAVID M 567 ELM ST HOUSTON TX 77001 SEX M EYES BRN HT 5-11 DONOR: Y",
        "ILLINOIS DRIVERS LICENSE DL: I1234567890 CLASS: D GARCIA MARIA ELENA DOB: 01/30/1993 EXP: 01/30/2027 ISS: 01/30/2023 SEX: F HEIGHT: 5-05 EYES: BRN 890 STATE ST CHICAGO IL 60601 RSTR: NONE",
        "WASHINGTON DRIVER LICENSE WDL: ASMITH123AA SMITH MICHAEL JAMES DOB: 04/15/1983 EXPIRES: 04/15/2028 CLASS: A CDL ENDORSEMENTS: H RESTRICTIONS: B 234 PINE RD SEATTLE WA 98101 SEX: M HEIGHT: 6-02 EYES: HAZ",
        "ARIZONA DRIVERS LICENSE D01234567 CLASS D BROWN ASHLEY NICOLE ISSUED: 06/20/2022 EXPIRES: 06/20/2026 DOB: 08/10/1991 SEX: F HEIGHT: 5-07 EYES: GRN 456 DESERT WAY PHOENIX AZ 85001",
        "PENNSYLVANIA DRIVER'S LICENSE PA DL: 12345678 CLASS: C JOHNSON WILLIAM T DOB: 12/03/1989 ISSUED: 08/01/2021 EXP: 12/03/2025 SEX: M HT: 5-09 EYES: BLU 789 LIBERTY AVE PHILADELPHIA PA 19103",
        "MICHIGAN OPERATOR LICENSE D 123 456 789 012 CLASS: D ANDERSON EMILY ROSE DOB 02/14/1994 EXP 02/14/2028 ISS 02/14/2024 SEX F EYES BLU HT 5-08 END NONE 321 RIVER ST DETROIT MI 48201",
    ]
    labels = ['passport', 'passport','passport','passport','passport',
              'passport','passport','passport','passport','passport',
              'driver licence', 'driver licence', 'driver licence', 'driver licence', 'driver licence',
              'driver licence', 'driver licence', 'driver licence', 'driver licence', 'driver licence']
    
    # Train and save
    # Transform text to TF-IDF features
    X = vectorizer.fit_transform(training_data)
    # Train the model
    model.fit(X, labels)
    # Save both vectorizer and model
    joblib.dump(vectorizer, os.path.join(current_dir, 'vectorizer.joblib'))
    joblib.dump(model, os.path.join(current_dir, 'model.joblib'))

if __name__ == "__main__":
    train_civil_classifier()